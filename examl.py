from Bio import SeqIO

import sys, subprocess, argparse

#**********************************************
desStr = 'Infers ExaML trees from an alignment'

parser = argparse.ArgumentParser(description=desStr,
              formatter_class=argparse.RawDescriptionHelpFormatter)
              
parser.add_argument('alnFileName', help='Alignment file in FASTA format')

args = parser.parse_args()
 
#*************************************************

# Open a log file to monitor progress

fh = open('demodel.log','a')

# Converting the fasta file to relaxed phylip format
# This is because ExaML only accepts relaxed phylip files

SeqIO.convert(args.alnFileName,'fasta','input.phy','phylip-relaxed')

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
