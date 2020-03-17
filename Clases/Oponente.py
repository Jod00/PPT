import sys, pygame
from pygame.locals import *
from random import randint

class Oponente(pygame.sprite.Sprite):
     def __init__(self):
          self.EleccionOponente= randint(1,3)

     def Dibujar(self,superficie,papel,piedra,tijera):
          if(self.EleccionOponente==1):
               superficie.blit(piedra,(320,290))
          elif(self.EleccionOponente==2):
               superficie.blit(papel,(320,290))
          else:
               superficie.blit(tijera,(320,290))
          
