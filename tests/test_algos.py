import pytest as pt
from src.algos import *
from tests.boards import *


class TestAlgos:
    def test_backtrack (self):
        assert check_board(backtrack(easy_board), False) == True
        for i in range(len(problem_boards)):
            assert backtrack(problem_boards[i]) == solution_boards[i]
