"""
genie.py

Galaxy wrapper for inferring demographic history from molecular phylogenies using GENIEv3.0

"""


import sys,optparse,os,subprocess,tempfile,shutil


class genie:
  '''
  '''

  def __init__(self,opts=None):
    self.opts = opts
    self.model = ''
    
    
  #*******************************************************  
  def runGenie(self):
  
    ## write the command file for running GENIEv3
    
    fStr = 'begin genie;'
    fStr += '\n\tload %s;' % self.opts.inTree
    fStr += '\n\tmod %s;' % self.model
    fStr += '\n\tml est;'
    fStr += '\nend;'
    
    fh = open('genieCommand.nex','w')
    fh.write(fStr)
    fh.close()
    
    #--------------------------
    
    tlf = open(self.opts.log,'a')
    
    tg = open('tempGenie.txt','w')
    
    tlf.write('GENIE started with %s model\n\n' % self.model)
    
    #fh.write('Model = %s\n\n' % mod)
        
    cl = '(echo "quit") | genie genieCommand.nex'
    
    ## run GENIEv3    
    process = subprocess.Popen(cl,shell=True,stderr=tg,stdout=tg)
    rval = process.wait()
    
    tg.close()
    
    tg = open('tempGenie.txt','r')
    
    if os.stat('tempGenie.txt').st_size != 0:
      tlf.write(tg.read()) # append the GENIE run output to the log file
    
    tg.close() 
    
    tlf.close()



  #*******************************************
  def run(self):
    tlf = open(self.opts.log,'w')
    tlf.write('GENIE log file begins.\n\n')
    tlf.close()
    
    fh = open(self.opts.output,'w')
    ##fh.write(self.opts.modType)
    ##fh.close()
    ##sys.exit(0)
    
    if self.opts.modType != 'all': # for single demographic model
      self.model = self.opts.modType
      self.runGenie()
    else: # all the demographic models are run in GENIE
      '''
      fh.write('Not yet implemented\n')
      fh.close()
      sys.exit(0)
      '''
      self.model = 'const'
      self.runGenie()
 
      self.model = 'expo'
      self.runGenie()
      
      self.model = 'expan'
      self.runGenie()

      self.model = 'log'
      self.runGenie()

      self.model = 'step'
      self.runGenie()

      self.model = 'pexpan'
      self.runGenie()

      self.model = 'plog'
      self.runGenie()
      
    # Output is summarised from the log file and written in output file  
    lines = [line.strip('\n') for line in open(self.opts.log,'r')]
    fh.write('Output from GENIE\n\n')
    
    for line in lines:
      words = line.replace('\t',' ').split(' ')
      if 'ln' in words: # get the likelihood headers
        fh.write('=====================================\n')
        fh.write(line.replace(' ','').replace('\t','\t\t'))
        fh.write('\n=====================================\n')
  
      elif words[0] is '0': # get the likelihood values
        fh.write(line.replace(' ','').replace('\t','\t\t'))
        fh.write('\n\n')
        
      elif 'Demographic' in words:
        if 'changed' not in words:
          fh.write(line)
          fh.write('\n') # write the demographic model's name
        
        
    fh.close()
  #***********************************************************  

       

#******************************************************************
if __name__ == "__main__":
    op = optparse.OptionParser()
    op.add_option('-m', '--modType', default='const',help='Demographic model')
    op.add_option('-i', '--inTree', default=None,help='Input tree file')
    op.add_option('-o', '--output', default='genieOut.txt',help='Output file')
    op.add_option('-l', '--log', default='genie.log.txt',help='Log file')

       
    opts, args = op.parse_args()
    assert opts.inTree <> None
    assert os.path.isfile(opts.inTree)
    c = genie(opts)
    c.run()
    
            

