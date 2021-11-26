#!/bin/bash

./make.sh

echo ###############################

bkdir=`pwd`
cd TESTS/t01_H2
./run.sh
cd $bkdir