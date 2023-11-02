from typing import Generic, TypeVar, Dict

from src.cache.exceptions.NotFoundException import NotFoundException
from src.cache.exceptions.StorageFullException import StorageFullException
from src.cache.storage.Storage import Storage

Key = TypeVar("Key")
Value = TypeVar("Value")


class HashmapBasedStorage(Storage[Key, Value], Generic[Key, Value]):

    def __init__(self, capacity: int) -> None:
        self.__hashmap: Dict[Key, Value] = {}
        self.__capacity: int = capacity

    def add(self, key: Key, value: Value) -> None:
        if self.__isStorageFull():
            raise StorageFullException("Capacity Full...")
        self.__hashmap[key] = value

    def remove(self, key: Key) -> None:
        if key not in self.__hashmap:
            raise NotFoundException(f"{key} doesn't exist in cache.")
        del self.__hashmap[key]

    def get(self, key: Key) -> Value:
        if key not in self.__hashmap:
            raise NotFoundException(f"{key} doesn't exist in cache.")
        return self.__hashmap[key]

    def __isStorageFull(self) -> bool:
        return len(self.__hashmap) == self.__capacity
