from pygame import *
import pygame

import sys


#FUNCION PARA CREAR BOTONES
def print_botones(screen, boton, mensaje):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(screen,(237,128,19),boton,0)
    else:
    #Elaoracion de Botones 
        draw.rect(screen,(44,84,30),boton,0)
    btnTxt=btnStart.render(mensaje,True,(220,220,220))
    screen.blit(btnTxt,(boton.x+(boton.width-btnTxt.get_width())/2,
                        boton.y+(boton.height-btnTxt.get_height())/2))#Ubicar valores de boton


pygame.init()

ancho=1000
alto=550
screen = pygame.display.set_mode((ancho,alto))

fondo=image.load('fondo.png')#cargar imagen
fondo=transform.scale(fondo,(1000,500))#Modificar imagen a la pantalla


#insertar carro
fondo1=image.load('auto2.png')
fondo1=transform.scale(fondo1,(100,100))

#insertar baches
baches=image.load('baches.png')
baches=transform.scale(baches,(90,90))

Texto=font.SysFont('Calibri',40)#tipografia para el texto en el sistema

btnStart=font.SysFont('Calibri',30)#tipografia de botonIniciar


x2,y2=10,300#imagen

x3,y3=20,40#baches


aceptar = Rect(50,500,200,50)
obstaculos = Rect(750,500,200,50)
while True:
    
    screen.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT: sys.exit()

        ## BOTONES AL DAR CLICK
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            if aceptar.collidedict(print_botones.__dir__):
                x2 += 1
                if x2 > ancho:
                        x2=0
            #if aceptar.collidepoint(mouse.get_pos()) :
                
                #print("Click Inicio")##PONER ACCIONES QUE REALIZA AL DAR CLICK
                
                
            if obstaculos.collidepoint(mouse.get_pos()):
                print("Click Obstaculos")

    

    #LLAMADO A LAS FUNCIONES
    print_botones(screen,aceptar,"INICIAR")
    print_botones(screen,obstaculos,"OBSTACULOS")
 
    ##imagenes en movimeinto
    
    
    if key.get_pressed()[K_s]:
        y2 +=1
    if key.get_pressed()[K_w]:
        y2 -=1
    
    ##fin de movimeinto

    screen.blit(fondo,(0,0))#se pone en la pantalla
    
    texto=Texto.render('UNIVERSIDAD TECNICA DE COTOPAXI',True,(50,70,80))#Poner texto en la pantalla principal
    screen.blit(texto,(250,0))#Posicionamiento del texto

    #insertacion de carrito
    screen.blit(fondo1,(x2,y2)) 
    pygame.time.delay(5)

    #insertacion de baches
    screen.blit(baches,(x3,y3))
    
    
    
    display.flip()
