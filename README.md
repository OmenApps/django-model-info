# django-model-info

[![image][]][1]

[![image][2]][3]

[![image][4]][5]

A Django Management Command for displaying details about your project's models

This package takes the original `list_model_info` command I wrote for `django-extensions` to a whole new level. More information and much more beautiful interface, thanks to [`rich`](https://github.com/willmcgugan/rich/)

## Documentation

The full documentation is at <https://django-model-info.readthedocs.io>.

## Quickstart

Install django-model-info:

    pip install django-model-info

Add it to your \`INSTALLED_APPS\`:

``` python
INSTALLED_APPS = (
    ...
    'django_model_info.apps.DjangoModelInfoConfig',
    ...
)
```

Add django-model-info's URL patterns:

``` python
from django_model_info import urls as django_model_info_urls


urlpatterns = [
    ...
    url(r'^', include(django_model_info_urls)),
    ...
]
```

## Features

-   TODO

## Running Tests

Does the code actually work?

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

## Development commands

    pip install -r requirements_dev.txt
    invoke -l

## Credits

Tools used in rendering this package:

-   [Cookiecutter][]
-   [cookiecutter-djangopackage][]

  [image]: https://badge.fury.io/py/django-model-info.svg
  [1]: https://badge.fury.io/py/django-model-info
  [2]: https://travis-ci.org/jacklinke/django-model-info.svg?branch=master
  [3]: https://travis-ci.org/jacklinke/django-model-info
  [4]: https://codecov.io/gh/jacklinke/django-model-info/branch/master/graph/badge.svg
  [5]: https://codecov.io/gh/jacklinke/django-model-info
  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [cookiecutter-djangopackage]: https://github.com/pydanny/cookiecutter-djangopackage