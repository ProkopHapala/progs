#!/bin/bash

dr=`pwd`
python gen_makefile.py
ln -s Makefile ../build/Makefile
cd ../build
make
cd $dr