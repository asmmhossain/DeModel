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

import sys, subprocess, os

if len(sys.argv) < 3:
  print('\nUSAGE: rootTree_LSD.py treeFile dateFile\n')
  sys.exit(0)
  
treeFile = sys.argv[1]
dateFile = sys.argv[2]

dates = [line.strip('\n') for line in open(dateFile,'r')] # get all the date information

dates = [`len(dates)`] + dates # first line contains the number of taxa for LSD

dateStr = '\n'.join(dates) # all the lines are joined in a string for writing in the file

print('\nWriting dates into file lsd.dates to be used by LSD\n')

fh = open('lsd.dates','w') # dates are stored in lsd.dates for LSD run
fh.write(dateStr)
fh.close()


cl = '~/apps/lsd -i %s -d lsd.dates -c -r' % treeFile # command line for running LSD
# -c poses constraints for dating, -r roots the tree

print('\nRunning LSD with the following command:\n')
print('\n\t%s'%cl)

fh = open('lsd.log','w') # lsd.log will contain the progress information



process = subprocess.Popen(cl,shell=True, stderr=fh,stdout=fh)

rval = process.wait()

fh.close()

if os.stat('ExaML_result_result_newick_date.txt').st_size != 0:
  print('\nLSD run is completed\n')
else:
  print('\nLSD run could not finish properly.')
  print('\nPlease refer to the lsd.log file for more information\n')

