import subprocess
import time
import pysnooper

@pysnooper.snoop('outputs/config.log')
def config():
  print('config running')
  
  try :
    import sys 
    subprocess.run('conda env create -f Sushmita_A100/env_score.yml',shell =True)
    subprocess.run('conda run -n env_score python Sushmita_A100/score.py',shell =True)
    subprocess.run('conda env remove -n env_score',shell =True)
 
  except :
    
    f = open('outputs/Exception.txt','w+')
    f.write(str(sys.exc_info()[0]))
    f.close()
  
