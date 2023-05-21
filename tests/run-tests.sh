#!/bin/env sh
fd -t f ".*\.py" ~/dev/sudoku-solver | entr -c pytest -v -s
