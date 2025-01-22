# Simple Utility that takes a notepad file (with CRLF) and converts to CR
# and then outputs a new file with a filename capatible with Tectronix 4051 emulator flash drive format name
# Author : Wayne Byrne
# Date : 21-Jan-2025


import os
import sys
import shutil
import subprocess


param_1= sys.argv[1] 

windows_line_ending = b'\r\n'
tec_line_ending = b'\r'

file_stats = os.stat(param_1)

print ('Filename:',param_1)
print(f'File Size in Bytes is {file_stats.st_size}')
file_noext, _ =os.path.splitext(param_1)

#process file with new format
print ('Converting to Tec format')
with open(param_1, 'rb') as f:
		content = f.read()
		content = content.replace(windows_line_ending, tec_line_ending)

print ('New file size :',str(len(content)))

#Very specific format for file name 
new_file_name='1      '+'ASCII'+'   PROG '+file_noext+' '+str(len(content)) 

# Writing out new file for Tektronix 4051 flash drive format
print ('Writing Tektronix 4051 emulator flash drive format file...')
with open(new_file_name, 'wb') as f:
		f.write(content)
print ('New Filename:',new_file_name)












