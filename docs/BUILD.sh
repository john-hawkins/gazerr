#!/bin/bash

rm ./source/gazerr.rst
rm ./source/modules.rst

make clean
sphinx-apidoc -o ./source ../gazerr
make html


