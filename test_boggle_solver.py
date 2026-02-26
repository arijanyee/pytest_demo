import unittest
import sys

sys.path.append("/home/codio/workspace/")

from boggle_solver import Boggle


class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

    # 3x3 Normal Case
    def test_normal_case_3x3(self):
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = sorted([x.upper() for x in solution])

        expected = sorted(["ABC", "ABDHI", "CFI", "DEA"])

        self.assertEqual(expected, solution)

    # 4x4 Larger Board
    def test_normal_case_4x4(self):
        grid = [
            ["T", "E", "S", "T"],
            ["A", "R", "E", "S"],
            ["B", "O", "G", "G"],
            ["L", "E", "X", "Y"]
        ]
        dictionary = ["test", "are", "bog", "boggle"]

        mygame = Boggle(grid, dictionary)
        solution = sorted([x.upper() for x in mygame.getSolution()])

        self.assertTrue("TEST" in solution)


class TestSuite_Simple_Edge_Cases(unittest.TestCase):

    # 1x1 Grid
    def test_square_grid_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "aa"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()

        self.assertEqual([], solution)

    # Empty Grid
    def test_empty_grid(self):
        grid = []
        dictionary = ["hello"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()

        self.assertEqual([], solution)

    # Empty Dictionary
    def test_empty_dictionary(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()

        self.assertEqual([], solution)

    # No Matches
    def test_no_matches(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["XYZ"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()

        self.assertEqual([], solution)


class TestSuite_Complete_Coverage(unittest.TestCase):

    # Diagonal Word
    def test_diagonal_word(self):
        grid = [
            ["C", "X"],
            ["X", "T"]
        ]
        dictionary = ["cat"]

        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]

        self.assertFalse("CT" in solution)

    # No Cell Reuse
    def test_no_cell_reuse(self):
        grid = [["A"]]
        dictionary = ["aa"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()

        self.assertFalse("aa" in solution)

    # Repeated Letters
    def test_repeated_letters(self):
        grid = [
            ["A", "A"],
            ["A", "A"]
        ]
        dictionary =["aaa"]

        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]

        self.assertTrue("AAA" in solution)


class TestSuite_Qu_and_St(unittest.TestCase):

    # QU Case
    def test_qu_case(self):
        grid = [
            ["Q", "U"],
            ["A", "T"]
        ]
        dictionary = ["quat"]

        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]

        self.assertTrue("QUAT" in solution)

    # ST Case
    def test_st_case(self):
        grid = [
            ["S", "T"],
            ["A", "R"]
        ]
        dictionary = ["star"]

        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]

        self.assertTrue("STAR" in solution)


if __name__ == '__main__':
    unittest.main()

