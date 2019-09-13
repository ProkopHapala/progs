FORM_RHO_ =  denmat.o denmat_es.o denmat_KS.o fermie.o denmata_ordern_fk.o denmatb_ordern_fk.o denmatc_ordern_fk.o ss12_fk.o \
	 build_rho.o build_rho_KS.o build_Ji.o koopman.o build_nij.o project_eh.o project_wfmdet.o
FORM_RHO_ORDERN =  chebft.o denmata_ordern.o denmatb_ordern.o denmatc_ordern.o denmat_fk.o formrho_sparse.o ss12.o
FORM_RHO =  $(FORM_RHO_) $(FORM_RHO_ORDERN)


KSPACE_ =  kspace.o kspace_KS.o kspace_ordern_fk.o diag_error.o diag_k.o diag_k_KS.o
KSPACE_DOUBLE =  kspace2.o
KSPACE_MPI-k =  kspace_MPI-k.o diag_k-MPI.o
KSPACE_ORDERN =  eandg.o xeandg.o formc_compact.o formsh_compact.o initguess.o kspace_fk.o kspace_ordern.o kspace_ordern_init.o \
	 kspace_ordern_slave.o ordern_init.o qralg.o set_dimensions.o set_maxdimension.o getsendrecv.o getstepsize.o
KSPACE =  $(KSPACE_) $(KSPACE_DOUBLE) $(KSPACE_MPI-k) $(KSPACE_ORDERN)


UTIL_ =  anderson.o anderson2.o fixfrags.o fixfrags2.o hampiece.o push_atoms.o writeout_ac.o writeout_cd.o writeout_charges.o \
	 writeout_dipole.o writeout_comph.o writeout_neighbors.o writeout_xv.o writeout_neighborsPP.o hamtrans.o mixer.o den2mesh.o \
	 ew2mesh.o ew2mesh_gamma.o postscf.o den2mesh_import.o broyden.o louie.o pulay.o compute_neutral_rho_grid.o ew2mesh_fourier.o \
	 ew2mesh_kscan.o ew2mesh_ARPES.o project_orb.o project_orb_complex.o excitations.o kvaziband.o band_project.o ARPES_LCAO.o \
	 writeout_eigenvec.o writeout_eigenvec_G.o writeCoefsLCAO.o
UTIL_MPI-k =  diag_k-MPI_slave.o bcast_k-MPI.o bcast_k-MPI_slave.o
UTIL =  $(UTIL_) $(UTIL_MPI-k)


DASSEMBLERS_ =  Dassemble_2c.o Dassemble_3c.o Dassemble_ca_2c.o Dassemble_ca_3c.o Dassemble_eh_2c.o Dassemble_hxc_2c.o Dassemble_hxc_3c.o \
	 Dassemble_lr.o Dassemble_snxc_on.o Dassemble_olsxc_on.o Dassemble_olsxc_2c.o Dassemble_olsxc_3c.o Dassemble_snxc_2c.o Dassemble_snxc_3c.o \
	 Dassemble_2c_PP.o Dassemble_3c_PP.o Dassemble_ca_olsxc_on.o Dassemble_ca_snxc_on.o Dassemble_ca_snxc_3c.o Dassemble_ca_olsxc_3c.o \
	 Dassemble_ca_snxc_2c.o Dassemble_ca_olsxc_2c.o Dassemble_ca_2c_dip.o Dassemble_ca_3c_dip.o Dassemble_lr_dip.o getforces_mcweda.o \
	 getforces_eh.o getforces_hxc.o getforces_KS.o getforces_classic.o getforces_classic_RGL.o getforces_classic_vdw.o getforces.o \
	 getforces_classic_tersoff.o getforces_zw.o Dassemble_zw_2c_ct.o Dassemble_zw_3c_ct.o Dassemble_zw_2c_na.o Dassemble_zw_3c_na.o \
	 Dassemble_zw_on_na.o
DASSEMBLERS_ORDERN =  Dassemble_2c_ordern_final.o Dassemble_3c_ordern_final.o Dassemble_ca_2c_ordern_final.o Dassemble_ca_3c_ordern_final.o
DASSEMBLERS =  $(DASSEMBLERS_) $(DASSEMBLERS_ORDERN)


INTERACTIONS_ =  cl_value.o Dtrescentros.o doscentros.o doscentrosPP.o doscentrosDipY.o doscentrosDipX.o get_ewald.o get_vdw.o \
	 getHarmonic.o trescentros.o unocentros.o smoother.o doscentrosS.o trescentrosS.o DtrescentrosS.o dosgaussians.o gelements_VXC.o \
	 Dgelements_VXC.o gelementsG_VXC.o DgelementsG_VXC.o gelementsG_VNA.o DgelementsG_VNA.o gelementsGS_VXC.o DgelementsGS_VXC.o \
	 gelementsG_VNA_SH.o DgelementsG_VNA_SH.o gelementsG_VNA_SH_RNA.o DgelementsG_VNA_SH_RNA.o trescentrosGHXC_VXC.o DtrescentrosGHXC_VXC.o \
	 trescentrosG_VNA.o DtrescentrosG_VNA.o trescentrosG_VXC.o DtrescentrosG_VXC.o trescentrosGS_VXC.o DtrescentrosGS_VXC.o trescentrosG_VNA_SH.o \
	 DtrescentrosG_VNA_SH.o doscentrosGS_overlap.o gelementsGS_overlap.o DgelementsGS_overlap.o doscentrosG_overlap.o gelementsG_overlap.o \
	 DgelementsG_overlap.o internalLambda.o tester2c.o
INTERACTIONS =  $(INTERACTIONS_)


UTIL_SPARSE =  build_transpose.o lanc.o sparse_add.o sparse_copy.o sparse_getdimension.o sparse_getpacksize.o sparse_mask.o \
	 sparse_mult.o sparse_norm2.o sparse_pack.o sparse_pack_elements.o sparse_pack_indices.o sparse_unpack.o sparse_unpack_elements.o \
	 sparse_unpack_indices.o sparse_vecprod.o



ALLOCATIONS_ =  allocate_f.o allocate_h.o allocate_neigh.o allocate_rho.o allocate_umb.o allocate_steered.o reallocate_f.o \
	 reallocate_h.o reallocate_neigh.o reallocate_rho.o allocate_dos.o allocate_grid.o allocate_trans.o
ALLOCATIONS_ORDERN =  allocate_ordern.o
ALLOCATIONS =  $(ALLOCATIONS_) $(ALLOCATIONS_ORDERN)


ASSEMBLERS_ =  assemble_olsxc_1c.o assemble_hxc_1c.o assemble_2c.o assemble_3c.o assemble_ca_2c.o assemble_3c_PP.o assemble_ca_3c.o \
	 assemble_eh_2c.o assemble_eh_usr.o assemble_F.o assemble_hxc_2c.o assemble_hxc_3c.o assemble_lr.o assemble_sVNL.o assemble_usr.o \
	 buildh.o assemble_olsxc_on.o assemble_olsxc_off.o build_olsxc_on.o build_olsxc_off.o average_rho.o build_snxc_on.o build_snxc_off.o \
	 assemble_snxc_on.o assemble_snxc_off.o build_ca_snxc_on.o build_ca_olsxc_on.o assemble_h.o assemble_mcweda.o assemble_hxc.o \
	 assemble_eh.o getenergy.o getenergy_hxc.o getenergy_mcweda.o getenergy_eh.o assemble_h_ks.o getenergy_KS.o assemble_S.o assemble_2c_S.o \
	 assemble_hartree.o assemble_scissor.o assemble_ca_2c_dip.o assemble_ca_3c_dip.o assemble_lr_dip.o assemble_zw_1c_na.o assemble_zw_2c_ct.o \
	 assemble_zw_3c_ct.o assemble_xczw.o assemble_zw_off_na.o assemble_zw_on_na.o build_zw_off_na.o build_zw_on_na.o assemble_1c_vdip.o \
	 getenergy_zw.o
ASSEMBLERS_ORDERN =  assemble_2c_ordern_final.o assemble_2c_ordern_init.o assemble_3c_ordern_final.o assemble_ca_2c_ordern_final.o \
	 assemble_ca_3c_ordern_final.o assemble_eh_2c_ordern_final.o
ASSEMBLERS =  $(ASSEMBLERS_) $(ASSEMBLERS_ORDERN)


GRID =  assemble_KS_den0.o assemble_KS_den.o assemble_KS_usr.o laplace_fft.o assemble_KS_dcc.o assemble_KS_mat.o mixer_KS.o \
	 writeout_charges_KS.o writeout_xsf.o assemble_KS_vna.o get_Hort.o



INITIALIZERS_ =  diagnostics.o initatomicE.o initconstraints.o initcharges.o initconstants.o initboxes.o initkpoints.o initmasses.o \
	 initneighbors.o welcome.o make_mu2shell.o make_munu.o make_munuPP.o restart.o make_munuDipY.o make_munuDipX.o zero_ang_mom.o \
	 initamat.o make_munuS.o initNH.o getkpoints.o greatKAuto.o greatKsubsAuto.o initgrid.o initdenmat.o get_info_orbital.o initbasics.o \
	 initcharges_KS.o initcDFT.o
INITIALIZERS_MPI-k =  init_MPI.o
INITIALIZERS =  $(INITIALIZERS_) $(INITIALIZERS_MPI-k)


INTERPOLATERS =  buildspline_1d.o interpolate_1d.o interpolate_2d.o recover_2c.o recover_3c.o recover_PP.o recoverC.o setterp_2d.o \
	 recover_2cDipY.o recover_2cDipX.o recover_S.o buildspline2_1d.o getpsi.o getYlm.o getvna.o



LOOPS =  main_loop.o main_loop_MD.o main_loop_CG.o scf_loop.o scf_loop_harris.o main_loop_NEB.o main_loop_DM.o scf_loop_ks.o \
	 main_loop_importrho.o main_loop_TDSE.o main_loop_MDET.o main_loop_MIN.o main_loop_NAC.o main_loop_FIRE.o main_loop_socket.o



MAIN_ =  fireball.o
MAIN =  $(MAIN_)


MD =  cross.o factorial.o predictor.o gaussT.o corrector.o imaged.o setgear.o phimat.o bvec.o soldm.o NHCThermostat.o get_enk.o \
	 writeHNose.o resetNHC.o move_ions.o



MODULES_ =  dimensions.o barrier.o charges.o configuration.o constants_fireball.o density.o forces.o fragments.o gaussG.o \
	 integrals.o interactions.o kpoints.o neighbor_map.o umbrella.o steered.o optimization.o module_dos.o dynamo.o cproc.o noseHoover.o \
	 scf.o grid.o wavefunction.o neb_module.o vnneutral.o transport.o matmultmod.o options.o outputs.o MD.o energy.o mpi_main.o \
	 tdse.o bias.o nonadiabatic.o hartree.o fsockets.o fb_socket.o classicMD.o
MODULES_MPI-k =  mpi_declarations.o
MODULES_ORDERN =  ordern.o
MODULES =  $(MODULES_) $(MODULES_MPI-k) $(MODULES_ORDERN)


