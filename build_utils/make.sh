#!/bin/bash

set -e   # stop on error  ; see  https://stackoverflow.com/questions/3474526/stop-on-first-error

dr=`pwd`
python gen_makefile.py
#ln -s Makefile ../build/Makefile
cd ../build
ln -s ../build_utils/Makefile      || true
#make | tee make.log
rm make.log                        || true
make 2>&1 | tee -a make.log
cd $dr
ln -s ../build/make.log .          || true