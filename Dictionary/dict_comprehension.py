cubes = {x: x**3 for x in range(1,10)}
print(cubes)

even_cubes = {x: val for x, val in cubes.items() if val % 2 == 0}
print(even_cubes)