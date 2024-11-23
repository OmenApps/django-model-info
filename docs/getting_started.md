# Getting Started

This guide will help you install and begin using django-model-info to explore your Django models.

## Installation

### Prerequisites

Before installing django-model-info, ensure your environment meets the following requirements:

- **Python**: Version 3.10 or higher
- **Django**: Version 4.2 or higher
- **Dependencies**: 
  - `rich`: Automatically installed with the package for console output
  - `networkx`: Required if using `modelgraph` command
  - `pydot`: Required if using `modelgraph` command

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

This will install four new management commands:
- [modelinfo](https://django-model-info.readthedocs.io/en/latest/modelinfo.html)
- [modelfilters](https://django-model-info.readthedocs.io/en/latest/modelfilters.html)
- [modelgraph](https://django-model-info.readthedocs.io/en/latest/modelgraph.html)
- [migrationgraph](https://django-model-info.readthedocs.io/en/latest/migrationgraph.html)

### Verifying Installation

To verify the installation was successful, run:

```bash
python manage.py help modelinfo
```

You should see the help text for the `modelinfo` command. If you receive an error, ensure that:
1. The package is installed (`pip list | grep django-model-info`)
2. The app is properly added to `INSTALLED_APPS`
3. Your virtual environment is activated (if using one)
