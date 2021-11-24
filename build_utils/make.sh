#!/bin/bash


# ======= LIBRARIES

#LPATH=/home/prokop/SW/intel/mkl/lib/intel64
#ls $LPATH
#PATH=$PATH:$LPATH
#LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LPATH
#LIBRARY_PATH=$LIBRARY_PATH:$LPATH
#echo "##### LD_LIBRARY_PATH :"
#echo $LD_LIBRARY_PATH
#echo "##### LIBRARY_PATH :"
#echo $LIBRARY_PATH

# ======================

set -e   # stop on error  ; see  https://stackoverflow.com/questions/3474526/stop-on-first-error

dr=`pwd`
python gen_makefile.py
#ln -s Makefile ../build/Makefile
cd ../build
ln -s ../build_utils/Makefile      || true
#make | tee make.log
rm make.log                        || true

echo "##### LD_LIBRARY_PATH :"
echo $LD_LIBRARY_PATH
echo "##### LIBRARY_PATH :"
echo $LIBRARY_PATH

#cat Makefile

make 2>&1 | tee -a make.log
cd $dr
ln -s ../build/make.log .          || true