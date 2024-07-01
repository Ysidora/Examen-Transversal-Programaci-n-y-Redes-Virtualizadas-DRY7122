from geopy.distance import geodesic

# Diccionario de coordenadas de algunas ciudades
coordenadas = {
    "Santiago": (-33.4489, -70.6693),
    "Buenos Aires": (-34.6037, -58.3816),
    "Valparaíso": (-33.0458, -71.6197),
    "Córdoba": (-31.4201, -64.1888)
}

def obtener_distancia(ciudad_origen, ciudad_destino):
    if ciudad_origen in coordenadas and ciudad_destino in coordenadas:
        coords_origen = coordenadas[ciudad_origen]
        coords_destino = coordenadas[ciudad_destino]
        distancia = geodesic(coords_origen, coords_destino)
        return distancia
    else:
        return None

def mostrar_menu():
    print("Seleccione el tipo de medio de transporte:")
    print("1. Automóvil")
    print("2. Avión")
    print("3. Bicicleta")

def main():
    while True:
        ciudad_origen = input("Ingrese la Ciudad de Origen (o 's' para salir): ")
        if ciudad_origen.lower() == 's':
            break
        ciudad_destino = input("Ingrese la Ciudad de Destino (o 's' para salir): ")
        if ciudad_destino.lower() == 's':
            break

        distancia = obtener_distancia(ciudad_origen, ciudad_destino)
        if distancia:
            print(f"Distancia entre {ciudad_origen} y {ciudad_destino}:")
            print(f"{distancia.miles:.2f} millas")
            print(f"{distancia.kilometers:.2f} kilómetros")

            mostrar_menu()
            transporte = input("Seleccione el número correspondiente al medio de transporte: ")

            if transporte == '1':
                duracion = distancia.kilometers / 80  # Suponiendo una velocidad promedio de 80 km/h
                tipo_transporte = "automóvil"
            elif transporte == '2':
                duracion = distancia.kilometers / 700  # Suponiendo una velocidad promedio de 700 km/h
                tipo_transporte = "avión"
            elif transporte == '3':
                duracion = distancia.kilometers / 20  # Suponiendo una velocidad promedio de 20 km/h
                tipo_transporte = "bicicleta"
            else:
                print("Opción no válida.")
                continue

            print(f"La duración del viaje en {tipo_transporte} es de aproximadamente {duracion:.2f} horas.")
            print(f"Narrativa del viaje: Desde {ciudad_origen} hasta {ciudad_destino} en {tipo_transporte}.")
        else:
            print("Ciudad de origen o destino no encontrada en la base de datos.")
