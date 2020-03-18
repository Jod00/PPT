import pygame
import Oponente
class Jugador(pygame.sprite.Sprite):
     def __init__(self,piedra,papel,tijera,x=70,y=90):
          self.piedraA =piedra
          self.papelA=papel
          self.tijeraA=tijera

          self.fin= True
          
          self.blanco=(230,230,230)
          self.Fuente =pygame.font.SysFont("Arial",20)
          
          self.jugadorTxt= self.Fuente.render("Jugador:",0,self.blanco)
          self.OponenteTxt= self.Fuente.render("Oponente:",0,self.blanco)
          self.Gano= self.Fuente.render("Felicidades Has Ganado!!!",14,(255,255,0))
          self.Perdio= self.Fuente.render("Lo siento Has Perdido :(",14,(255,255,0))
          self.Empato= self.Fuente.render("Empate",14,(255,255,0))
          
          self.FondoMensaje = pygame.Rect(200,200,300,45)
          
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
               oponente.Elecciones(1,ventana)
               
          elif cursor.colliderect(self.rectp):
               ventana.blit(self.jugadorTxt,(20,260))
               ventana.blit(self.OponenteTxt,(320,260))
               ventana.blit(self.papelA,(20,300))
               oponente.Dibujar(ventana,self.papelA,self.piedraA,self.tijeraA)
               oponente.Elecciones(2,ventana)
               
          elif cursor.colliderect(self.rectt):
               ventana.blit(self.jugadorTxt,(20,260))
               ventana.blit(self.OponenteTxt,(320,260))
               ventana.blit(self.tijeraA,(20,300))
               oponente.Dibujar(ventana,self.papelA,self.piedraA,self.tijeraA)
               oponente.Elecciones(3,ventana)

     def ganador(self,Eleccion,eleccionOponente,ventana):
          
          if (Eleccion==1 and eleccionOponente==2):
               pygame.draw.rect(ventana,(0,0,0),self.FondoMensaje)
               ventana.blit(self.Perdio,(210,200))
               self.fin = False
          
          elif(Eleccion==2 and eleccionOponente==3):
               pygame.draw.rect(ventana,(0,0,0),self.FondoMensaje)
               ventana.blit(self.Perdio,(210,200))
               self.fin = False
               
          elif(Eleccion==1 and eleccionOponente==3):
               pygame.draw.rect(ventana,(0,0,0),self.FondoMensaje)
               ventana.blit(self.Gano,(210,200))
               self.fin = False
          
          elif(Eleccion==2 and eleccionOponente==1):
               pygame.draw.rect(ventana,(0,0,0),self.FondoMensaje)
               ventana.blit(self.Gano,(210,200))
               self.fin = False
               
          elif(Eleccion==3 and eleccionOponente==1):
               pygame.draw.rect(ventana,(0,0,0),self.FondoMensaje)
               ventana.blit(self.Perdio,(210,200))
               self.fin = False
          
          elif(Eleccion==3 and eleccionOponente==2):
               pygame.draw.rect(ventana,(0,0,0),self.FondoMensaje)
               ventana.blit(self.Gano,(210,200))
               self.fin = False
               
          elif(Eleccion==eleccionOponente):
               pygame.draw.rect(ventana,(0,0,0),self.FondoMensaje)
               ventana.blit(self.Empato,(210,200))
               self.fin = False
               

               

          
     
          
          
          
