list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
list3=[]
for a,b in zip(list1,list2):
 list3.append([a,b])
print(list3)

print(dict(list3))