NEIGHBORS =  backnay.o common_neighbors.o find_neigh_max.o find_neigh_max_class.o mpairnay.o neighbors.o neighbors_pairs.o \
	 find_neighPP_max.o neighborsPP.o common_neighborsPP.o num_neigh_tot.o



PRESSURE =  hmetric.o initpressure.o invert3x3.o



READFILES =  append_string.o read_1c.o read_2c.o read_3c.o readbasis.o readbarrier.o readdata_2c.o readdata_3c.o readfragments.o \
	 readheader_2c.o readheader_3c.o readinfo.o readlvs.o readparam.o readphi.o readpressure.o readquench.o readsa.o readvdw.o \
	 readcgo.o readdos.o readgaussG.o findFdata.o readgrid.o read_wf.o read_vna.o readtrans.o readbind.o readhop.o readdata.o \
	 readdata_hxc.o readdata_mcweda.o readdata_xczw.o readdata_eh.o checksum_options.o readdata_KS.o getsections.o readdata_classicMD.o \
	 readhartree.o readephc.o



ROTATIONS =  chooser.o chooserd.o deps2center.o deps3center.o makeDmat.o makeDmatPP.o rotate.o rotated.o rotatedPP.o twister.o \
	 twisterd.o rotatePP.o epsilon.o



SOCKETS =  get_geometry.o create_socket.o send_geometry.o sendrecv.o soc_init.o



UMBRELLA =  assemble_umbrella.o Dassemble_umbrella.o get_umbrella.o readumbrella.o assemble_steered.o Dassemble_steered.o \
	 get_steered.o readsteered.o



XC =  ceperley_alder.o cepal.o



CG =  cgo.o bfgs.o l-bfgs-b.o FIRE.o



DOS =  dos.o writeout_dos.o writeout_dosng.o hoppings.o writeout_atom.o hamilt_atom.o



NEB =  initneb.o neb.o



TDSE =  ete_loop.o psi2es.o eigenHS.o tddenmat.o tddiag_k.o diag_Sk.o diag_Hk.o allocate_tdse.o tdbc.o propTpsi.o readtdse.o \
	 initpsi.o ortho_H.o get_QLow.o get_QMul.o postete.o wrtout_psiT.o



TRANS =  assemble_t12_fit.o assemble_t12_bare.o calcG.o assemble_Hsam.o assemble_Gsam.o assemble_Dxx.o sqrt_mat.o interpolate_hop.o \
	 gethop.o



BIAS =  assemble_bias.o Dassemble_bias.o allocate_bias.o reallocate_bias.o readbias.o



NAC =  allocate_nac.o assemble_G_S.o nacouplings.o build_gover1c.o init_mdet.o mdetdenmat.o getforces_mdet.o save_mdetstuff.o \
	 evolve_ks_states.o deallocate_nac.o dcdt_nac.o Dassemble_2c_mdet.o Dassemble_2c_PP_mdet.o Dassemble_olsxc_on_mdet.o Dassemble_olsxc_2c_mdet.o \
	 Dassemble_3c_mdet.o Dassemble_3c_PP_mdet.o Dassemble_olsxc_3c_mdet.o fewest_switches.o mc_switch.o transition.o Dassemble_ca_2c_mdet.o \
	 Dassemble_ca_3c_mdet.o Dassemble_lr_mdet.o Dassemble_ca_olsxc_on_mdet.o Dassemble_ca_olsxc_2c_mdet.o Dassemble_ca_olsxc_3c_mdet.o \
	 move_correc.o move_predic.o



QMMM =  main_loop_MDET_qmmm.o main_loop_MD_qmmm.o fireball_qmmm_loop.o assemble_qmmm.o assemble_qmmm_dip.o Dassemble_qmmm.o \
	 Dassemble_qmmm_dip.o Dassemble_qmmm_mdet.o Dassemble_qmmm_mdet_dip.o



DFTD3 =  common.o sizes.o pars.o core.o api.o dftd3_corrections.o



OBJECTS_SERVER =  $(MODULES)  $(DFTD3)  $(INITMPI)  $(ORDERN)  $(ALLOCATIONS)  $(ASSEMBLERS)  $(DASSEMBLERS)  $(INITIALIZERS)  \
	 $(INTERACTIONS)  $(INTERPOLATERS)  $(LOOPS, MD)  $(NEIGHBORS)  $(PRESSURE)  $(READFILES)  $(ROTATIONS)  $(SOLVESH_DIAG)  \
	 $(FORM_RHO)  $(UMBRELLA UTIL)  $(UTIL_SPARSE)  $(VISUALIZATION)  $(XC)  $(CG)  $(DOS)  $(THERMOINT)  $(NEB)  $(TRANS)  $(GRID)  \
	 $(TDSE)  $(BIAS)  $(NAC)  $(MAIN_SERVER) 

OBJECTS =  $(MODULES)  $(DFTD3)  $(INITMPI)  $(ORDERN)  $(ALLOCATIONS)  $(ASSEMBLERS)  $(DASSEMBLERS)  $(INITIALIZERS)  $(INTERACTIONS)  \
	 $(INTERPOLATERS)  $(LOOPS, MD)  $(NEIGHBORS)  $(PRESSURE)  $(READFILES)  $(ROTATIONS)  $(SOLVESH_DIAG)  $(FORM_RHO)  $(UMBRELLA UTIL)  \
	 $(UTIL_SPARSE)  $(VISUALIZATION)  $(XC)  $(CG)  $(DOS)  $(THERMOINT)  $(NEB)  $(TRANS)  $(GRID)  $(TDSE)  $(BIAS)  $(NAC)  \
	 $(MAIN) 

all : 
	make fireball.x

veryclean :  clean
	rm -f fireball.x libfireball.a

extraclean : veryclean

libfireball : $(OBJECTS_QMMM)
	ar rv libfireball.a $(OBJECTS_QMMM)
	ranlib libfireball.a

.PHONY :  clean veryclean extraclean

clean : 
	rm -f -r core *.o .nfs* rii_files fireball.x.ip*  *.mod ldtmp* *.vo *~ *.il

F90 = gfortran
FFLAGS = -O3 -mtune=native -ftree-vectorize  -ffree-form -ffree-line-length-none -freal-4-real-8 

LFLAGS_ =  -lmkl_scalapack_lp64 -lmkl_blacs_openmpi_lp64 -lmkl_lapack95_lp64 -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -liomp5 -lpthread -lfftw3xf_gnu -lm -Bdynamic -lmpi 

LPATHS =  -L/home/prokop/intel/mkl/lib/intel64 -L/home/prokop/intel/mkl/lib/intel64 -I/home/prokop/intel/mkl/include/fftw -L/usr/lib/x86_64-linux-gnu/openmpi/lib -I/usr/lib/x86_64-linux-gnu/openmpi/include 

LFLAGS =  $(LPATHS)  $(LFLAGS_) 

fireball.x : $(OBJECTS)
	$(F90) -o fireball.x  $(FFLAGS) $(OBJECTS) $(LFLAGS)

fireball_server.x : $(OBJECTS)
	$(F90) -o fireball_server.x  $(FFLAGS) $(OBJECTS_SERVER) $(LFLAGS)

sockets.o : ../MODULES/sockets.c
	$(CC) $(CFLAGS)   -c ../MODULES/sockets.c
cclient.o : ../THERMOINT/cclient.c
	$(CC) $(CFLAGS)   -c ../THERMOINT/cclient.c


#**************************************************
#   FORM_RHO
#**************************************************
#====== variant : ''
denmat.o : ../SRC/FORM_RHO/denmat.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/denmat.f90
denmat_es.o : ../SRC/FORM_RHO/denmat_es.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/denmat_es.f90
denmat_KS.o : ../SRC/FORM_RHO/denmat_KS.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/denmat_KS.f90
fermie.o : ../SRC/FORM_RHO/fermie.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/fermie.f90
denmata_ordern_fk.o : ../SRC/FORM_RHO/denmata_ordern_fk.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/denmata_ordern_fk.f90
denmatb_ordern_fk.o : ../SRC/FORM_RHO/denmatb_ordern_fk.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/denmatb_ordern_fk.f90
denmatc_ordern_fk.o : ../SRC/FORM_RHO/denmatc_ordern_fk.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/denmatc_ordern_fk.f90
ss12_fk.o : ../SRC/FORM_RHO/ss12_fk.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/ss12_fk.f90
build_rho.o : ../SRC/FORM_RHO/build_rho.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/build_rho.f90
build_rho_KS.o : ../SRC/FORM_RHO/build_rho_KS.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/build_rho_KS.f90
build_Ji.o : ../SRC/FORM_RHO/build_Ji.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/build_Ji.f90
koopman.o : ../SRC/FORM_RHO/koopman.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/koopman.f90
build_nij.o : ../SRC/FORM_RHO/build_nij.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/build_nij.f90
project_eh.o : ../SRC/FORM_RHO/project_eh.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/project_eh.f90
project_wfmdet.o : ../SRC/FORM_RHO/project_wfmdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/project_wfmdet.f90
#====== variant : 'ORDERN'
chebft.o : ../SRC/FORM_RHO/chebft.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/chebft.f90
denmata_ordern.o : ../SRC/FORM_RHO/denmata_ordern.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/denmata_ordern.f90
denmatb_ordern.o : ../SRC/FORM_RHO/denmatb_ordern.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/denmatb_ordern.f90
denmatc_ordern.o : ../SRC/FORM_RHO/denmatc_ordern.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/denmatc_ordern.f90
denmat_fk.o : ../SRC/FORM_RHO/denmat_fk.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/denmat_fk.f90
formrho_sparse.o : ../SRC/FORM_RHO/formrho_sparse.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/formrho_sparse.f90
ss12.o : ../SRC/FORM_RHO/ss12.f90
	$(F90) $(FFLAGS)  -c ../SRC/FORM_RHO/ss12.f90




