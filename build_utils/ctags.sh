#!/bin/bash

dr=`pwd`
cd "../SRC"

# http://ctags.sourceforge.net/ctags.html

#ctags -R
#ctags -R --fortran-kinds=fs --h ".h.c.cpp.cc.f90.f77.f"
ctags -R --sort=no --fortran-kinds=fs -h ".f90.f77.f" 
#ctags -R --format=1 --langmap=fortran
cd $dr
