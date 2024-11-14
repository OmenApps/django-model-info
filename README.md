# django-model-info

[![PyPI version](https://badge.fury.io/py/django-model-info.svg)](https://badge.fury.io/py/django-model-info)
[![Build Status](https://travis-ci.org/jacklinke/django-model-info.svg?branch=master)](https://travis-ci.org/jacklinke/django-model-info)
[![codecov](https://codecov.io/gh/jacklinke/django-model-info/branch/master/graph/badge.svg)](https://codecov.io/gh/jacklinke/django-model-info)

**Instantly understand your Django models' structure and relationships with beautiful, intuitive output.**

Working with complex Django projects? Need to quickly understand model relationships and fields? `django-model-info` is an ideal solution for diving into any Django codebase with confidence.

## Why django-model-info?

- **Perfect for New Team Members**: Quickly understand existing codebases without diving through multiple files
- **Great for Documentation**: Export beautiful HTML or Markdown documentation of your models' structure
- **Ideal for Large Projects**: Filter by app or model to focus on what matters
- **Time-Saving**: Instantly see all fields, relationships, and methods in one place
- **Rich Output**: Leverages [rich](https://github.com/willmcgugan/rich/) for beautiful, clear console output

See an example of the [HTML output](https://htmlpreview.github.io/?https://github.com/jacklinke/django-model-info/blob/master/example-output.html) or the [Markdown Output](https://github.com/OmenApps/django-model-info/blob/main/example-output.md).

## Quick Start

1. Install the package:
```bash
pip install django-model-info
```

2. Add to INSTALLED_APPS:
```python
INSTALLED_APPS = (
    ...
    'django_model_info.apps.DjangoModelInfoConfig',
    ...
)
```

3. Run the command:
```bash
python manage.py model_info
```

That's it! You'll see a beautiful overview of all your models.

## Key Features

- **Multiple Output Levels**: Choose from 4 verbosity levels to see exactly what you need
  - Level 0: Just model names
  - Level 1: Fields and basic method names
  - Level 2: Detailed field info and method signatures
  - Level 3: Complete information including docstrings and source locations

- **Smart Filtering**: Focus on specific apps or models:
```bash
python manage.py model_info -f myapp myapp.SpecificModel
```

- **Export Options**: Generate documentation in multiple formats:
```bash
python manage.py model_info -e documentation.html  # HTML output
python manage.py model_info -e documentation.md    # Markdown output
```

- **Print Markdown to screen**: As an alternative to the rich output:
```bash
python manage.py model_info --markdown
```

- **Rich or Markdown Information Display**:
  - Field types and database representations
  - Relationship mappings (forward and reverse)
  - Method signatures and locations
  - Database details (table names, indexes, etc.)
  - Source file locations and line numbers

## Configuration

Optionally configure defaults in your Django settings:

```python
# Default verbosity level (0-3)
MODEL_INFO_VERBOSITY = 2

# Default models/apps to display
MODEL_INFO_FILTER = ["myapp", "otherapp.SpecificModel"]
```

## Documentation

For detailed usage and examples, visit our [full documentation](https://django-model-info.readthedocs.io).

## Roadmap

- [ ] List manager and queryset methods
- [ ] Include signals and other model-level methods
- [ ] Add MermaidJS support for visualizing relationships

## Contributing

We welcome contributions! This project uses:

- [Cookiecutter](https://github.com/audreyr/cookiecutter)
- [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
- [rich](https://github.com/willmcgugan/rich/)

## License

MIT License
