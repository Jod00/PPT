import pygame

class Jugador(pygame.sprite.Sprite):
     def __init__(self,piedra,papel,tijera,x=70,y=90):
          self.piedraA =piedra
          self.papelA=papel
          self.tijeraA=tijera
          self.blanco=(230,230,230)
          self.Fuente =pygame.font.SysFont("Arial",20)
          self.jugadorTxt= self.Fuente.render("Jugador:",0,self.blanco)
          self.OponenteTxt= self.Fuente.render("Oponente:",0,self.blanco)

          self.rectpi =self.piedraA.get_rect()
          self.rectp =self.papelA.get_rect()
          self.rectt =self.tijeraA.get_rect()
          
          self.rectpi.left,self.rectpi.top =(x,y)
          self.rectp.left,self.rectp.top =(180,y)
          self.rectt.left,self.rectt.top =(320,y)
          
     def seleccion(self,cursor,ventana,oponente):
          
          if cursor.colliderect(self.rectpi):
               ventana.blit(self.jugadorTxt,(20,260))
               ventana.blit(self.OponenteTxt,(320,260))
               ventana.blit(self.piedraA,(20,300))
               oponente.Dibujar(ventana,self.papelA,self.piedraA,self.tijeraA)
               
          elif cursor.colliderect(self.rectp):
               ventana.blit(self.jugadorTxt,(20,260))
               ventana.blit(self.OponenteTxt,(320,260))
               ventana.blit(self.papelA,(20,300))
               oponente.Dibujar(ventana,self.papelA,self.piedraA,self.tijeraA)
               
          elif cursor.colliderect(self.rectt):
               ventana.blit(self.jugadorTxt,(20,260))
               ventana.blit(self.OponenteTxt,(320,260))
               ventana.blit(self.tijeraA,(20,300))
               oponente.Dibujar(ventana,self.papelA,self.piedraA,self.tijeraA)
