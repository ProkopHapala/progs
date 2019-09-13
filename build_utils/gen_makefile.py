#!/usr/bin/python

def insertGroup( groups, group_names, name, variant, objs ):
    #groups.append( (group_name,variant,objs) )
    if name in groups:
        groups[name][variant] = objs
    else:
        groups[name] = {variant:objs}
        group_names.append(name)

def fromMakeFile( fname  ):
    fin = open(fname,"r")
    group_names = []
    var_names   = [ "" ]
    var_set     = set()
    group_dict  = {}
    group_name  = None
    objs = []
    variant = ""
    key_if    = "findstring"
    key_if_nc = len(key_if)
    for line in fin:
        ws = line.split()
        nw = len(ws)
        #if   (nw>=1):  print ws[0]
        if   (nw>=1) and (ws[0] == 'ifneq' ):
            i0 = line     .find( key_if )+key_if_nc
            i1 = line[i0:].find( "," )
            variant = line[i0:i0+i1].strip()
            if not variant in var_set: 
                var_names.append(variant)
                var_set  .add(variant)
            #print variant, i0, i1
        elif (nw>=1) and (ws[0] == 'endif' ):
            variant=""
        elif (nw>=2) and (ws[1] == '='):
            if group_name is not None:
                insertGroup( group_dict, group_names, group_name, variant, objs )
            objs = []
            group_name = ws[0]
        objs += [ w[:-2] for w in ws if w[-2:]=='.o' ]
    if group_name is not None:
        insertGroup( group_dict, group_names, group_name, variant, objs )
    return group_dict, group_names, var_names

def diffListSet(lst,st):
    common = [ o for o in lst if o     in st ]
    diff   = [ o for o in lst if o not in st ]
    return diff, common

def diffTwoLists( lst1, lst2 ):
    diff1,common = diffListSet( lst1, set(lst2) )
    diff2,common = diffListSet( lst2, set(lst1) )
    return common, diff1, diff2 

def pruneVariants(groups):
    '''
    remove objects files form specialized variants which are already in default variant
    '''
    for name,vardict in groups:
        if "" in vardict:
            default_objs = set(vardict[""])
            for key in vardict:
                if key != "":
                    vardict[key] , _ = diffListSet( vardict[key], default_objs )

def toMakefile_list( fout, name, lst, pre=" ", post=".o", nclmax=120 ):
    s   = name+" = "
    ncl = len ( s )
    fout.write( s )
    no  = len(lst)
    for i in range(no):
        o = lst[i]
        s = pre+o+post
        ncl += len(s)
        if ( i<(no-1) ):
            if ncl > nclmax:
                s += " \\\n\t"
                ncl = 0
        fout.write( s )
    fout.write( "\n" )

def toMakefile_obj_groups( fout, group_dict, group_names, var_names, build_path="", nclmax=120 ):
    ncl = 0
    for name in group_names:
        varinants = group_dict[name]
        if len(varinants) == 1:
            #toMakefile_obj_group( fout, name, varinants[ varinants.keys()[0] ],    nclmax=nclmax )
            for var in var_names:
                if var in varinants:
                    toMakefile_list( fout, name, varinants[var],    nclmax=nclmax )
                    fout.write( "\n\n\n" )
                    break
        else:
            for var in var_names:
                if var in varinants:
                    #toMakefile_obj_group( fout, name+"_"+var, varinants[var],    nclmax=nclmax )
                    toMakefile_list( fout, name+"_"+var, varinants[var],    nclmax=nclmax )
            fout.write( name+" = " )
            for var in var_names:
                if var in varinants:
                    fout.write( " $(%s_%s)" %(name,var) )
            fout.write( "\n\n\n" )

def toMakefile_cc_obj( fout, o, pre="../", post=".f90", fflags="$(FFLAGS)", compiler="$(F90)" ):
    src = pre+o+post
    obj = o+".o"
    fout.write( obj+" : "+src+"\n" )
    fout.write( "\t" + compiler + " " + fflags + " -c "+src + "\n" )

def toMakefile_cc_objs( fout, group_dict, group_names, var_names, src_path="", ccomment='*', ncomment=50 ):
    ncl = 0
    for name in group_names:
        varinants = group_dict[name]
        fout.write("\n\n")
        cmline = "#"   +(ccomment*ncomment)+"\n"
        fout.write( cmline )
        fout.write( "#   " + name +"\n" )
        fout.write( cmline )
        for var in var_names:
            if var in varinants:
                fout.write("#====== variant : '" + var +"'\n" )
                for o in varinants[var]:
                    toMakefile_cc_obj( fout, o, pre=src_path+name+"/" )
        fout.write("\n\n")

def listToPython(fout, name, lst, pre="'", mid="' : [", post="],\n", nclmax=120 ):
    s = pre+ name +mid
    ncl = len(s)
    fout.write( s )
    no = len(lst)
    for i in range(no):
        o = lst[i]
        s = "'"+o+"'"
        ncl += len(s)
        if ( i<no-1 ):
            s += ","
            if ncl > nclmax:
                s += "\n        "
                ncl = 0
        fout.write( s )
    fout.write( post )
    ncl = 0

