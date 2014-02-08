import argparse
import shutil
import os.path
import sys

# version check, newline character def
if sys.version_info.major == 3:
	newline = '/n'
else:
	newline = '\n'

# some defs
new_total_str = 'New House Points Total: '
current_total_str = 'Current House Points Total: '

# parser setup
parser = argparse.ArgumentParser(description='display current house points')
group = parser.add_mutually_exclusive_group()
group.add_argument('-a', '--add', action='store', type=int)
group.add_argument('-s', '--subtract', action='store', type=int)

args = parser.parse_args()

# if block: how to handle arguments
## adding points
if args.add:
	if os.path.isfile('pointstracker'):
		with open('pointstracker', 'r') as oldfile:
			line = oldfile.readline()
			points = int(line)
			points += args.add
			print new_total_str, points
			oldfile.seek(0)
			with open('temp', 'w') as tempfile:
				tempstring = str(points) + newline + oldfile.read()
				tempfile.write(tempstring)
		shutil.move('temp', 'pointstracker')				
	else:
		print new_total_str, args.add
		with open('pointstracker', 'w') as newfile:
			newfile.write(str(args.add))

## subtracting points
elif args.subtract:
	if os.path.isfile('pointstracker'):
		with open('pointstracker','r') as oldfile:
			line = oldfile.readline()
			points = int(line)
			points -= args.subtract
			print new_total_str, points
			oldfile.seek(0)
			with open('temp', 'w') as tempfile:
				tempstring = str(points) + newline + oldfile.read()
				tempfile.write(tempstring)
		shutil.move('temp', 'pointstracker')
	else:
		print new_total_str, 0 - args.subtract
		with open('pointstracker', 'w') as newfile:
			newfile.write(str(0 - args.subtract))

## displaying current points (default behavior)
else:
	if os.path.isfile('pointstracker'):
		with open('pointstracker', 'r') as f:
			print 'Curent House Points Total: ', f.readline()
	else:
		print 'Current House Points Total: 0'			
