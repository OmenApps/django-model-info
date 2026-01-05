# History

## Unreleased

-   Ensure deterministic output for `migrationgraph` and `modelgraph` commands by sorting nodes and edges.
-   Update example project for Django 5.1 compatibility.

## 2024.11.5 (2024-11-28)

-   Correct issue where `modelinfo` with `-m` flag was not outputting reverse relations.
-   Add migrations for the example project.
-   Update documentation and README.

## 2024.11.4 (2024-11-23)

-   Add new `migrationgraph` command.
-   Rename commands to follow Django standards:
    -   `model_filters` -> `modelfilters`
    -   `model_graph` -> `modelgraph`
    -   `model_info` -> `modelinfo`
-   Embed graphs from mermaid.live instead of raw markdown.
-   Refactor and clean up old files.

## 2024.11.x (Nov 2024)

-   Switch to date-based versioning scheme.
-   Major refactor and move source code to `src` directory.
-   Add `example_project` for testing and demonstration.
-   Modernize project configuration (`pyproject.toml`, `uv`).

## 0.2.1 (2021-12-13)

- Fix incorrct type checking placement.

## 0.2.0 (2021-12-13)

-   Improve argument handling.
-   Improve readme.
-   Update PyPI classifiers.

## 0.1.0 (2021-12-12)

-   First release on PyPI.
