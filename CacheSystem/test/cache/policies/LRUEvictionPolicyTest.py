import unittest

from src.cache.policies.LRUEvictionPolicy import LRUEvictionPolicy


class LRUEvictionPolicyTest(unittest.TestCase):

    def setUp(self):
        self.lruEvictionPolicy: LRUEvictionPolicy[int] = LRUEvictionPolicy()

    def testNoKeyToEvictInitially(self):
        self.assertIsNone(self.lruEvictionPolicy.evictKey())

    def testKeysAreEvictedInTheOrderTheyWereAccessed(self):
        self.lruEvictionPolicy.keyAccessed(1)
        self.lruEvictionPolicy.keyAccessed(2)
        self.lruEvictionPolicy.keyAccessed(3)
        self.lruEvictionPolicy.keyAccessed(4)
        self.assertEqual(1, self.lruEvictionPolicy.evictKey())
        self.assertEqual(2, self.lruEvictionPolicy.evictKey())
        self.assertEqual(3, self.lruEvictionPolicy.evictKey())
        self.assertEqual(4, self.lruEvictionPolicy.evictKey())

    def testReaccessingKeyPreventsItFromEviction(self):
        self.lruEvictionPolicy.keyAccessed(1)
        self.lruEvictionPolicy.keyAccessed(2)
        self.lruEvictionPolicy.keyAccessed(3)
        self.lruEvictionPolicy.keyAccessed(2)
        self.lruEvictionPolicy.keyAccessed(4)
        self.lruEvictionPolicy.keyAccessed(1)
        self.lruEvictionPolicy.keyAccessed(5)
        self.assertEqual(3, self.lruEvictionPolicy.evictKey())
        self.assertEqual(2, self.lruEvictionPolicy.evictKey())
        self.assertEqual(4, self.lruEvictionPolicy.evictKey())
        self.assertEqual(1, self.lruEvictionPolicy.evictKey())
        self.assertEqual(5, self.lruEvictionPolicy.evictKey())
