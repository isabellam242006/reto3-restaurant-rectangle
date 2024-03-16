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


    

    
    

