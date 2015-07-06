from Bio import Phylo

import os, argparse

#**********************************************
desStr = 'Convert "newick" trees into "nexus" trees using "Phylo" package of Biopython'

parser = argparse.ArgumentParser(description=desStr,
              formatter_class=argparse.RawDescriptionHelpFormatter)
              
parser.add_argument('inTree', help='Input tree in "Newick" format')
parser.add_argument('outTree', help='Output tree in "Nexus" format')


args = parser.parse_args()
 
#*************************************************
  
treeIn = args.inTree
treeOut = args.outTree


Phylo.convert(treeIn,'newick',treeOut,'nexus')
