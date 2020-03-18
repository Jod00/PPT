import sys, pygame
from pygame.locals import *
from random import randint

class Oponente(pygame.sprite.Sprite):
     def __init__(self,jugador):
          self.EleccionOponente= randint(1,3)
          self.Player = jugador
     def Dibujar(self,superficie,papel,piedra,tijera):
          if(self.EleccionOponente==1):
               superficie.blit(piedra,(320,290))
               
          
          elif(self.EleccionOponente==2):
               superficie.blit(papel,(320,290))
               
          else:
               superficie.blit(tijera,(320,290))

     def Elecciones(self,Eleccion,ventana):
          self.JugadorMano = Eleccion
          self.Player.ganador(self.JugadorMano,self.EleccionOponente,ventana)
               
