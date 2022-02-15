#!/bin/bash
set -e   # stop on error  ; see  https://stackoverflow.com/questions/3474526/stop-on-first-error

mode=VERY_OPT
#mode=DEBUG

dr=`pwd`
cd build_utils
python gen_makefile.py $mode
#python build_utils/gen_makefile.py
#rm  ../build/Makefile
echo "!!!!!!!!!!!!!!!!!!!!!!"
echo "!!!!!!!!!!!!!!!!!!!!!!"
echo "!!!!!!!!!!!!!!!!!!!!!!"
echo "!!!!!!!!!!!!!!!!!!!!!!"
pwd
mv Makefile ../Makefile 
cd $dr


drbuild=build_$mode

echo " drbuild: " $drbuild

mkdir $drbuild  || true
cd    $drbuild

ln -s ../Makefile      || true
#make | tee make.log
rm make.log                        || true
pwd
echo "==== START make "
make $1 2>&1 | tee -a make.log
echo "==== END   make "
cd $dr
