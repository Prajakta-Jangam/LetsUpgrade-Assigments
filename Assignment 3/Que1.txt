d1 = d2 =""

with open('one.txt') as fp:
  d1=fp.read()
  
with open('two.txt') as fp:
  d2=fp.read()
  
d1 += "\n"
d1 += d2

with open('three.txt', 'w') as fp:
  fp.write(d1)

