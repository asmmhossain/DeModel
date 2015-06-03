'''
This program calls physher to amke rooted time tree

physher command line:

~/apps/physher -m HKY -i Vill_01_Feb2015_5yr_gag.muscle.new -t ExaML_result.outTree -C strict -o physherOut


'''

import sys, subprocess, os

if len(sys.argv) < 6:
  print('\nUSAGE: timeTree_physher.py alignmentFile treeFile subModel clockType outStem')
  sys.exit(0)
  
aln = sys.argv[1]
inTree = sys.argv[2]
subMod = sys.argv[3]
clock = sys.argv[4]
outStem = sys.argv[5]

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



#process = subprocess.Popen(cl,shell=True,stderr=fh,stdout=fh)
#rval = process.wait()

fName = outStem + '.strict.tree'
#print(fName)

if os.stat(fName).st_size != 0:
  msg = '\nPhysher run is completed\n'
  msg += '\nRooted time tree in nexus format is written in <%s>\n' % fName
  print(msg)
  fh.write(msg)
  
  newickName = outStem + '.strict.newick'
  cl = 'Rscript nexus2newick.R %s %s' % (fName,newickName)
  
  process = subprocess.Popen(cl,shell=True,stderr=fh,stdout=fh)
  rval = process.wait()

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

