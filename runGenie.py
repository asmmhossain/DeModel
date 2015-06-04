import sys,os,subprocess

if len(sys.argv) < 3:
  msg = '\nUSAGE: runGenie.py inputNexusTreeFile demographicModel\n'
  msg += '\nSupported demographic models:'
  msg += '\nconst\texpo\tlog\texpan\tstep\tplog\tpexpan\n\n'
  print(msg)
  sys.exit(0)
  
inTree = sys.argv[1]
mod = sys.argv[2]

deModels = ['const','expo','log','expan','step','plog','pexpan']

if mod.lower() not in deModels:
  msg = '\nUnsupported demographic model. Please use one of the following:\n'
  msg += 'const\texpo\tlog\texpan\tstep\tplog\tpexpan\n\n'
  print(msg)
  sys.exit(0)
  
if os.stat(inTree).st_size == 0:
  msg = '\nThe input tree file is not found.'
  msg += ' Please make sure you provide a correct tree file\n\n'
  msg += 'The program could not finish properly\n\n'
  print(msg)
  sys.exit(0)
  

## write the command file for running genie
inStr = ''
inStr += 'begin genie;'
#inStr += '\n\tlog tempGenie.txt;'
inStr += '\n\tload %s;' % inTree
inStr += '\n\tmod %s;' % mod.lower()
inStr += '\n\tml est;'
#inStr += '\n\tlog;'
inStr += '\nend;'

fh = open('genieIn.nex','w')
fh.write(inStr)
fh.close() 
##*******************************************

fh = open('tempGenie.txt','w')

print('\n\nGENIE is started with %s model\n' % mod.lower())
  
cl = '(echo "quit") | genie genieIn.nex'

process = subprocess.Popen(cl,shell=True,stdout=fh)
rval = process.wait()

fh.close() # close tempGenie.txt

#*********************
if os.stat('tempGenie.txt').st_size == 0 :
  print('\n\nGENIE could not finish properly.\n\n')
  sys.exit(0)

else:
  msg = '\nGENIE finished.\n'
  print(msg)

#************ read tempGenie.txt file and display the parameters

lines = [line.strip('\n') for line in open('tempGenie.txt','r')]
print('\n\nModel = %s\n' % mod.lower())

for line in lines:
  words = line.replace('\t',' ').split(' ')
  #print(words)
  if 'ln' in words:
    print('=====================================')
    print(line.replace(' ','').replace('\t','\t\t'))
    print('=====================================')
  
  elif words[0] is '0':
    print(line.replace(' ','').replace('\t','\t\t'))

print('')    
#*******************************************************************