#**************************************************
#   KSPACE
#**************************************************
#====== variant : ''
kspace.o : ../SRC/KSPACE/kspace.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace.f90
kspace_KS.o : ../SRC/KSPACE/kspace_KS.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace_KS.f90
kspace_ordern_fk.o : ../SRC/KSPACE/kspace_ordern_fk.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace_ordern_fk.f90
diag_error.o : ../SRC/KSPACE/diag_error.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/diag_error.f90
diag_k.o : ../SRC/KSPACE/diag_k.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/diag_k.f90
diag_k_KS.o : ../SRC/KSPACE/diag_k_KS.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/diag_k_KS.f90
#====== variant : 'SCALAPACK'
blacsaba.o : ../SRC/KSPACE/blacsaba.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/blacsaba.f90
kspace_MPI.o : ../SRC/KSPACE/kspace_MPI.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace_MPI.f90
kspace_MPI_slave.o : ../SRC/KSPACE/kspace_MPI_slave.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace_MPI_slave.f90
pclagetter.o : ../SRC/KSPACE/pclagetter.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/pclagetter.f90
pclaputter.o : ../SRC/KSPACE/pclaputter.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/pclaputter.f90
#====== variant : 'ORDERN'
eandg.o : ../SRC/KSPACE/eandg.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/eandg.f90
xeandg.o : ../SRC/KSPACE/xeandg.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/xeandg.f90
formc_compact.o : ../SRC/KSPACE/formc_compact.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/formc_compact.f90
formsh_compact.o : ../SRC/KSPACE/formsh_compact.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/formsh_compact.f90
initguess.o : ../SRC/KSPACE/initguess.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/initguess.f90
kspace_fk.o : ../SRC/KSPACE/kspace_fk.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace_fk.f90
kspace_ordern.o : ../SRC/KSPACE/kspace_ordern.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace_ordern.f90
kspace_ordern_init.o : ../SRC/KSPACE/kspace_ordern_init.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace_ordern_init.f90
kspace_ordern_slave.o : ../SRC/KSPACE/kspace_ordern_slave.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace_ordern_slave.f90
ordern_init.o : ../SRC/KSPACE/ordern_init.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/ordern_init.f90
qralg.o : ../SRC/KSPACE/qralg.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/qralg.f90
set_dimensions.o : ../SRC/KSPACE/set_dimensions.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/set_dimensions.f90
set_maxdimension.o : ../SRC/KSPACE/set_maxdimension.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/set_maxdimension.f90
getsendrecv.o : ../SRC/KSPACE/getsendrecv.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/getsendrecv.f90
getstepsize.o : ../SRC/KSPACE/getstepsize.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/getstepsize.f90
#====== variant : 'LAPACK95'
kspace_l95.o : ../SRC/KSPACE/kspace_l95.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace_l95.f90
#====== variant : 'DOUBLE'
kspace2.o : ../SRC/KSPACE/kspace2.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace2.f90
#====== variant : 'GAMMA'
kspace_withnok.o : ../SRC/KSPACE/kspace_withnok.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace_withnok.f90
#====== variant : 'MPI-k'
kspace_MPI-k.o : ../SRC/KSPACE/kspace_MPI-k.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/kspace_MPI-k.f90
diag_k-MPI.o : ../SRC/KSPACE/diag_k-MPI.f90
	$(F90) $(FFLAGS)  -c ../SRC/KSPACE/diag_k-MPI.f90




#**************************************************
#   UTIL
#**************************************************
#====== variant : ''
anderson.o : ../SRC/UTIL/anderson.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/anderson.f90
anderson2.o : ../SRC/UTIL/anderson2.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/anderson2.f90
fixfrags.o : ../SRC/UTIL/fixfrags.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/fixfrags.f90
fixfrags2.o : ../SRC/UTIL/fixfrags2.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/fixfrags2.f90
hampiece.o : ../SRC/UTIL/hampiece.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/hampiece.f90
push_atoms.o : ../SRC/UTIL/push_atoms.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/push_atoms.f90
writeout_ac.o : ../SRC/UTIL/writeout_ac.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/writeout_ac.f90
writeout_cd.o : ../SRC/UTIL/writeout_cd.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/writeout_cd.f90
writeout_charges.o : ../SRC/UTIL/writeout_charges.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/writeout_charges.f90
writeout_dipole.o : ../SRC/UTIL/writeout_dipole.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/writeout_dipole.f90
writeout_comph.o : ../SRC/UTIL/writeout_comph.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/writeout_comph.f90
writeout_neighbors.o : ../SRC/UTIL/writeout_neighbors.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/writeout_neighbors.f90
writeout_xv.o : ../SRC/UTIL/writeout_xv.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/writeout_xv.f90
writeout_neighborsPP.o : ../SRC/UTIL/writeout_neighborsPP.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/writeout_neighborsPP.f90
hamtrans.o : ../SRC/UTIL/hamtrans.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/hamtrans.f90
mixer.o : ../SRC/UTIL/mixer.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/mixer.f90
den2mesh.o : ../SRC/UTIL/den2mesh.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/den2mesh.f90
ew2mesh.o : ../SRC/UTIL/ew2mesh.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/ew2mesh.f90
ew2mesh_gamma.o : ../SRC/UTIL/ew2mesh_gamma.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/ew2mesh_gamma.f90
postscf.o : ../SRC/UTIL/postscf.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/postscf.f90
den2mesh_import.o : ../SRC/UTIL/den2mesh_import.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/den2mesh_import.f90
broyden.o : ../SRC/UTIL/broyden.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/broyden.f90
louie.o : ../SRC/UTIL/louie.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/louie.f90
pulay.o : ../SRC/UTIL/pulay.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/pulay.f90
compute_neutral_rho_grid.o : ../SRC/UTIL/compute_neutral_rho_grid.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/compute_neutral_rho_grid.f90
ew2mesh_fourier.o : ../SRC/UTIL/ew2mesh_fourier.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/ew2mesh_fourier.f90
ew2mesh_kscan.o : ../SRC/UTIL/ew2mesh_kscan.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/ew2mesh_kscan.f90
ew2mesh_ARPES.o : ../SRC/UTIL/ew2mesh_ARPES.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/ew2mesh_ARPES.f90
project_orb.o : ../SRC/UTIL/project_orb.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/project_orb.f90
project_orb_complex.o : ../SRC/UTIL/project_orb_complex.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/project_orb_complex.f90
excitations.o : ../SRC/UTIL/excitations.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/excitations.f90
kvaziband.o : ../SRC/UTIL/kvaziband.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/kvaziband.f90
band_project.o : ../SRC/UTIL/band_project.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/band_project.f90
ARPES_LCAO.o : ../SRC/UTIL/ARPES_LCAO.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/ARPES_LCAO.f90
writeout_eigenvec.o : ../SRC/UTIL/writeout_eigenvec.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/writeout_eigenvec.f90
writeout_eigenvec_G.o : ../SRC/UTIL/writeout_eigenvec_G.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/writeout_eigenvec_G.f90
writeCoefsLCAO.o : ../SRC/UTIL/writeCoefsLCAO.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/writeCoefsLCAO.f90
#====== variant : 'LAPACK95'
anderson_l95.o : ../SRC/UTIL/anderson_l95.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/anderson_l95.f90
#====== variant : 'MPI-k'
diag_k-MPI_slave.o : ../SRC/UTIL/diag_k-MPI_slave.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/diag_k-MPI_slave.f90
bcast_k-MPI.o : ../SRC/UTIL/bcast_k-MPI.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/bcast_k-MPI.f90
bcast_k-MPI_slave.o : ../SRC/UTIL/bcast_k-MPI_slave.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL/bcast_k-MPI_slave.f90




#**************************************************
#   DASSEMBLERS
#**************************************************
#====== variant : ''
Dassemble_2c.o : ../SRC/DASSEMBLERS/Dassemble_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_2c.f90
Dassemble_3c.o : ../SRC/DASSEMBLERS/Dassemble_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_3c.f90
Dassemble_ca_2c.o : ../SRC/DASSEMBLERS/Dassemble_ca_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_ca_2c.f90
Dassemble_ca_3c.o : ../SRC/DASSEMBLERS/Dassemble_ca_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_ca_3c.f90
Dassemble_eh_2c.o : ../SRC/DASSEMBLERS/Dassemble_eh_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_eh_2c.f90
Dassemble_hxc_2c.o : ../SRC/DASSEMBLERS/Dassemble_hxc_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_hxc_2c.f90
Dassemble_hxc_3c.o : ../SRC/DASSEMBLERS/Dassemble_hxc_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_hxc_3c.f90
Dassemble_lr.o : ../SRC/DASSEMBLERS/Dassemble_lr.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_lr.f90
Dassemble_snxc_on.o : ../SRC/DASSEMBLERS/Dassemble_snxc_on.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_snxc_on.f90
Dassemble_olsxc_on.o : ../SRC/DASSEMBLERS/Dassemble_olsxc_on.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_olsxc_on.f90
Dassemble_olsxc_2c.o : ../SRC/DASSEMBLERS/Dassemble_olsxc_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_olsxc_2c.f90
Dassemble_olsxc_3c.o : ../SRC/DASSEMBLERS/Dassemble_olsxc_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_olsxc_3c.f90
Dassemble_snxc_2c.o : ../SRC/DASSEMBLERS/Dassemble_snxc_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_snxc_2c.f90
Dassemble_snxc_3c.o : ../SRC/DASSEMBLERS/Dassemble_snxc_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_snxc_3c.f90
Dassemble_2c_PP.o : ../SRC/DASSEMBLERS/Dassemble_2c_PP.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_2c_PP.f90
Dassemble_3c_PP.o : ../SRC/DASSEMBLERS/Dassemble_3c_PP.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_3c_PP.f90
Dassemble_ca_olsxc_on.o : ../SRC/DASSEMBLERS/Dassemble_ca_olsxc_on.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_ca_olsxc_on.f90
Dassemble_ca_snxc_on.o : ../SRC/DASSEMBLERS/Dassemble_ca_snxc_on.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_ca_snxc_on.f90
Dassemble_ca_snxc_3c.o : ../SRC/DASSEMBLERS/Dassemble_ca_snxc_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_ca_snxc_3c.f90
Dassemble_ca_olsxc_3c.o : ../SRC/DASSEMBLERS/Dassemble_ca_olsxc_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_ca_olsxc_3c.f90
Dassemble_ca_snxc_2c.o : ../SRC/DASSEMBLERS/Dassemble_ca_snxc_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_ca_snxc_2c.f90
Dassemble_ca_olsxc_2c.o : ../SRC/DASSEMBLERS/Dassemble_ca_olsxc_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_ca_olsxc_2c.f90
Dassemble_ca_2c_dip.o : ../SRC/DASSEMBLERS/Dassemble_ca_2c_dip.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_ca_2c_dip.f90
Dassemble_ca_3c_dip.o : ../SRC/DASSEMBLERS/Dassemble_ca_3c_dip.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_ca_3c_dip.f90
Dassemble_lr_dip.o : ../SRC/DASSEMBLERS/Dassemble_lr_dip.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_lr_dip.f90
getforces_mcweda.o : ../SRC/DASSEMBLERS/getforces_mcweda.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/getforces_mcweda.f90
getforces_eh.o : ../SRC/DASSEMBLERS/getforces_eh.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/getforces_eh.f90
getforces_hxc.o : ../SRC/DASSEMBLERS/getforces_hxc.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/getforces_hxc.f90
getforces_KS.o : ../SRC/DASSEMBLERS/getforces_KS.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/getforces_KS.f90
getforces_classic.o : ../SRC/DASSEMBLERS/getforces_classic.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/getforces_classic.f90
getforces_classic_RGL.o : ../SRC/DASSEMBLERS/getforces_classic_RGL.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/getforces_classic_RGL.f90
getforces_classic_vdw.o : ../SRC/DASSEMBLERS/getforces_classic_vdw.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/getforces_classic_vdw.f90
getforces.o : ../SRC/DASSEMBLERS/getforces.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/getforces.f90
getforces_classic_tersoff.o : ../SRC/DASSEMBLERS/getforces_classic_tersoff.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/getforces_classic_tersoff.f90
getforces_zw.o : ../SRC/DASSEMBLERS/getforces_zw.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/getforces_zw.f90
Dassemble_zw_2c_ct.o : ../SRC/DASSEMBLERS/Dassemble_zw_2c_ct.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_zw_2c_ct.f90
Dassemble_zw_3c_ct.o : ../SRC/DASSEMBLERS/Dassemble_zw_3c_ct.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_zw_3c_ct.f90
Dassemble_zw_2c_na.o : ../SRC/DASSEMBLERS/Dassemble_zw_2c_na.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_zw_2c_na.f90
Dassemble_zw_3c_na.o : ../SRC/DASSEMBLERS/Dassemble_zw_3c_na.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_zw_3c_na.f90
Dassemble_zw_on_na.o : ../SRC/DASSEMBLERS/Dassemble_zw_on_na.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_zw_on_na.f90
#====== variant : 'OPENMP'
Dassemble_lr_OMP.o : ../SRC/DASSEMBLERS/Dassemble_lr_OMP.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_lr_OMP.f90
#====== variant : 'ORDERN'
Dassemble_2c_ordern_final.o : ../SRC/DASSEMBLERS/Dassemble_2c_ordern_final.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_2c_ordern_final.f90
Dassemble_3c_ordern_final.o : ../SRC/DASSEMBLERS/Dassemble_3c_ordern_final.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_3c_ordern_final.f90
Dassemble_ca_2c_ordern_final.o : ../SRC/DASSEMBLERS/Dassemble_ca_2c_ordern_final.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_ca_2c_ordern_final.f90
Dassemble_ca_3c_ordern_final.o : ../SRC/DASSEMBLERS/Dassemble_ca_3c_ordern_final.f90
	$(F90) $(FFLAGS)  -c ../SRC/DASSEMBLERS/Dassemble_ca_3c_ordern_final.f90




