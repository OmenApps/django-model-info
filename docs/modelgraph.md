# Usage Guide for modelgraph

## Overview
The `modelgraph` management command helps developers visualize and analyze Django model relationships by generating graphs and detailed relationship analysis. The command supports visual (DOT and MermaidJS formats) and textual analysis outputs, with other formats planned for future development.

## Key Features
- Generate visual model relationship diagrams
- Analyze model relationships and dependencies
- Support for filtering specific apps/models
- Multiple output formats (DOT, MermaidJS, text analysis)
- Customizable relationship visualization
- Cache support for improved performance

## Command Syntax
```bash
python manage.py modelgraph [options]
```

## Options

### Model Selection Options
- **positional args**: Apps, models, or `app.Model` to include in the graph
  ```bash
  python manage.py modelgraph auth sales.Order
  ```

- **`-e, --exclude`**: Apps, models, or `app.Model` to exclude
  ```bash
  python manage.py modelgraph -e auth Permission
  ```

- **`--prefix`**: Include only models with specific prefix
  ```bash
  python manage.py modelgraph --prefix User
  ```

### Model Type Options
- **`-a, --abstract`**: Include abstract models
- **`-p, --proxy`**: Include proxy models

### Output Options
- **`-f, --format`**: Output format (choices: `dot`, `mermaid`, `analysis`; default: `analysis`)
- **`-o, --output`**: Output file path (required for `dot` format, optional for `mermaid`)

### Cache Control
- **`--use-cache`**: Use cached results if available
- **`--clear-cache`**: Clear cached results before running

## Settings
All settings are optional, and should be added as dictionary key-value entries in the **`DJANGO_MODELINFO`** setting.

- **`CACHE_ENABLED`**: *bool* Enable caching of results (default: False)
- **`CACHE_ALWAYS`**: *bool* Always cache results, even if the --use-cache flag is not used (default: False)
- **`CACHE_ALIAS`**: *str* The cache alias to use for caching results (default: "default")
- **`CACHE_TIMEOUT`**: *int* The cache timeout in seconds (default: 3600)
- **`CACHE_KEY_PREFIX`**: *str* The prefix to use for cache keys (default: "modelfilters:")

## Output Formats

### Analysis Format
Provides a detailed text analysis of model relationships including:

1. Basic Statistics:
   - Total number of models
   - Total number of relationships

2. Model Analysis:
   - Strongly connected components
   - Isolated models
   - Degree centrality
   - Detected cycles
   - Relationship patterns

### DOT Format
Generates a visual representation of model relationships using the DOT graph description language.

#### Features:
1. Color-coded relationships:
   - OneToOneField: chartreuse4
   - ForeignKey: blue
   - ManyToManyField: red

2. Relationship styles:
   - Forward relationships: solid lines
   - Reverse relationships: dashed lines

3. Includes a legend showing all relationship types

### Mermaid Format
Generates a visual representation of model relationships using [MermaidJS](https://mermaid.js.org/syntax/flowchart.html).

#### Features:
1. Relationship styles:
   - Forward relationships: thick solid lines
   - Reverse relationships: thin dashed lines

## Common Use Cases

The `modelgraph` command is particularly valuable when working with large Django applications where understanding the overall model structure is crucial. Here are some typical scenarios:

### Exploring a New Project
When joining an existing project, you can quickly understand the data model:

```bash
# Get an overview of the entire project's relationships
python manage.py modelgraph

# Focus on a specific app's models
python manage.py modelgraph sales -f dot -o sales_models.dot
```

The analysis output helps you identify:
- Core models with many relationships
- Isolated models that might need review
- Complex relationship patterns

### Validating Architecture Decisions
When implementing architectural patterns like bounded contexts or microservices:

```bash
# Analyze boundaries between functional areas
python manage.py modelgraph -f dot -o boundaries.dot authentication sales analytics
```

Use the visual output to:
- Verify proper separation between domains
- Identify unwanted cross-domain dependencies
- Ensure compliance with architectural constraints

### Finding Critical Models
Identify models that are central to your application:

```bash
# Generate analysis of the entire project
python manage.py modelgraph
```

The analysis output highlights:
- Models with high degree centrality (many relationships)
- Models in strongly connected components
- Key junction models in many-to-many relationships

### Creating Architecture Documentation
Generate visual documentation for your project:

```bash
# Create full-project relationship diagram
python manage.py modelgraph -f dot -o model_architecture.dot

# Create focused diagrams for specific parts of the project
python manage.py modelgraph sales inventory -f dot -o sales_inventory.dot
```

Use these diagrams to:
- Include in architecture documentation
- Create onboarding materials for new team members
- Discuss system design in team meetings

## Example

Generate a basic analysis of all models in an app:

```bash
python manage.py modelgraph sales
```

Example output:
```
Model Graph Analysis
===================

Basic Statistics:
  Models: 5
  Relationships: 4

Strongly Connected Components (each model can reach all others):
  Component 1:
    - sales.order
    - sales.orderitem
    - sales.shippingaddress

Isolated Models (no relationships to other models):
    - sales.bankaccount
    - sales.creditcard

Centrality Analysis (higher values indicate more connected models):
  sales.order:
    Overall Centrality: 1.000
    Incoming: 0.500
    Outgoing: 0.500
  sales.orderitem:
    Overall Centrality: 0.500
    Incoming: 0.250
    Outgoing: 0.250
  sales.shippingaddress:
    Overall Centrality: 0.500
    Incoming: 0.250
    Outgoing: 0.250

Cycles Detected (models involved in circular relationships):
  - sales.orderitem -> sales.order -> sales.orderitem
  - sales.order -> sales.shippingaddress -> sales.order

Model Relationships:
  sales.order:
    ← sales.orderitem
      ManyToOneRel (reverse: items)
    → sales.shippingaddress
      ForeignKey (shipping_address)
  sales.orderitem:
    → sales.order
      ForeignKey (order)
  sales.shippingaddress:
    ← sales.order
      ManyToOneRel (reverse: order)
```
