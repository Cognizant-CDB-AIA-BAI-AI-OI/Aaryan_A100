import subprocess
import time
import pysnooper
'''
@pysnooper.snoop('outputs/config.log')
def config():
  print('config running')
  
  try :
    import sys 
    subprocess.run('conda env create -f Aaryan_A100/envs/whisper_env.yml',shell =True)
    subprocess.run('conda run -n whisper_env python Aaryan_A100/whisper.py',shell =True)
    subprocess.run('conda env remove -n whisper_env',shell =True)
 
  except :
    
    f = open('outputs/Exception.txt','w+')
    f.write(str(sys.exc_info()[0]))
    f.close()
  '''

@pysnooper.snoop('outputs/config.log')
def config():
  from Aaryan_A100.whisper import main_func
  print('\nrunning main_func\n')
  time.sleep(16)
  main_func()
  print('\n DOne main_func\n')

  
