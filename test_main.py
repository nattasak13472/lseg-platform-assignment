import unittest
from main import get_nested_value

class TestGetNestedValue(unittest.TestCase):
    
    def test_success(self):
        obj = {"a": {"b": {"c": "d"}}}
        self.assertEqual(get_nested_value(obj, "a/b/c"), "d")
        
    def test_five_level(self):
        obj = {"a": {"b": {"c": {"d": { "e": "f"}}}}}
        self.assertEqual(get_nested_value(obj, "a/b/c/d/e"), "f")
            
    def test_key_not_match(self):
        obj = {"a": {"b": {"c": "d"}}}
        with self.assertRaises(KeyError):
            get_nested_value(obj, "a/b/d")

    def test_invalid_key(self):
        obj = {"a": {"b": {"c": "d"}}}
        with self.assertRaises(KeyError):
            get_nested_value(obj, "a-b-c")

    def test_object_invalid_type(self):
        obj = [{"a": {"b": {"c": "d"}}}]
        with self.assertRaises(TypeError):
            get_nested_value(obj, "a/b")

if __name__ == '__main__':
    unittest.main()