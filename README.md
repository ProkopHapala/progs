
Fork of `https://github.com/fireball-QMD/progs` with cleaned-up code and modified build system. Project aims to reorganize the code and make further development easier.

FIREBALL is a local-orbital DFT implementation of molecular dynamics. The method allows for the simulation and calculation of very large supercells of thousands of atoms or very long MD simulations with ease.

### Instalation

Quick build can be done running:

 * `git clone https://github.com/ProkopHapala/Fireball-progs.git`
 * `cd Fireball-progs`
 * `./make.sh`

The script `./make.sh` uses simple python based build system which generated `Makefile` by running `build_utils/gen_makefile.py` (currently written in python 2.7). 

In case of any problems you may try to do the compilation manually using `Makefile-ref` generated during recent test-build. To do so run:

 * `git clone https://github.com/ProkopHapala/Fireball-progs.git`
 * `cd Fireball-progs`
 * `mkdir build`
 * `cp Makefile-ref build/Makefile`
 * `cd build`
 * `make`

To test fireball program you can run examples from test folder:

 * `cd TESTS`
 * `./distroted_benzene.sh`
 * `./graphene_2x2.sh`

These tests should produce outputs `answer.xyz` and `relaxation.out` inside respective folders `TESTS/distroted_benzene` and `TESTS/graphene_2x2`

#### **Known issues:**
 * Make sure to install intel Math Kernel Library (MKL) and link it properly within the scripts (`./distroted_benzene.sh` and `./graphene_2x2.sh`) by chaining the line `LD_LIBRARY_PATH=/home/prokop/intel/mkl/lib/intel64:$LD_LIBRARY_PATH` according your local system settings.

### Support / Service

* Download Fdata (Integral tables, basis-functions)
    * [ minimal  HCNOS (Biology)](http://fireball.ftmc.uam.es/Fdata_HCNOS.tar.gz)
    * [ extended HCNOS (Biology)](http://fireball.ftmc.uam.es/Fdata_HCNOS_ext.tar.gz)

### Documantation

 * For more detials visit: https://fireball-qmd.github.io/
 * [WIKI](https://nanosurf.fzu.cz/wiki/doku.php?id=fireball)
 * [Open course](http://fireball.ftmc.uam.es/moodle/login/index.php)  tutorials, static executables, etc … (log as a guest)
 *

### Cite like this:

 * Advances and applications in the FIREBALL ab initio tight-binding molecular-dynamics formalism
 * James P. Lewis , Pavel Jelínek, José Ortega, Alexander A. Demkov, Daniel G. Trabada, Barry Haycock , Hao Wang, Gary Adams, John K. Tomfohr , Enrique Abad, Hong Wang, and David A. Drabold
 * Phys. Status Solidi B 248, No. 9, 1989-2007 (2011) / DOI 10.1002/pssb.201147259
