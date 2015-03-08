# Test hamcrest with Docker

## Simple testing steps

(this assumes that you have [Docker](https://docker.com) installed)

1. cd to the directory containing PyHamcrest's `tox.ini` file.
2. run `docker run --rm -v $(pwd):/src chrisr/pybuilder:latest`

That's it!

This will test PyHamcrest with all supported versions of Python

## Tweaking the build image

1. in this directory, modify the `Dockerfile` to have the setup you want
2. `docker build --tag $USER/pybuilder:latest .`
3. run your build
4. submit a pull request to the `hamcrest/PyHamcrest` repo with your
   changes to the Dockerfile

We'll merge and publish the new tag to `chrisr/pybuilder:latest`,
making the new instructions up to date.
