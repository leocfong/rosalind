from itertools import permutations
import math
f = open("out.txt", "w")
num=5
s=1 
e=s+num
p=math.factorial(num)
print(p)
f.write(str(p) + '\n')
l = list(permutations(range(s, e)))

for i in range(p):
    for j in range(num):
        print(l[i][j], end=' ')
        f.write(str(l[i][j]) + ' ')
    print('')    
    f.write('\n')
f.close()    