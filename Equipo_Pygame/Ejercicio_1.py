# Antonio Ramos Gonzalez
# Matricula:372576
# 25/05/2024
# Expo Juegos: Ejercicio 1 
import pgzrun 

WIDTH = 800
HEIGHT = 600

car = Actor('carro1') 
car.pos = 50, HEIGHT // 2
goal_x = 750

def Draw():
    screen.clear()
    screen.blit('DIBUJAR FONDO', (0, 0))
    car.draw()
    screen.draw.line((goal_x, 0), (goal_x, HEIGHT), 'white')

def MouseDown(pos):
    if car.x < goal_x:
        car.x += 35
    if car.x >= goal_x:
        print("GANASTE")
        exit()

pgzrun.go()