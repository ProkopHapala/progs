import os
import sys
#import ahocorasick
import re
import traceback
import string

def insertRecord( dct, name, fname, il, iw ):
    #loc = [(il,iw)]
    loc = [il]
    if name in dct:
        dct_name = dct[name]
        dct_name[fname] = dct_name.get(fname,[]) + loc
    else:
        dct[name] = {fname:loc}

def searchKeywordsInFile_re( fpath, fname, keyw_dict, re_split, bToLowerCase=True, bFname=True, found=None, verbose=False ):
    if found is None:
        #found = [ [] for k in keyw_dict ]
        found = [ {} for k in keyw_dict ]
    with open( fpath, 'r' ) as fin:
        for iline,line in enumerate(fin):
            c=line[0]
            if c=='C' or c=='c' or c=='*' or c=='!' : continue     # old-style comments
            #ic=line.find("!") # comment
            #if ic>=0: line=line[:ic]
            #line = line.translate(trans_table)
            ws = re_split.findall(line)
            #print iline, ws
            for iw,w in enumerate(ws):
                if w == '!': break
                w = w.lower()
                ikey = keyw_dict.get(w,-1)
                if ikey >=0:
                    try:
                        w_prev = ws[iw-1].lower()
                        if ((iw==0)or(w_prev!='end')):
                            w_next = ws[iw+1].lower()
                            i = keyw_dict[w]
                            #if bFname:
                            #    #rec = (ikey,w_next, iw,iline, fname)
                            #    rec = ( w_next, iw,iline, fname )
                            #else:
                            #    #rec = (ikey,w_next, iw,iline )
                            #    rec = (w_next, iw,iline )
                            if(verbose): print "found.append( %s )" %str(rec)
                            #found.append( rec )
                            #found[ikey].append( rec )
                            #dct = found[ikey]
                            #dct[w_next] = dct.get(w_next,[]) + [ (fname,iline,iw) ]
                            insertRecord( found[ikey], w_next, fname, iline, iw )

                    except Exception as e:
                        #print e
                        traceback.print_exc()
                        print "DEBUG w{"+w+"} line{"+line+"}"
                        print "DEBUG ws = ",  ws
                        raise Exception("ERROR in searchKeywordsInFile_split [%i,%i] of %s" %(iline,iw,fname)  )
    return found

def searchKeywordsInPath( root_path, keywords, exts=['.f90','.f'], wchars="a-zA-Z0-9_", tab_dir='----', tab_file='    ', verbose=True, bToLowerCase=True, bStorePath=True ):
    exts_set = set(exts)
    #aho, re_wstart, re_wend = prepareKewordSearch( keywords, wchars=wchars )
    keyw_dict = { kw:i for i,kw in enumerate(keywords) }
    #re_split  = re.compile(''' '.*?' | ".*?" | \S+ ''' )
    #re_split  = re.compile(''''.*?'|".*?"|[a-zA-Z0-9]''' )
    #re_split  = re.compile( '''".*?"|'.*?'|\w+''' )
    re_split  = re.compile( '''!|'.*?'|".*?"|\w+''' )
    #found = []
    #found = [ [] for k in keyw_dict ]
    found = [ {} for k in keyw_dict ]
    nkw = len(keywords)
    for path, dirs, files in os.walk(root_path):
        path_lst     = path.split(os.sep)
        level=len(path_lst)
        #print "path: ", path, " root_path: ", root_path
        path_rel = os.path.relpath( path, root_path )
        if(verbose): print tab_dir*(level-1), os.path.basename(path)
        for fname in files:
            name,ext = os.path.splitext(fname)
            fpath = path+os.sep+fname
            #print tab_file*len(path), ext, "      ", fname
            if ext in exts_set:
                if(verbose):
                    nfound0 = [ len(found[i]) for i in xrange(nkw) ]
                #searchKeywordsInFile( fpath, aho, re_wstart, re_wend, found=found, bToLowerCase=bToLowerCase )
                #searchKeywordsInFile_split( fpath, keyw_dict, found=found, bToLowerCase=bToLowerCase )
                #searchKeywordsInFile_re( fpath, keyw_dict, re_split, found=found, bToLowerCase=bToLowerCase )
                fname_=fname
                if bStorePath:fname_= path_rel +os.sep+ fname
                searchKeywordsInFile_re( fpath, fname_, keyw_dict, re_split, found=found, bToLowerCase=bToLowerCase )
                if(verbose):
                    nfound  = [ len(found[i])-nfound0[i] for i in xrange(nkw) ]
                    print tab_file*level, fname, "       ", nfound
    return found

def writeTabled(fout,s,ic,nc_min):
    nspace = nc_min-ic
    fout.write( (" "*nspace ) )
    fout.write( s                  )
    return ic+nspace+len(s)

def writeTags( fout, dct, tab="    ",  ntab1=35, ntab2=80, bSortNames=True ):
    names = dct.keys()
    if bSortNames:
        names=sorted(names)
    #for name,recs in dct.items():
    for name in names:
        ic=0
        recs = dct[name]
        nrec = len(recs)
        if nrec==0:
            #raise Exception("record for name{"+name+"} is empty" )
            print "WARRNING: record for name{"+name+"} is empty" 
        elif nrec==1:
            rec=next(iter(recs))
            #fout.write( "'%s' :[%s],\n" %( name , str(recs[0]) ) )
            ic= writeTabled(fout, "'%s'" %name, 0,0 )
            ic= writeTabled(fout, ":[", ic,ntab1-5 )
            #ic= writeTabled(fout, "%s],\n"  %str(recs[0]), ic, ntabed )
            ic= writeTabled(fout, "'%s'"  %str(rec), ic, ntab1 )
            ic= writeTabled(fout, ":%s"  %str(recs[rec]), ic, ntab2 )
            ic= writeTabled(fout, "],\n", ic, ntab2 )
        else:
            #fout.write( "'%s' :[" %name )
            ic= writeTabled(fout, "'%s'" %name, 0,0 )
            ic= writeTabled(fout, ":[", ic,ntab1-5 )
            fnames=recs.keys()
            if bSortNames:
                fnames=sorted(fnames)
            for rec in fnames:
                fout.write("\n")
                #fout.write( tab+str(rec)+",\n" )
                ic = writeTabled(fout, "'%s'"  %str(rec), 0, ntab1 )
                ic = writeTabled(fout, ":%s,"  %str(recs[rec]), ic, ntab2 )
            ic= writeTabled(fout, "],\n", ic, ntab2 )
            #fout.write( "],\n",  )

