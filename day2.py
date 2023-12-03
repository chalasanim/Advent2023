import re
games= open('day2.txt','r').read().strip().split('\n')
cubes= {'blue':14,'red':12, 'green':13}
total=0
round={}
for game in games:
    game=game.rstrip().split(':')
    subs=game[1].split(';')
    limit=False
    for sub in subs:
        ccounts=sub.split(',')
        for ccount in ccounts:
            count=int(re.findall(r'\d+',ccount)[0])
            if  (('blue' in ccount and count>cubes['blue']) or
                ('red' in ccount and count>cubes['red']) or
                ('green' in ccount and count>cubes['green'])):
                 limit=True
                 break
        if  limit:
            break
    if not limit :
        print(game[0])
        total+=int(game[0].split()[1])
print('total:',total)
