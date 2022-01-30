#!/usr/bin/env python3
import sys

def b2s(string, base):
	return ''.join([chr(int(s, base)) for s in string.split()])


if len(sys.argv) < 2:
	print('invalid args')
	exit()

string = ' '.join(sys.argv[1:])
for base in [2, 4, 8, 10, 16, 32]:
	s = 'err'
	try:
		s = ''.join([chr(int(s, base)) for s in string.split()]);
	except:
		pass	
	print(f'base={base} string={s}')

try:
	print(f"decoded={bytes.fromhex(string).decode('utf-8')}")
except:
	print('err from hex')


