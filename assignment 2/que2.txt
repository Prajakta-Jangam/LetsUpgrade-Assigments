a="Python programming is easy to learn with Letsupgrade, Python is a simple language to learn"
print(a)
b=a.split()
c=[]

for i in b:
  if(a.count(i)>1 and (i not in c) or a.count(i)==1):
    c.append(i)
print(' '.join(c))
 