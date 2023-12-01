import re

data= open(r'./day1.txt','r')
res1=[]
res2=[]
dict_digits={'eightwo':'82','twone':'21','nineight':'98','oneight':'18','threeight':'38','fiveight':'58','eighthree':'83',
'one':'1','two':'2','three':'3','four':'4', 'five':'5','six':'6', 'seven':'7', 'eight':'8', 'nine':'9',}


for line in data:
    digits=re.findall('\d',line)
    res1.append(int(digits[0]+digits[-1]))

    for word,number in dict_digits.items():
        if word in line:
            line=line.replace(word,number)
    digits=re.findall('\d',line)
    res2.append(int(digits[0]+digits[-1]))

data.close()


print(sum(res1), sum(res2))
