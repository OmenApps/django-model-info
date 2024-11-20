# Usage Guide for model_info

This guide will help you begin using django-model-info to explore your Django models.

## Basic Usage

### Quick Start Command

The simplest way to use django-model-info is:

```bash
python manage.py model_info
```

This will display information about all models in your project using the default verbosity level (2).

For a specific app or model:
```bash
python manage.py model_info -f myapp
python manage.py model_info -f myapp.MyModel
```

### Understanding Default Output

The default output (verbosity level 2) includes:

1. **Model Information**
   ```
   myapp.MyModel
   ├── Model Info
   │   ├── Database Table: myapp_mymodel
   │   ├── Verbose Name: My Model
   │   └── ...
   ├── Fields
   │   ├── Regular Fields
   │   ├── Relations
   │   └── Reverse Relations
   └── Methods
   ```

Each section provides:
- **Model Info**: Basic model configuration and metadata
- **Fields**: All model fields with their types and properties
- **Methods**: Available model methods with signatures

### Common Use Cases

#### 1. Exploring a New Project
When joining a project or returning after time away:
```bash
# Get a high-level overview of all models
python manage.py model_info -v 1

# Deep dive into a specific app
python manage.py model_info -f myapp -v 3
```

This helps you:
- Understand the project's data structure
- Identify key models and their relationships
- Find important fields and methods

#### 2. Documenting Models
Generate documentation for your models:
```bash
# Generate HTML documentation
python manage.py model_info -e models.html

# Generate Markdown for your repo
python manage.py model_info -e models.md
```

Tips for documentation:
- Use verbosity level 2 or 3 for comprehensive documentation
- Filter by app to create focused documentation sections
- Include the output in your project's documentation

#### 3. Debugging Relationships
When working with model relationships:
```bash
# Focus on a specific model with full details
python manage.py model_info -f myapp.MyModel -v 3
```

This helps you:
- View all forward and reverse relationships
- Understand how models are connected
- Find related field names for queries
- Identify potential optimization points

Pro tip: When debugging relationships, pay special attention to the "Relations" and "Reverse Relations" sections in the output. These show how your model connects to others and what field names to use in queries.

### Next Steps

Now that you've installed and tried basic commands, you can:
1. Explore different verbosity levels to control output detail
2. Use filters to focus on specific parts of your project
3. Export model information in various formats
4. Configure default settings for your project

See the [Configuration & Options](usage_configuration.md) section for more detailed information about customizing django-model-info for your needs.

## Configuration & Options

django-model-info can be configured through both Django settings and command-line options. This section covers all available configuration options and when to use them.

### MODEL_INFO_VERBOSITY

Controls the default level of detail in the output.

```python
# settings.py
MODEL_INFO_VERBOSITY = 2  # Default value
```

#### Valid Options
- **0**: Model names only
  - Best for: Quick overview of available models
  - Use when: You need a simple list of models
  ```python
  # Output Example:
  myapp.UserProfile
  myapp.Order
  myapp.Product
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

### MODEL_INFO_FILTER

Specifies which models or apps to display by default.

```python
# settings.py
MODEL_INFO_FILTER = [
    "myapp",                    # Entire app
    "otherapp.SpecificModel",   # Specific model
]
```

#### Format Specifications
- **App Filter**: Just the app name (e.g., `"myapp"`)
- **Model Filter**: App and model name separated by dot (e.g., `"myapp.Model"`)
- **Multiple Items**: List of strings with any combination

#### Example Patterns
```python
# Show multiple apps
MODEL_INFO_FILTER = ["users", "orders", "products"]

# Show specific models
MODEL_INFO_FILTER = ["users.User", "orders.Order"]

# Mix of apps and models
MODEL_INFO_FILTER = ["users", "orders.Order", "products.Product"]
```

## Command Line Options

### Verbosity Levels (`-v`, `--verbosity`)

Override the default verbosity level:

```bash
# Model names only
python manage.py model_info -v 0

# Basic information
python manage.py model_info -v 1

# Detailed information (default)
python manage.py model_info -v 2

# Complete information
python manage.py model_info -v 3
```

### Filtering (`-f`, `--filter`)

Filter which models to display:

```bash
# Single app
python manage.py model_info -f myapp

# Single model
python manage.py model_info -f myapp.MyModel

# Multiple filters
python manage.py model_info -f myapp otherapp.Model
```

#### By App
Shows all models in specified app(s):
```bash
python manage.py model_info -f users
python manage.py model_info -f users orders
```

#### By Model
Shows specific model(s):
```bash
python manage.py model_info -f users.User
python manage.py model_info -f users.User orders.Order
```

#### Multiple Filters
Combine app and model filters:
```bash
python manage.py model_info -f users orders.Order products
```

### Export Options (`-e`, `--export`)

Export the output in different formats:

#### HTML Format
```bash
python manage.py model_info -e output.html
```
- Includes rich formatting and styling
- Interactive navigation (if supported by the template)
- Ideal for documentation websites

#### Markdown Format
```bash
python manage.py model_info -e output.md
```
- Perfect for GitHub documentation
- Easy to read in plain text
- Can be converted to other formats

#### Text Format
```bash
python manage.py model_info -e output.txt
```
- Plain text output
- No formatting
- Useful for processing with other tools

### Other Options

#### `--exclude-defaults`
Excludes Django's default fields and methods:
```bash
python manage.py model_info --exclude-defaults
```
- Hides common Django fields (e.g., id, created_at)
- Excludes standard model methods
- Shows only custom fields and methods

#### `--markdown`
Outputs in markdown format directly to console:
```bash
python manage.py model_info --markdown
```
- Useful for copying into documentation
- No file creation needed
- Can be piped to other commands

## Option Precedence

When options are specified in multiple places, they are prioritized as follows:

1. Command line options (highest priority)
2. Django settings
3. Default values (lowest priority)