def toPython_groups( fout, group_dict, group_names, var_names, nclmax=120 ):
    ncl = 0
    #fout.write( "'%s' : {\n" %name )
    listToPython(fout, "group_names",     group_names, pre="", mid=" = [", post="]\n\n", nclmax=nclmax )
    listToPython(fout, "variant_names",   var_names  , pre="", mid=" = [", post="]\n\n", nclmax=nclmax )
    fout.write( "GROUPS = {\n" )
    for name in group_names:
        varinants = group_dict[name]
        fout.write( "'%s' : {\n" %name )
        for var in var_names:
            if var in varinants:
                #fout.write("# ====== variant : " + var )
                listToPython(fout, var, varinants[var] )
        fout.write("}, #END %s\n\n"  %(name)   )
    fout.write("} #END GROUPS\n\n")

def toMakefile_cc_obj_c(fout, o, pre="../MODULES/", post=".c", fflags="$(CFLAGS)", compiler="$(CC)" ):
    toMakefile_cc_obj( fout, o, pre=pre, post=post, fflags=fflags, compiler=compiler )

def toMakefile_list_vars( fout, name, lst, pre=" $(", post=") " ):
    toMakefile_list( fout, name, lst,  pre=pre, post=post )
    fout.write( "\n" )

def toMakefile_name( fout, name, val ):
    fout.write( name + " = " + val + "\n\n" )

if __name__ == "__main__":

    '''
    groups, var_names = fromMakeFile( "Makefile.in" )
    pruneVariants(groups)

    # groups_dct = dict(groups)
    # common, diff1, diff2 = diffTwoLists( groups_dct['INTERACTIONS']['SCALAPACK'], groups_dct['INTERACTIONS']['ORDERN'] )
    # print "common ", common
    # print "diff1 ", diff1
    # print "diff2 ", diff2
    # exit(0)

    with open("Makefile",'w') as fout:
        toMakefile_obj_groups( fout, groups, var_names )
        toMakefile_cc_objs   ( fout, groups, var_names )
    with open("Makefile_objects-New.py",'w') as fout:
        toPython_groups( fout, groups, var_names )
    '''

    import Makefile_targets
    from Makefile_targets  import *
    from Makefile_objects  import *
    from Makefile_machines import *
    import inspect

    #print [item for item in dir(Makefile_targets) if not item.startswith("__")]
    #print dict(inspect.getmembers( Makefile_targets ))["f_globals"]
    #print dir(Makefile_targets)
    #print Makefile_targets["OBJECTS"]
    #print "====================================="
    #for g in Makefile_targets._gobals_:
    #    print "\n ---------: "+g+" : \n", Makefile_targets._gobals_[g]
    #print  Makefile_targets._gobals_
    #exit()

    #build_path = "build/"
    src_path = "../SRC/"
    MKL_PATH = "/home/prokop/SW/intel/"
    MPI_PATH = "/usr/lib/x86_64-linux-gnu/openmpi"
    FFLAGS, LFLAGS_, LPATHS = genFlags( ["OPT"], MKL_PATH=MKL_PATH, MPI_PATH=MPI_PATH )

    #variant_names_ = ['','DOUBLE','GAMMA']
    variant_names_ = ['','DOUBLE']

    with open("Makefile",'w') as fout:
        
        toMakefile_obj_groups( fout, GROUPS, group_names, variant_names_ )

        toMakefile_list_vars( fout, "OBJECTS_SERVER", OBJECTS_SERVER, )
        toMakefile_list_vars( fout, "OBJECTS",        OBJECTS,        )

        for key,body in inline_targets.iteritems() :
            writeInlineTarget( fout, key, body )

        #fout.write( "(OBJ)/%.o" + "\n\n" )
        fout.write( "F90 = gfortran\n" )
        toMakefile_name( fout, "FFLAGS",  FFLAGS  )
        toMakefile_name( fout, "LFLAGS_", LFLAGS_ )
        toMakefile_name( fout, "LPATHS",  LPATHS  )
        toMakefile_list_vars( fout, "LFLAGS", ["LPATHS",""] )
        #toMakefile_name( fout, "FFLAGS", FFLAGS )


        #writeTarget( fout, "fireball.x"       , "$(OBJECTS)"       , [OBJECTS       ] )
        #writeTarget( fout, "fireball_server.x", "$(OBJECTS_SERVER)", [OBJECTS_SERVER] )

        writeTarget( fout, "fireball.x"       , "$(OBJECTS)", [OBJECTS       ] )
        writeTarget( fout, "fireball_server.x", "$(OBJECTS)", [OBJECTS_SERVER] )

        #cclient.o : THERMOINT/cclient.c
        #    $(CC) $(CFLAGS) -c THERMOINT/cclient.c

        #toMakefile_cc_obj( fout, "sockets", pre="../MODULES/", post=".c", fflags="$(CFLAGS)", compiler="$(CC)" )
        #toMakefile_cc_obj( fout, "cclient", pre="../MODULES/", post=".c", fflags="$(CFLAGS)", compiler="$(CC)" )

        toMakefile_cc_obj_c( fout, "sockets", pre="../MODULES/"   )
        toMakefile_cc_obj_c( fout, "cclient", pre="../THERMOINT/" )
        #toMakefile_cc_obj( fout, o, pre="../", post=".f90", fflags="$(FFLAGS)", compiler="$(F90)" )

        toMakefile_cc_objs   ( fout, GROUPS, group_names, variant_names, src_path=src_path )




