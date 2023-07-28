#!/bin/env sh
fd -t f ".*\.py" ~/dev/susopy | entr -c pytest -v -s
