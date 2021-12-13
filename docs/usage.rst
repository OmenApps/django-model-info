=====
Usage
=====

To use django-model-info in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_model_info.apps.DjangoModelInfoConfig',
        ...
    )

Add django-model-info's URL patterns:

.. code-block:: python

    from django_model_info import urls as django_model_info_urls


    urlpatterns = [
        ...
        url(r'^', include(django_model_info_urls)),
        ...
    ]
