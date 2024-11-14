# Terminology and Definitions

This guide explains key terms used throughout the django-model-info package and documentation. If you are experienced with Django, you probably know these already. But new developers or those unfamiliar with Django may find this helpful.

## Django Model Concepts

### Field Types
- **Primary Key (PK)**: The main identifier field for a model, usually an auto-incrementing ID.
- **Foreign Key**: A field that creates a one-to-many relationship between models.
- **Many-to-Many**: A field type that allows multiple records to be related to multiple other records.
- **One-to-One**: A field type that creates a unique one-to-one relationship between models.

### Relationships
- **Forward Relation**: A relationship defined directly on a model (e.g., a ForeignKey field).
- **Reverse Relation**: The automatic relationship created on the "other" model when a forward relation exists.
- **Related Name**: The attribute name used to access reverse relations (default is `modelname_set`).

### Method Types
- **Dunder Methods**: Special Python methods surrounded by double underscores (e.g., `__str__`, `__init__`).
- **Private Methods**: Methods starting with a single underscore, indicating they're intended for internal use.
- **Manager Methods**: Methods available through the model's manager (usually accessed via `Model.objects`).

## Database Concepts

### Table Information
- **Database Table**: The actual SQL table where model data is stored.
- **Table Space**: A storage location where the actual database files are kept.
- **Column**: The database representation of a model field.
- **Index**: A database structure that improves the speed of data retrieval.
- **Constraint**: A rule enforced on the data (e.g., unique constraints, check constraints).

### Field Properties
- **Verbose Name**: A human-readable name for a field, used in forms and admin.
- **DB Type**: The database-specific data type for a field (e.g., varchar, integer).
- **DB Column**: The actual name of the column in the database table.

## Model Metadata

### Model Properties
- **Abstract Model**: A model that serves as a base for other models but doesn't create a database table.
- **Proxy Model**: A model that inherits from another model but doesn't create a new table.
- **Managed Model**: A model whose database table is automatically created/modified by Django.
- **Label**: The full Python path to a model (e.g., 'myapp.MyModel').

## django-model-info Specific

### Verbosity Levels
- **Level 0**: Shows only model names
- **Level 1**: Shows model names, field names, and non-dunder/common method names
- **Level 2**: Shows Level 1 info plus field details and method signatures
- **Level 3**: Shows Level 2 info plus all method details including source locations

## Development Terms

### Code Location
- **File Path**: The location of a model or method in the codebase
- **Line Number**: The specific line where a model or method is defined
- **Method Resolution Order (MRO)**: The order in which Python searches for methods in class inheritance

### Documentation
- **Docstring**: The Python string literal that appears as the first statement in a module, class, or method
- **Signature**: The definition of a method showing its parameters and return type
