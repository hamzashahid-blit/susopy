import pytest as pt
from src.main import *
from tests.boards import *


class TestCheck:
    def test_check_cell(self):
        for i in range(9): check_cell(i)
        check_cell(None)
        with pt.raises(Exception): check_cell(10)
        with pt.raises(Exception): check_cell(-1)

    def test_check_index(self):
        for i in range(9): check_index(i)
        with pt.raises(InvalidIndex): check_index(None)
        with pt.raises(InvalidIndex): check_index(10)
        with pt.raises(InvalidIndex): check_index(-1)

    def test_is_vector_valid(self):
        assert is_vector_valid([i for i in range(9)]) is True
        assert is_vector_valid([2, 3, 5, 4, 1, 7, 8, 6, 0]) is True
        assert is_vector_valid([2, 3, 5, 4, 1, 7, 8, 1, 4]) is False
        assert is_vector_valid([0, 1, 2, 0, 1, 2, 0, 1, 2]) is False
        assert is_vector_valid([None for i in range(9)]) is False
        assert is_vector_valid([None, 0, 1, 2, None, None, 4, None, 7]) is False
        assert is_vector_valid([0, 1, 2, None, 3, 4, 8, 7, 6]) is False
        with pt.raises(InvalidVector): is_vector_valid([])
        with pt.raises(InvalidVector): is_vector_valid([i for i in range(10)])
        with pt.raises(InvalidCell): is_vector_valid([10 for i in range(9)])
        with pt.raises(InvalidCell): is_vector_valid([-1 for i in range(9)])
        with pt.raises(InvalidCell): is_vector_valid([i for i in range(-1,8)])

    def test_flatten(self):
        assert flatten([]) == []
        assert flatten([[1,2],[3,4,5]]) == [1,2,3,4,5]
        assert flatten([0,-1,[-99,"Ho",1,1,0],[123,[None,-22,(True, [55, "loss"]),1],77,2.4],b'\x00']) == \
                       [0,-1,-99,'Ho',1,1,0,123,None,-22,True,55,"loss",1,77,2.4,b'\x00']

    def test_is_group_valid(self):
        assert is_group_valid([[i*3+j for j in range(3)] for i in range(3)]) is True
        assert is_group_valid([[0, 1, 2], [8, 6, 5], [3, 7, 4]]) is True
        assert is_group_valid([[0, 0, 0], [0, 1, 2], [0, 2, 4]]) is False
        with pt.raises(InvalidCell): is_group_valid([[0, 10, 0], [0, 1, 2], [0, 2, 4]])
        with pt.raises(InvalidCell): is_group_valid([[0, 1, 2], [9, 6, 5], [3, 7, 4]])
        with pt.raises(InvalidCell): is_group_valid([[0, 1, 2], [-1, 6, 5], [3, 7, 4]])
        with pt.raises(InvalidVector): is_group_valid([[0, 1, 2], [3, 7, 4]])
        assert is_group_valid([[None]*3 for i in range(3)]) is False
        with pt.raises(InvalidVector): is_group_valid([[0, 10], [0, 1, 2], [0, 2, 4]])

    def test_get_group(self):
        assert get_group(wrong_complete_board, 0) == [[9, 7, 4], [6, 3, 8], [1, 2, 5]]
        assert get_group(wrong_complete_board, 5) == [[2, 8, 9], [5, 6, 3], [4, 1, 7]]
        assert get_group(wrong_complete_board, 8) == [[3, 9, 4], [8, 7, 1], [6, 2, 5]]
        assert get_group(right_complete_board, 8) == [[7, 6, 5], [1, 9, 2], [4, 3, 8]]
        assert get_group(bogus_board, 6)          == [[54, 55, 56], [63, 64, 65], [72, 73, 74]]
        with pt.raises(InvalidIndex): get_group(wrong_complete_board, 9)
        with pt.raises(InvalidIndex): get_group(bogus_board, -1)
