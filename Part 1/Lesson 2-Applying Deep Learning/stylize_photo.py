import os
import glob
import sys
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
sys.path.insert(0, 'fast-style-transfer')
sys.path.insert(0, 'fast-style-transfer\\src')

from evaluate import ffwd_to_img


def get_files(extension, path=''):
    '''returns files in folder with given extension and path'''
    cwd = os.getcwd()
    os.chdir(cwd)
    return glob.glob(path + "*." + extension)

checkpoint_files = [file.split("\\")[1] for file in get_files('ckpt', 'checkpoint/')]
input_files = [file.split("\\")[1] for file in get_files('jpg', 'input\\') + get_files('png', 'input\\') ]

print("/nChoose input file : ")
for count, file in enumerate(input_files):
	print(str(count+1) + '-' + file,end='\t')
input_number = int(input("\nNumber : "))

print("/nChoose art style to apply : ")
for count, file in enumerate(checkpoint_files):
	print(str(count+1) + '-' + file,end='\t')
checkpoint_number = int(input("\nNumber : "))

input_file=input_files[input_number-1]
output_file=input_file.replace(input_file.split('.')[1],"_"+checkpoint_files[checkpoint_number-1].split('.')[0]+'.'+input_file.split('.')[1])
input_path='.\\input\\'+input_file
checkpoint_path='.\\checkpoint\\'+checkpoint_files[checkpoint_number-1]
output_path='.\\output\\'+output_file
ffwd_to_img(in_path=input_path,out_path=output_path,checkpoint_dir=checkpoint_path)

print("Done stylizing "+input_file+" to "+output_file+"...")
