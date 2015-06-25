'''
This program runs chronos() function to make rooted time tree

'''

import sys, subprocess, os, argparse


#*********************************************************

desStr = 'Convert into rooted time tree from rooted tree of time sampled sequences'


parser = argparse.ArgumentParser(description=desStr,
              formatter_class=argparse.RawDescriptionHelpFormatter)
              
parser.add_argument('treeFileName', help='Tree file in "newick" format')
parser.add_argument('outFileName', help='Output tree file name')
parser.add_argument('-c','--ncat',default=4,type=int,help='number of discrete rate categories')

args = parser.parse_args()

inTree = args.treeFileName
outTree = args.outFileName
numCat = args.ncat

#**********************************************************  
  

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
