import sys
print(sys.version)
for line in sys.stdin:
    if line.rstrip()=='q':
        break
    print("input=",line)
sys.stdout.write('test\n')

print('exit')
