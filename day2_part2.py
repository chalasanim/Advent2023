import re

rows=open('day2.txt').read().rstrip().split('\n')
cubes= {'r':12, 'g':13, 'b':14}
total=0
for row in rows:
    exceed =False
    result={'r':0,'g':0,'b':0}
    g_num=int(row.split(':')[0].split()[1])
    for n,c in re.findall(r'(\d+) (\w)',row):
        for col,count in result.items():
            if (col==c and count<int(n)):
                result[col]=int(n)
    total+=result['r']*result['g']*result['b']
print('total:',total)
