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