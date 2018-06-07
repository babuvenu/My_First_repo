import os
import traceback
import sys

#path =(os.getcwd()) + "/sys.argv[0]"
path = (os.getcwd())
program_name = sys.argv[0]
arguments = sys.argv[1]
main_path = path + '/'+ arguments
#path= self.parser.add_option('(os.getcwd())'+'/--path_name')
cmd = main_path
print cmd
def main():
	run1 = os.system("git add . %s"% (cmd))
	#import pdb;pdb.set_trace()
	status = os.system(" git status")
	print status
	run2 = os.system("git commit -m 'automation'")
	run3 = os.system("git push origin master")


if __name__ == '__main__':
	main()