#**************************************************
#   INTERACTIONS
#**************************************************
#====== variant : ''
cl_value.o : ../SRC/INTERACTIONS/cl_value.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/cl_value.f90
Dtrescentros.o : ../SRC/INTERACTIONS/Dtrescentros.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/Dtrescentros.f90
doscentros.o : ../SRC/INTERACTIONS/doscentros.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/doscentros.f90
doscentrosPP.o : ../SRC/INTERACTIONS/doscentrosPP.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/doscentrosPP.f90
doscentrosDipY.o : ../SRC/INTERACTIONS/doscentrosDipY.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/doscentrosDipY.f90
doscentrosDipX.o : ../SRC/INTERACTIONS/doscentrosDipX.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/doscentrosDipX.f90
get_ewald.o : ../SRC/INTERACTIONS/get_ewald.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/get_ewald.f90
get_vdw.o : ../SRC/INTERACTIONS/get_vdw.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/get_vdw.f90
getHarmonic.o : ../SRC/INTERACTIONS/getHarmonic.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/getHarmonic.f90
trescentros.o : ../SRC/INTERACTIONS/trescentros.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/trescentros.f90
unocentros.o : ../SRC/INTERACTIONS/unocentros.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/unocentros.f90
smoother.o : ../SRC/INTERACTIONS/smoother.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/smoother.f90
doscentrosS.o : ../SRC/INTERACTIONS/doscentrosS.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/doscentrosS.f90
trescentrosS.o : ../SRC/INTERACTIONS/trescentrosS.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/trescentrosS.f90
DtrescentrosS.o : ../SRC/INTERACTIONS/DtrescentrosS.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DtrescentrosS.f90
dosgaussians.o : ../SRC/INTERACTIONS/dosgaussians.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/dosgaussians.f90
gelements_VXC.o : ../SRC/INTERACTIONS/gelements_VXC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/gelements_VXC.f90
Dgelements_VXC.o : ../SRC/INTERACTIONS/Dgelements_VXC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/Dgelements_VXC.f90
gelementsG_VXC.o : ../SRC/INTERACTIONS/gelementsG_VXC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/gelementsG_VXC.f90
DgelementsG_VXC.o : ../SRC/INTERACTIONS/DgelementsG_VXC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DgelementsG_VXC.f90
gelementsG_VNA.o : ../SRC/INTERACTIONS/gelementsG_VNA.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/gelementsG_VNA.f90
DgelementsG_VNA.o : ../SRC/INTERACTIONS/DgelementsG_VNA.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DgelementsG_VNA.f90
gelementsGS_VXC.o : ../SRC/INTERACTIONS/gelementsGS_VXC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/gelementsGS_VXC.f90
DgelementsGS_VXC.o : ../SRC/INTERACTIONS/DgelementsGS_VXC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DgelementsGS_VXC.f90
gelementsG_VNA_SH.o : ../SRC/INTERACTIONS/gelementsG_VNA_SH.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/gelementsG_VNA_SH.f90
DgelementsG_VNA_SH.o : ../SRC/INTERACTIONS/DgelementsG_VNA_SH.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DgelementsG_VNA_SH.f90
gelementsG_VNA_SH_RNA.o : ../SRC/INTERACTIONS/gelementsG_VNA_SH_RNA.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/gelementsG_VNA_SH_RNA.f90
DgelementsG_VNA_SH_RNA.o : ../SRC/INTERACTIONS/DgelementsG_VNA_SH_RNA.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DgelementsG_VNA_SH_RNA.f90
trescentrosGHXC_VXC.o : ../SRC/INTERACTIONS/trescentrosGHXC_VXC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/trescentrosGHXC_VXC.f90
DtrescentrosGHXC_VXC.o : ../SRC/INTERACTIONS/DtrescentrosGHXC_VXC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DtrescentrosGHXC_VXC.f90
trescentrosG_VNA.o : ../SRC/INTERACTIONS/trescentrosG_VNA.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/trescentrosG_VNA.f90
DtrescentrosG_VNA.o : ../SRC/INTERACTIONS/DtrescentrosG_VNA.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DtrescentrosG_VNA.f90
trescentrosG_VXC.o : ../SRC/INTERACTIONS/trescentrosG_VXC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/trescentrosG_VXC.f90
DtrescentrosG_VXC.o : ../SRC/INTERACTIONS/DtrescentrosG_VXC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DtrescentrosG_VXC.f90
trescentrosGS_VXC.o : ../SRC/INTERACTIONS/trescentrosGS_VXC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/trescentrosGS_VXC.f90
DtrescentrosGS_VXC.o : ../SRC/INTERACTIONS/DtrescentrosGS_VXC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DtrescentrosGS_VXC.f90
trescentrosG_VNA_SH.o : ../SRC/INTERACTIONS/trescentrosG_VNA_SH.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/trescentrosG_VNA_SH.f90
DtrescentrosG_VNA_SH.o : ../SRC/INTERACTIONS/DtrescentrosG_VNA_SH.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DtrescentrosG_VNA_SH.f90
doscentrosGS_overlap.o : ../SRC/INTERACTIONS/doscentrosGS_overlap.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/doscentrosGS_overlap.f90
gelementsGS_overlap.o : ../SRC/INTERACTIONS/gelementsGS_overlap.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/gelementsGS_overlap.f90
DgelementsGS_overlap.o : ../SRC/INTERACTIONS/DgelementsGS_overlap.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DgelementsGS_overlap.f90
doscentrosG_overlap.o : ../SRC/INTERACTIONS/doscentrosG_overlap.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/doscentrosG_overlap.f90
gelementsG_overlap.o : ../SRC/INTERACTIONS/gelementsG_overlap.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/gelementsG_overlap.f90
DgelementsG_overlap.o : ../SRC/INTERACTIONS/DgelementsG_overlap.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/DgelementsG_overlap.f90
internalLambda.o : ../SRC/INTERACTIONS/internalLambda.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/internalLambda.f90
tester2c.o : ../SRC/INTERACTIONS/tester2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/tester2c.f90
#====== variant : 'OPENMP'
get_ewald_OMP.o : ../SRC/INTERACTIONS/get_ewald_OMP.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERACTIONS/get_ewald_OMP.f90




#**************************************************
#   UTIL_SPARSE
#**************************************************
#====== variant : 'ORDERN'
build_transpose.o : ../SRC/UTIL_SPARSE/build_transpose.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/build_transpose.f90
lanc.o : ../SRC/UTIL_SPARSE/lanc.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/lanc.f90
sparse_add.o : ../SRC/UTIL_SPARSE/sparse_add.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_add.f90
sparse_copy.o : ../SRC/UTIL_SPARSE/sparse_copy.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_copy.f90
sparse_getdimension.o : ../SRC/UTIL_SPARSE/sparse_getdimension.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_getdimension.f90
sparse_getpacksize.o : ../SRC/UTIL_SPARSE/sparse_getpacksize.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_getpacksize.f90
sparse_mask.o : ../SRC/UTIL_SPARSE/sparse_mask.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_mask.f90
sparse_mult.o : ../SRC/UTIL_SPARSE/sparse_mult.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_mult.f90
sparse_norm2.o : ../SRC/UTIL_SPARSE/sparse_norm2.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_norm2.f90
sparse_pack.o : ../SRC/UTIL_SPARSE/sparse_pack.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_pack.f90
sparse_pack_elements.o : ../SRC/UTIL_SPARSE/sparse_pack_elements.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_pack_elements.f90
sparse_pack_indices.o : ../SRC/UTIL_SPARSE/sparse_pack_indices.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_pack_indices.f90
sparse_unpack.o : ../SRC/UTIL_SPARSE/sparse_unpack.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_unpack.f90
sparse_unpack_elements.o : ../SRC/UTIL_SPARSE/sparse_unpack_elements.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_unpack_elements.f90
sparse_unpack_indices.o : ../SRC/UTIL_SPARSE/sparse_unpack_indices.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_unpack_indices.f90
sparse_vecprod.o : ../SRC/UTIL_SPARSE/sparse_vecprod.f90
	$(F90) $(FFLAGS)  -c ../SRC/UTIL_SPARSE/sparse_vecprod.f90




#**************************************************
#   ALLOCATIONS
#**************************************************
#====== variant : ''
allocate_f.o : ../SRC/ALLOCATIONS/allocate_f.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/allocate_f.f90
allocate_h.o : ../SRC/ALLOCATIONS/allocate_h.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/allocate_h.f90
allocate_neigh.o : ../SRC/ALLOCATIONS/allocate_neigh.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/allocate_neigh.f90
allocate_rho.o : ../SRC/ALLOCATIONS/allocate_rho.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/allocate_rho.f90
allocate_umb.o : ../SRC/ALLOCATIONS/allocate_umb.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/allocate_umb.f90
allocate_steered.o : ../SRC/ALLOCATIONS/allocate_steered.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/allocate_steered.f90
reallocate_f.o : ../SRC/ALLOCATIONS/reallocate_f.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/reallocate_f.f90
reallocate_h.o : ../SRC/ALLOCATIONS/reallocate_h.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/reallocate_h.f90
reallocate_neigh.o : ../SRC/ALLOCATIONS/reallocate_neigh.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/reallocate_neigh.f90
reallocate_rho.o : ../SRC/ALLOCATIONS/reallocate_rho.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/reallocate_rho.f90
allocate_dos.o : ../SRC/ALLOCATIONS/allocate_dos.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/allocate_dos.f90
allocate_grid.o : ../SRC/ALLOCATIONS/allocate_grid.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/allocate_grid.f90
allocate_trans.o : ../SRC/ALLOCATIONS/allocate_trans.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/allocate_trans.f90
#====== variant : 'ORDERN'
allocate_ordern.o : ../SRC/ALLOCATIONS/allocate_ordern.f90
	$(F90) $(FFLAGS)  -c ../SRC/ALLOCATIONS/allocate_ordern.f90




