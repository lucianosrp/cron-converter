import unittest
from part import Part
from units import units

from tests.statics.invalid_ranges import invalid_ranges


class PartTestInvalid(unittest.TestCase):

    def test_from_string_invalid_0(self):
        for invalid_range in invalid_ranges:
            with self.subTest(range=invalid_range):
                part = Part(units[invalid_range['unit']], {})
                with self.assertRaises(ValueError, msg=invalid_range['error']):
                    part.from_string(invalid_range['input'])
