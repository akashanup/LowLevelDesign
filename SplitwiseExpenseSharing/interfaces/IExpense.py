from abc import ABCMeta, abstractmethod


class IExpense(metaclass=ABCMeta):

    @abstractmethod
    def split(self) -> dict:
        """Abstract Method"""
