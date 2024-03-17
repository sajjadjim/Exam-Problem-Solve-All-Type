product_name =[]
product_price =[]
product_quantity =[]
product_discount=[]

product_name.append("Bananna")
product_price.append(10)
product_quantity.append(2)
product_discount.append(10)

product_name.append("Milkshake")
product_price.append(28)
product_quantity.append(2)
product_discount.append(3)

product_name.append("Kitkat")
product_price.append(70)
product_quantity.append(2)
product_discount.append(1)

product_name.append("Flower")
product_price.append(150)
product_quantity.append(2)
product_discount.append(3)

x =len(product_name)
sum =0

for i in range(x):
    price =int(product_price.pop())
    quantity =float(product_quantity.pop())
    discount =int(product_discount.pop())
    calculate_Price= price*(discount/10)
    print(f"Product Name ->{product_name.pop()} ,Price-> {price} ,Quantity->> {quantity}")
    sum = sum + price*quantity

print("\n!<--------------- Totall Price ----------------->!")
print(f"Total Money of coast ->> {sum}")


