import random 

class Jugador:
    nombre = ' '
    intentos = ' '
    tipo = ' '
    def __init__(self,nombre, tipo):
        self.nombre = nombre
        self.intentos = 0
        self.tipo = tipo

nombre = input("Binvenido, introduce tu nombre: ")
jugador = Jugador(nombre, "humano")
seguir_jugando = "si"
turno = 1
maquina = Jugador("ia","maquina")

while seguir_jugando == "si":
    jugador.intentos = 0
    maquina.intentos = 0
    if turno == 0:
        print("Empiezas adivinando {}, di un numero cualquiera".format(jugador.nombre))
        n=random.randrange(0,100)
        a = n + 1
        while a != n :
            a = int( input())
            jugador.intentos+=1
            if a < n :
                print("mas alto")
            elif a > n:
                print("mas bajo")
            else :
                print("Has ganado!!!! Y solo te ha costado {} intentos.". format(jugador.intentos))
    if turno == 1:
        print("Es mi turno de adivinar un numero ")
        respuesta = "no"
        inferior = 0
        superior = 100
        while respuesta != "si":
            n=random.randrange(inferior,superior)
            respuesta = input("El numero en el que estas pensando es el {} (mayor/menor/si): ".format(n))
            maquina.intentos+=1
            if respuesta == "mayor":
                inferior = n
            elif respuesta == "menor":
                superior = n
            elif respuesta == "si":
                print("Siiiii!!!!! He ganado, y solo me ha costado {} intentos ", format(maquina.intentos))
            else:
                print("No he entendido tu respuesta (este no cuenta como intento)")
                maquina.intentos-=1
            if inferior == superior:
                respuesta = input("YA SE!!! El numero en el que estabas pensando era el {} a que si (si/no)? ".format(n))
                if respuesta == "no":
                    print("No estaras haciendo trampas?")
                    inferior=0
                    superior=100
                else:
                    print("Siiiii!!!!! He ganado, y solo me ha costado {} intentos ", format(maquina.intentos))
    if turno == 0:
        turno = 1
    else:
        turno = 0
    
    seguir_jugando = input("Quieres seguir jugando (si/no): ")
print("Gracias por jugar!!!")
