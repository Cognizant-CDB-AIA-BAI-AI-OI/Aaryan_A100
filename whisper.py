import pysnooper

@pysnooper.snoop('outputs/file.log')
def main_func():
    import os
    import time

    #file_path = 'Aaryan_A100/1minvid.webm'
    
    #s = 'whisper ' + file_path + ' --language en --model large --output_dir outputs --condition_on_previous_text False --verbose False'

    #os.system(s)
    
    '''
    import subprocess
    subprocess.run('pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html',shell =True)
    
    import torch
    print('Active CUDA Device: GPU', torch.cuda.current_device())
    print ('Available devices ', torch.cuda.device_count())
    print ('Current cuda device ', torch.cuda.current_device())
    '''
    
    f = open('outputs/test_file.txt','w+')
    f.write('this is just a test line')
    f.close()
    
    time.sleep(100)
    
    
main_func()
