#!/usr/bin/env bash
set -eu -o pipefail
HERE="$(
    unset CDPATH
    cd "$(dirname "$0")"
    pwd
)"
cd "$HERE"

HATCH_CURRENT=$(hatch version)
TAG=${1:?"a tag must be provided. Consider using hatch's next: V$HATCH_CURRENT"}

# towncrier needs the version to be tagged before running
git tag "$TAG"

# generate the changelog
hatch run towncrier build --yes

# re-tag
git tag -f "$TAG"

echo "To release, run 'git push origin --tags \"$TAG\"'"
