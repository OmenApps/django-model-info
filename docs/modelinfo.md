# Usage Guide for modelinfo

This guide will help you begin using django-model-info to explore your Django models.

## Basic Usage

### Quick Start Command

The simplest way to use django-model-info is:

```bash
python manage.py modelinfo
```

This will display information about all models in your project using the default verbosity level (2).

For specific apps, models, or a combination, add them to the command. Any of the following formats are valid:
```bash
python manage.py modelinfo sales
python manage.py modelinfo sales.Order
python manage.py modelinfo sales.Order sales.OrderItem auth
```

### Understanding Default Output

The default output (verbosity level 2) includes:

1. **Model Information**
   ```
   sales.Order
   ├── Model Info
   │   ├── Model Name: Order
   │   ├── Verbose Name: order
   |   ├── Verbose Name Plural: orders
   │   └── ...
   ├── Fields
   │   ├── Regular Fields (Field Name | Field Type | Database Column | Database Type | Verbose Name)
   │   ├── Relations (Field Name | Field Type | Database Column | Database Type | Related Model | Related Name)
   │   └── Reverse Relations (Field Name | Field Type Database Type | Related Model | Field Name on Related Model | Field Type on Related Model)
   ├── Methods
   │   ├── Other Methods (Method Name | Signature)
   │   ├── Private Methods (Method Name | Signature)
   │   ├── Dunder Methods (Method Name | Signature)
   │   └── Common Django Methods (Method Name | Signature)
   └── Custom Managers
       ├── Custom Managers
       └── Custom QuerySets
   ```

Each section provides:
- **Model Info**: Basic model configuration and metadata
- **Fields**: All model fields with their types and properties
- **Methods**: Available model methods with signatures
- **Custom Managers**: Custom managers and querysets

### Common Use Cases

#### 1. Exploring a New Project
When joining a project or returning after time away:
```bash
# Get a high-level overview of all models
python manage.py modelinfo -v 1

# Deep dive into a specific app
python manage.py modelinfo sales -v 3
```

This helps you:
- Understand the project's data structure
- Identify key models and their relationships
- Find important fields and methods

#### 2. Documenting Models
Generate documentation for your models:
```bash
# Generate HTML documentation
python manage.py modelinfo -o models.html

# Generate Markdown for your repo
python manage.py modelinfo -o models.md
```

Tips for documentation:
- Use verbosity level 2 or 3 for comprehensive documentation
- Filter by app to create focused documentation sections
- Include the output in your project's documentation

#### 3. Debugging Relationships
When working with model relationships:
```bash
# Focus on a specific model with full details
python manage.py modelinfo sales.Order -v 3
```

This helps you:
- View all forward and reverse relationships
- Understand how models are connected
- Find related field names for queries
- Identify potential optimization points

Pro tip: When debugging relationships, pay special attention to the "Relations" and "Reverse Relations" sections in the output. These show how your model connects to others and what field names to use in queries.

## Configuration & Options

The `modelinfo` command can be configured through both Django settings and command-line options. All settings are optional, and should be added as dictionary key-value entries in the **`DJANGO_MODELINFO`** setting.

### MODELINFO_VERBOSITY

Controls the default level of detail in the output.

```python
# settings.py
DJANGO_MODELINFO = {
    "MODELINFO_VERBOSITY": 2  # Default value
}
```

#### Valid Options
- **0**: Model names only
  - Best for: Quick overview of available models
  - Use when: You need a simple list of models
  ```python
  # Output Example:
  sales.BankAccount
  sales.Order
  sales.OrderItem
  ```

- **1**: Basic information
  - Best for: General model exploration
  - Shows: Model names, field names, basic method names
  - Use when: You need to know what fields and methods exist
  ```python
  # Output includes:
  - Field names (without details)
  - Method names (without signatures)
  - Basic model properties
  ```

- **2**: Detailed information (Default)
  - Best for: Daily development work
  - Shows: Field details, method signatures, relationships
  - Use when: You need to understand model structure
  ```python
  # Output includes:
  - Field types and properties
  - Method signatures
  - Relationship details
  ```

- **3**: Complete information
  - Best for: Documentation and deep analysis
  - Shows: Everything including docstrings and source locations
  - Use when: You need full understanding or documentation
  ```python
  # Output includes:
  - All level 2 information
  - Method docstrings
  - Source file locations
  - Line numbers
  ```

### MODELINFO_FILTER

Specifies which models or apps to display by default.

```python
# settings.py
DJANGO_MODELINFO = {
    "MODELINFO_FILTER": ["sales", "auth.User"]
}
```

#### Format Specifications
- **App Filter**: Just the app name (e.g., `"sales"`)
- **Model Filter**: App and model name separated by dot (e.g., `"sales.Order"`)
- **Multiple Items**: List of strings with any combination

#### Example Patterns
```python
# Show multiple apps
MODELINFO_FILTER = ["auth", "sales", "inventory"]

# Show specific models
MODELINFO_FILTER = ["auth.User", "sales.Order"]

# Mix of apps and models
MODELINFO_FILTER = ["auth", "sales.Order", "inventory.Product"]
```

## Command Line Options

### Verbosity Levels (`-v`, `--verbosity`)

Override the default verbosity level:

```bash
# Model names only
python manage.py modelinfo -v 0

# Basic information
python manage.py modelinfo -v 1

# Detailed information (default)
python manage.py modelinfo -v 2

# Complete information
python manage.py modelinfo -v 3
```

### Filtering (positional arg)

Filter which models to display:

```bash
# Single app
python manage.py modelinfo sales

# Single model
python manage.py modelinfo sales.Order

# Multiple filters
python manage.py modelinfo sales auth.User
```

#### By App
Shows all models in specified app(s):
```bash
python manage.py modelinfo auth
python manage.py modelinfo auth orders
```

#### By Model
Shows specific model(s):
```bash
python manage.py modelinfo auth.User
python manage.py modelinfo auth.User sales.Order
```

#### Multiple Filters
Combine app and model filters:
```bash
python manage.py modelinfo auth sales.Order inventory
```

### Output Options (`-o`, `--output`)

Export the output in different formats:

#### HTML Format
```bash
python manage.py modelinfo -o output.html
```
- Includes rich formatting and styling
- Interactive navigation (if supported by the template)
- Ideal for documentation websites

#### Markdown Format
```bash
python manage.py modelinfo - output.md
```
- Perfect for GitHub documentation
- Easy to read in plain text
- Can be converted to other formats

#### Text Format
```bash
python manage.py modelinfo -o output.txt
```
- Plain text output
- No formatting
- Useful for processing with other tools

### Other Options

#### `--exclude-defaults`
Excludes Django's default fields and methods:
```bash
python manage.py modelinfo --exclude-defaults
```
- Hides common Django fields (e.g., id, created_at)
- Excludes standard model methods
- Shows only custom fields and methods

#### `--markdown`
Outputs in markdown format directly to console:
```bash
python manage.py modelinfo --markdown
```
- Useful for copying into documentation
- No file creation needed
- Can be piped to other commands

## Option Precedence

When options are specified in multiple places, they are prioritized as follows:

1. Command line options (highest priority)
2. Django settings
3. Default values (lowest priority)
