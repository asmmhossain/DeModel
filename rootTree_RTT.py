'''
This program runs rtt() function from ape package to root the tree

'''

import sys, subprocess, os, argparse

#**********************************************************

desStr = 'Roots a phologenetic tree using rtt() method of "ape" package'


parser = argparse.ArgumentParser(description=desStr,
              formatter_class=argparse.RawDescriptionHelpFormatter)
              
parser.add_argument('treeFileName', help='Tree file in "newick" format')

args = parser.parse_args()

#**********************************************************
  
inTree = args.treeFileName # contains the name of the input tree

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
