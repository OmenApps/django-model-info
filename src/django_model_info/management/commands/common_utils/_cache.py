
import logging

from django.core.cache import caches
from django.core.management.base import BaseCommand

from ._settings import CACHE_ALIAS, CACHE_ENABLED, CACHE_KEY_PREFIX, CACHE_VERSION_KEY

logger = logging.getLogger(__name__)


cache = {}

if CACHE_ENABLED:
    try:
        cache = caches[CACHE_ALIAS]
    except KeyError as e:
        raise ValueError(f"Cache alias '{CACHE_ALIAS}' not found in settings.CACHES") from e


def get_cache_version() -> int:
    """Get the current cache version."""
    return cache.get(CACHE_VERSION_KEY, 0)

def increment_cache_version(command: BaseCommand) -> None:
    """Increment the cache version to invalidate all cached results."""
    current_version = command.get_cache_version()
    cache.set(CACHE_VERSION_KEY, current_version + 1)
    command.stdout.write(command.style.SUCCESS("Cleared all cached results"))

def clear_model_filters_cache(command: BaseCommand):
    """Clear all cached results for model_filters."""
    # Get all keys that start with our prefix
    keys = cache.keys(f"{CACHE_KEY_PREFIX}*")
    if keys:
        cache.delete_many(keys)
        command.stdout.write(command.style.SUCCESS(f"Cleared {len(keys)} cached results"))
    else:
        command.stdout.write("No cached results found")
