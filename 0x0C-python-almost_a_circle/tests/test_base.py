#!/usr/bin/python3
""" Uniitest for Base() """



import unittest
from models.base import Base


class TestPep8(unittest.TestCase):
    """Pep8 models/base.py & tests/test_models/test_base.py"""
    def test_pep8(self):
        """Pep8"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/base.py", "tests/test_models/test_base.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')


class TestBase_instances(unittest.TestCase):
    """run test with python3 -m unittest -v tests.base"""

    def test_class_docstring(self):
        classDoc = Base.__doc__
        self.assertTrue(len(classDoc) > 1)

    def test_no_arg(self):
        a = Base()
        b = Base()
        self.assertEqual(a.id, b.id - 1)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(3, 6)

    def test_None_id(self):
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_unique_id(self):
        c = Base(33)
        self.assertEqual(c.id, 33)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, b2.id + 1)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_boolean_id(self):
        self.assertEqual(Base(True).id, True)

    def test_id_public(self):
        b = Base(10)
        b.id = 13
        self.assertEqual(b.id, 13)

    def test_str_id(self):
        b = Base("Base-10")
        self.assertEqual(b.id, "Base-10")

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(3).__nb_instances)

    def test_float_id(self):
        self.assertEqual(3.4, Base(3.4).id)

    def test_list_id(self):
        self.assertEqual([3, 2, 1.6], Base([3, 2, 1.6]).id)

    def test_tuple_id(self):
        self.assertEqual((2, 5, 6), Base((2, 5, 6)).id)

    def test_dict_id(self):
        dic = {"a": 2, "b": 3, "c": 7}
        self.assertEqual(dic, Base(dic).id)

    def test_set_id(self):
        self.assertEqual({2, 3, 4}, Base({2, 3, 4}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({2, 3, 4}), Base(frozenset({2, 3, 4})).id)

    def test_range_id(self):
        self.assertEqual(range(4), Base(range(4)).id)

    def test_byte_id(self):
        self.assertEqual(b'Holberton', Base(b'Holberton').id)

    


if __name__ == "__main__":
    unittest.main()
