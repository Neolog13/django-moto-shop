from django.core.cache import cache


class CacheMixin:
    """
    Retrieves data from the cache or sets it if not already cached.

    If the data for the specified cache name is not found, the method
    will execute the query, store the result in the cache, and return it.
    If the data is already cached, it will be returned directly.

    Args:
        query (any): The data or query to be cached if it is not found in the cache.
        cache_name (str): The key used to store and retrieve data from the cache.
        cache_time (int): The time (in seconds) for which the data should remain in the cache.

    Returns:
        any: The data either retrieved from the cache or set after executing the query.
    """
    def set_get_cache(self, query, cache_name, cache_time):
        data = cache.get(cache_name)

        if not data:
            data = query
            cache.set(cache_name, data, cache_time)

        return data