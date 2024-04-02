import math

from dataclasses import dataclass

@dataclass
class Render(object):
    ms_retraso:int


@dataclass
class Pantalla(object):
    anchura:int
    altura:int
    mitad_anchura:int
    mitad_altura:int
    @staticmethod
    def build_pantalla(anchura, altura):
        p=Pantalla(anchura, altura, int(anchura/2), int(altura/2))
        return p

@dataclass
class Raycasting(object):
    incr_angulo_en_raycasting:float
    precision_raycasting:int

@dataclass
class Jugador(object):
    x:int
    y:int
    angulo_jugador:int
    semi_fov:int
    fov:int
    

class Mapa(object):
    @staticmethod
    def get_mapa():
        mapa=[
            [1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,1,1,0,1,0,0,1],
            [1,0,0,1,0,0,1,0,0,1],
            [1,0,0,1,0,0,1,0,0,1],
            [1,0,0,1,0,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1],
        ]
        return mapa
    
def build_objetos(anchura=640, altura=480, fov=60, x0=5,y0=5,angulo_jugador=90,
                  precision_raycasting=64):
    pantalla=Pantalla.build_pantalla(anchura,altura)
    render=Render(30)
    raycasting=Raycasting(incr_angulo_en_raycasting=fov/anchura,precision_raycasting=precision_raycasting)
    semifov=fov/2
    jugador=Jugador(x0,y0,angulo_jugador,semifov,fov)
    mapa=Mapa.get_mapa()
    return (pantalla,render,raycasting,jugador,mapa)

def grados_a_radianes(grados):
    pi=math.pi
    return grados*pi/180
