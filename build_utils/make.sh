#!/bin/bash

dr=`pwd`
python gen_makefile.py
#ln -s Makefile ../build/Makefile
cd ../build
ln -s ../build_utils/Makefile
#make | tee make.log
rm make.log
make 2>&1 | tee -a make.log
cd $dr
ln -s ../build/make.log .