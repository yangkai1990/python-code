mylist = [x*x for x in range(3)]
print(mylist)
mygen=(x*x for x in range(3))
print(mygen)
for i in mygen:
    print(i)