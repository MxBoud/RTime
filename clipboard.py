#!/usr/bin/env python

import subprocess, os, Tkinter

def write_to_clipboard(output):
    output = output.replace('.',',') #Replace dot by comma for french convention for wrinting numbers 
    if os.name:
        r = Tkinter.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(output.encode('utf-8'))
        r.destroy
        #pyperclip.copy('The text to be copied to the clipboard.')
        #spam = pyperclip.paste()
    else: 
        process = subprocess.Popen(
            'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
        process.communicate(output.encode('utf-8'))
    

    