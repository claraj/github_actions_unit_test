from unittest import TestCase
import shape 


class TestShape(TestCase):

    def test_circle_area(self):
        expected = 314.159265359
        actual = shape.circle_area(10)
        self.assertAlmostEqual(expected, actual)


    def test_triangle_area(self):
        expected = 6   # base = 3, height = 4 area = 3 * 4 / 2 = 6
        actual = shape.triangle_area(3, 4)
        self.assertEqual(expected, actual)

        