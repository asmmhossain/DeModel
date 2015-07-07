'''
This program calls physher to amke rooted time tree

physher command line:

~/apps/physher -m HKY -i Vill_01_Feb2015_5yr_gag.muscle.new -t ExaML_result.outTree -C strict -o physherOut


'''

import sys, subprocess, os, argparse, shutil
#from Bio import Phylo

#**********************************************************

desStr = 'Creating a rooted time tree using Physher'


parser = argparse.ArgumentParser(description=desStr,
              formatter_class=argparse.RawDescriptionHelpFormatter)
              
parser.add_argument('alnFileName', help='Alignment file in "FASTA/NEXUS" format')
parser.add_argument('treeFileName', help='Tree file in "newick/NEXUS" format')
parser.add_argument('subModel', default = 'GTR', help='Nucleotide/codon substitution model (default: GTR; others: HKY, K80, JC69, GY94)')
parser.add_argument('clockType', default = 'strict', help='strict/local/discrete clock (default: strict)')
parser.add_argument('outStem', help='Output is written to <outStem>.[strict/local/discrete].newick.tree')



args = parser.parse_args()

#**********************************************************

aln = args.alnFileName
inTree = args.treeFileName
subMod = args.subModel
clock = args.clockType
outStem = args.outStem

fh = open('demodel.log','a')

msg = '\nPhysher is called with the command below to get a time tree:\n'
print(msg)
fh.write(msg)

cl = ''
cl += '~/Downloads/physher-src.v0.2/Release/physher '
cl += '-i %s -t %s -m %s ' % (aln,inTree,subMod)
cl += '-C %s -o %s' % (clock,outStem)

msg = '\t%s\n' % cl
print(msg)
fh.write(msg)



process = subprocess.Popen(cl,shell=True,stderr=fh,stdout=fh)
rval = process.wait()

fName = outStem + '.' + clock +'.tree'
#print(fName)

if os.stat(fName).st_size != 0:
  msg = '\nPhysher run is completed\n'
  msg += '\nRooted time tree in nexus format is written in <%s>\n' % fName
  print(msg)
  fh.write(msg)
  
  newickName = outStem + '.' + clock + '.newick.tree'
  
  #Phylo.convert(fName,'nexus',newickName,'newick')
  #cl = 'Rscript nexus2newick.R %s %s' % (fName,newickName)
  
  #process = subprocess.Popen(cl,shell=True,stderr=fh,stdout=fh)
  #rval = process.wait()

#*****************************************************  
  import rpy2.robjects as rob
  from rpy2.robjects.packages import importr
  
  r = rob.r
  g = rob.globalenv
  
  ape = importr('ape')
  
#**********************************************************

  shutil.copy(fName,'in.tre')
  
  r('''
    tre <- read.nexus('in.tre')
    write.tree(tre,'out.tre')
  ''')  

  if os.stat('out.tre').st_size != 0:
    os.rename('out.tre',newickName)
    
  if os.stat('in.tre').st_size != 0:
    os.remove('in.tre')
      
  if os.stat(newickName).st_size != 0:
    msg ='Rooted time tree in newick format is written in <%s>\n' % newickName
    print(msg)
    fh.write(msg)
  
else:
  msg = '\nPhysher run could not finish properly.\n'
  msg += '\nPlease refer to the demodel.log file for more information\n'
  print(msg)
  fh.write(msg)


fh.close()

