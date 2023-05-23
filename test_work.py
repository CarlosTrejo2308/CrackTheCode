import unittest
import work

class TestWork(unittest.TestCase):
    def test_square(self):
        cases = [
            (4, 16),
            (9, 81),
            (16, 256)
        ]

        for inp, expected in cases:
            with self.subTest(inp=inp, expected=expected):
                obtained = work.square(inp)
                self.assertEqual(obtained, expected, "square(%s) should be %s" % (inp, expected))

    def test_bubbleSort(self):
        cases = [
            ([5, 3, 5, 1, 9, 2, 4, 7, 8, 6, 12], [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 12]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        ]

        for inp, expected in cases:
            with self.subTest(inp=inp, expected=expected):
                obtained = work.bubbleSort(inp)
                self.assertEqual(obtained, expected, "bubblesort(%s) should be %s" % (inp, expected))

    def test_triple(self):
        cases = [
            (3, 9),
            (7, 21),
            (11,33)
        ]
        for inp, expected in cases:
            with self.subTest(inp=inp, expected=expected):
                obtained = work.triple(inp)
                self.assertEqual(obtained, expected, "Triple(%s) should be %s" % (inp, expected))

    def test_minNum(self):
        cases = [
            ([2,4,5,1,6,7,9],1),
            ([32,12,54,49,53,13,42],12),
            ([8,23,12,49,21,43,23,85,54,12],8)
            ]
        for inp, expected in cases:
            with self.subTest(inp=inp, expected=expected):
                obtained = work.minNum(inp)
                self.assertEqual(obtained, expected, "minNum(%s) should be %s" % (inp, expected))

    def test_sumArray(self):
        cases = [
            ([1,2,3,4,5,6,7,8,9],45),
            ([5,5,5,5,5,5],30),
            ([7,18,3,5,12,2,9,1],57)
            ]
        for inp, expected in cases:
            with self.subTest(inp=inp, expected=expected):
                obtained = work.sumArray(inp)
                self.assertEqual(obtained, expected, "sumArray(%s) should be %s" % (inp, expected))

if __name__ == '__main__':
    unittest.main()