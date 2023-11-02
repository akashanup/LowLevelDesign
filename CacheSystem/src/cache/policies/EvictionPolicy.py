from abc import ABC, abstractmethod
from typing import TypeVar, Generic

Key = TypeVar("Key")


class EvictionPolicy(ABC, Generic[Key]):
    @abstractmethod
    def keyAccessed(self, key: Key) -> None:
        """
        Track the key which would be used while eviction.
        """
        pass

    @abstractmethod
    def evictKey(self) -> Key:
        """
        Evict key from eviction policy and return it

        Returns:
             Evicted key
        """
        pass