#**************************************************
#   ASSEMBLERS
#**************************************************
#====== variant : ''
assemble_olsxc_1c.o : ../SRC/ASSEMBLERS/assemble_olsxc_1c.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_olsxc_1c.f90
assemble_hxc_1c.o : ../SRC/ASSEMBLERS/assemble_hxc_1c.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_hxc_1c.f90
assemble_2c.o : ../SRC/ASSEMBLERS/assemble_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_2c.f90
assemble_3c.o : ../SRC/ASSEMBLERS/assemble_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_3c.f90
assemble_ca_2c.o : ../SRC/ASSEMBLERS/assemble_ca_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_ca_2c.f90
assemble_3c_PP.o : ../SRC/ASSEMBLERS/assemble_3c_PP.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_3c_PP.f90
assemble_ca_3c.o : ../SRC/ASSEMBLERS/assemble_ca_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_ca_3c.f90
assemble_eh_2c.o : ../SRC/ASSEMBLERS/assemble_eh_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_eh_2c.f90
assemble_eh_usr.o : ../SRC/ASSEMBLERS/assemble_eh_usr.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_eh_usr.f90
assemble_F.o : ../SRC/ASSEMBLERS/assemble_F.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_F.f90
assemble_hxc_2c.o : ../SRC/ASSEMBLERS/assemble_hxc_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_hxc_2c.f90
assemble_hxc_3c.o : ../SRC/ASSEMBLERS/assemble_hxc_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_hxc_3c.f90
assemble_lr.o : ../SRC/ASSEMBLERS/assemble_lr.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_lr.f90
assemble_sVNL.o : ../SRC/ASSEMBLERS/assemble_sVNL.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_sVNL.f90
assemble_usr.o : ../SRC/ASSEMBLERS/assemble_usr.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_usr.f90
buildh.o : ../SRC/ASSEMBLERS/buildh.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/buildh.f90
assemble_olsxc_on.o : ../SRC/ASSEMBLERS/assemble_olsxc_on.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_olsxc_on.f90
assemble_olsxc_off.o : ../SRC/ASSEMBLERS/assemble_olsxc_off.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_olsxc_off.f90
build_olsxc_on.o : ../SRC/ASSEMBLERS/build_olsxc_on.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/build_olsxc_on.f90
build_olsxc_off.o : ../SRC/ASSEMBLERS/build_olsxc_off.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/build_olsxc_off.f90
average_rho.o : ../SRC/ASSEMBLERS/average_rho.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/average_rho.f90
build_snxc_on.o : ../SRC/ASSEMBLERS/build_snxc_on.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/build_snxc_on.f90
build_snxc_off.o : ../SRC/ASSEMBLERS/build_snxc_off.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/build_snxc_off.f90
assemble_snxc_on.o : ../SRC/ASSEMBLERS/assemble_snxc_on.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_snxc_on.f90
assemble_snxc_off.o : ../SRC/ASSEMBLERS/assemble_snxc_off.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_snxc_off.f90
build_ca_snxc_on.o : ../SRC/ASSEMBLERS/build_ca_snxc_on.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/build_ca_snxc_on.f90
build_ca_olsxc_on.o : ../SRC/ASSEMBLERS/build_ca_olsxc_on.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/build_ca_olsxc_on.f90
assemble_h.o : ../SRC/ASSEMBLERS/assemble_h.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_h.f90
assemble_mcweda.o : ../SRC/ASSEMBLERS/assemble_mcweda.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_mcweda.f90
assemble_hxc.o : ../SRC/ASSEMBLERS/assemble_hxc.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_hxc.f90
assemble_eh.o : ../SRC/ASSEMBLERS/assemble_eh.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_eh.f90
getenergy.o : ../SRC/ASSEMBLERS/getenergy.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/getenergy.f90
getenergy_hxc.o : ../SRC/ASSEMBLERS/getenergy_hxc.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/getenergy_hxc.f90
getenergy_mcweda.o : ../SRC/ASSEMBLERS/getenergy_mcweda.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/getenergy_mcweda.f90
getenergy_eh.o : ../SRC/ASSEMBLERS/getenergy_eh.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/getenergy_eh.f90
assemble_h_ks.o : ../SRC/ASSEMBLERS/assemble_h_ks.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_h_ks.f90
getenergy_KS.o : ../SRC/ASSEMBLERS/getenergy_KS.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/getenergy_KS.f90
assemble_S.o : ../SRC/ASSEMBLERS/assemble_S.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_S.f90
assemble_2c_S.o : ../SRC/ASSEMBLERS/assemble_2c_S.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_2c_S.f90
assemble_hartree.o : ../SRC/ASSEMBLERS/assemble_hartree.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_hartree.f90
assemble_scissor.o : ../SRC/ASSEMBLERS/assemble_scissor.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_scissor.f90
assemble_ca_2c_dip.o : ../SRC/ASSEMBLERS/assemble_ca_2c_dip.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_ca_2c_dip.f90
assemble_ca_3c_dip.o : ../SRC/ASSEMBLERS/assemble_ca_3c_dip.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_ca_3c_dip.f90
assemble_lr_dip.o : ../SRC/ASSEMBLERS/assemble_lr_dip.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_lr_dip.f90
assemble_zw_1c_na.o : ../SRC/ASSEMBLERS/assemble_zw_1c_na.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_zw_1c_na.f90
assemble_zw_2c_ct.o : ../SRC/ASSEMBLERS/assemble_zw_2c_ct.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_zw_2c_ct.f90
assemble_zw_3c_ct.o : ../SRC/ASSEMBLERS/assemble_zw_3c_ct.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_zw_3c_ct.f90
assemble_xczw.o : ../SRC/ASSEMBLERS/assemble_xczw.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_xczw.f90
assemble_zw_off_na.o : ../SRC/ASSEMBLERS/assemble_zw_off_na.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_zw_off_na.f90
assemble_zw_on_na.o : ../SRC/ASSEMBLERS/assemble_zw_on_na.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_zw_on_na.f90
build_zw_off_na.o : ../SRC/ASSEMBLERS/build_zw_off_na.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/build_zw_off_na.f90
build_zw_on_na.o : ../SRC/ASSEMBLERS/build_zw_on_na.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/build_zw_on_na.f90
assemble_1c_vdip.o : ../SRC/ASSEMBLERS/assemble_1c_vdip.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_1c_vdip.f90
getenergy_zw.o : ../SRC/ASSEMBLERS/getenergy_zw.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/getenergy_zw.f90
#====== variant : 'ORDERN'
assemble_2c_ordern_final.o : ../SRC/ASSEMBLERS/assemble_2c_ordern_final.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_2c_ordern_final.f90
assemble_2c_ordern_init.o : ../SRC/ASSEMBLERS/assemble_2c_ordern_init.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_2c_ordern_init.f90
assemble_3c_ordern_final.o : ../SRC/ASSEMBLERS/assemble_3c_ordern_final.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_3c_ordern_final.f90
assemble_ca_2c_ordern_final.o : ../SRC/ASSEMBLERS/assemble_ca_2c_ordern_final.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_ca_2c_ordern_final.f90
assemble_ca_3c_ordern_final.o : ../SRC/ASSEMBLERS/assemble_ca_3c_ordern_final.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_ca_3c_ordern_final.f90
assemble_eh_2c_ordern_final.o : ../SRC/ASSEMBLERS/assemble_eh_2c_ordern_final.f90
	$(F90) $(FFLAGS)  -c ../SRC/ASSEMBLERS/assemble_eh_2c_ordern_final.f90




#**************************************************
#   GRID
#**************************************************
#====== variant : ''
assemble_KS_den0.o : ../SRC/GRID/assemble_KS_den0.f90
	$(F90) $(FFLAGS)  -c ../SRC/GRID/assemble_KS_den0.f90
assemble_KS_den.o : ../SRC/GRID/assemble_KS_den.f90
	$(F90) $(FFLAGS)  -c ../SRC/GRID/assemble_KS_den.f90
assemble_KS_usr.o : ../SRC/GRID/assemble_KS_usr.f90
	$(F90) $(FFLAGS)  -c ../SRC/GRID/assemble_KS_usr.f90
laplace_fft.o : ../SRC/GRID/laplace_fft.f90
	$(F90) $(FFLAGS)  -c ../SRC/GRID/laplace_fft.f90
assemble_KS_dcc.o : ../SRC/GRID/assemble_KS_dcc.f90
	$(F90) $(FFLAGS)  -c ../SRC/GRID/assemble_KS_dcc.f90
assemble_KS_mat.o : ../SRC/GRID/assemble_KS_mat.f90
	$(F90) $(FFLAGS)  -c ../SRC/GRID/assemble_KS_mat.f90
mixer_KS.o : ../SRC/GRID/mixer_KS.f90
	$(F90) $(FFLAGS)  -c ../SRC/GRID/mixer_KS.f90
writeout_charges_KS.o : ../SRC/GRID/writeout_charges_KS.f90
	$(F90) $(FFLAGS)  -c ../SRC/GRID/writeout_charges_KS.f90
writeout_xsf.o : ../SRC/GRID/writeout_xsf.f90
	$(F90) $(FFLAGS)  -c ../SRC/GRID/writeout_xsf.f90
assemble_KS_vna.o : ../SRC/GRID/assemble_KS_vna.f90
	$(F90) $(FFLAGS)  -c ../SRC/GRID/assemble_KS_vna.f90
get_Hort.o : ../SRC/GRID/get_Hort.f90
	$(F90) $(FFLAGS)  -c ../SRC/GRID/get_Hort.f90




