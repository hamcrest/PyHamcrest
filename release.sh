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

function do_test() {
    local rc
    local ver=$1; shift
    local python=${1:-python}; shift
    rm -rf $HERE/build
    tox -e $ver
    rc=$?
    return $rc
}

function do_all_vers() {
    for python_version in py35 py36 py37; do
        $1 $python_version || failed="$failed $python_version"
    done
    $1 pypy pypy || failed="$failed pypy"
    # $1 jython jython || failed="$failed jython"

    rc=0

    for f in $failed; do
        rc=1
        echo "$1 failed for $f"
    done

    if [ $rc -ne 0 ]; then
        echo "Skipping $1 due to failures"
        return $rc
    fi
}

do_all_vers do_test || exit 1
do_all_vers do_release || exit 1

echo "All releases uploaded; uploading source release as well"
$HERE/.tox/py37/bin/python $HERE/setup.py sdist upload

exit $rc
