def myfunc(n): 
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
myFourth= myfunc(4)

print(mydoubler(11))
print(mytripler(11))
print(myFourth(11))



