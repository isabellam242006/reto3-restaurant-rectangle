# reto3 - Rectángulo y Restaurante

1.Create a repo with the class exercise

1.1. Create class Line
- length, slope, start, end: Instance attributes, two of them being points (so a line is composed at least of two points).
- compute_length(): should return the line´s length
- compute_slope(): should return the slope of the line from tje horizontal in deg.
- compute_horizontal_cross(): should return if exists the intersection with x-axis
- compute_vertical_cross(): should return if exists the intersection with y-axis

```python
import math

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def compute_length(self):
        return math.sqrt((self.end[0] - self.start[0])**2 + (self.end[1] - self.start[1])**2)

    def compute_slope(self):
        if self.end[0] - self.start[0] != 0:
            slope = (self.end[1] - self.start[1]) / (self.end[0] - self.start[0])
            return math.degrees(math.atan(slope))
        else:
            return None

    def compute_horizontal_cross(self):
        if self.start[1] < 0 and self.end[1] > 0 or self.start[1] > 0 and self.end[1]<0:
            return True
        else:
            return False
        #Para que cruce en x se tiene que cumplir que: El signo end_y sea distinto al signo de start_y
        

    #Para que cruce en y se tiene que cumplir que: El signo end_x sea distinto al signo de start_x   

    def compute_vertical_cross(self):
        if (self.start[0] < 0 and self.end[0] > 0) or (self.start[0] > 0 and self.end[0]<0):   #jerarquia de operaciones
            return True
        else:
            return False


start_x = float(input("Ingrese la coordenada x de inicio: "))
end_x = float(input("Ingrese la coordenada x de final: "))
start_y = float(input("Ingrese la coordenada y de inicio: "))
end_y = float(input("Ingrese la coordenada y de final: "))

# Tupla de coordenadas
start = (start_x, start_y)
end = (end_x, end_y)

 
line = Line(start, end)
slope = line.compute_slope() 
interseccion_eje_y = line.compute_vertical_cross()
interseccion_eje_x = line.compute_horizontal_cross()

print("La longitud de la línea es", line.compute_length()) 
print("La pendiente en grados de la línea es", line.compute_slope())  

if interseccion_eje_y:
    print("La línea cruza el eje y")
else:
    print("La línea no cruza el eje y")

if interseccion_eje_x:
    print("La línea cruza el eje x")
else:
    print("La línea no cruza el eje x")
```
1.2 Redefine the class Rectangle, adding a new method of initialization using 4 Lines (composition at its best, a rectangle is compose of 4 lines).

