"""Management command to visualize migrations and dependencies for apps in the project."""
import re

from django.apps import apps as django_apps
from django.core.management.base import BaseCommand, CommandError
from django.db.migrations.loader import MigrationLoader


class Command(BaseCommand):
    """A management command to Visualize migrations and dependencies for applications in the project."""

    help = "Visualize migrations and dependencies for apps in the project, limiting to the specified apps, if any."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nodes = set()
        self.edges = set()
        self.app_labels = set()
        self.loader = None
        self.reverse_dependencies = {}

    def add_arguments(self, parser):
        """Add optional argument to specify apps to show migrations for."""
        parser.add_argument(
            "app_labels",
            nargs="*",
            help="Optional list of application labels.",
        )

    def handle(self, *args, **options):
        """Handle the command."""
        app_labels = options["app_labels"]
        self.loader = MigrationLoader(None, ignore_no_migrations=True)

        if not app_labels:
            app_labels = [app_config.label for app_config in django_apps.get_app_configs()]
        else:
            # Validate that provided app labels are installed
            for app_label in app_labels:
                try:
                    django_apps.get_app_config(app_label)
                except LookupError as e:
                    raise CommandError(f"{e}. Are you sure your INSTALLED_APPS setting is correct?") from e

        self.app_labels = set(app_labels)
        self._build_reverse_dependencies()

        for idx, app in enumerate(app_labels):
            self._print_success(f"[{app}]")
            self._print_app_migrationgraph(app)
            if idx != len(app_labels) - 1:
                self.stdout.write("\n")

        # Collect nodes from edges and print MermaidJS flowchart
        self._collect_nodes_from_edges()
        self._print_mermaidjs_flowchart()

    def _build_reverse_dependencies(self):
        """Build a mapping of reverse dependencies for all migrations."""
        self.reverse_dependencies = {}
        for (app_label, migration_name), node in self.loader.graph.nodes.items():
            for dep_app, dep_name in node.dependencies:
                # Resolve __first__ dependencies
                if dep_name == "__first__":
                    root_nodes = self.loader.graph.root_nodes(dep_app)
                    for root_node in root_nodes:
                        self.reverse_dependencies.setdefault(root_node, set()).add((app_label, migration_name))
                else:
                    dep_key = (dep_app, dep_name)
                    self.reverse_dependencies.setdefault(dep_key, set()).add((app_label, migration_name))

    def _print_migration_info(self, app_label, migration_name, node):
        """Print detailed information about a migration."""
        self._print_label(f"{app_label}/{migration_name}")

        # Print dependencies
        dependencies = [(dep_app, dep_name) for dep_app, dep_name in node.dependencies if dep_app != app_label]
        if dependencies:
            self._print_title("\tDepends on:")
            for dep_app, dep_name in dependencies:
                # Resolve __first__ to actual migration name
                if dep_name == "__first__":
                    root_nodes = self.loader.graph.root_nodes(dep_app)
                    for root_app, root_name in root_nodes:
                        self._print_notice(f"\t\t{root_app}/{root_name}")
                else:
                    self._print_notice(f"\t\t{dep_app}/{dep_name}")

        # Print reverse dependencies
        migration_key = (app_label, migration_name)
        reverse_deps = self.reverse_dependencies.get(migration_key, set())
        reverse_deps = [
            (rev_app, rev_name) for rev_app, rev_name in reverse_deps if rev_app in self.app_labels
        ]  # Filter to requested apps
        if reverse_deps:
            self._print_title("\tDepended upon by:")
            for rev_app, rev_name in sorted(reverse_deps):
                self._print_notice(f"\t\t{rev_app}/{rev_name}")

    def _get_node_key(self, node):
        """Get the app_label and migration_name for a node."""
        # Handle both Node objects and tuples
        if hasattr(node, "key"):
            return node.key
        return node

    def _collect_nodes_from_edges(self):
        """Ensure all nodes in edges are included in nodes."""
        for edge in self.edges:
            from_node_key, to_node_key = edge
            from_node = self.loader.graph.node_map.get(from_node_key)
            to_node = self.loader.graph.node_map.get(to_node_key)
            if from_node:
                self.nodes.add(from_node)
            if to_node:
                self.nodes.add(to_node)

    def _print_styled(self, style, text):
        """Print the text with the specified style."""
        self.stdout.write(style(text) + "\n")

    def _print_label(self, text):
        """Print the label."""
        self._print_styled(self.style.MIGRATE_LABEL, text)

    def _print_warn(self, text):
        """Print the warning."""
        self._print_styled(self.style.WARNING, text)

    def _print_title(self, text):
        """Print the title."""
        self._print_styled(self.style.MIGRATE_HEADING, text)

    def _print_notice(self, text):
        """Print the notice."""
        self._print_styled(self.style.NOTICE, text)

    def _print_error(self, text):
        """Print the error."""
        self._print_styled(self.style.ERROR, text)

    def _print_success(self, text):
        """Print the success."""
        try:
            style = self.style.SUCCESS
        except AttributeError:
            style = self.style.MIGRATE_SUCCESS
        self._print_styled(style, text)

    def _get_node_id(self, node_key):
        """Get the node ID."""
        app_label, migration_name = node_key
        node_id = f"{app_label}_{migration_name}"
        # Replace any non-alphanumeric characters with underscores
        node_id = re.sub(r"\W|^(?=\d)", "_", node_id)
        return node_id

    def _get_node_label(self, node_key):
        """Get the node label."""
        app_label, migration_name = node_key
        match = re.match(r"^(\d+)_", migration_name)
        if match:
            prefix = match.group(1)
        else:
            prefix = migration_name[:9]
        label = f"{app_label}/{prefix}"
        return label

    def _print_app_migrationgraph(self, app):
        """Print the migrations graph for the specified app."""
        try:
            migrations = []
            # Collect all migrations for this app
            for (app_label, migration_name), node in self.loader.graph.nodes.items():
                if app_label == app:
                    migrations.append((migration_name, node))
                    # Add this node to our nodes set
                    self.nodes.add((app_label, migration_name))
                    # Collect edges from this node's dependencies
                    for dep_app, dep_name in node.dependencies:
                        if dep_name == "__first__":
                            root_nodes = self.loader.graph.root_nodes(dep_app)
                            for root_node in root_nodes:
                                self.edges.add((root_node, (app_label, migration_name)))
                        else:
                            self.edges.add(((dep_app, dep_name), (app_label, migration_name)))

            # Sort migrations by name to ensure consistent ordering
            migrations.sort()

            for migration_name, node in migrations:
                self._print_migration_info(app, migration_name, node)

        except KeyError:
            self._print_error(f"Migrations for `{app}` application were not found")
            return

    def _print_mermaidjs_flowchart(self):
        """Print the MermaidJS flowchart."""
        self.stdout.write("\n_____________________")
        self.stdout.write("Migrations Flowchart:\n")
        self.stdout.write("\n```mermaid\n")
        self.stdout.write("graph TD\n")
        # First, define nodes
        for node_key in self.nodes:
            node_id = self._get_node_id(node_key)
            node_label = self._get_node_label(node_key)
            self.stdout.write(f'    {node_id}["{node_label}"]\n')
        # Then, define edges
        for from_key, to_key in self.edges:
            from_id = self._get_node_id(from_key)
            to_id = self._get_node_id(to_key)
            self.stdout.write(f"    {from_id} --> {to_id}\n")
        self.stdout.write("```\n")
