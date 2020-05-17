'''
This code is very important as I started the program tweaker.py from here only and it guided me how to work with files in Python and perform the tasks which I wanted to do.
If you want to see how file handling works in Python , tweak the below code and check the outputs.'''

file_read = open('data.txt','r+')
file_write = open('temp.txt','r+')

sum=0
while True:
	x = file_read.readline()
	if(x == ''):
		print('eof reached')
		break
	if x.find(' ') != -1:
		print(x) 
		x = x.split()
		print(x)
		print(x[0] + '--' + x[1])
	else :
		sum = sum + int(x)
		file_write.write(x)

file_write.write(str(sum))
file_read.write('------------')
file_write.write('hurrah')
file_write.close()
file_read.seek(0)
#file_read.close()

t = '\n' + 'a' + '\n' + 'b'

#files_read = open('data.txt','w')
#files_read.write(data)
file_read.write(t)
file_read.close()