from abc import ABC, abstractmethod
from typing import TypeVar, Generic

Key = TypeVar("Key")
Value = TypeVar("Value")


class Storage(ABC, Generic[Key, Value]):
    @abstractmethod
    def add(self, key: Key, value: Value) -> None:
        """
        Add a key-value pair to storage

        Raises:
            StorageFullException: If the storage is full.
        """
        pass

    @abstractmethod
    def remove(self, key: Key) -> None:
        """
        Remove the value associated with 'key' from the storage.

        Raises:
             NotFoundException: If the key is not found.
        """
        pass

    @abstractmethod
    def get(self, key: Key) -> Value:
        """
        Get the value associated with 'key'.

        Returns:
            The value associated with 'key'

        Raises:
             NotFoundException: If the key is not found.
        """
        pass