```python
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def compute_length(self):
        return math.sqrt((self.end[0] - self.start[0])**2 + (self.end[1] - self.start[1])**2)

    def compute_slope(self):
        if self.end[0] - self.start[0] != 0:
            slope = (self.end[1] - self.start[1]) / (self.end[0] - self.start[0])
            return math.degrees(math.atan(slope))
        else:
            return None

class Rectangulo:
    def __init__(self, ancho, largo, punto_centro) -> float:
        self.ancho = ancho
        self.largo = largo
        self.centro = punto_centro
    
    def computar_area(self):
        resultado = self.ancho * self.largo
        return resultado
    
    def computar_perimetro(self):
        resultado = 2*(self.ancho + self.largo)
        return resultado
    
    def computar_interferencia_punto(self, Punto):
        if Punto.x < self.ancho and Punto.y < self.largo:
            return True
        else:
            return False


class Cuadrado(Rectangulo):
    def __init__(self, lado, punto_centro):
        super().__init__(ancho=lado, largo=lado, punto_centro=punto_centro)


    
metodo = int(input("Ingrese un método, 1,2,3,4: "))

if metodo == 1:
    largo = float(input("Ingrese el largo: "))
    ancho = float(input("Ingrese el ancho: "))
    punto_centro_x = int(input("Ingrese componente x para el punto centro: "))
    punto_centro_y = int(input("Ingrese componente y del punto centro: "))
    punto_izquierdo_x = punto_centro_x - (ancho/2)
    punto_izquierdo_y = punto_centro_y - (largo/2)

elif metodo == 2:
    largo = float(input("Ingrese el largo: "))
    ancho = float(input("Ingrese el ancho: "))
    punto_centro_x = int(input("Ingrese componente x para el punto centro: "))
    punto_centro_y = int(input("Ingrese componente y del punto centro: "))

elif metodo == 3:
    largo = float(input("Ingrese el largo: "))
    ancho = float(input("Ingrese el ancho: "))
    punto_centro_x = int(input("Ingrese componente x para el punto centro: "))
    punto_centro_y = int(input("Ingrese componente y del punto centro: "))
    punto_izquierdo_x = punto_centro_x - (ancho/2)
    punto_izquierdo_y = punto_centro_y - (largo/2)
    punto_derecho_x = punto_centro_x + (ancho/2)
    punto_derecho_y = punto_centro_y + (largo/2)


elif metodo == 4:
    # Coordenadas de inicio y final para el ancho
    start_x_ancho = float(input("Ingrese la coordenada x de inicio para el ancho: "))
    end_x_ancho = float(input("Ingrese la coordenada x de final para el ancho: "))
    start_y_ancho = float(input("Ingrese la coordenada y de inicio para el ancho: "))
    end_y_ancho = float(input("Ingrese la coordenada y de final para el ancho: "))

    # Coordenadas de inicio y final para el largo
    start_x_largo = float(input("Ingrese la coordenada x de inicio para el largo: "))
    end_x_largo = float(input("Ingrese la coordenada x de final para el largo: "))
    start_y_largo = float(input("Ingrese la coordenada y de inicio para el largo: "))
    end_y_largo = float(input("Ingrese la coordenada y de final para el largo: "))

    # Crear las líneas
    linea_ancho = Line((start_x_ancho, start_y_ancho), (end_x_ancho, end_y_ancho))   #Crear las tuplas con las variables que dé el usuario
    linea_largo = Line((start_x_largo, start_y_largo), (end_x_largo, end_y_largo))

    # Calcular el ancho y el largo
    ancho = linea_ancho.compute_length()
    largo = linea_largo.compute_length()

    # Calcular el punto centro
    punto_centro_x = (start_x_ancho + end_x_ancho) / 2
    punto_centro_y = (start_y_ancho + end_y_ancho) / 2


else:
    print("Ingrese un método válido")

r = Rectangulo(ancho, largo, Punto(punto_centro_x, punto_centro_y))
print("El área del rectángulo es ", r.computar_area(), "y el perímetro del rectángulo es", r.computar_perimetro())

c = Cuadrado(lado=ancho, punto_centro=Punto(punto_centro_x, punto_centro_y))     #Importante especificar a qué equivale cada valor
print("El área del cuadrado es ", c.computar_area(), "y el perímetro del cuadrado es", c.computar_perimetro())

interferencia_punto_x = int(input("Ingrese coordenada x: "))
interferencia_punto_y = int(input("Ingrese coordenada y: "))
interferencia_punto = Punto(interferencia_punto_x, interferencia_punto_y)
interferencia = r.computar_interferencia_punto(interferencia_punto)

if interferencia:
    print("Las coordenadas dadas están dentro del rectángulo")
else:
    print("Las coordenadas dadas no están dentro del rectángulo")
```
2.Restaurant scenario: You want to design a program to calculate the bill for a customer's order in a restaurant.
- Define a base class MenuItem: This class should have attributes like name, price, and a method to calculate the total price.
- Create subclasses for different types of menu items: Inherit from MenuItem and define properties specific to each type (e.g., Beverage, Appetizer, MainCourse).
- Define an Order class: This class should have a list of MenuItem objects and methods to add items, calculate the total bill amount, and potentially apply specific discounts based on the order composition.
- Create a class diagram with all classes and their relationships. The menu should have at least 10 items. The code should follow PEP8 rules

