import unittest
from vector import Vector

class TestVector(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1,2
        return super().setUp()
    

    def create_2D_vector(self):
        return Vector(self.x, self.y)
    

    def test_create_2D_vector(self):
        v = self.create_2D_vector()
        self.assertEqual(v.numbers, (self.x, self.y))


    def test_create_5D_vector(self):
        v = Vector(-1, 0, -5, -50.2, 52.2)
        self.assertEqual(v.numbers, (-1, 0, -5, -50.2, 52.2))


    def test_create_empty_vector(self):
        with self.assertRaises(ValueError):
            v = Vector()
    

    def test_2_vectors_equal(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1,2)
        self.assertEqual(v1,v2)
        '''
        ytlig likhet vs djup likhet
        om inte __eq__ är implementerat jämförs bara minnesaddressen

        '''
    

    def test_2_vectors_not_equal(self):
        v1 = self.create_2D_vector()
        v2 = Vector(3, 2)
    

    def test_add_2_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1, -2)
        self.assertEqual(v1+v2, Vector(2,0))


    def test_add_vector_diff_dimensions(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1,0,1)
        with self.assertRaises(TypeError):
            v3 = v1+v2


    def test_multiply_scalar(self):
        v1 = self.create_2D_vector()
        v2 = v1*5
        self.assertEqual(v2, Vector(5,10))


    def test_rmult_scalar(self):
        v1 = self.create_2D_vector()
        v2 = 5*v1
        self.assertEqual(v2, Vector(5,10))


    def test_sub_2_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1,2)
        self.assertEqual(v1-v2, Vector(0,0))


    def test_len(self):
        v1 = self.create_2D_vector()
        self.assertEqual(len(v1), 2)


    def test_getitem(self):
        v1 = self.create_2D_vector()
        for i, number in enumerate((1, 2)):
            self.assertEqual(v1[i], number)


    def test_abs(self):
        v1 = Vector(0,1)
        self.assertEqual(abs(v1), 1)


if __name__ == "__main__":
    unittest.main()