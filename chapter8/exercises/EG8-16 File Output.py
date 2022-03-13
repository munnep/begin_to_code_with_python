# EG8-16 File Output

output_file=open('test.txt','w')
output_file.write('line 1\n')
output_file.write('line 2\n')
output_file.close()

output_file=open('test.txt','a')
output_file.write('line 3\n')
output_file.write('line 4\n')
output_file.close()
