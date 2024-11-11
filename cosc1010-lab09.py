# Ryan Dennis
# UWYO COSC 1010
# Submission Date 11/11/2024
# Lab 09
# Lab Section:14
# Sources, people worked with, help given to:Geeks for Geeks, Stack Overflow
# Your
# Comments
# Here

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.
class Pizza:
    def __init__ (self, size, toppings, sauce="Red"):
        self.size = size
        self.sauce = sauce
        self.toppings = toppings.split() + ["Cheese"]
        if int(self.size) >= 10:
            self.size = int(self.size)
        else:
            self.size = 10
    def topp(self):
        return self.toppings
    def pizza_size(self):
        return self.size
    def amount_toppings(self):
        amount = len(self.toppings)
        return amount
    def sauce_type(self):
        return self.sauce



# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.
class Pizzeria():
    def __init__ (self):
        self.orders = 0
        self.price_per_topping = 0.30
        self.price_per_inch = 0.60
        self.pizzas = []
    def placeorder(self):
        size = input("How big do you want your pizza? Please enter as a whole number bigger than 10.")
        sauce = input("What kind of sauce do you want on your pizza? Leave blank for Red.")
        if sauce == "":
            sauce = "Red"
        topping = input("What toppings do you want on your pizza.")
        pizza = Pizza(size, topping, sauce)
        self.pizzas.append(pizza)
        self.orders += 1
    def get_price(self):
        pizza = self.pizzas[-1]
        price = (self.price_per_inch * pizza.pizza_size()) + (self.price_per_topping * pizza.amount_toppings())
        print(price)
    def get_receipt(self):
        pizza = self.pizzas[-1]
        size_cost = (self.price_per_inch * pizza.pizza_size())
        toppings_cost = (self.price_per_topping * pizza.amount_toppings())
        print(f"Your pizza is {pizza.pizza_size()} inches, has {pizza.sauce_type()} sauce, has {pizza.topp()}, and has {pizza.amount_toppings()} types of toppings.")
        print(f"The size of your pizza costs {size_cost}")
        print(f"The toppings on your pizza cost {toppings_cost}")
        print(f"The total cost is {size_cost + toppings_cost}")
    def get_number_of_orders(self):
        print(f"The total number of orders is {self.orders}")

# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.
pizzeria = Pizzeria()
while True:
    answer = input("Do you want to order a pizza? Type 'exit' to exit.")
    if answer.lower() == "yes":
        pizzeria.placeorder()
        pizzeria.get_receipt()
        continue
    else:
        pizzeria.get_number_of_orders()
        break

# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""