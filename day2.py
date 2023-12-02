import re

games= open('day2.txt','r').read().strip().split('\n')
data=['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

cubes= {'blue':14,'red':12, 'green':12}

dict_tally={}
for game in games[11:12]:
    blue=[]
    red=[]
    green=[]
    game=game.rstrip().split(':')
    subs=game[1].split(';')
    for sub in subs:
        ccounts=sub.split(',')
        for ccount in ccounts:
            if 'blue' in ccount:
                blue+=re.findall(r'\d+',ccount)
            elif 'red' in ccount:
                red+=re.findall(r'\d+',ccount)
            elif 'green' in ccount:
                green+=re.findall(r'\d+',ccount)
    blue_count=sum([int(x) for x in blue])
    red_count=sum([int(x) for x in red])
    green_count=sum([int(x) for x in green])
    dict_tally[game[0]]  ={'blue':blue_count,'red':red_count,'green':green_count}
print(dict_tally)
total=0
exceed=False
for game,tally in dict_tally.items():
   for pick_col,pick_tally in tally.items():
       for cube_col,cube_tally in cubes.items():
           if (pick_col==cube_col) and (pick_tally>cube_tally):
              exceed=True
              break

       if exceed==False :
         total+=int(game[-1])
         break


print(total)
