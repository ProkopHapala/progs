#!/bin/bash

fireball="../build/fireball.x"

#PATH=$PATH:/home/prokop/SW/intel/mkl/lib/intel64
#LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/prokop/SW/intel/mkl/lib/intel64
#LD_LIBRARY_PATH=/home/prokop/SW/intel/mkl/lib/intel64:$LD_LIBRARY_PATH
LD_LIBRARY_PATH=/home/prokop/intel/mkl/lib/intel64:$LD_LIBRARY_PATH
export $LD_LIBRARY_PATH
echo $LD_LIBRARY_PATH

#export OMP_NUM_THREADS=1 #important for some calculations on super-computers

cd graphene_2x2
ln -s ../Fdata_HC_minimal Fdata

cp fireball.in-opt fireball.in
echo "running optimization of Benzene with FIRE & McWEDA"
#../../fireball.x > relaxation.out
#../$fireball > relaxation.out
../$fireball | tee relaxation.out

echo "optimization done"