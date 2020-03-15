import sys, pygame
from pygame.locals import *
#----variables-globales-----
blanco=(230,230,230)

#----------------------------
pygame.init()
ventana = pygame.display.set_mode((450,450))
pygame.display.set_caption("Ventanita")


Fuente =pygame.font.SysFont("console",20)
Bienvenida= Fuente.render("Bienvenido a Piedra, Papel y Tijera",10,blanco)
Indicaciones= Fuente.render("Elija una de las 3 Opciones",0,blanco)


#==========================================
while True:
     # posibles entradas del teclado
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit()
               sys.exit()
     ventana.blit(Bienvenida,(20,25))
     ventana.blit(Indicaciones,(20,50))
     pygame.display.update()
