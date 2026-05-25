#Pedimos al usuario cantidad de puntos que va a ingresar
n = int(input("¿Cuantos puntos desea ingresar?: "))
coords = []

#Guardamos los puntos en una lista
for i in range (n):
    lat = float(input(f"Ingrese la latitud del punto {i+1}: "))
    lon = float(input(f"Ingrese la longitud del punto {i+1}: "))
    coords.append((lat, lon))

#Funcion haversine donde el radio de la tierra es 6371km
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distancia = R * c
    return distancia


#Vamos a calcular la distancia de estos puntos entre si y la total con Haversine
total = 0
for i in range (len(coords)-1):
    tramo = haversine(coords[i][0],coords[i][1], coords[i+1][0], coords[i+1][1])
    total += tramo

print(f"La distancia entre punto {i+1} y punto {i+2} es: {tramo:.2f} km")
print("\nLa distancia total de la ruta es:", round(total,2), "km")
