# Antonio Ramos Gonzalez
# Matricula:372576
# 25/05/2024
# Expo Juegos: Ejercicio 1 
import pgzrun

WIDTH = 800
HEIGHT = 600

Car1 = Actor('carro1')
Car1.pos = 50, HEIGHT // 3

Car2 = Actor('carro2')
Car2.pos = 50, 2 * HEIGHT // 3

Meta = 750

Ganador = None

def Draw():
    screen.clear()
    screen.blit('DIBUJAR FONDO', (0, 0))
    Car1.draw()
    Car2.draw()
    screen.draw.line((Meta, 0), (Meta, HEIGHT), 'white')
    if Ganador:
        screen.draw.text(Ganador, center=(WIDTH//2, HEIGHT//2), fontsize=50, color='white')

def KeyDown(key):
    global Ganador
    if Ganador is None and key == keys.UP:
        Car1.x += 35
        check_Ganador()

def MouseDown(pos):
    global Ganador
    if Ganador is None:
        Car2.x += 35
        check_Ganador()

def Ganador():
    global Ganador
    if Car1.x >= Meta:
        Ganador = "HA GANADO EL CARRO 1"
    elif Car2.x >= Meta:
        Ganador = "HA GANADO EL CARRO 2"
    
    if Ganador:
        print(Ganador)
        exit()

pgzrun.go()