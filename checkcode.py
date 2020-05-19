programfile = open('/home/jyotirmaya/ws/mlops1/program.py','r')	#connecting to the code file
code = programfile.read()				#reading the code file

if 'keras' or 'tensorflow' in code:						#because keras or tensorflow keyword is a cmust have for a dl program
	if 'Conv2D' in code:				#beacuse if a code is of CNN conv2D layer is a must have
		print('kerasCNN')
	else:
		print('not kerasCNN')
else:
	print('not deep learning')
