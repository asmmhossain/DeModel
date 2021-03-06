'''
This program will run LSD to get a rooted time tree 
  - A newick tree and sampled dates will be provided
  - At first the dates are written in 'lsd.dates'
  - LSD is run next. The following files are generated:
    - <lsd.log> for logging the progress of LSD run
    - <ExaML_result_result.txt> contains parameter values, rate, TMRCA
    - <ExaML_result_result_newick_brl.txt> new rooted time tree with branch lengths
    - <ExaML_result_result_newick_date.txt> new rooted time tree with branch lengths as dates
    - <ExaML_result_result_nexus.txt> new rooted time tree as nexus file 
'''

import sys, subprocess, os, argparse

#************************************************

desStr = 'Converts a phylogenetic tree into a rooted time tree. '
desStr += 'The taxa of the tree are time sampled'


parser = argparse.ArgumentParser(description=desStr,
              formatter_class=argparse.RawDescriptionHelpFormatter)
              
parser.add_argument('treeFileName', help='Tree file in "newick" format')
parser.add_argument('dateFileName', help='Tab separated date file')

args = parser.parse_args()


#************************************************
  
fh = open('demodel.log','a') # lsd.log will contain the progress information


treeFile = args.treeFileName
dateFile = args.dateFileName

dates = [line.strip('\n') for line in open(dateFile,'r')] # get all the date information

dates = [`len(dates)`] + dates # first line contains the number of taxa for LSD

dateStr = '\n'.join(dates) # all the lines are joined in a string for writing in the file

msg = '\nWriting dates into file lsd.dates to be used by LSD\n'
print(msg)
fh.write(msg)

lh = open('lsd.dates','w') # dates are stored in lsd.dates for LSD run
lh.write(dateStr)
lh.close()


cl = '~/apps/lsd -i %s -d lsd.dates -c -r' % treeFile # command line for running LSD
# -c poses constraints for dating, -r roots the tree

msg = '\nRunning LSD with the following command:\n'
msg += '\n\t%s'%cl
print(msg)
fh.write(msg)



process = subprocess.Popen(cl,shell=True, stderr=fh,stdout=fh)

rval = process.wait()

#fh.close()

if os.stat('ExaML_result_result_newick_date.txt').st_size != 0:
  msg = '\nLSD run is completed'
  msg += '\nRooted time tree is written in <ExaML_result_result_newick_date.txt>\n'
  print(msg)
  fh.write(msg)
else:
  msg = '\nLSD run could not finish properly.'
  msg += '\nPlease refer to the demodel.log file for more information\n'
  print(msg)
  fh.write(msg)

