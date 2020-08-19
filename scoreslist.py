scores=[]
y=[]
h=0
l=0



maxscores=0
minscores=100
total=0
for i in range(5):
    y=input("名字:")
    n=int(input("成績:"))
    scores.append(n)
    if n > maxscores:
        maxscores=n
        h=y
    if n < minscores:
        minscores=n 
        l=y
    total=total+n
s=total/len(scores)
print("總分:",total)
print("平均:",s) 
print("最高分",maxscores,h)
print("最低分",minscores,l)



          
    




















