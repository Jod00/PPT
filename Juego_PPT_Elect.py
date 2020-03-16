import sys, pygame
from pygame.locals import *

#----variables-globales-----
blanco=(230,230,230)
amarillo=(255,255,0)
rojo=(255,0,0)
tijera = pygame.image.load("Imagenes\scissor.png")
papel = pygame.image.load("Imagenes\paper-line.png")
piedra = pygame.image.load("Imagenes\piedra-de-grava-vexels.png")
#--------------Datos-de-ventana-mensajaes------------
pygame.init()
#ventana.fill()
ventana = pygame.display.set_mode((750,550))
pygame.display.set_caption("Ventanita")

Fuente =pygame.font.SysFont("Arial",20)
Bienvenida= Fuente.render("Bienvenido a Piedra, Papel y Tijera",10,amarillo)
Indicaciones= Fuente.render("Elija una de las 3 Opciones:",0,blanco)
jugadorTxt= Fuente.render("Jugador:",0,blanco)
OponenteTxt= Fuente.render("Oponente:",0,blanco)
#-----Funciones-------------------
def Impresor():
     ventana.blit(Bienvenida,(20,25))
     ventana.blit(Indicaciones,(20,50))
     ventana.blit(piedra,(70,90))
     ventana.blit(papel,(180,90))
     ventana.blit(tijera,(320,90))
     
     #ventana.blit(jugadorTxt,(20,265))
     #ventana.blit(OponenteTxt,(320,265))
class oponente(pygame.sprite.Sprite):
     def __init__(self):
          print "hi"

class Jugador(pygame.sprite.Sprite):
     def __init__(self):
          
          pass
#==========================================
def PPTGame():
     
     while True:
          mouse= pygame.mouse.get_pos()
          # posibles entradas del teclado
          for event in pygame.event.get():
               if event.type ==pygame.MOUSEBUTTONDOWN:
                    print "clic"
                         
               if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
          
          Impresor()
          pygame.display.update()
PPTGame()
