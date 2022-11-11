import pysnooper

@pysnooper.snoop('outputs/file.log')
def main_func():
    import os

    file_path = 'Aaryan_A100/1minvid.webm'
    
    s = 'whisper ' + file_path + ' --language en --model large --output_dir outputs --condition_on_previous_text False --verbose False'

    os.system(s)
    

main_func()


