#!/bin/bash

set -e   # stop on error  ; see  https://stackoverflow.com/questions/3474526/stop-on-first-error

dr=`pwd`
cd build_utils
python gen_makefile.py
#python build_utils/gen_makefile.py
#rm  ../build/Makefile
echo "!!!!!!!!!!!!!!!!!!!!!!"
echo "!!!!!!!!!!!!!!!!!!!!!!"
echo "!!!!!!!!!!!!!!!!!!!!!!"
echo "!!!!!!!!!!!!!!!!!!!!!!"
pwd
mv Makefile ../Makefile
#ln -s ./Makefile ../build/Makefile
cd $dr

mkdir build  || true
cd    build
ln -s ../Makefile      || true
#make | tee make.log
rm make.log                        || true
pwd
echo "==== START make "
make $1 2>&1 | tee -a make.log
echo "==== END   make "
cd $dr
ln -s build/make.log .             || true