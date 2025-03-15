temperatures_celsius = [20, 22, 25, 23, 21, 24, 26]

temperatures_farenheit = [((x*9/5)+32) for x in temperatures_celsius]
print("All temperatures in farenheit ",temperatures_farenheit)

temperatures_farenheit = [((y*9/5)+32) for y in temperatures_celsius if y > 23]
print("All temperatures in farenheit which are above 23 C ",temperatures_farenheit)
