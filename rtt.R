args <- commandArgs(trailingOnly=T)

if(length(args) < 1)
{
	stop('Tree file name not provided')
}
tName <- args[1]
#tName <- paste(args[1],'.nex',sep='')
rttName <- paste(args[1],'.rtt.newick',sep='')

#print(tName)
#print(rttName)

library('ape')

#t <- read.nexus(tName)
t <- read.tree(tName)
#print(names(t))

dates <- numeric(length(t$tip.label))

for(i in 1:length(dates)){dates[i]<-as.numeric(strsplit(t$tip.label[i],'_')[[1]][2])}

#print(dates[1])

rtt(t,dates)

write.tree(t,rttName)


