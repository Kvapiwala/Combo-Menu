total = 0
order = []
prices = {
  "chicken": 5.25,
  "beef": 6.25,
  "tofu": 5.75,
  "small_drink": 1.00,
  "medium_drink": 1.75,
  "large_drink": 2.25,
  "small_fry": 1.00,
  "medium_fry": 1.50,
  "large_fry": 2.00,
  "ketchup": 0.25
}

sandwich_ordered = []
drinks_ordered = []
fries_ordered = []
user_ketchup = 0
sandwich_price = 0
drinks_price = 0
fries_price = 0
ketchup_cost = 0

Sandwiches = ["chicken", "$5.25", "beef", "$6.25", "tofu", "$5.75"]
print(Sandwiches)

edit_keywords = "Keywords to remove items from your order: sandwiches, drinks, fries, ketchup"

def sandwich_shenanigans():
  global total
  global sandwich_price
  user_sandwich = ""
  total_sandwiches = ""
  while total_sandwiches.isdigit() == False:
    total_sandwiches = (input("How many sandwiches would you like?: "))
  total_sandwiches = int(total_sandwiches)
  if total_sandwiches > 0:
    while not(user_sandwich in Sandwiches):
      user_sandwich = input("What kind of sandwich would you like?: ")
    if user_sandwich == "chicken":
      print(f"You have ordered {total_sandwiches} chicken sandwhiches")
      sandwich_ordered.append(f"{total_sandwiches} chicken sandwiches")
      sandwich_price = (prices["chicken"] * total_sandwiches)
      total += sandwich_price
    elif user_sandwich == "beef":
      sandwich_ordered.append(f"{total_sandwiches} beef sandwiches")
      sandwich_price = (prices["beef"] * total_sandwiches)
      total += sandwich_price
      print(f"You have ordered {total_sandwiches} beef sandwiches")
    elif user_sandwich == "tofu":
      print("You have ordered a tofu sandwich")
      sandwich_price = (prices["tofu"] * total_sandwiches)
      total += sandwich_price
      sandwich_ordered.append(f"{total_sandwiches} tofu sandwiches")
  elif total_sandwiches == 0:
    print("You did not order a sandwhich")
  elif total_sandwiches < 0:
    print("Please enter a positive number")
    sandwich_shenanigans()
    


def drink_shenanigans():
  global total
  global drinks_price
  Drinks = ["small", "$1.00", "medium", "$1.75", "large", "$2.25"]
  print(Drinks)
  
  user_drink = ""
  total_drinks = ""
  while total_drinks.isdigit() == False:
    total_drinks = input("How many drinks would you like?: ")
  total_drinks = int(total_drinks)
  if total_drinks > 0:
    while not(user_drink in Drinks):
      user_drink = input("What size drink would you like: ")
    if user_drink == "small":
      drinks_ordered.append(f"{total_drinks} small drinks")
      print(f"You have ordered {total_drinks} small drinks")
      drinks_price = (prices["small_drink"] * total_drinks)
      total += drinks_price
    elif user_drink == "medium":
      drinks_ordered.append(f"{total_drinks} medium drinks")
      print(f"You have ordered {total_drinks} medium drinks")
      drinks_price = (prices["medium_drink"] * total_drinks)
      total += drinks_price
    elif user_drink == "large":
      drinks_ordered.append(f"{total_drinks} large drinks")
      print(f"You have ordered {total_drinks} large drinks")
      drinks_price = (prices["large_drink"] * total_drinks)
      total += drinks_price
  elif total_drinks == 0:
      print("You did not order a drink")
  elif total_drinks < 0:
    print("Please enter a positive number")
    drink_shenanigans()



