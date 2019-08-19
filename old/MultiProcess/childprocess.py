import subprocess
import sys
import os
#print('$ nslookup www.python.org')
#r = subprocess.call(['nslookup', 'www.python.org'])
#print('Exit code:', r)


#f = subprocess.call(['ping','192.168.1.1'])


p = subprocess.Popen(['ping','192.168.1.1'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate()
print(p)
# print(output.decode('gbk'))
print('Exit code:', p.returncode)