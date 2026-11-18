
import sys
import bpy, math 

COLORES = [
    (0.20, 0.45, 0.80, 1),   # blue
    (0.30, 0.75, 0.65, 1),   # teal
    (0.95, 0.80, 0.25, 1),   # yellow
    (0.90, 0.50, 0.15, 1),   # orange
    (0.85, 0.25, 0.25, 1),   # red
    (0.55, 0.30, 0.70, 1),   # purple
]


RUTA_SRC = r"C:\Users\Domenica Palomino\OneDrive\Ciclo 2026 - II\Algoritmos y estructura de Datos\proyecto_final\src"

if RUTA_SRC not in sys.path:
    sys.path.append(RUTA_SRC)

from algoritmos.ejecutar import ejecutar 
from algoritmos.hanoi_recursivo import hanoi 

def crear_material(nombre, color):
    mat = bpy.data.materials.new(name=nombre)      
    mat.diffuse_color = color                       
    mat.use_nodes = True
    mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = color   # 2b. color in the render
    return mat

def crear_discos(n):
    discos = {}

    for k in range(1,n+1):
        bpy.ops.mesh.primitive_cylinder_add(radius=0.3+0.2*k, depth=0.25, location=(0,0,(n-k)*0.25 + 0.125))
        discos[k] = bpy.context.object 
        mat  = crear_material(f"color_disco_{k}", COLORES[(k-1) % len(COLORES)]) 
        discos[k].data.materials.append(mat)

    return discos 
def animar(discos, pasos): 
    frame = 1 
    altura_vuelo = 2.5 
    for p in pasos: 
        disco = discos[p["disco"]]

        disco.keyframe_insert("location", frame = frame)

        frame = frame + 8

        disco.location.z = altura_vuelo 

        disco.keyframe_insert("location", frame = frame) 

        frame = frame + 8

        x = p["destino"] * 3 

        disco.location.x = x 

        disco.keyframe_insert("location", frame = frame)

        frame = frame + 8 

        abajo = len(p["torres"][p["destino"]]) - 1 
        
        z = abajo*0.25 + 0.125 

        disco.location.z = z 

        disco.keyframe_insert("location", frame = frame)

    bpy.context.scene.frame_end = frame 



def crear_escenario():
    for i in range(3):
        bpy.ops.mesh.primitive_cylinder_add(radius = 0.1, depth = 2, location=(3*i,0,1))
        
    bpy.ops.mesh.primitive_cube_add(size=1, location=(3,0,-0.1))
    bpy.context.object.scale = (8,2,0.2)


def texto_torres(torres): 

    return "A " + str(torres[0]) + "  B " + str(torres[1]) + "  C " + str(torres[2])  


def crear_texto(contenido):
    bpy.ops.object.text_add(location=(3, 0, 3.5))     
    texto = bpy.context.object
    texto.data.body = contenido                         
    texto.data.size = 0.4                             
    texto.data.align_x = 'CENTER'                      
    texto.rotation_euler = (math.radians(90), 0, 0)     
    return texto


def visible(obj, mostrar, frame): 
    obj.hide_viewport = not mostrar
    obj.hide_render = not mostrar
    obj.keyframe_insert("hide_viewport", frame=frame)
    obj.keyframe_insert("hide_render", frame=frame)    

def mostrar_textos(textos): 

    for j in range(len(textos)): 
        texto = textos[j]
        inicio = 1 + j*24 
        fin = inicio + 24

        visible(texto, False, 0)
        visible(texto, True, inicio)

        if j<len(textos)-1: 
            visible(texto, False, fin)

def crear_camara_y_luz():
   
    bpy.ops.object.camera_add(location=(3, -14, 4),
                              rotation=(math.radians(80), 0, 0))
    bpy.context.scene.camera = bpy.context.object    


    bpy.ops.object.light_add(type='SUN', location=(0, 0, 10),
                             rotation=(math.radians(40), 0, math.radians(30)))
    bpy.context.object.data.energy = 3              


if __name__ == "__main__":
    N = 5  # número de discos

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    crear_escenario()
    crear_camara_y_luz()
    discos = crear_discos(N)
    movs =[]
    hanoi(N,0,2,1, movs)
    pasos = ejecutar(N, movs)
    animar(discos,pasos)
    textos = []
    inicial = [list(range(N,0, -1)), [],[]]
    textos.append(crear_texto(texto_torres(inicial)))
    for p in pasos: 
        textos.append(crear_texto(texto_torres(p["torres"])))
    mostrar_textos(textos)
    bpy.context.scene.frame_end += 48