#**************************************************
#   INITIALIZERS
#**************************************************
#====== variant : ''
diagnostics.o : ../SRC/INITIALIZERS/diagnostics.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/diagnostics.f90
initatomicE.o : ../SRC/INITIALIZERS/initatomicE.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initatomicE.f90
initconstraints.o : ../SRC/INITIALIZERS/initconstraints.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initconstraints.f90
initcharges.o : ../SRC/INITIALIZERS/initcharges.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initcharges.f90
initconstants.o : ../SRC/INITIALIZERS/initconstants.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initconstants.f90
initboxes.o : ../SRC/INITIALIZERS/initboxes.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initboxes.f90
initkpoints.o : ../SRC/INITIALIZERS/initkpoints.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initkpoints.f90
initmasses.o : ../SRC/INITIALIZERS/initmasses.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initmasses.f90
initneighbors.o : ../SRC/INITIALIZERS/initneighbors.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initneighbors.f90
welcome.o : ../SRC/INITIALIZERS/welcome.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/welcome.f90
make_mu2shell.o : ../SRC/INITIALIZERS/make_mu2shell.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/make_mu2shell.f90
make_munu.o : ../SRC/INITIALIZERS/make_munu.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/make_munu.f90
make_munuPP.o : ../SRC/INITIALIZERS/make_munuPP.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/make_munuPP.f90
restart.o : ../SRC/INITIALIZERS/restart.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/restart.f90
make_munuDipY.o : ../SRC/INITIALIZERS/make_munuDipY.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/make_munuDipY.f90
make_munuDipX.o : ../SRC/INITIALIZERS/make_munuDipX.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/make_munuDipX.f90
zero_ang_mom.o : ../SRC/INITIALIZERS/zero_ang_mom.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/zero_ang_mom.f90
initamat.o : ../SRC/INITIALIZERS/initamat.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initamat.f90
make_munuS.o : ../SRC/INITIALIZERS/make_munuS.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/make_munuS.f90
initNH.o : ../SRC/INITIALIZERS/initNH.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initNH.f90
getkpoints.o : ../SRC/INITIALIZERS/getkpoints.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/getkpoints.f90
greatKAuto.o : ../SRC/INITIALIZERS/greatKAuto.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/greatKAuto.f90
greatKsubsAuto.o : ../SRC/INITIALIZERS/greatKsubsAuto.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/greatKsubsAuto.f90
initgrid.o : ../SRC/INITIALIZERS/initgrid.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initgrid.f90
initdenmat.o : ../SRC/INITIALIZERS/initdenmat.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initdenmat.f90
get_info_orbital.o : ../SRC/INITIALIZERS/get_info_orbital.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/get_info_orbital.f90
initbasics.o : ../SRC/INITIALIZERS/initbasics.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initbasics.f90
initcharges_KS.o : ../SRC/INITIALIZERS/initcharges_KS.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initcharges_KS.f90
initcDFT.o : ../SRC/INITIALIZERS/initcDFT.f90
	$(F90) $(FFLAGS)  -c ../SRC/INITIALIZERS/initcDFT.f90
#====== variant : 'MPI-k'
init_MPI.o : ../SRC/INITIALIZERS/init_MPI.f90
	$(F90) $(FFLAGS) -I/usr/include/mpich -c ../SRC/INITIALIZERS/init_MPI.f90




#**************************************************
#   INTERPOLATERS
#**************************************************
#====== variant : ''
buildspline_1d.o : ../SRC/INTERPOLATERS/buildspline_1d.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/buildspline_1d.f90
interpolate_1d.o : ../SRC/INTERPOLATERS/interpolate_1d.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/interpolate_1d.f90
interpolate_2d.o : ../SRC/INTERPOLATERS/interpolate_2d.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/interpolate_2d.f90
recover_2c.o : ../SRC/INTERPOLATERS/recover_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/recover_2c.f90
recover_3c.o : ../SRC/INTERPOLATERS/recover_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/recover_3c.f90
recover_PP.o : ../SRC/INTERPOLATERS/recover_PP.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/recover_PP.f90
recoverC.o : ../SRC/INTERPOLATERS/recoverC.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/recoverC.f90
setterp_2d.o : ../SRC/INTERPOLATERS/setterp_2d.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/setterp_2d.f90
recover_2cDipY.o : ../SRC/INTERPOLATERS/recover_2cDipY.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/recover_2cDipY.f90
recover_2cDipX.o : ../SRC/INTERPOLATERS/recover_2cDipX.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/recover_2cDipX.f90
recover_S.o : ../SRC/INTERPOLATERS/recover_S.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/recover_S.f90
buildspline2_1d.o : ../SRC/INTERPOLATERS/buildspline2_1d.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/buildspline2_1d.f90
getpsi.o : ../SRC/INTERPOLATERS/getpsi.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/getpsi.f90
getYlm.o : ../SRC/INTERPOLATERS/getYlm.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/getYlm.f90
getvna.o : ../SRC/INTERPOLATERS/getvna.f90
	$(F90) $(FFLAGS)  -c ../SRC/INTERPOLATERS/getvna.f90




#**************************************************
#   LOOPS
#**************************************************
#====== variant : ''
main_loop.o : ../SRC/LOOPS/main_loop.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/main_loop.f90
main_loop_MD.o : ../SRC/LOOPS/main_loop_MD.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/main_loop_MD.f90
main_loop_CG.o : ../SRC/LOOPS/main_loop_CG.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/main_loop_CG.f90
scf_loop.o : ../SRC/LOOPS/scf_loop.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/scf_loop.f90
scf_loop_harris.o : ../SRC/LOOPS/scf_loop_harris.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/scf_loop_harris.f90
main_loop_NEB.o : ../SRC/LOOPS/main_loop_NEB.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/main_loop_NEB.f90
main_loop_DM.o : ../SRC/LOOPS/main_loop_DM.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/main_loop_DM.f90
scf_loop_ks.o : ../SRC/LOOPS/scf_loop_ks.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/scf_loop_ks.f90
main_loop_importrho.o : ../SRC/LOOPS/main_loop_importrho.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/main_loop_importrho.f90
main_loop_TDSE.o : ../SRC/LOOPS/main_loop_TDSE.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/main_loop_TDSE.f90
main_loop_MDET.o : ../SRC/LOOPS/main_loop_MDET.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/main_loop_MDET.f90
main_loop_MIN.o : ../SRC/LOOPS/main_loop_MIN.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/main_loop_MIN.f90
main_loop_NAC.o : ../SRC/LOOPS/main_loop_NAC.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/main_loop_NAC.f90
main_loop_FIRE.o : ../SRC/LOOPS/main_loop_FIRE.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/main_loop_FIRE.f90
main_loop_socket.o : ../SRC/LOOPS/main_loop_socket.f90
	$(F90) $(FFLAGS)  -c ../SRC/LOOPS/main_loop_socket.f90




#**************************************************
#   MAIN
#**************************************************
#====== variant : ''
fireball.o : ../SRC/MAIN/fireball.f90
	$(F90) $(FFLAGS)  -c ../SRC/MAIN/fireball.f90
#====== variant : 'SERVER'
fireball_server.o : ../SRC/MAIN/fireball_server.f90
	$(F90) $(FFLAGS)  -c ../SRC/MAIN/fireball_server.f90
fireball_server_amber.o : ../SRC/MAIN/fireball_server_amber.f90
	$(F90) $(FFLAGS)  -c ../SRC/MAIN/fireball_server_amber.f90




#**************************************************
#   MD
#**************************************************
#====== variant : ''
cross.o : ../SRC/MD/cross.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/cross.f90
factorial.o : ../SRC/MD/factorial.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/factorial.f90
predictor.o : ../SRC/MD/predictor.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/predictor.f90
gaussT.o : ../SRC/MD/gaussT.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/gaussT.f90
corrector.o : ../SRC/MD/corrector.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/corrector.f90
imaged.o : ../SRC/MD/imaged.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/imaged.f90
setgear.o : ../SRC/MD/setgear.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/setgear.f90
phimat.o : ../SRC/MD/phimat.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/phimat.f90
bvec.o : ../SRC/MD/bvec.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/bvec.f90
soldm.o : ../SRC/MD/soldm.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/soldm.f90
NHCThermostat.o : ../SRC/MD/NHCThermostat.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/NHCThermostat.f90
get_enk.o : ../SRC/MD/get_enk.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/get_enk.f90
writeHNose.o : ../SRC/MD/writeHNose.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/writeHNose.f90
resetNHC.o : ../SRC/MD/resetNHC.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/resetNHC.f90
move_ions.o : ../SRC/MD/move_ions.f90
	$(F90) $(FFLAGS)  -c ../SRC/MD/move_ions.f90




#**************************************************
#   MODULES
#**************************************************
#====== variant : ''
dimensions.o : ../SRC/MODULES/dimensions.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/dimensions.f90
barrier.o : ../SRC/MODULES/barrier.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/barrier.f90
charges.o : ../SRC/MODULES/charges.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/charges.f90
configuration.o : ../SRC/MODULES/configuration.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/configuration.f90
constants_fireball.o : ../SRC/MODULES/constants_fireball.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/constants_fireball.f90
density.o : ../SRC/MODULES/density.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/density.f90
forces.o : ../SRC/MODULES/forces.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/forces.f90
fragments.o : ../SRC/MODULES/fragments.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/fragments.f90
gaussG.o : ../SRC/MODULES/gaussG.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/gaussG.f90
integrals.o : ../SRC/MODULES/integrals.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/integrals.f90
interactions.o : ../SRC/MODULES/interactions.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/interactions.f90
kpoints.o : ../SRC/MODULES/kpoints.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/kpoints.f90
neighbor_map.o : ../SRC/MODULES/neighbor_map.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/neighbor_map.f90
umbrella.o : ../SRC/MODULES/umbrella.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/umbrella.f90
steered.o : ../SRC/MODULES/steered.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/steered.f90
optimization.o : ../SRC/MODULES/optimization.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/optimization.f90
module_dos.o : ../SRC/MODULES/module_dos.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/module_dos.f90
dynamo.o : ../SRC/MODULES/dynamo.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/dynamo.f90
cproc.o : ../SRC/MODULES/cproc.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/cproc.f90
noseHoover.o : ../SRC/MODULES/noseHoover.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/noseHoover.f90
scf.o : ../SRC/MODULES/scf.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/scf.f90
grid.o : ../SRC/MODULES/grid.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/grid.f90
wavefunction.o : ../SRC/MODULES/wavefunction.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/wavefunction.f90
neb_module.o : ../SRC/MODULES/neb_module.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/neb_module.f90
vnneutral.o : ../SRC/MODULES/vnneutral.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/vnneutral.f90
transport.o : ../SRC/MODULES/transport.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/transport.f90
matmultmod.o : ../SRC/MODULES/matmultmod.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/matmultmod.f90
options.o : ../SRC/MODULES/options.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/options.f90
outputs.o : ../SRC/MODULES/outputs.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/outputs.f90
MD.o : ../SRC/MODULES/MD.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/MD.f90
energy.o : ../SRC/MODULES/energy.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/energy.f90
mpi_main.o : ../SRC/MODULES/mpi_main.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/mpi_main.f90
tdse.o : ../SRC/MODULES/tdse.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/tdse.f90
bias.o : ../SRC/MODULES/bias.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/bias.f90
nonadiabatic.o : ../SRC/MODULES/nonadiabatic.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/nonadiabatic.f90
hartree.o : ../SRC/MODULES/hartree.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/hartree.f90
fsockets.o : ../SRC/MODULES/fsockets.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/fsockets.f90
fb_socket.o : ../SRC/MODULES/fb_socket.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/fb_socket.f90
classicMD.o : ../SRC/MODULES/classicMD.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/classicMD.f90
#====== variant : 'ORDERN'
ordern.o : ../SRC/MODULES/ordern.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/ordern.f90
#====== variant : 'MPI-k'
mpi_declarations.o : ../SRC/MODULES/mpi_declarations.f90
	$(F90) $(FFLAGS)  -c ../SRC/MODULES/mpi_declarations.f90




