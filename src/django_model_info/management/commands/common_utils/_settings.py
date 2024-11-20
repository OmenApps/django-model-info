"""Django management command to display model field relationships."""
import logging

from django.core.exceptions import ImproperlyConfigured

logger = logging.getLogger(__name__)

try:
    from django.conf import settings
except ImproperlyConfigured as e:
    logger.error("Settings could not be imported: %s", e)
    settings = None  # pylint: disable=C0103
except ImportError as e:
    logger.error("Django could not be imported. Settings cannot be loaded: %s", e)
    settings = None  # pylint: disable=C0103

_DJANGO_MODEL_INFO = getattr(settings, "DJANGO_MODEL_INFO", {})
"""dict: The settings for the django-model-info app."""

CACHE_ENABLED = _DJANGO_MODEL_INFO.get("CACHE_ENABLED", False)
"""bool: Enable caching of results."""

CACHE_ALWAYS = _DJANGO_MODEL_INFO.get("CACHE_ALWAYS", False)
"""bool: Always cache results, even if the --use-cache flag is not used."""

CACHE_ALIAS = _DJANGO_MODEL_INFO.get("CACHE_ALIAS", "default")
"""str: The cache alias to use for caching results."""

CACHE_TIMEOUT = _DJANGO_MODEL_INFO.get("CACHE_TIMEOUT", 3600)
"""int: The cache timeout in seconds."""

CACHE_KEY_PREFIX = _DJANGO_MODEL_INFO.get("CACHE_KEY_PREFIX", "model_filters:")
"""str: The prefix to use for cache keys."""

CACHE_VERSION_KEY = f"{CACHE_KEY_PREFIX}version"
"""str: The cache key for the cache version."""
