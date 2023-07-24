import pytest as pt
from src.check import *
from tests.boards import *


class TestCheck:
    def test_check_cell(self):
        for i in range(9): check_cell(i)
        check_cell(0)
        with pt.raises(Exception): check_cell(10)
        with pt.raises(Exception): check_cell(-1)

    def test_check_index(self):
        for i in range(9): check_index(i)
        with pt.raises(InvalidIndex): check_index(None)
        with pt.raises(InvalidIndex): check_index(10)
        with pt.raises(InvalidIndex): check_index(-1)

    def test_is_vector_valid(self):
        assert is_vector_valid([i for i in range(1,10)]) is True
        assert is_vector_valid([2, 3, 5, 4, 1, 7, 8, 6, 9]) is True
        assert is_vector_valid([2, 3, 5, 4, 1, 7, 8, 6, 0]) is False
        assert is_vector_valid([2, 3, 5, 4, 1, 7, 8, 1, 4]) is False
        assert is_vector_valid([0, 1, 2, 0, 1, 2, 0, 1, 2]) is False
        assert is_vector_valid([0, 1, 2, 0, 1, 2, 0, 1, 2], True) is False
        assert is_vector_valid([2, 3, 5, 4, 1, 7, 8, 6, 9], True) is True
        assert is_vector_valid([2, 3, 5, 4, 1, 7, 8, 6, 0], True) is True
        assert is_vector_valid([2, 3, 5, 4, 1, 7, 8, 1, 4], True) is False
        assert is_vector_valid([0 for i in range(9)]) is False
        assert is_vector_valid([0, 1, 2, 3, 0, 0, 5, 0, 8]) is False
        assert is_vector_valid([1, 2, 3, 0, 4, 5, 9, 8, 7]) is False
        assert is_vector_valid([0, 1, 2, 3, 0, 0, 5, 0, 8], True) is True # empty cell repitition is allowed
        assert is_vector_valid([1, 2, 3, 0, 4, 5, 9, 8, 7], True) is True
        with pt.raises(InvalidVector): is_vector_valid([])
        with pt.raises(InvalidVector): is_vector_valid([i for i in range(10)])
        with pt.raises(InvalidCell): is_vector_valid([10 for i in range(9)])
        with pt.raises(InvalidCell): is_vector_valid([-1 for i in range(9)])

    def test_flatten(self):
        assert flatten([]) == []
        assert flatten([[1,2],[3,4,5]]) == [1,2,3,4,5]
        assert flatten([0,-1,[-99,"Ho",1,1,0],[123,[None,-22,(True, [55, "loss"]),1],77,2.4],b'\x00']) == \
                       [0,-1,-99,'Ho',1,1,0,123,None,-22,True,55,"loss",1,77,2.4,b'\x00']

    def test_is_group_valid(self):
        assert is_group_valid([[i*3+j+1 for j in range(3)] for i in range(3)]) is True
        assert is_group_valid([[1, 2, 3], [9, 7, 6], [4, 8, 5]]) is True
        assert is_group_valid([[1, 1, 1], [1, 2, 3], [1, 3, 5]]) is False
        with pt.raises(InvalidCell): is_group_valid([[1, 11, 1], [1, 2, 3], [1, 3, 5]])
        with pt.raises(InvalidCell): is_group_valid([[1, 2, 3], [10, 7, 6], [4, 8, 5]])
        with pt.raises(InvalidCell): is_group_valid([[1, 2, 3], [-1, 7, 6], [4, 8, 5]])
        with pt.raises(InvalidVector): is_group_valid([[1, 2, 3], [4, 8, 5]])
        assert is_group_valid([[0]*3 for i in range(3)]) is False
        with pt.raises(InvalidVector): is_group_valid([[0, 10], [0, 1, 2], [0, 2, 4]])
        with pt.raises(InvalidVector): is_group_valid([[1, 11], [1, 2, 3], [1, 3, 5]])

    def test_get_group(self):
        assert get_group(wrong_complete_board, 0) == [[7, 9, 4], [6, 3, 8], [1, 2, 5]]
        assert get_group(wrong_complete_board, 5) == [[2, 8, 9], [5, 6, 3], [4, 1, 7]]
        assert get_group(wrong_complete_board, 8) == [[3, 9, 4], [8, 7, 1], [6, 2, 5]]
        assert get_group(right_complete_board, 8) == [[7, 6, 5], [1, 9, 2], [4, 3, 8]]
        assert get_group(bogus_board, 6)          == [[54, 55, 56], [63, 64, 65], [72, 73, 74]]
        with pt.raises(InvalidIndex): get_group(wrong_complete_board, 9)
        with pt.raises(InvalidIndex): get_group(bogus_board, -1)

    def test_get_groups(self):
        assert get_groups(pattern_board) == [[[0, 1, 2], [0, 1, 2], [0, 1, 2]],
                                             [[3, 4, 5], [3, 4, 5], [3, 4, 5]],
                                             [[6, 7, 8], [6, 7, 8], [6, 7, 8]],
                                             [[0, 1, 2], [0, 1, 2], [0, 1, 2]],
                                             [[3, 4, 5], [3, 4, 5], [3, 4, 5]],
                                             [[6, 7, 8], [6, 7, 8], [6, 7, 8]],
                                             [[0, 1, 2], [0, 1, 2], [0, 1, 2]],
                                             [[3, 4, 5], [3, 4, 5], [3, 4, 5]],
                                             [[6, 7, 8], [6, 7, 8], [6, 7, 8]]]
        assert get_groups(wrong_complete_board) == [[[7, 9, 4], [6, 3, 8], [1, 2, 5]],
                                                    [[2, 3, 6], [5, 9, 1], [4, 8, 7]],
                                                    [[1, 5, 8], [7, 4, 2], [9, 3, 6]],
                                                    [[3, 1, 6], [7, 4, 2], [5, 8, 9]],
                                                    [[7, 5, 4], [9, 1, 8], [3, 6, 2]],
                                                    [[2, 8, 9], [5, 6, 3], [4, 1, 7]],
                                                    [[8, 6, 7], [2, 5, 3], [4, 9, 1]],
                                                    [[1, 2, 5], [6, 4, 9], [8, 7, 3]],
                                                    [[3, 9, 4], [8, 7, 1], [6, 2, 5]]]

    def test_check_board(self):
        for board in solution_boards:
            assert check_board(board) == True
        # TODO: Find a wrong dataset...
        assert check_board(wrong_complete_board) == False
        assert check_board(right_complete_board) == True
