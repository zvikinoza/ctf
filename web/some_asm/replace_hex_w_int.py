import sys

if len(sys.argv) != 2:
	print('try python filename.py file_to_replace')
	exit()
hexchars = '0123456789ABCDEFabcdef'
with open(sys.argv[1], 'r') as f:
	for line in f:
		line += ' '
		c, start = str(line), -1
		for i in range(len(line)):
			if start != -1 and c[i] not in hexchars:
				c = c[:start] + str(int(c[start:i], 16)) + c[i:]
				start = -1
				
			if c[i:i+2] == '0x':
				start = i
				print(start)
		print(c)
