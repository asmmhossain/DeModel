from Bio import SeqIO

import sys, subprocess

if len(sys.argv) < 2:
  print('\n\tUSAGE: examl.py alnFile')
  sys.exit(0)
  

# Open a log file to monitor progress

fh = open('examl.log','w')

# Converting the fasta file to relaxed phylip format
# This is because ExaML only accepts relaxed phylip files

SeqIO.convert(sys.argv[1],'fasta','input.phy','phylip-relaxed')

# Now ExaML parser is called to transform the alignment into binary
# The binary file will be called input.binary

cl = ''

cl += '~/Downloads/ExaML/parser/parse-examl -s input.phy -m DNA -n input'

process = subprocess.Popen(cl,shell=True,stderr=fh,stdout=fh)
rval = process.wait()

# Next is to generate the starting tree
# This is done using RAxML
# Starting tree is stored in 'RAxML_parsimonyTree.startTree'

cl = ''

cl += 'raxmlHPC-SSE3 -y -m GTRCAT -p 12345'
cl += ' -s input.phy -n startTree'

process = subprocess.Popen(cl,shell=True,stderr=fh,stdout=fh)
rval = process.wait()

# the ExaML tree is generated from:
#		- the binary alignment file
#		- the starting tree
# The ExaML tree is written in ExaML_result.outTree

cl = ''
cl += '/home/mukarram/Downloads/ExaML/examl/examl -a -B 10 -D -m GAMMA -n outTree -s input.binary -t RAxML_parsimonyTree.startTree'

process = subprocess.Popen(cl,shell=True,stderr=fh,stdout=fh)
rval = process.wait()
 
fh.close() 
