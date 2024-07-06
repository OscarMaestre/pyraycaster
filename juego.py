import pygame,math
from pyraycastinglib import atributos

ANCHURA=640
ALTURA=480

#Globales
(PANTALLA,RENDER,RAYCASTING,JUGADOR,MAPA)=atributos.build_objetos(ANCHURA,ALTURA)
SCREEN = pygame.display.set_mode((ANCHURA,ALTURA))


def calcular_distancia_rayo(rayo):
    x=pow(JUGADOR.x-rayo.x,2)
    y=pow(JUGADOR.y-rayo.y,2)
    distancia=math.sqrt(x+y)
    return distancia

def hacer_raycasting():
    angulo_rayo=JUGADOR.angulo_jugador-JUGADOR.semi_fov
    #Trazamos los rayos para todo el ancho de la pantalla
    for num_rayo in range(0, ANCHURA):
        rayo=atributos.Rayo(JUGADOR.x, JUGADOR.y,angulo_rayo)
        
        muro=0
        while muro==0:
            rayo.avanzar_rayo()
            muro=MAPA[rayo.y_int][rayo.x_int]
        # print("Muro hallado"+str(num_rayo))
        distancia=calcular_distancia_rayo(rayo)
        #Corrección ojo de pez
        distancia=distancia*math.cos(atributos.grados_a_radianes(angulo_rayo-JUGADOR.angulo_jugador))
        altura_muro=math.floor(PANTALLA.mitad_altura/distancia)

        altura_linea_suelo=PANTALLA.mitad_altura-altura_muro
        altura_linea_muro=PANTALLA.mitad_altura+altura_muro

        pygame.draw.line(SCREEN,"blue",[num_rayo,0],[num_rayo,altura_linea_suelo],1)
        pygame.draw.line(SCREEN,"red",[num_rayo,altura_linea_suelo],[num_rayo,altura_linea_muro],1)
        
        pygame.draw.line(SCREEN,"green",[num_rayo,altura_linea_muro],[num_rayo,PANTALLA.altura],1)
        
        angulo_rayo=angulo_rayo+RAYCASTING.incr_angulo_en_raycasting
        #Fin del bucle



def jugar():
    
    
    pygame.init()
    
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        SCREEN.fill("black")
        hacer_raycasting()
        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()


        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            grados_jugador=atributos.grados_a_radianes(JUGADOR.angulo_jugador)
            player_cos=math.cos(grados_jugador)*0.5
            player_sin=math.sin(grados_jugador)*0.5
            nuevo_x=JUGADOR.x+player_cos
            nuevo_y=JUGADOR.y+player_sin
            if MAPA[math.floor(nuevo_y)][math.floor(nuevo_x)]==0:
                JUGADOR.x=nuevo_x
                JUGADOR.y=nuevo_y
        if keys[pygame.K_s]:
            grados_jugador=atributos.grados_a_radianes(JUGADOR.angulo_jugador)
            player_cos=math.cos(grados_jugador)*0.5
            player_sin=math.sin(grados_jugador)*0.5
            nuevo_x=JUGADOR.x-player_cos
            nuevo_y=JUGADOR.y-player_sin
            if MAPA[math.floor(nuevo_y)][math.floor(nuevo_x)]==0:
                JUGADOR.x=nuevo_x
                JUGADOR.y=nuevo_y
        if keys[pygame.K_a]:
            JUGADOR.angulo_jugador-=5
        if keys[pygame.K_d]:
            JUGADOR.angulo_jugador+=5
        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__=="__main__":
    jugar()