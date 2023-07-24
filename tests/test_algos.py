import pytest as pt
from src.algos import *
from tests.boards import *


class TestAlgos:
    def test_backtrack (self):
        # assert backtrack(problem_boards[0]) is solution_boards[0]
        assert check_board(backtrack_recursive(easy_board), False) == True
        # assert check_board(problem_boards[0], True) == True
