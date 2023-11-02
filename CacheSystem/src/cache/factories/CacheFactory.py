from typing import TypeVar, Generic

from src.cache.Cache import Cache
from src.cache.policies.LRUEvictionPolicy import LRUEvictionPolicy
from src.cache.storage.HashmapBasedStorage import HashmapBasedStorage

Key = TypeVar("Key")
Value = TypeVar("Value")


class CacheFactory(Generic[Key, Value]):

    def defaultCache(self, capacity: int) -> Cache[Key, Value]:
        cache: Cache[Key, Value] = Cache[Key, Value](LRUEvictionPolicy[Key](), HashmapBasedStorage[Key, Value](capacity))
        return cache