#**************************************************
#   NEIGHBORS
#**************************************************
#====== variant : ''
backnay.o : ../SRC/NEIGHBORS/backnay.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEIGHBORS/backnay.f90
common_neighbors.o : ../SRC/NEIGHBORS/common_neighbors.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEIGHBORS/common_neighbors.f90
find_neigh_max.o : ../SRC/NEIGHBORS/find_neigh_max.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEIGHBORS/find_neigh_max.f90
find_neigh_max_class.o : ../SRC/NEIGHBORS/find_neigh_max_class.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEIGHBORS/find_neigh_max_class.f90
mpairnay.o : ../SRC/NEIGHBORS/mpairnay.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEIGHBORS/mpairnay.f90
neighbors.o : ../SRC/NEIGHBORS/neighbors.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEIGHBORS/neighbors.f90
neighbors_pairs.o : ../SRC/NEIGHBORS/neighbors_pairs.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEIGHBORS/neighbors_pairs.f90
find_neighPP_max.o : ../SRC/NEIGHBORS/find_neighPP_max.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEIGHBORS/find_neighPP_max.f90
neighborsPP.o : ../SRC/NEIGHBORS/neighborsPP.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEIGHBORS/neighborsPP.f90
common_neighborsPP.o : ../SRC/NEIGHBORS/common_neighborsPP.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEIGHBORS/common_neighborsPP.f90
num_neigh_tot.o : ../SRC/NEIGHBORS/num_neigh_tot.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEIGHBORS/num_neigh_tot.f90




#**************************************************
#   PRESSURE
#**************************************************
#====== variant : ''
hmetric.o : ../SRC/PRESSURE/hmetric.f90
	$(F90) $(FFLAGS)  -c ../SRC/PRESSURE/hmetric.f90
initpressure.o : ../SRC/PRESSURE/initpressure.f90
	$(F90) $(FFLAGS)  -c ../SRC/PRESSURE/initpressure.f90
invert3x3.o : ../SRC/PRESSURE/invert3x3.f90
	$(F90) $(FFLAGS)  -c ../SRC/PRESSURE/invert3x3.f90




#**************************************************
#   READFILES
#**************************************************
#====== variant : ''
append_string.o : ../SRC/READFILES/append_string.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/append_string.f90
read_1c.o : ../SRC/READFILES/read_1c.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/read_1c.f90
read_2c.o : ../SRC/READFILES/read_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/read_2c.f90
read_3c.o : ../SRC/READFILES/read_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/read_3c.f90
readbasis.o : ../SRC/READFILES/readbasis.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readbasis.f90
readbarrier.o : ../SRC/READFILES/readbarrier.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readbarrier.f90
readdata_2c.o : ../SRC/READFILES/readdata_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readdata_2c.f90
readdata_3c.o : ../SRC/READFILES/readdata_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readdata_3c.f90
readfragments.o : ../SRC/READFILES/readfragments.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readfragments.f90
readheader_2c.o : ../SRC/READFILES/readheader_2c.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readheader_2c.f90
readheader_3c.o : ../SRC/READFILES/readheader_3c.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readheader_3c.f90
readinfo.o : ../SRC/READFILES/readinfo.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readinfo.f90
readlvs.o : ../SRC/READFILES/readlvs.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readlvs.f90
readparam.o : ../SRC/READFILES/readparam.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readparam.f90
readphi.o : ../SRC/READFILES/readphi.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readphi.f90
readpressure.o : ../SRC/READFILES/readpressure.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readpressure.f90
readquench.o : ../SRC/READFILES/readquench.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readquench.f90
readsa.o : ../SRC/READFILES/readsa.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readsa.f90
readvdw.o : ../SRC/READFILES/readvdw.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readvdw.f90
readcgo.o : ../SRC/READFILES/readcgo.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readcgo.f90
readdos.o : ../SRC/READFILES/readdos.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readdos.f90
readgaussG.o : ../SRC/READFILES/readgaussG.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readgaussG.f90
findFdata.o : ../SRC/READFILES/findFdata.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/findFdata.f90
readgrid.o : ../SRC/READFILES/readgrid.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readgrid.f90
read_wf.o : ../SRC/READFILES/read_wf.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/read_wf.f90
read_vna.o : ../SRC/READFILES/read_vna.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/read_vna.f90
readtrans.o : ../SRC/READFILES/readtrans.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readtrans.f90
readbind.o : ../SRC/READFILES/readbind.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readbind.f90
readhop.o : ../SRC/READFILES/readhop.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readhop.f90
readdata.o : ../SRC/READFILES/readdata.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readdata.f90
readdata_hxc.o : ../SRC/READFILES/readdata_hxc.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readdata_hxc.f90
readdata_mcweda.o : ../SRC/READFILES/readdata_mcweda.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readdata_mcweda.f90
readdata_xczw.o : ../SRC/READFILES/readdata_xczw.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readdata_xczw.f90
readdata_eh.o : ../SRC/READFILES/readdata_eh.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readdata_eh.f90
checksum_options.o : ../SRC/READFILES/checksum_options.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/checksum_options.f90
readdata_KS.o : ../SRC/READFILES/readdata_KS.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readdata_KS.f90
getsections.o : ../SRC/READFILES/getsections.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/getsections.f90
readdata_classicMD.o : ../SRC/READFILES/readdata_classicMD.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readdata_classicMD.f90
readhartree.o : ../SRC/READFILES/readhartree.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readhartree.f90
readephc.o : ../SRC/READFILES/readephc.f90
	$(F90) $(FFLAGS)  -c ../SRC/READFILES/readephc.f90




#**************************************************
#   ROTATIONS
#**************************************************
#====== variant : ''
chooser.o : ../SRC/ROTATIONS/chooser.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/chooser.f90
chooserd.o : ../SRC/ROTATIONS/chooserd.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/chooserd.f90
deps2center.o : ../SRC/ROTATIONS/deps2center.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/deps2center.f90
deps3center.o : ../SRC/ROTATIONS/deps3center.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/deps3center.f90
makeDmat.o : ../SRC/ROTATIONS/makeDmat.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/makeDmat.f90
makeDmatPP.o : ../SRC/ROTATIONS/makeDmatPP.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/makeDmatPP.f90
rotate.o : ../SRC/ROTATIONS/rotate.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/rotate.f90
rotated.o : ../SRC/ROTATIONS/rotated.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/rotated.f90
rotatedPP.o : ../SRC/ROTATIONS/rotatedPP.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/rotatedPP.f90
twister.o : ../SRC/ROTATIONS/twister.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/twister.f90
twisterd.o : ../SRC/ROTATIONS/twisterd.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/twisterd.f90
rotatePP.o : ../SRC/ROTATIONS/rotatePP.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/rotatePP.f90
epsilon.o : ../SRC/ROTATIONS/epsilon.f90
	$(F90) $(FFLAGS)  -c ../SRC/ROTATIONS/epsilon.f90




#**************************************************
#   THERMOINT
#**************************************************




#**************************************************
#   SOCKETS
#**************************************************
#====== variant : ''
get_geometry.o : ../SRC/SOCKETS/get_geometry.f90
	$(F90) $(FFLAGS)  -c ../SRC/SOCKETS/get_geometry.f90
create_socket.o : ../SRC/SOCKETS/create_socket.f90
	$(F90) $(FFLAGS)  -c ../SRC/SOCKETS/create_socket.f90
send_geometry.o : ../SRC/SOCKETS/send_geometry.f90
	$(F90) $(FFLAGS)  -c ../SRC/SOCKETS/send_geometry.f90
sendrecv.o : ../SRC/SOCKETS/sendrecv.f90
	$(F90) $(FFLAGS)  -c ../SRC/SOCKETS/sendrecv.f90
soc_init.o : ../SRC/SOCKETS/soc_init.f90
	$(F90) $(FFLAGS)  -c ../SRC/SOCKETS/soc_init.f90




#**************************************************
#   UMBRELLA
#**************************************************
#====== variant : ''
assemble_umbrella.o : ../SRC/UMBRELLA/assemble_umbrella.f90
	$(F90) $(FFLAGS)  -c ../SRC/UMBRELLA/assemble_umbrella.f90
Dassemble_umbrella.o : ../SRC/UMBRELLA/Dassemble_umbrella.f90
	$(F90) $(FFLAGS)  -c ../SRC/UMBRELLA/Dassemble_umbrella.f90
get_umbrella.o : ../SRC/UMBRELLA/get_umbrella.f90
	$(F90) $(FFLAGS)  -c ../SRC/UMBRELLA/get_umbrella.f90
readumbrella.o : ../SRC/UMBRELLA/readumbrella.f90
	$(F90) $(FFLAGS)  -c ../SRC/UMBRELLA/readumbrella.f90
assemble_steered.o : ../SRC/UMBRELLA/assemble_steered.f90
	$(F90) $(FFLAGS)  -c ../SRC/UMBRELLA/assemble_steered.f90
Dassemble_steered.o : ../SRC/UMBRELLA/Dassemble_steered.f90
	$(F90) $(FFLAGS)  -c ../SRC/UMBRELLA/Dassemble_steered.f90
get_steered.o : ../SRC/UMBRELLA/get_steered.f90
	$(F90) $(FFLAGS)  -c ../SRC/UMBRELLA/get_steered.f90
readsteered.o : ../SRC/UMBRELLA/readsteered.f90
	$(F90) $(FFLAGS)  -c ../SRC/UMBRELLA/readsteered.f90




#**************************************************
#   XC
#**************************************************
#====== variant : ''
ceperley_alder.o : ../SRC/XC/ceperley_alder.f90
	$(F90) $(FFLAGS)  -c ../SRC/XC/ceperley_alder.f90
cepal.o : ../SRC/XC/cepal.f90
	$(F90) $(FFLAGS)  -c ../SRC/XC/cepal.f90




#**************************************************
#   CG
#**************************************************
#====== variant : ''
cgo.o : ../SRC/CG/cgo.f90
	$(F90) $(FFLAGS)  -c ../SRC/CG/cgo.f90
bfgs.o : ../SRC/CG/bfgs.f90
	$(F90) $(FFLAGS)  -c ../SRC/CG/bfgs.f90
l-bfgs-b.o : ../SRC/CG/l-bfgs-b.f90
	$(F90) $(FFLAGS)  -c ../SRC/CG/l-bfgs-b.f90
FIRE.o : ../SRC/CG/FIRE.f90
	$(F90) $(FFLAGS)  -c ../SRC/CG/FIRE.f90




#**************************************************
#   DOS
#**************************************************
#====== variant : ''
dos.o : ../SRC/DOS/dos.f90
	$(F90) $(FFLAGS)  -c ../SRC/DOS/dos.f90
writeout_dos.o : ../SRC/DOS/writeout_dos.f90
	$(F90) $(FFLAGS)  -c ../SRC/DOS/writeout_dos.f90
writeout_dosng.o : ../SRC/DOS/writeout_dosng.f90
	$(F90) $(FFLAGS)  -c ../SRC/DOS/writeout_dosng.f90
hoppings.o : ../SRC/DOS/hoppings.f90
	$(F90) $(FFLAGS)  -c ../SRC/DOS/hoppings.f90
writeout_atom.o : ../SRC/DOS/writeout_atom.f90
	$(F90) $(FFLAGS)  -c ../SRC/DOS/writeout_atom.f90
