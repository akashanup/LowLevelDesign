import unittest

from src.cache.Cache import Cache
from src.cache.factories.CacheFactory import CacheFactory


class CacheTest(unittest.TestCase):

    def setUp(self):
        self.cache: Cache[int, int] = CacheFactory[int, int]().defaultCache(3)

    def testItShouldBeAbleToGetAndAddItemsInTheCache(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        # Accessing 1 after 2 got inserted which makes 2 the least recently used till now.
        self.assertEqual(1, self.cache.get(1))
        self.cache.put(3, 3)
        self.assertEqual(3, self.cache.get(3))
        # Now if I try to add any element, the eviction should happen
        # Also eviction should happen based on LeastRecentlyUsedItem which is 2 in this case.
        self.cache.put(4, 4)
        # This should throw exception "Tried to access non-existing key."
        self.cache.get(2)
