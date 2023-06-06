# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ADm4gM4nNgQdcE_8_zrj6pb-N6IggZ4P
"""

import random
import queue
# Creamos los procesos 
num_procesos = random.randint(5, 8) 
procesos = [] 


for i in range(num_procesos):
    duracion = random.randint(80, 120) 
    tickets = random.randint(1, 4) 
    proceso = {"id": i+1, "duracion": duracion, "tickets": tickets} 
    procesos.append(proceso) 


# Imprime Tabla 
print("Planteamiento de Loteria:")
print("ID\tDuración\tBoletos")
for proceso in procesos:
    print("{}\t{}\t\t{}".format(proceso['id'], proceso['duracion'], proceso['tickets']))


# Crea la cola de procesos
cola = queue.Queue()


# Agrega procesos a la cola de procesos
for proceso in procesos:
    cola.put(proceso)


# Simular ejecución de procesos
while not cola.empty():
    # Obtener el proceso ganador de la lotería
    winner = None
    tickets_totales = 0
    for proceso in cola.queue:
        tickets_totales += proceso["tickets"]
    if tickets_totales > 0:
        num_loteria = random.randint(1, tickets_totales)
        for proceso in cola.queue:
            if num_loteria <= proceso["tickets"]:
                winner = proceso
                break
            num_loteria -= proceso["tickets"]
    
    if winner is None:
        continue


    # Ejecuta el proceso ganador por un quantum
    winner["duracion"] -= 1
    print(f"Tick {winner['id']}: Proceso {winner['id']} ejecutándose")


    # Si el proceso aún no ha terminado, volver a agregarlo a la cola de procesos
    if winner["duracion"] > 0:
        cola.put(winner)


print("Todos los procesos han terminado.")