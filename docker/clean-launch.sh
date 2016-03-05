#!/bin/bash
find /src -depth \( -name __pycache__ -o -name '*.pyc' \) -print0 | xargs -0 rm -rf
exec "$@"
