value = [1, 2,3,4,5,6,7,8,9]
value2=[1,2,3]

for  item in value :
    if item == 5 :
        continue
    print("Break")
    for item2 in value2:
        print(item,item2)