
cities_of_spain = ["Madrid", "Toledo", "Salamanca", "Barcelona"]

print("The first item of the list is: " + cities_of_spain[0])
print("The last item of the list is: " + cities_of_spain[-1])

# We can add a new item using:
cities_of_spain.append("Cuenca")
print("The new item is: " + cities_of_spain[-1])

# We can add various new items using:
cities_of_spain.extend(["Sevilla", "Valencia"])
print("The new items are: " + cities_of_spain[-2] + " and " + cities_of_spain[-1])

# We can insert an item in a specify position using:
cities_of_spain.insert(0,"Alicante")
print("The new item in the position 0 is: " + cities_of_spain[0])
print("The last item in the position 0 now is the position 1: " + cities_of_spain[1])

# We can remove an element using:
cities_of_spain.pop(-1)

# We can delete the entire list using:
count = len(cities_of_spain)
print(f"The list has {count} elements")
cities_of_spain.clear()
count = len(cities_of_spain)
print(f"Now after use clean the list has {count} elements")

# Combining lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][2])