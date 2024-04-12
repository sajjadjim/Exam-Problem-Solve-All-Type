Height = {'Child':[30, 40 ,35 , 45 , 30] ,
          'Teenage': [50 , 60 , 55 , 65 ,60] ,
          'Adult': [85 , 90 , 92 ,88 ,82],
          }
   
avarage_Height = {}
for age_list ,Height_list in Height.items():
#new arguments = sum of (All Key elements )/ length of Key elements 
    avarage_Heights = sum(Height_list) / len(Height_list) 
    avarage_Height[age_list] = avarage_Heights

print(avarage_Height) 
# Print Length of Dictionary
print(len(Height))

# Print which type of OPERATION
print(type(Height))
