'''
This program runs chronos() function to make rooted time tree

'''

import sys, subprocess, os

if len(sys.argv) < 4:
  print('\nUSAGE: timeTree_chronos.py treeFile outFile numCat')
  sys.exit(0)
  
inTree = sys.argv[1] # contains the name of the input tree
outTree = sys.argv[2]
numCat = sys.argv[3]

fh = open('demodel.log','a')

msg = '\nrunning chronos() for dating the tree\n'
print(msg)
fh.write(msg)
 
cl = ''
cl += 'Rscript chronos.R %s %s %s' % (inTree,outTree,numCat) # calling chronos.R to run chronos()

process = subprocess.Popen(cl,shell=True,stderr=fh,stdout=fh)
rval = process.wait()



if os.stat(outTree).st_size != 0:
  msg = '\nchronos() run is completed\n'
  msg += '\nRooted time tree is written in <%s>\n' % outTree
  print(msg)
  fh.write(msg)
  
else:
  msg = '\nchronos() run could not finish properly.\n'
  msg += '\nPlease refer to the demodel.log file for more information\n'
  print(msg)
  fh.write(msg)
  
fh.close()
