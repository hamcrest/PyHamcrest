#!/usr/bin/env bash
HERE=$(unset CDPATH; cd `dirname $0`; pwd)
cd $HERE

function do_release() {
    local rc
    local ver=$1; shift
    local python=${1:-python}; shift
    rm -rf $HERE/build
    $HERE/.tox/$ver/bin/$python $HERE/setup.py build bdist_egg upload
    rc=$?
    return $rc
}

for python_version in py25 py27 py31 py26 py32; do
    do_release $python_version || failed="$failed $python_version"
done
do_release pypy pypy || failed="$failed pypy"
# do_release jython jython || failed="$failed jython"

rc=0

for f in $failed; do
    rc=1
    echo "Failed to release $f"
done

if [ $rc -ne 0 ]; then
    echo "Skipping the source release due to failures"
    exit $rc
fi

$HERE/.tox/py27/bin/python $HERE/setup.py sdist upload

exit $rc
