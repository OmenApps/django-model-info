"""Nox sessions for django-model-info."""

import sys

import nox

DJANGO_STABLE_VERSION = "5.2"
DJANGO_VERSIONS = ["4.2", "5.1", "5.2", "6.0"]
PYTHON_STABLE_VERSION = "3.14"
PYTHON_VERSIONS = ["3.11", "3.12", "3.13", "3.14"]
PACKAGE = "django_model_info"

nox.options.default_venv_backend = "uv"
nox.options.sessions = ["pre-commit", "pip-audit", "tests"]


@nox.session(name="pre-commit", python=PYTHON_STABLE_VERSION)
def precommit(session: nox.Session) -> None:
    """Run pre-commit hooks on all files."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox.session(name="pip-audit", python=PYTHON_STABLE_VERSION)
def pip_audit(session: nox.Session) -> None:
    """Scan dependencies for known vulnerabilities."""
    pyproject = nox.project.load_toml("pyproject.toml")
    deps = nox.project.dependency_groups(pyproject, "dev")
    session.install(".", *deps)
    session.install("pip-audit")
    session.run("pip-audit")


@nox.session(
    python=PYTHON_VERSIONS,
    tags=["tests"],
)
@nox.parametrize("django", DJANGO_VERSIONS)
def tests(session: nox.Session, django: str) -> None:
    """Run the test suite across Python and Django versions."""
    # Django 4.2 supports only Python 3.11-3.12
    if django == "4.2" and session.python in ("3.13", "3.14"):
        session.skip("Django 4.2 supports only Python 3.11-3.12")
    # Django 5.1 supports only Python 3.11-3.13
    if django == "5.1" and session.python == "3.14":
        session.skip("Django 5.1 supports only Python 3.11-3.13")
    # Django 6.0 requires Python 3.12+
    if django == "6.0" and session.python == "3.11":
        session.skip("Django 6.0 requires Python 3.12+")

    pyproject = nox.project.load_toml("pyproject.toml")
    deps = nox.project.dependency_groups(pyproject, "dev")
    session.install(".", *deps)
    session.install(f"django~={django}.0")
    session.run("python", "manage.py", "makemigrations", "--no-input")
    session.run(
        "coverage",
        "run",
        "-m",
        "pytest",
        "-vv",
        *session.posargs,
    )

    if sys.stdin.isatty():
        session.notify("coverage")


@nox.session(python=PYTHON_STABLE_VERSION)
def coverage(session: nox.Session) -> None:
    """Combine and report coverage."""
    session.install("coverage[toml]")
    session.run("coverage", "combine", success_codes=[0, 1])
    session.run("coverage", "report")


@nox.session(name="docs-build", python=PYTHON_STABLE_VERSION)
def docs_build(session: nox.Session) -> None:
    """Build the documentation."""
    session.install("-r", "docs/requirements.txt")
    session.install(".")
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session(name="docs", python=PYTHON_STABLE_VERSION)
def docs(session: nox.Session) -> None:
    """Build and serve the documentation with live reload."""
    session.install("-r", "docs/requirements.txt")
    session.install("sphinx-autobuild")
    session.install(".")
    session.run("sphinx-autobuild", "docs", "docs/_build", "--open-browser")
