# Usage Guide for model_info

This guide will help you install and begin using django-model-info to explore your Django models.

## Installation

### Prerequisites

Before installing django-model-info, ensure your environment meets the following requirements:

- **Python**: Version 3.10 or higher
- **Django**: Version 4.2 or higher
- **Dependencies**: 
  - `rich`: Automatically installed with the package for console output
  - `networkx`: Optional, for graphing models
  - `pydot`: Optional, for graphing models

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

## Next Steps

For usage information specific to each command, please see that command's usage page:

- [model_info]
- [model_filters]
- [model_graph]
