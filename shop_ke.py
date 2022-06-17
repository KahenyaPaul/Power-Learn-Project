discount = float (0.10)
item_cost = float (input("Cost of the item:"))
quantities = float (input("The quantity of the items:"))
total_cost = float ()

total_cost_1 = item_cost*quantities


if total_cost >1000:
    total_cost = discount*item_cost*total_cost

    print("**********RECEIPT**********")
   # print("\n")
    print("The total cost is:",total_cost)

print("Total cost is:",total_cost_1)