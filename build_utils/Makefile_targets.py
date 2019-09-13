
from Makefile_machines import *

OBJECTS_COM = [ 
    'DFTD3', 'INITMPI', 'ORDERN', 'ALLOCATIONS', 'ASSEMBLERS', 
    'DASSEMBLERS', 'INITIALIZERS', 'INTERACTIONS', 'INTERPOLATERS',
    'LOOPS, MD',  'NEIGHBORS', 'PRESSURE', 'READFILES', 
    'ROTATIONS', 'SOLVESH_DIAG', 'FORM_RHO', 'UMBRELLA UTIL', 
    'UTIL_SPARSE', 'VISUALIZATION', 'XC', 'CG', 'DOS', 'THERMOINT', 
    'NEB', 'TRANS', 'GRID', 'TDSE', 'BIAS', 'NAC',
]

OBJECTS              = [ "MODULES"] + OBJECTS_COM + [ "MAIN" ]
OBJECTS_QMMM         = [ "MODULES"] + OBJECTS_COM + [ "QMMM" ]
OBJECTS_SERVER       = [ "MODULES"] + OBJECTS_COM + [ "MAIN_SERVER" ]
OBJECTS_SERVER_AMBER = [ "MODULES"] + OBJECTS_COM + [ "MAIN_SERVER_AMBER" ]

_gobals_ = globals()

#print _gobals_

import inspect

default_obj_name_exclude = set('o')

def retrieve_name(var):
    #callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    #return [var_name for var_name, var_val in callers_local_vars if (var_val is var) and (var_name not in exclude) ]
    #return [key for key,val in _gobals_.iteritems() if (val is var) ]
    ret = [key for key,val in _gobals_.iteritems() if (val is var) ]
    if len(ret)>0: 
        return ret[0]
    else:
        raise Exception( "Module "+__name__+" does not contain global variable with value ", var )
        return  None
    
def writeInlineTarget( fout, name, body ):
    fout.write( name +" : "+body+"\n\n" )

def writeTarget( fout, name, depend, objs, compiler="$(F90)", fflags="$(FFLAGS)", lflags="$(LFLAGS)" ):
    fout.write( name +" : "+depend+"\n" )
    fout.write( "\t"+compiler+" -o "+name+" " )
    fout.write( " "+fflags )
    for o in objs:
        oname = retrieve_name( o )
        fout.write( " $(%s)" %oname )
    fout.write( " "+lflags )
    fout.write( "\n\n" )

"""
def toMakefileTargets(fout):

    print inspect.currentframe().f_back.f_globals.items()

    '''
    for key,body in inline_targets :
        writeInlineTarget( key, body )

    writeTarget( fout, "fireball.x"       , "$(OBJECTS)"       ,  [OBJECTS       , VISFLAGS, PARLFLAGS, LFLAGS] )
    writeTarget( fout, "fireball_server.x", "$(OBJECTS_SERVER)",  [OBJECTS_SERVER, VISFLAGS, PARLFLAGS, LFLAGS] )
    '''
"""

# ==================================================

inline_targets = {

".PHONY" :" clean veryclean extraclean",

"clean" : '''
	rm -f -r core *.o .nfs* rii_files fireball.x.ip*  *.mod ldtmp* *.vo *~ *.il''',

"veryclean": ''' clean
	rm -f fireball.x libfireball.a''',

"extraclean": "veryclean",

"all":'''
	make fireball.x''',

"libfireball": '''$(OBJECTS_QMMM)
	ar rv libfireball.a $(OBJECTS_QMMM)
	ranlib libfireball.a''',
}


# ==================================================

"""

"server": '''$(OBJECTS_SERVER)
	$(F90)  -o  fireball_server.x $(FFLAGS) $(OBJECTS_SERVER) $(VISFLAGS) $(PARLFLAGS) $(LFLAGS) 
''',

"server_amber": '''$(OBJECTS_SERVER_AMBER)
	$(F90)  -o  fireball_server $(FFLAGS) $(OBJECTS_SERVER_AMBER) $(VISFLAGS) $(PARLFLAGS) $(LFLAGS) 
''',

"fireball.x" : ''' $(OBJECTS)
	$(F90) -o  fireball.x $(FFLAGS) $(OBJECTS) $(VISFLAGS) $(PARLFLAGS) $(LFLAGS) 
''',

"""