def fries_shenanigans():
  global total
  global fries_price
  Fries = ["small", "$1.00", "medium", "$1.50", "large", "$2.00"]
  print(Fries)

  user_fries = ""
  total_fries = ""
  while total_fries.isdigit() == False:
    total_fries = input("How many fries would you like?: ")
  total_fries = int(total_fries)
  if total_fries > 0:
    while not(user_fries in Fries):
      user_fries = input("What size fries would you like: ")
    
    if user_fries == "small":
      print(f"You have ordered {total_fries} small fries.")
      fries_ordered.append(f"{total_fries} small fries")
      fries_price = (prices["small_fry"] * total_fries)
      total += fries_price
      fry_upgrade = ""
      upgrade = ["yes", "no"]
      while not(fry_upgrade in upgrade):
        fry_upgrade = input("Would you like to mega-size your fries?(yes or no): ")
        
      if fry_upgrade == "yes":
        fries_ordered.append(f"{total_fries} (Mega-Size)Large fries")
        fries_ordered.remove(f"{total_fries} small fries")
        fries_price = (prices["large_fry"] * total_fries)
        total += fries_price
        print("You have mega-sized your small fries to a large")
      elif fry_upgrade == "no":
        print("You have kept your small fry order")
    
    elif user_fries == "medium":
      fries_ordered.append(f"{total_fries} medium fries")
      fries_price = (prices["medium_fry"] * total_fries)
      total += fries_price
      print(f"You have ordered {total_fries} medium fries")
    elif user_fries == "large":
      fries_ordered.append(f"{total_fries} large fries")
      fries_price = (prices["large_fry"] * total_fries)
      total += fries_price
      print(f"You have ordered {total_fries} large fries")
  
  elif total_fries == 0:
    print("You did not order any fries")  
  elif total_fries < 0:
    print("please enter a positive number")
    fries_shenanigans()




def ketchup_shenanigans():
  global total
  global user_ketchup
  global ketchup_cost
  ketchup = ("Sauces: Ketchup $0.25")
  ketchup_cost = 0.00
  user_ketchup = input("How many ketchup packets would you like?: ")
  while user_ketchup.isdigit() == False:
    user_ketchup = input("How many ketchup packets would you like?: ")
  user_ketchup = int(user_ketchup)
  if user_ketchup > 0:
   ketchup_cost = (user_ketchup * prices["ketchup"])
   print(f"You ordered {user_ketchup} ketchup packets")
   order.append(f"{user_ketchup} ketchup packets")
   total += ketchup_cost
   total -= 1.00
  elif user_ketchup < 0:
    print("Please enter a positive number or zero")
    ketchup_shenanigans()
  elif user_ketchup == 0:
    print("You did not order any ketchup")

sandwich_shenanigans()
drink_shenanigans()
fries_shenanigans()
ketchup_shenanigans()


order = [sandwich_ordered, drinks_ordered, fries_ordered, user_ketchup]
print(f"Your current order is{order} ketchup packets")
print(f"Your current total is ${total}")

def removing_shenanigans():
  global total
  global sandwich_price
  global fries_price
  global drinks_price
  global ketchup_cost

  edit = ["yes","no"]
  edit_order = ""
  print(edit_order)
  while not(edit_order in edit):
    edit_order = input("Would you like to remove anything from your order?(yes/no): ")
  if edit_order == "yes":
    remove = ["sandwiches", "drinks", "fries", "ketchup"]
    remove_items = ""
    while not(remove_items in remove):
      print(f"The follow items are removable {order}")
      print ("\n" + edit_keywords + "\n")
      remove_items = input("What item would you like to remove?: ")
    if remove_items == "sandwiches":
      order.remove(order[0])
      total -= sandwich_price
    elif remove_items == "drinks":
      order.remove(order[1])
      total -= drinks_price
    elif remove_items == "fries":
      order.remove(order[2])
      total -= fries_price
    elif remove_items == "ketchup":
      order.remove(order[3])
      total -= ketchup_cost
  elif edit_order == "no":
    print("Okay you have kept your order")
    
removing_shenanigans()

print(f"Your final order is {order} ketchup packets")
print(f"Your final total is ${total}")