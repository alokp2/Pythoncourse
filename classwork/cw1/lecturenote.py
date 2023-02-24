l=[1,2,3,4,2.2,3.2,0,0,1,2,"True",False]
print(l)
l.append(100)
l2=l.copy()
print(l2)
l3=l2.copy()
print(l3)

l3.pop()
print(l3)
l3=[1000,30000.8,40005]
l.extend(l3)
print(l)
l.remove(40005)
print(l)
l.insert(2,40005)
print(l)
for i in l:
    print(i)
   
