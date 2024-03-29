toppings = [
  "pepperoni",
  "pineapple",
  "cheese",
  "sausage",
  "olives",
  "anchovies",
  "mushrooms"
]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print("We have " + str(num_two_dollar_slices) + " types of $2 slice pizzas")
print()

num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
print()

pizza_and_prices = [ [2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print("Original list of toppings")
print(pizza_and_prices)
print()

pizza_and_prices.sort()
print("Sorted list of toppings")
print(pizza_and_prices)
print()

cheapest_pizza = pizza_and_prices[0]
print("Our cheapest pizza")
print(cheapest_pizza)
print()

priciest_pizza = pizza_and_prices[-1]
print("Our priciest pizza")
print(priciest_pizza)
print()

pizza_and_prices.pop()

pizza_and_prices.insert(3, [2.5, "peppers"])
print("Our new pizza menu with our added pepper topping")
print(pizza_and_prices)
print()

three_cheapest = pizza_and_prices[:3]
print("Our 3 cheapest pizzas")
print(three_cheapest)
print()