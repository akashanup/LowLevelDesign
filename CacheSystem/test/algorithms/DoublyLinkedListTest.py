import unittest

from src.algorithms.DoublyLinkedList import DoublyLinkedList
from src.algorithms.DoublyLinkedListNode import DoublyLinkedListNode
from typing import List


class DoublyLinkedListTest(unittest.TestCase):

    def testDLLAddition(self):
        node1: DoublyLinkedListNode[int] = DoublyLinkedListNode(1)
        node2: DoublyLinkedListNode[int] = DoublyLinkedListNode(2)
        node3: DoublyLinkedListNode[int] = DoublyLinkedListNode(3)
        node4: DoublyLinkedListNode[int] = DoublyLinkedListNode(4)

        dll: DoublyLinkedList[int] = DoublyLinkedList[int]()

        dll.addNodeAtLast(node1)
        self.__verifyDLL(dll, [1])

        dll.addNodeAtLast(node2)
        self.__verifyDLL(dll, [1, 2])

        dll.addNodeAtLast(node3)
        self.__verifyDLL(dll, [1, 2, 3])

        dll.addNodeAtLast(node4)
        self.__verifyDLL(dll, [1, 2, 3, 4])

        dll.addElementAtLast(5)
        self.__verifyDLL(dll, [1, 2, 3, 4, 5])

    def testDLLNodeDetachment(self):
        dll: DoublyLinkedList[int] = DoublyLinkedList[int]()
        node1: DoublyLinkedListNode[int] = dll.addElementAtLast(1)
        node2: DoublyLinkedListNode[int] = dll.addElementAtLast(2)
        node3: DoublyLinkedListNode[int] = dll.addElementAtLast(3)
        node4: DoublyLinkedListNode[int] = dll.addElementAtLast(4)
        node5: DoublyLinkedListNode[int] = dll.addElementAtLast(5)

        self.__verifyDLL(dll, [1, 2, 3, 4, 5])

        dll.detachNode(node1)
        self.__verifyDLL(dll, [2, 3, 4, 5])

        dll.detachNode(node5)
        self.__verifyDLL(dll, [2, 3, 4])

        dll.detachNode(node3)
        self.__verifyDLL(dll, [2, 4])

        dll.detachNode(node2)
        self.__verifyDLL(dll, [4])

    def __verifyDLL(self, dll: DoublyLinkedList[int], expected: List[int]):
        self.assertEqual(expected[0], dll.getFirstNode().element)
        self.assertEqual(expected[-1], dll.getLastNode().element)
        currentNode = dll.getFirstNode()
        for element in expected:
            self.assertIsNotNone(currentNode)
            self.assertEqual(element, currentNode.element)
            currentNode = currentNode.next
        self.assertIsNone(currentNode.element)