hamilt_atom.o : ../SRC/DOS/hamilt_atom.f90
	$(F90) $(FFLAGS)  -c ../SRC/DOS/hamilt_atom.f90




#**************************************************
#   NEB
#**************************************************
#====== variant : ''
initneb.o : ../SRC/NEB/initneb.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEB/initneb.f90
neb.o : ../SRC/NEB/neb.f90
	$(F90) $(FFLAGS)  -c ../SRC/NEB/neb.f90




#**************************************************
#   TDSE
#**************************************************
#====== variant : ''
ete_loop.o : ../SRC/TDSE/ete_loop.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/ete_loop.f90
psi2es.o : ../SRC/TDSE/psi2es.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/psi2es.f90
eigenHS.o : ../SRC/TDSE/eigenHS.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/eigenHS.f90
tddenmat.o : ../SRC/TDSE/tddenmat.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/tddenmat.f90
tddiag_k.o : ../SRC/TDSE/tddiag_k.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/tddiag_k.f90
diag_Sk.o : ../SRC/TDSE/diag_Sk.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/diag_Sk.f90
diag_Hk.o : ../SRC/TDSE/diag_Hk.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/diag_Hk.f90
allocate_tdse.o : ../SRC/TDSE/allocate_tdse.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/allocate_tdse.f90
tdbc.o : ../SRC/TDSE/tdbc.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/tdbc.f90
propTpsi.o : ../SRC/TDSE/propTpsi.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/propTpsi.f90
readtdse.o : ../SRC/TDSE/readtdse.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/readtdse.f90
initpsi.o : ../SRC/TDSE/initpsi.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/initpsi.f90
ortho_H.o : ../SRC/TDSE/ortho_H.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/ortho_H.f90
get_QLow.o : ../SRC/TDSE/get_QLow.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/get_QLow.f90
get_QMul.o : ../SRC/TDSE/get_QMul.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/get_QMul.f90
postete.o : ../SRC/TDSE/postete.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/postete.f90
wrtout_psiT.o : ../SRC/TDSE/wrtout_psiT.f90
	$(F90) $(FFLAGS)  -c ../SRC/TDSE/wrtout_psiT.f90




#**************************************************
#   TRANS
#**************************************************
#====== variant : ''
assemble_t12_fit.o : ../SRC/TRANS/assemble_t12_fit.f90
	$(F90) $(FFLAGS)  -c ../SRC/TRANS/assemble_t12_fit.f90
assemble_t12_bare.o : ../SRC/TRANS/assemble_t12_bare.f90
	$(F90) $(FFLAGS)  -c ../SRC/TRANS/assemble_t12_bare.f90
calcG.o : ../SRC/TRANS/calcG.f90
	$(F90) $(FFLAGS)  -c ../SRC/TRANS/calcG.f90
assemble_Hsam.o : ../SRC/TRANS/assemble_Hsam.f90
	$(F90) $(FFLAGS)  -c ../SRC/TRANS/assemble_Hsam.f90
assemble_Gsam.o : ../SRC/TRANS/assemble_Gsam.f90
	$(F90) $(FFLAGS)  -c ../SRC/TRANS/assemble_Gsam.f90
assemble_Dxx.o : ../SRC/TRANS/assemble_Dxx.f90
	$(F90) $(FFLAGS)  -c ../SRC/TRANS/assemble_Dxx.f90
sqrt_mat.o : ../SRC/TRANS/sqrt_mat.f90
	$(F90) $(FFLAGS)  -c ../SRC/TRANS/sqrt_mat.f90
interpolate_hop.o : ../SRC/TRANS/interpolate_hop.f90
	$(F90) $(FFLAGS)  -c ../SRC/TRANS/interpolate_hop.f90
gethop.o : ../SRC/TRANS/gethop.f90
	$(F90) $(FFLAGS)  -c ../SRC/TRANS/gethop.f90




#**************************************************
#   BIAS
#**************************************************
#====== variant : ''
assemble_bias.o : ../SRC/BIAS/assemble_bias.f90
	$(F90) $(FFLAGS)  -c ../SRC/BIAS/assemble_bias.f90
Dassemble_bias.o : ../SRC/BIAS/Dassemble_bias.f90
	$(F90) $(FFLAGS)  -c ../SRC/BIAS/Dassemble_bias.f90
allocate_bias.o : ../SRC/BIAS/allocate_bias.f90
	$(F90) $(FFLAGS)  -c ../SRC/BIAS/allocate_bias.f90
reallocate_bias.o : ../SRC/BIAS/reallocate_bias.f90
	$(F90) $(FFLAGS)  -c ../SRC/BIAS/reallocate_bias.f90
readbias.o : ../SRC/BIAS/readbias.f90
	$(F90) $(FFLAGS)  -c ../SRC/BIAS/readbias.f90




#**************************************************
#   NAC
#**************************************************
#====== variant : ''
allocate_nac.o : ../SRC/NAC/allocate_nac.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/allocate_nac.f90
assemble_G_S.o : ../SRC/NAC/assemble_G_S.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/assemble_G_S.f90
nacouplings.o : ../SRC/NAC/nacouplings.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/nacouplings.f90
build_gover1c.o : ../SRC/NAC/build_gover1c.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/build_gover1c.f90
init_mdet.o : ../SRC/NAC/init_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/init_mdet.f90
mdetdenmat.o : ../SRC/NAC/mdetdenmat.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/mdetdenmat.f90
getforces_mdet.o : ../SRC/NAC/getforces_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/getforces_mdet.f90
save_mdetstuff.o : ../SRC/NAC/save_mdetstuff.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/save_mdetstuff.f90
evolve_ks_states.o : ../SRC/NAC/evolve_ks_states.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/evolve_ks_states.f90
deallocate_nac.o : ../SRC/NAC/deallocate_nac.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/deallocate_nac.f90
dcdt_nac.o : ../SRC/NAC/dcdt_nac.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/dcdt_nac.f90
Dassemble_2c_mdet.o : ../SRC/NAC/Dassemble_2c_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_2c_mdet.f90
Dassemble_2c_PP_mdet.o : ../SRC/NAC/Dassemble_2c_PP_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_2c_PP_mdet.f90
Dassemble_olsxc_on_mdet.o : ../SRC/NAC/Dassemble_olsxc_on_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_olsxc_on_mdet.f90
Dassemble_olsxc_2c_mdet.o : ../SRC/NAC/Dassemble_olsxc_2c_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_olsxc_2c_mdet.f90
Dassemble_3c_mdet.o : ../SRC/NAC/Dassemble_3c_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_3c_mdet.f90
Dassemble_3c_PP_mdet.o : ../SRC/NAC/Dassemble_3c_PP_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_3c_PP_mdet.f90
Dassemble_olsxc_3c_mdet.o : ../SRC/NAC/Dassemble_olsxc_3c_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_olsxc_3c_mdet.f90
fewest_switches.o : ../SRC/NAC/fewest_switches.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/fewest_switches.f90
mc_switch.o : ../SRC/NAC/mc_switch.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/mc_switch.f90
transition.o : ../SRC/NAC/transition.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/transition.f90
Dassemble_ca_2c_mdet.o : ../SRC/NAC/Dassemble_ca_2c_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_ca_2c_mdet.f90
Dassemble_ca_3c_mdet.o : ../SRC/NAC/Dassemble_ca_3c_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_ca_3c_mdet.f90
Dassemble_lr_mdet.o : ../SRC/NAC/Dassemble_lr_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_lr_mdet.f90
Dassemble_ca_olsxc_on_mdet.o : ../SRC/NAC/Dassemble_ca_olsxc_on_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_ca_olsxc_on_mdet.f90
Dassemble_ca_olsxc_2c_mdet.o : ../SRC/NAC/Dassemble_ca_olsxc_2c_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_ca_olsxc_2c_mdet.f90
Dassemble_ca_olsxc_3c_mdet.o : ../SRC/NAC/Dassemble_ca_olsxc_3c_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/Dassemble_ca_olsxc_3c_mdet.f90
move_correc.o : ../SRC/NAC/move_correc.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/move_correc.f90
move_predic.o : ../SRC/NAC/move_predic.f90
	$(F90) $(FFLAGS)  -c ../SRC/NAC/move_predic.f90




#**************************************************
#   QMMM
#**************************************************
#====== variant : 'QMMM'
main_loop_MDET_qmmm.o : ../SRC/QMMM/main_loop_MDET_qmmm.f90
	$(F90) $(FFLAGS)  -c ../SRC/QMMM/main_loop_MDET_qmmm.f90
main_loop_MD_qmmm.o : ../SRC/QMMM/main_loop_MD_qmmm.f90
	$(F90) $(FFLAGS)  -c ../SRC/QMMM/main_loop_MD_qmmm.f90
fireball_qmmm_loop.o : ../SRC/QMMM/fireball_qmmm_loop.f90
	$(F90) $(FFLAGS)  -c ../SRC/QMMM/fireball_qmmm_loop.f90
assemble_qmmm.o : ../SRC/QMMM/assemble_qmmm.f90
	$(F90) $(FFLAGS)  -c ../SRC/QMMM/assemble_qmmm.f90
assemble_qmmm_dip.o : ../SRC/QMMM/assemble_qmmm_dip.f90
	$(F90) $(FFLAGS)  -c ../SRC/QMMM/assemble_qmmm_dip.f90
Dassemble_qmmm.o : ../SRC/QMMM/Dassemble_qmmm.f90
	$(F90) $(FFLAGS)  -c ../SRC/QMMM/Dassemble_qmmm.f90
Dassemble_qmmm_dip.o : ../SRC/QMMM/Dassemble_qmmm_dip.f90
	$(F90) $(FFLAGS)  -c ../SRC/QMMM/Dassemble_qmmm_dip.f90
Dassemble_qmmm_mdet.o : ../SRC/QMMM/Dassemble_qmmm_mdet.f90
	$(F90) $(FFLAGS)  -c ../SRC/QMMM/Dassemble_qmmm_mdet.f90
Dassemble_qmmm_mdet_dip.o : ../SRC/QMMM/Dassemble_qmmm_mdet_dip.f90
	$(F90) $(FFLAGS)  -c ../SRC/QMMM/Dassemble_qmmm_mdet_dip.f90




#**************************************************
#   DFTD3
#**************************************************
#====== variant : ''
common.o : ../SRC/DFTD3/common.f90
	$(F90) $(FFLAGS)  -c ../SRC/DFTD3/common.f90
sizes.o : ../SRC/DFTD3/sizes.f90
	$(F90) $(FFLAGS)  -c ../SRC/DFTD3/sizes.f90
pars.o : ../SRC/DFTD3/pars.f90
	$(F90) $(FFLAGS)  -c ../SRC/DFTD3/pars.f90
core.o : ../SRC/DFTD3/core.f90
	$(F90) $(FFLAGS)  -c ../SRC/DFTD3/core.f90
api.o : ../SRC/DFTD3/api.f90
	$(F90) $(FFLAGS)  -c ../SRC/DFTD3/api.f90
dftd3_corrections.o : ../SRC/DFTD3/dftd3_corrections.f90
	$(F90) $(FFLAGS)  -c ../SRC/DFTD3/dftd3_corrections.f90


