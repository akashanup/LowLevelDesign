from typing import TypeVar, Generic, Optional

Element = TypeVar("Element")


class DoublyLinkedListNode(Generic[Element]):

    def __init__(self, element: Element) -> None:
        self.element: Element = element
        self.next: Optional[DoublyLinkedListNode[Element]] = None
        self.prev: Optional[DoublyLinkedListNode[Element]] = None
