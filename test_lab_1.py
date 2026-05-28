import unittest
from lab_1 import is_empty

class TestIsEmpty(unittest.TestCase):

    def test_empty_stack(self):
        self.assertTrue(is_empty([]), "Должно возвращать True для пустого стека")

    def test_one_element(self):
        self.assertFalse(is_empty([5]), "Должно возвращать False для стека с одним элементом")

    def test_many_elements(self):
        self.assertFalse(is_empty([1, 2, 3, 4]), "Должно возвращать False для непустого стека")

    def test_after_clear(self):
        stack = [1, 2, 3]
        stack.clear()
        self.assertTrue(is_empty(stack), "Должно возвращать True после очистки стека")

if __name__ == '__main__':
    unittest.main()