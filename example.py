import math
import matplotlib.pyplot as plt

# mostramos un mensaje de bienvenida
print('¡Hola! Vamos a resolver una ecuación de segundo grado:')
print('    ax² + bx + c = 0\n')

# pedimos los coeficientes al usuario
a, b, c = [float(input(f'Dame el coeficiente {coef}: ')) for coef in ('a', 'b', 'c')]

# calculamos el discriminante
discriminante =  b * b - 4 * a * c

#calculamos punto medio
puntoMedio = -b/(2*a)

if discriminante < 0: # comprobamos si no existen soluciones reales
    print(f'La ecuación no tiene soluciones reales.')
else:
    raiz = math.sqrt(discriminante)      # calculamos la raíz
    x_1 = (-b + raiz) / (2 * a)     # calculamos una primera solución
    if discriminante != 0:          # comprobamos si hay otra solución
        x_2 = (-b - raiz) / (2 * a) # calculamos la segunda solución
        print(f'Las soluciones son {x_1} y {x_2}.') # mostramos las dos soluciones
        print(f'Punto medio: {puntoMedio}.') # mostramos la discriminante
    else:
        print(f'La única solución es x = {x_1}') # mostramos la única solución
        print(f'Punto medio: {puntoMedio}.') # mostramos la discriminante


puntoMedio = int(puntoMedio)
 
# x axis values
x = [i for i in range( round(puntoMedio-10), round(puntoMedio+10))]

# corresponding y axis values
y = [((a*i**2) + (b*i) + (c))  for i in x ]





for yindex in range(puntoMedio-10,-1):
    for xindex in range(puntoMedio+10,1):
        if y[xindex] == yindex:
            print("*", end='')
        else:
            print(" ", end='')
    print()
    
fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()