from typing import Generic, TypeVar, Optional

from src.cache.exceptions.NotFoundException import NotFoundException
from src.cache.exceptions.StorageFullException import StorageFullException
from src.cache.policies.EvictionPolicy import EvictionPolicy
from src.cache.storage.Storage import Storage

Key = TypeVar("Key")
Value = TypeVar("Value")


class Cache(Generic[Key, Value]):

    def __init__(self, evictionPolicy: EvictionPolicy[Key], storage: Storage[Key, Value]) -> None:
        self.__evictionPolicy: EvictionPolicy[Key] = evictionPolicy
        self.__storage: Storage[Key, Value] = storage

    def put(self, key: Key, value: Value) -> None:
        try:
            self.__storage.add(key, value)
            self.__evictionPolicy.keyAccessed(key)
        except StorageFullException as ex:
            print("Got storage full. Will try to evict.")
            keyToRemove: Key = self.__evictionPolicy.evictKey()
            if not keyToRemove:
                raise RuntimeError("Unexpected state. Storage full and no key to evict.")
            self.__storage.remove(keyToRemove)
            self.put(key, value)

    def get(self, key: Key) -> Optional[Value]:
        try:
            value: Value = self.__storage.get(key)
            self.__evictionPolicy.keyAccessed(key)
            return value
        except NotFoundException as ex:
            print("Tried to access non-existing key.")
            return None
