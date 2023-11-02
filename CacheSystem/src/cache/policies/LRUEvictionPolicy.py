from typing import TypeVar, Generic, Dict, Optional

from src.algorithms.DoublyLinkedList import DoublyLinkedList
from src.algorithms.DoublyLinkedListNode import DoublyLinkedListNode
from src.cache.policies.EvictionPolicy import EvictionPolicy

Key = TypeVar("Key")


class LRUEvictionPolicy(EvictionPolicy[Key], Generic[Key]):
    """
    Eviction policy based on LRU algorithm.
    """

    def __init__(self):
        self.__dll: DoublyLinkedList[Key] = DoublyLinkedList[Key]()
        self.__mapper: Dict[Key, DoublyLinkedListNode[Key]] = {}

    def keyAccessed(self, key: Key) -> None:
        if key in self.__mapper:
            self.__dll.detachNode(self.__mapper[key])
            self.__dll.addNodeAtLast(self.__mapper[key])
        else:
            node: DoublyLinkedListNode[Key] = self.__dll.addElementAtLast(key)
            self.__mapper[key] = node

    def evictKey(self) -> Optional[Key]:
        firstNode: DoublyLinkedListNode[Key] = self.__dll.getFirstNode()
        if not firstNode:
            return None
        self.__dll.detachNode(firstNode)
        return firstNode.element
