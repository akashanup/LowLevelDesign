from typing import TypeVar, Generic, Optional

from src.algorithms.DoublyLinkedListNode import DoublyLinkedListNode
from src.algorithms.exceptions.InvalidElementException import InvalidElementException

Element = TypeVar("Element")


class DoublyLinkedList(Generic[Element]):

    def __init__(self):
        # Instantiate dummy head and tail by null, since we are never going to use values for these dummy nodes
        self.__head: DoublyLinkedListNode[Element] = DoublyLinkedListNode[Element](None)
        self.__tail: DoublyLinkedListNode[Element] = DoublyLinkedListNode[Element](None)
        # Also initially there are no items, so join head and tail. We can add items in between them easily.
        self.__head.next = self.__tail
        self.__tail.prev = self.__head

    def detachNode(self, node: DoublyLinkedListNode[Element]) -> None:
        """
        Method to detach a random node from the doubly linked list.
        The node itself will not be removed from the memory.
        Just that it will be removed from the list and become orphaned.

        :param node:
            Node to remove from the doubly linked list
        """
        if node:
            node.prev.next = node.next
            node.next.prev = node.prev

    def addElementAtLast(self, element: Element) -> DoublyLinkedListNode[Element]:
        """
        Method to add an element at the end of the list.

        :param element:
            Element to be added at last
        :return:
            Node that is added for the element.
        """
        if not element:
            raise InvalidElementException("")
        node: DoublyLinkedListNode[Element] = DoublyLinkedListNode[Element](element)
        self.addNodeAtLast(node)
        return node

    def getFirstNode(self) -> Optional[DoublyLinkedListNode[Element]]:
        if not self.__isListPresent():
            return None
        return self.__head.next

    def getLastNode(self) -> Optional[DoublyLinkedListNode[Element]]:
        if not self.__isListPresent():
            return None
        return self.__tail.prev

    def __isListPresent(self) -> bool:
        """
        Method to check whether the list is present

        :return:
            True if the list exists else False
        """
        return self.__head.next != self.__tail

    def addNodeAtLast(self, node: DoublyLinkedListNode[Element]) -> None:
        """
        Helper method to add a node at the end of the list.
        :param node:
            Node to add at the last of doubly linked list
        """
        trailPrev: DoublyLinkedListNode[Element] = self.__tail.prev
        trailPrev.next = node
        node.prev = trailPrev
        node.next = self.__tail
        self.__tail.prev = node