```python
class MenuItem:
    def __init__(self, nombre, precio, impuesto, propina):
        self.precio = precio
        self.impuesto = impuesto
        self.propina = propina
        self.nombre = nombre

    def calcularPrecio(self):
        impuesto = self.precio * self.impuesto
        propina = self.precio * self.propina
        total = self.precio + impuesto + propina
        return total
    
class Entrada(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, tipo):
        super().__init__(nombre, precio, impuesto, propina)
        self.tipo = tipo

class Sopa(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, ingrediente_principal):
        super().__init__(nombre, precio, impuesto, propina)
        self.ingrediente_principal = ingrediente_principal

class Postre(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, tipo):
        super().__init__(nombre, precio, impuesto, propina)
        self.tipo = tipo

class Bebida(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, tipo):
        super().__init__(nombre, precio, impuesto, propina)
        self.tipo = tipo

class Ensalada(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, vinagreta):
        super().__init__(nombre, precio, impuesto, propina)
        self.vinagreta = vinagreta

class Pasta(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, tipo_pasta):
        super().__init__(nombre, precio, impuesto, propina)
        self.tipo_pasta = tipo_pasta

class Order:
    def __init__(self):
        self.items = []
    
    def agregarItem(self, item):   #Esta parte nos permite agregar los items que se deseen
        self.items.append(item)       


    def calcularTotal(self):
        total = 0
        for item in self.items:
            total += item.calcularPrecio()   #Aquí se utiliza la función que se hereda de la clase MenuItem para calcular el precio
        return total

    def imprimirFactura(self):
        for item in self.items:
            print(item.nombre, "- $",item.calcularPrecio())  #Imprime nombre y precio del Item
        print("Total: $",self.calcularTotal())
    
    def aplicarDescuento(self):         #Aplica descuento del 10% con condición
        total = self.calcularTotal()
        if total > 400000:
            for item in self.items:
                item.precio = item.precio * 0.9
  

#Creamos el menu con cada item y sus atributos

entrada1 = Entrada("Burrata Figliata", 105000, 0.7, 0.10, "Queso")
entrada2 = Entrada("Berenjenas a la parmesana", 38000, 0.7, 0.10, "Vegetal")
entrada3 = Entrada("Carpaccio de Res", 70000, 0.7, 0.10, "Carne")

pasta1 = Pasta("Pasta Carbonara", 80000, 0.7, 0.10, "Spaghetti")
pasta2 = Pasta("Pasta Pomodoro", 70000, 0.7, 0.10, "Pasta corta")
pasta3 = Pasta("Pasta Putanesca", 75000, 0.7, 0.10, "Spaghetti")
pasta4 = Pasta("Pasta Bolognesa", 85000, 0.7, 0.10, "Fetuccini")
pasta5 = Pasta("Pasta Alfredo", 90000, 0.7, 0.10, "Fetuccini")

postre1 = Postre('Tiramisu de la casa', 22000, 0.7, 0.10, "Tiramisú")
postre2 = Postre("Copa Amaretto", 26000, 0.7, 0.10, "Copa")
postre3 = Postre("Gelato al Pistacchio", 40000, 0.7, 0.10, "Gelatina")
postre4 = Postre("Torta de chocolate", 26000, 0.7, 0.10, "Torta")

bebida1 = Bebida("Bubble Fizz", 50000, 0.7, 0.10, "Licor")
bebida2 = Bebida("Coca Cola", 10000, 0.7, 0.10, 'Refresco')
bebida3 = Bebida("Capuccino", 10000, 0.7, 0.10, "Bebida caliente")
bebida4 = Bebida("Limonada de coco", 14000, 0.7, 0.10, "Limonada")
bebida5 = Bebida("Jugo de Mora", 10000, 0.7, 0.10, "Jugo")

ensalada1 = Ensalada("Insalata Di garedino", 55000, 0.7, 0.10, "Vinagreta Oliva Limón")
ensalada2 = Ensalada("Kale César", 40000, 0.7, 0.10, "Vinagreta tradicional")

sopa1 = Sopa("Sopa Minestrone", 26000, 0.7, 0.10, "Verduras")
sopa2 = Sopa("Sopa Di Pomodoro", 26000, 0.7, 0.10, "Tomates")



# Crea una nueva orden
orden1 = Order()
orden2 = Order()
orden3 = Order()

# Agrega todos los objetos a la orden
orden1.agregarItem(entrada1)
orden1.agregarItem(pasta3)
orden1.agregarItem(postre3)
orden1.agregarItem(bebida4)

orden2.agregarItem(entrada2)
orden2.agregarItem(pasta5)
orden2.agregarItem(postre1)
orden2.agregarItem(sopa1)

orden3.agregarItem(ensalada2)
orden3.agregarItem(pasta2)
orden3.agregarItem(postre2)
orden3.agregarItem(bebida2)

# Imprime el menú con su descuento si existe
print("La factura de la orden 1 es:")
print()

orden1.aplicarDescuento()
orden1.imprimirFactura()
print()
print("La factura de la orden 2 es:")
print()

orden2.aplicarDescuento()
orden2.imprimirFactura()

print()
print("La factura de la orden 3 es:")

orden3.aplicarDescuento()
orden3.imprimirFactura()
```
