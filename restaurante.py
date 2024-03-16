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
            total += item.calcularPrecio()   #Aquí se utiliza la función de MenuItem para calcular el precio
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




 