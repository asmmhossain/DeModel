args <- commandArgs(trailingOnly=T)

if(length(args) < 2)
{
	msg1 = 'File name is not given.'
	msg2 = '\n\nUsage: Rscript nexus2newick.R nexusFileName newickFileName\n\n'
	msg = paste(msg1,msg2,sep='')
	stop(msg)
}
library(ape)

tre <- read.nexus(args[1])

write.tree(tre,args[2])
