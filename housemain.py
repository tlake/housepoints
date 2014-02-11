import argparse
import shutil
import os
import sys

# python version check, newline character def
if sys.version_info.major == 3:
	newline = '/n'
else:
	newline = '\n'

# some defs
new_total_str = 'New House Points Total: '
current_total_str = 'Current House Points Total: '
homedir = os.path.expanduser('~')
points_dir = homedir + '/local/share/'
points_file = 'pointstracker'
points_path = points_dir + points_file

def file_checker(dirname, filename):
	if not os.path.isdir(dirname):
		print  'Directory not found; creating ' + points_path
		os.makedirs(dirname)
		with open(dirname + filename, 'w') as newfile:
			newfile.write('0')
		return
	elif not os.path.isfile(dirname + filename):
		print 'File \'pointstracker\' not found; creating ' + points_path
		with open(dirname + filename, 'w') as newfile:
			newfile.write('0')
		return
	return

def file_reader(path_to_file):
	with open(path_to_file, 'r') as oldfile:
		return oldfile.readline()

def file_updater(path_to_file, string_to_add):
	with open('temp', 'w') as tempfile:
		with open(path_to_file, 'r') as oldfile:
			tempfile.write(string_to_add + newline + oldfile.read())
	shutil.move('temp', path_to_file)

# parser setup
parser = argparse.ArgumentParser(description='display current house points')
group = parser.add_mutually_exclusive_group()
group.add_argument('-a', '--add', action='store', type=int)
group.add_argument('-s', '--subtract', action='store', type=int)

args = parser.parse_args()


# if block: how to handle arguments
## adding points
if args.add:
	file_checker(points_dir, points_file)
	points = str(int(file_reader(points_path)) + args.add)
	print new_total_str + points
	file_updater(points_path, points)

## subtracting points
elif args.subtract:
	file_checker(points_dir, points_file)
	points = str(int(file_reader(points_path)) - args.subtract)
	print new_total_str + points
	file_updater(points_path, points)

## displaying current points (default behavior)
else:
	file_checker(points_dir, points_file)
	print current_total_str + file_reader(points_path)
