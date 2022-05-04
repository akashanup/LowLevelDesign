from enum import Enum


class ExpenseType(Enum):
    EQUAL = 'equal'
    EXACT = 'exact'
    PERCENT = 'percent'
