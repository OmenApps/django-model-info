# Usage

# Getting Started with django-model-info

This guide will help you install and begin using django-model-info to explore your Django models.

## Installation

### Prerequisites

Before installing django-model-info, ensure your environment meets the following requirements:

- **Python**: Version 3.10 or higher
- **Django**: Version 4.2 or higher
- **Dependencies**: 
  - `rich`: Automatically installed with the package

### Installation Methods

#### Via pip
```bash
pip install django-model-info
```

### Adding to INSTALLED_APPS

Add django-model-info to your Django project's `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    ...
    'django_model_info.apps.DjangoModelInfoConfig',
    ...
)
```

### Verifying Installation

To verify the installation was successful, run:

```bash
python manage.py help model_info
```

You should see the help text for the `model_info` command. If you receive an error, ensure that:
1. The package is installed (`pip list | grep django-model-info`)
2. The app is properly added to `INSTALLED_APPS`
3. Your virtual environment is activated (if using one)

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

# Configuration & Options

django-model-info can be configured through both Django settings and command-line options. This section covers all available configuration options and when to use them.

## Django Settings

You can configure default behavior by adding settings to your Django project's settings file.

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

# Understanding the Output

django-model-info provides detailed information about your Django models in a structured format. This guide explains how to interpret each section of the output.

## Model Information

Every model's output starts with a header showing the model's label (e.g., `myapp.MyModel`), followed by detailed sections.

### Basic Model Details
```
Model Info
├── Model Name: User
├── Verbose Name: user
├── Verbose Name Plural: users
└── Docstring: Custom user model for the application
```

Key elements:
- **Model Name**: The class name of the model
- **Verbose Name**: Human-readable singular name (used in admin)
- **Verbose Name Plural**: Plural form used in admin and API
- **Docstring**: The model's documentation string

### Meta Options
```
Meta Options
├── Is Abstract: False
├── Is Proxy: False
├── Is Managed: True
├── Ordering: ['-created_at']
├── Permissions: [('can_view_profile', 'Can view user profile')]
└── Default Permissions: ['add', 'change', 'delete', 'view']
```

These options affect model behavior:
- **Is Abstract**: Whether the model is an abstract base class
- **Is Proxy**: Whether this is a proxy model
- **Is Managed**: Whether Django manages the database table
- **Ordering**: Default ordering for queries
- **Permissions**: Custom model permissions
- **Default Permissions**: Standard Django permissions

### Database Information
```
Database Info
├── Database Table: myapp_user
├── Database Table Comment: User accounts table
├── Database Tablespace: 
├── Indexes: [<Index: myapp_user_email_idx>]
└── Constraints: [<UniqueConstraint: name='unique_email'>]
```

Database-specific details:
- **Table**: Actual database table name
- **Table Comment**: Optional comment in database
- **Tablespace**: Custom database tablespace if used
- **Indexes**: Database indexes on the model
- **Constraints**: Database constraints (unique, check, etc.)

## Field Information

Fields are grouped into three categories: regular fields, relations, and reverse relations.

### Field Types and Descriptions
```
Fields
├── id (pk)
│   ├── Type: AutoField
│   ├── Column: id
│   └── DB Type: integer
├── email
│   ├── Type: EmailField
│   ├── Column: email
│   ├── DB Type: varchar(254)
│   └── Verbose Name: Email Address
```

For each field:
- **Type**: Python/Django field class
- **Column**: Actual database column name
- **DB Type**: Database-specific type
- **Verbose Name**: Human-readable field name

### Field Relationships
```
Relations
├── profile
│   ├── Type: OneToOneField
│   ├── Related Model: accounts.UserProfile
│   └── Related Name: user
├── orders
│   ├── Type: ForeignKey
│   ├── Related Model: orders.Order
│   └── Related Name: customer_orders
```

#### Forward Relationships
(Fields defined on this model)
```
└── groups
    ├── Type: ManyToManyField
    ├── Through: auth.UserGroups
    └── Related Name: user_set
```

Key information:
- **Type**: Relationship type (OneToOne, ForeignKey, ManyToMany)
- **Related Model**: Target model
- **Related Name**: Name for reverse access
- **Through**: Intermediate model for M2M relations

#### Reverse Relationships
(Fields from other models pointing to this one)
```
Reverse Relations
└── authored_posts
    ├── From Model: blog.Post
    ├── Through Field: author
    └── Related Name: authored_posts
```

Shows:
- **From Model**: Model containing the relationship
- **Through Field**: Field name on the other model
- **Related Name**: Name used to access related objects

## Method Information

Methods are categorized by type and show different details based on verbosity level.

### Method Types

#### Dunder Methods
```
Dunder Methods
└── __str__
    ├── Signature: (self)
    ├── Source: accounts/models.py:45
    └── Docstring: String representation of User
```

Python special methods (e.g., `__str__`, `__repr__`)

#### Private Methods
```
Private Methods
└── _normalize_email
    ├── Signature: (self, email)
    ├── Source: accounts/models.py:78
    └── Docstring: Normalize the email address
```

Internal methods starting with underscore

#### Custom Methods
```
Other Methods
└── get_full_name
    ├── Signature: (self) -> str
    ├── Source: accounts/models.py:92
    └── Docstring: Returns the user's full name
```

User-defined public methods

### Method Signatures
```
def get_display_name(self, format_type: str = 'full') -> str:
```

Shows:
- Parameters and their types
- Default values
- Return type annotations

### Source Locations
```
Source
├── File: accounts/models.py
└── Line: 92
```

Helps locate method definitions:
- Relative file path
- Line number in file
- Module location
