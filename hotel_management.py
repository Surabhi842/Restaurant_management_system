#Restaurant Management..
menu={ "mountain dew":25,    #create dictionary named menu
      "tea":15,               #which contains list of items
      "hot coffee":50,         #present in restaurant
      "cold coffee":70,
      "cold coffee with ice cream":100,
      "veg noodles":110,
      "momos":69,
      "chilli potato":149,
      "crispy baby corn":169,
      "manchurian with fried rice":159,
      "french fries":49,
      "masala dosa":110,
      "chola bhatura":120,
      "kachori sabji":60,
      "spring roll":59,
      "handi paneer":220,"kadhayi paneer":260,
      "paneer do pyaaza":189,
      "butter roti":20,
      "butter naan":45, "tandoori roti":12,"gulab jamun":12,"ras malai":15,
      "plain roti":10,"jalebi":7,"pista roll":20,"rajbhog":12,
      "mixed veg":110,
      "handi mushroom":210 }
print("Hello Sir/Ma'am\nWelcome in ABC Restaurant...")  #greet customer
print("Here is the Menu of our restaurant:")
print("\nSTARTER:\n1.Veg Noodles: Rs 110\n2.Momos: Rs 69 per plate(8 peices)\n3.Chilli potato: Rs 149\n4.Crispy Baby Corn: Rs 169\n5.Manchurian with Fried Rice: Rs 159\n6.French Fries: Rs 49\n7.Masala Dosa: Rs 110\n8.Chola Bhatura:Rs 120\n9.Spring Roll: Rs 59(4 peices)")
print("\nMAIN COURSE:\n1.Kachori Sabji:Rs 60\n2.Handi Paneer:Rs 220\n3.Paneer Do Pyaaza:Rs 189\n4.Mixed Veg:Rs 110\n5.Handi Mushroom:Rs 210\n6.Kadhayi Paneer:Rs 260")
print("\nCHAPATI'S:\n1.Plain Roti:Rs 10\n2.Butter Roti:Rs 20\n3.Butter Naan:Rs 45\n4.Tandoori Roti:Rs 12")
print("\nSWEETS:\n1.Gulab Jamun:Rs 12/peice\n2.Ras Malai:Rs 15/peice\n3.Jalebi:Rs 7/peice\n4.Pista Roll:Rs 20/peice\n5.Rajbhog:Rs 12/peice")
print("\nDRINKS:\n1.Tea:Rs 15\n2.Cold Coffee:Rs 70\n3.Cold Coffee with Ice-cream:Rs 100\n4.Mountain Dew:Rs 25\n5.Hot Coffee:Rs 50")
total_cost=0 #initialize total cost of customer
quantity=1
order=input("\nWhat do you want to order? :") #take order from customer
quantity=int(input("Enter quantity or no. of plates of your order:"))
if order in menu: #check if the item is present or not
    print("Order is in processed...")
else:
    print("Sorry sir/ma'am,This item is currently not available in  restaurant.")
total_cost+=menu[order]*quantity
quantity=1
while True:
    a = input("Want to order more items? (yes/no):")
    if a.lower()=='yes':
        order = input("\nWhat do you want to order? :")
        quantity=int(input("Enter quantity or no. of plates of your order:"))
        if order in menu:
            print("Order is being processed...")
            total_cost += menu[order]*quantity
            quantity=1
        else:
             print("Sorry sir/ma'am, This item is currently not available in the restaurant.")
    elif a.lower()=='no':
        break
    else:
        print("Please enter 'yes' or 'no'.")
print("Your Total Bill is:",total_cost)
print("Thank You Sir/Ma'am for Visiting,Hope to See You Again..")