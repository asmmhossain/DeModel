'''
This program runs rtt() function from ape package to root the tree

'''

import sys, subprocess, os, argparse, shutil


#**********************************************************

desStr = 'Roots a phologenetic tree using rtt() method of "ape" package'


parser = argparse.ArgumentParser(description=desStr,
              formatter_class=argparse.RawDescriptionHelpFormatter)
              
parser.add_argument('treeFileName', help='Tree file in "newick" format')

args = parser.parse_args()

#**********************************************************
  
inTree = args.treeFileName # contains the name of the input tree

outTree = inTree + 'rtt.newick'

fh = open('demodel.log','a')

msg = '\nrunning rtt() from ape package\n'
print(msg)
fh.write(msg)

#***********************************************
import rpy2.robjects as rob
from rpy2.robjects.packages import importr

r = rob.r

g = rob.globalenv

ape = importr('ape')

#**************************************************
shutil.copy(inTree,'in.tre')


r('''
  t <- read.tree('in.tre')
  dates <- numeric(length(t$tip.label))
  for(i in 1:length(dates)){dates[i]<-as.numeric(strsplit(t$tip.label[i],'_')[[1]][2])}

  #print(dates[1])

  rtt(t,dates)

  write.tree(t,'out.tre')
  #plot(t)
  #dev.off()
  
''')

if os.stat('out.tre').st_size != 0:
  os.rename('out.tre','ExaML_result.outTree.rtt.newick')
  
if os.stat('in.tre').st_size != 0:
  os.remove('in.tre')  
#**************************************************

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
