'''
This program runs rtt() function from ape package to root the tree

'''

import sys, subprocess, os

if len(sys.argv) < 2:
  print('\nUSAGE: rootTree_RTT.py treeFile')
  sys.exit(0)
  
inTree = sys.argv[1] # contains the name of the input tree

fh = open('demodel.log','a')

msg = '\nrunning rtt() from ape package\n'
print(msg)
fh.write(msg)
 
cl = ''
cl += 'Rscript rtt.R %s' % inTree # calling rtt.R to run rtt() from ape package

process = subprocess.Popen(cl,shell=True,stderr=fh,stdout=fh)
rval = process.wait()



if os.stat('ExaML_result.outTree.rtt.newick').st_size != 0:
  msg = '\nrtt() run is completed\n'
  msg += '\nRooted tree is written in <ExaML_result.outTree.rtt.newick>\n'
  print(msg)
  fh.write(msg)
  
else:
  msg = '\nrtt() run could not finish properly.\n'
  msg += '\nPlease refer to the demodel.log file for more information\n'
  print(msg)
  fh.write(msg)
  
fh.close()
