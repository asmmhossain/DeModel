import sys

from Bio import SeqIO

if len(sys.argv) < 3:
  print('\n\tUSAGE: mapSeqName.py seqFile dateFile\n')
  sys.exit(0) # terminate if both alignment file and date file is not given
  

#************ get the sequences******************
  
seqFile = sys.argv[1]  
seqs = list(SeqIO.parse(seqFile,'fasta')) # read in the alignment in a list

#print(len(seqs))

nSeqs = len(seqs) # nSeqs holds the number of sequences

#*************get the dates*******************

dateLines = [line.strip('\n') for line in open(sys.argv[2],'r')]

seqIds = []
seqDates = []

# extract the sequence IDs and the dates and store in lists
for line in dateLines:
  words = line.split('\t')
  seqIds.append(words[0])
  seqDates.append(words[1])
  
if nSeqs != len(seqIds):
  print('\nSequence numbers do not match in alignment and date file')
  print('\nThe program is exiting\n')
  sys.exit(0)
  

mStr = '' # mStr will hold the mapping list: oldName newName

for i in xrange(nSeqs):
  if seqs[i].id in seqIds: # if the sequence IDs in both alignment and date file matches
    ind = seqIds.index(seqs[i].id) # get the date for that sequence
    mStr += seqs[i].id + '\t' + 'X' + `i+1` + '_' + seqDates[ind] + '\n' # mStr contains ID	Xi_date in each line
  else:
    print('\nSequence %s is not present in date file\n' % seqs[i].id)
    sys.exit(0)



mName = seqFile + '.map' # name of the mapping file

print('\nGenerating mapping file %s\n' % mName)


fh = open(mName,'w')
fh.write(mStr)
fh.close()

#*******************renaming sequences in alignment and date file based on mapping*********
alnStr = ''
nDates = []

nDateStr = ''


for i in xrange(nSeqs):
  ind = seqIds.index(seqs[i].id)  # get the index of the sequence for getting date
  alnStr += '>X' + `i+1` + '_' + seqDates[ind] + '\n' + str(seqs[i].seq) + '\n'
  nDates.append(seqDates[ind])
  nDateStr += 'X' + `i+1` + '_' + seqDates[ind] + '\t' + seqDates[ind] + '\n'

nSeqName = seqFile + '.new'
fh = open(nSeqName,'w')
fh.write(alnStr)
fh.close()

print('\nWriting new alignment file in %s\n' % nSeqName)


nDateFileName = seqFile + '.nDate'
fh = open(nDateFileName,'w')
fh.write(nDateStr)
fh.close()

print('\nWriting new date file in %s\n' % nDateFileName)

