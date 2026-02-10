
age = 10

if (age >= 18):
    print("you can vote")
else:
    print("You can't vote")



# elif ladder

a = [10,20,30]
b = [11,22,33]
c = [111,222]

if (len(a) > len(b)) and (len(a) > len(c)):
    print("list a is max")
elif (len(b) > len(a)) and (len(b) > len(c)):
    print("list b is max")
elif (len(c) > len(a)) and (len(c) > len(b)):
    print("list c is max")
else:
    print("all list are equal")




# nested if

products = ["1.chai", "2.coffee", "3.pani", "4.exit"]

chai_types = ["ginger", "normal"]

for product in products:
    print(product)

selected_product = int(input("Select product:"))

if selected_product == 1:
    print("chai")
    for chai in chai_types:
        print(chai)
    selected_chai = int(input("Select chai:"))
    if selected_chai == 1:
        print("ginger")
    elif selected_chai == 2:
        print("normal")
    else:
        print("biji cha nathi")
elif selected_product == 2:
    print("coffee")
elif selected_product == 3:
    print("pani")
else:
    print("biju kasu nathi")

