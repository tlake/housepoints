import argparse
import shutil
import os
import sys

default_store = os.path.join(os.path.expanduser('~'), 'local', 'share', 'pointstracker')
# parser setup
parser = argparse.ArgumentParser(description='display current house points')
parser.add_argument('--storefile',
	nargs='?',
	default=default_store,
	metavar='FILE',
	help='default ~/local/share/pointstracker')
parser.add_argument('-s',
	'--subtract',
	dest='subtract',
	action='store_true',
	help='if given, will subtract amounts')
parser.add_argument('amounts',
	metavar='N',
	type=int,
	nargs='*',
	help='amounts to add/subtract')

args = parser.parse_args()
if not os.path.exists(os.path.dirname(args.storefile)):
	os.makedirs(os.path.dirname(args.storefile))

# some defs
new_total = 'New House Points Total: '
current_total = 'Current House Points Total: '

try:
	if not args.amounts:
		with open(args.storefile, 'r') as f:
			print sum(int(line) for line in f)
	else:
		# begin my favorite line
		numbers = ((-1 if args.subtract else 1) * n for n in args.amounts)
		# end my favorite line
		with open(args.storefile, 'a') as f:
			f.writelines(str(n) for n in numbers)
			f.write('\n')
except IOError as e:
	print e.strerror
