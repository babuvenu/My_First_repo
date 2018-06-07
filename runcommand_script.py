import sys
import os

path = (os.getcwd())
#import pdb;pdb.set_trace()
program_name = sys.argv[0] 
print program_name
arguments = sys.argv[1:]
#import pdb;pdb.set_trace()
#path2= path +'/'+ ".join(arguments)
path2 = path + '/'+''.join(arguments)
import pdb;pdb.set_trace()
print arguments
count = len(arguments)
print count
