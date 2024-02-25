import unittest
from prostoe import prost

class ProstTestCase(unittest.TestCase):
    def test_prost(self):
        self.assertEqual(prost(4),False)
        self.assertEqual(prost(3), True)
        self.assertEqual(prost(4),True)#здесь тест провалится (строка 8)

if __name__ == "__main__":
  unittest.main()