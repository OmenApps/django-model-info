
# django-model-info

[![image][]][1]

[![image][2]][3]

[![image][4]][5]

A Django Management Command for displaying details about your project's models.

**Warning**: This project is still very new. Expect to see proper testing and an example app demonstrating the command soon.

When working with large projects or when returning to a code base after some time away, it can be challenging to remember all of the fields and methods associated with your models. This command makes it easy to see:

- basic details about each model, such as the database table name, the file and line number where the model is located, etc.
- what fields are available
- how each field is referred to in queries (direct/reverse relations)
- each field’s class
- each field’s representation type in the database
- what methods are available
- method signatures
- method location and line number
- etc

This package takes the original [`list_model_info`](https://django-extensions.readthedocs.io/en/latest/list_model_info.html) command I wrote for django-extensions to a whole new level. I attempted to simplify some aspects of configuration, while increasing the overall amount of information provided.

The beautiful interface is thanks to [`rich`](https://github.com/willmcgugan/rich/)

## Documentation

The full documentation will (soon) be at <https://django-model-info.readthedocs.io>.

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

Run the management command:

``` bash
>>> python manage.py model_info
```

An example of the resulting output can be seen [here](https://htmlpreview.github.io/?https://github.com/jacklinke/django-model-info/blob/master/example-output.html). This example shows the most verbose (level 3)  details for a single model.

## Features

You can customize the output in a number of ways.

### Verbosity

Verbosity levels adjust the amount of information displayed to the console, and is set with the `-v` or `--verbosity` argument.

- 0  - Model names only - Convenient when you just need a list of all your project's models in one place
- 1  - Model names, field names, and non-dunder/common model method names
- 2  - Model names, field names & details, and non-dunder/common model method names & details
- 3  - Model names, field names & details, and all model method names & full details

Note: The default verbosity in `django-model-info` is **2**

From the command-line:
``` bash
>>> python manage.py model_info --v 0
>>> python manage.py model_info --verbosity 0
```

You can specify a different default verbosity value in your settings file.

``` python
MODEL_INFO_VERBOSITY = 1
```

### Filter

By default, all models within your project are processed and displayed. For large projects, this can result in an enormous output. If you want to limit output to a subset of models, you can use the `-f` or `--filter` argument, providing one or more of the following:

- Models, in the form of `appname.Model`
- Apps, in the form of `appname`

If Django is unable to find provided entries, a message will be written to the console, and the remaining models will be processed and displayed.

From the command-line, here is an example that processes all models in the `myapp` and `auth` apps, and also the `otherapp.SpecificModel` model:
``` bash
>>> python manage.py model_info --f myapp otherapp.SpecificModel auth
>>> python manage.py model_info --filter myapp otherapp.SpecificModel auth
```

You can specify a list of default apps and models to process in your settings file. Using the command-line example names above:

``` python
MODEL_INFO_FILTER = ["myapp", "otherapp.SpecificModel", "auth"]
```

### Export

`django-model-info` can optionally export the console output to an html or text file. The extension of the provided filename must be `.txt`, `.htm`, or `.html`.

``` bash
>>> python manage.py model_info -e myfilename.html
>>> python manage.py model_info --export myfilename.html
```


## Running Tests

In progress.

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

## Credits

Tools used in rendering this package:

-   [Cookiecutter](https://github.com/audreyr/cookiecutter)
-   [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
-   [rich](https://github.com/willmcgugan/rich/)

  [image]: https://badge.fury.io/py/django-model-info.svg
  [1]: https://badge.fury.io/py/django-model-info
  [2]: https://travis-ci.org/jacklinke/django-model-info.svg?branch=master
  [3]: https://travis-ci.org/jacklinke/django-model-info
  [4]: https://codecov.io/gh/jacklinke/django-model-info/branch/master/graph/badge.svg
  [5]: https://codecov.io/gh/jacklinke/django-model-info
  