def writeFoundTagFiles_py( keywords, found ):
    for ik,key in enumerate(keywords):
        with open("tags_%s.py" %key, 'w' ) as fout:
            fout.write( "tag_dict_%s ={\n" %key )
            writeTags(fout, found[ik] )
            fout.write( "}\n\n" )

if __name__ == "__main__":

    keywords = [ 'function', 'subroutine', 'call', 'use' ]

    #path = "../SRC/LOOPS"
    path = "../SRC"
    found = searchKeywordsInPath( path, keywords )
    writeFoundTagFiles_py( keywords, found )

    exit()

    fname = '../SRC/ASSEMBLERS/assemble_3c_ordern_final.f90'
    fname = "../SRC/LOOPS/main_loop_FIRE.f90"
    
    #aho, re_wstart, re_wend = prepareKewordSearch( keywords )
    #found  = searchKeywordsFile(fname, aho, re_wstart, re_wend )
    #found  = searchKeywordsInFile_split(fname, set(keywords) )

    keyw_dict = { kw:i for i,kw in enumerate(keywords) }
    #re_split  = re.compile(''''.*?'|".*?"|\S+''' )
    #re_split  = re.compile(''''.*?'|".*?"|*[a-zA-Z0-9]''' )
    #re_split  = re.compile(''''.*?'|".*?"|\w+''' )
    re_split  = re.compile( '''!|'.*?'|".*?"|\w+''' )
    found  = searchKeywordsInFile_re(fname, keyw_dict, re_split )
    print "found ", found

# ===================== Other versions - currently not used

'''

def processPath( path, ext=['.f90','.f','.c'], tab_dir='----', tab_file='    ', verbose=True ):
    for root, dirs, files in os.walk(path):
        path = root.split(os.sep)
        if(verbose): print tab_dir*(len(path) - 1), os.path.basename(root)
        for file in files:
            if(verbose): print  tab_file* len(path), file

def prepareKewordSearch( keywords, wchars="a-zA-Z0-9_" ):
    aho = ahocorasick.Automaton()
    for i,key in enumerate(keywords):
        nc = len(key)
        aho.add_word( key, (i,nc) )
    aho.make_automaton()
    found = []
    re_wstart = re.compile("[%s]"  %wchars )
    re_wend   = re.compile("[^%s]" %wchars )
    return aho, re_wstart, re_wend

def searchKeywordsInFile( fname, aho, re_wstart, re_wend, bToLowerCase=True, bFname=True, found=[] ):
    with open( fname, 'r' ) as fin:
        for iline,line in enumerate(fin):
            ic=line.find("!") # comment
            if ic>=0: line=line[:ic]
            for iend,(ikey,nc) in aho.iter(line):
                iend+=1
                #istart = iend - nc
                try:
                    i0 = re_wstart.search( line, iend ).start()
                    i1 = re_wend  .search( line, i0   ).start()
                except Exception as e:
                    #print e
                    traceback.print_exc()
                    istart = iend - nc
                    print "#l: "+str(iline)+" found: {" + line[istart:iend] +"} name:{"+line[i0:i1]+"}      "+str((istart,iend))+" "+str((i0,i1)) 
                    raise Exception("ERROR in searchKeywordsInFile [%i,%i] of %s" %(iline,iend,fname)  )
                #print "#l: "+str(iline)+" found: {" + line[istart:iend] +"} name:{"+line[i0:i1]+"}" 
                s = line[i0:i1]
                if bToLowerCase: s = s.lower()
                if bFname:
                    rec = (ikey,i0,s, iline, fname)
                else:
                    rec = (ikey,i0,s, iline )
                found.append( rec )
    return found

def searchKeywordsInFile_split( fname, keyw_dict, bToLowerCase=True, bFname=True, found=[], quotes="\'\"`" ):
    print quotes; exit()
    seps = ' [](){},;:~.+-*/=%\t\n'
    trans_table = string.maketrans( seps, ' '*len(seps) )
    with open( fname, 'r' ) as fin:
        for iline,line in enumerate(fin):
            ic=line.find("!") # comment
            if ic>=0: line=line[:ic]
            line = line.translate(trans_table)
            ws = line.split()
            #print ws
            for iw,w in enumerate(ws):
                w = w.lower()
                ikey = keyw_dict.get(w,-1)
                if ikey >=0:
                    try:
                        w_prev = ws[iw-1].lower()
                        if ((iw==0)or(w_prev!='end')):
                            w_next = ws[iw+1].lower()
                            i = keyw_dict[w]
                            if bFname:
                                rec = (ikey,w_next, iw,iline, fname)
                            else:
                                rec = (ikey,w_next, iw,iline )
                            found.append( rec )
                    except Exception as e:
                        #print e
                        traceback.print_exc()
                        print "w{"+w+"} line{"+line+"}"
                        raise Exception("ERROR in searchKeywordsInFile_split [%i,%i] of %s" %(iline,iw,fname)  )
    return found

'''