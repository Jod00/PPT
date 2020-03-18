import sys, pygame
from pygame.locals import *
import time
from random import randint
from Clases import Oponente
from Clases import Jugador
#----variables-globales-----
alto=550
ancho=750
blanco=(230,230,230)
amarillo=(255,255,0)
rojo=(255,0,0)
tijera = pygame.image.load("Imagenes\scissor.png")
papel = pygame.image.load("Imagenes\paper-line.png")
piedra = pygame.image.load("Imagenes\piedra-de-grava-vexels.png")
#--------------Datos-de-ventana-mensajaes------------
pygame.init()
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Ventanita")
ventana.fill((0,180,30))

Fuente =pygame.font.SysFont("Arial",20)
Bienvenida= Fuente.render("Bienvenido a Piedra, Papel y Tijera",10,amarillo)
Indicaciones= Fuente.render("Elija una de las 3 Opciones:",0,blanco)

#-----Funciones-------------------
def Impresor():
     ventana.blit(Bienvenida,(20,25))
     ventana.blit(Indicaciones,(20,50))
     ventana.blit(piedra,(70,90))
     ventana.blit(papel,(180,90))
     ventana.blit(tijera,(320,90))
          
class Cursor(pygame.Rect):
     def __init__(self):
          pygame.Rect.__init__(self,0,0,1,1)
     def update(self):
          self.left,self.top= pygame.mouse.get_pos()
#==========================================
def PPTGame():
     #-----objetos---------------
     cursor= Cursor()
     jugador= Jugador(piedra,papel,tijera)
     oponente= Oponente(jugador)
     while True:          
          cursor.update() 
          for event in pygame.event.get():
               if event.type ==pygame.MOUSEBUTTONDOWN:
                    jugador.seleccion(cursor,ventana,oponente)
               if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
          Impresor()
          pygame.display.update()
PPTGame()
