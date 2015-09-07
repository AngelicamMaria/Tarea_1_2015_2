"""
doscuartos.py.py
------------

Ejemplo de un entorno muy simple y agentes idem

"""

__author__ = 'juliowaissman'
"""
Modificado para 6 cuartos en 2 pisos.
By: Angelica
"""

import entornos6cuartos
from random import choice
import random


class DosCuartos(entornos6cuartos.Entorno):

    def transicion(self, estado, accion):
        if not self.accion_legal(estado, accion):
            print "La accion no es legal para este estado"
            return estado
        
        robot, A, B, C, D, F, E = estado[0], estado[1], estado[2], estado[3], estado[4], estado[5], estado[6]
        """
        Las reglas en caso de derecha o izquierda. Sabiendo la accion. Son reglas de los 6 cuartos
        """

        #em caso que todo este limpio.. se queda.
        if A == B == C == D == E == F== 'limpio':
            return (robot, A, B, C, D, E, F)

        if accion == 'Derecha':
            if robot == 'A' and A == 'limpio':
                return ('B', A, B, C, D, E, F)
            if robot == 'B' and B == 'limpio':
                return ('C', A, B, C, D, E, F)
            if robot == 'D' and D == 'limpio':
                return ('E', A, B, C, D, E, F)
            if robot == 'E' and E == 'limpio':
                return ('F', A, B, C, D, E, F)
            else:
                return (robot, A, B, C, D, E, F)
        """
        En caso de la accion de la izquierda...
        """
        if accion == 'Izquierda':
            if robot == 'E' and E == 'limpio':
                return ('D', A, B, C, D, E, F)
            if robot == 'F' and F == 'limpio':
                return ('E', A, B, C, D, E, F)
            if robot == 'B' and B == 'limpio':
                return ('A', A, B, C, D, E, F)
            if robot == 'C' and C == 'limpio':
                return ('B', A, B, C, D, E, F)
            else:
                return (robot, A, B, C, D, E, F)
        """
        En caso de la accion Subir..
        """
        if accion == 'Subir':
            if robot == 'C' and C == 'limpio':
                return ('F', A, B, C, D, E, F)
            if robot == 'A' and A == 'limpio':
                return ('D', A, B, C, D, E, F)
            else:
                return (robot, A, B, C, D, E, F)
          
        """
        En caso de la accion Bajar..
        """
        if accion == 'Bajar':
            if robot == 'D' and D == 'limpio':
                return ('A', A, B, C, D, E, F)
            if robot == 'F' and F == 'limpio':
                return ('C', A, B, C, D, E, F)
            else:
                return (robot, A, B, C, D, E, F)
        """
        En caso de la accion Limpiar
        """
        if accion == 'limpiar':
            if robot == 'A' and A == 'sucio':
                return (robot,'limpio', B, C, D, E ,F)
            if robot =='B' and B == 'sucio':
                return (robot, A, 'limpio', C, D, E, F)
            if robot == 'C' and C == 'sucio':
                return (robot, A, B, 'limpio', D, E ,F)
            if robot == 'D' and D == 'sucio':
                return (robot, A, B, C, 'limpio', E, F)
            if robot == 'E' and E == 'sucio':
                return (robot, A, B, C, D, 'limpio', F)
            if robot == 'F' and F == 'sucio':
                return (robot, A, B, C, D, E, 'limpio')
            else:
                return (robot, A, B, C, D, E, F)
        if accion == 'noOp':
            return (robot, A, B, C, D, E, F)
        

    def sensores(self, estado):

        robot, A, B, C, D, E, F = estado
        """
        robot, A, B, C, D, E, F = estado"""

        if robot == 'A':
            return robot, A
        if robot == 'B':
            return robot, B
        if robot == 'C':
            return robot, C
        if robot == 'D':
            return robot, D
        if robot == 'E':
            return robot, E
        if robot == 'F':
            return robot, F


        """return robot, A if robot == 'A' else B"""

    def accion_legal(self, estado, accion):
        robot = estado[0]
        #print estado , '........', accion

        #dependiando del lugar las acciones se reducen. Si el robot sabe en que cuarto esta, las acciones que este puede realisar serian limitadas. 
        #dependeran del cuarto.  Mayor probabilidades de terminar.
        
        return accion in ('limpiar','Derecha', 'Subir', 'Bajar', 'Izquierda', 'noOp')
         

    def desempeno_local(self, estado, accion):
        robot, A, B,C,D,E,F = estado
        #primero se revisa si todos los cuartos estan limpios
        if A == B == C == D == E == F == 'limpio':
            return 0
        #Se revisa si laaccion  es nada
        if accion == 'noOp':
            return 0
        #despues, se dice si es subir o bajar son mas costosas que ir de derecha o izquierda.
        if accion == 'Subir' or accion == 'Bajar':
            return 2
        if accion == 'Derecha'  or accion == 'Izquierda' or accion == 'limpiar':
            return 1

            
        #return 0 if accion == 'noOp' and A == B == C == D == E == F == 'limpio' else -1


class AgenteAleatorio(entornos6cuartos.Agente):
    """
    Un agente que solo regresa una accion al azar entre las acciones legales

    """
    def __init__(self, acciones):
        self.acciones = acciones

    def programa(self, percepcion):
        #print 'Percepcion: ', percepcion, '\t AgenteAleatorio'
        return choice(self.acciones)


class AgenteReactivoDoscuartos(entornos6cuartos.Agente):
    """
    Un agente reactivo simple

    """

    def programa(self, percepcion):

        robot = percepcion[0]
        situacion = percepcion[1]
        # print 'Percepcion: ', situacion,'Robot: ',robot, '\t AgenteReactivoDosCuartos'
        #return 'noNe'
        a = random.random()*10
        #print a 
        #return 'noOp'
        #print 'Robot', robot, 'situacion: ', situacion
        if situacion == 'sucio':
            return 'limpiar'
        
        if robot == 'B' or robot == 'E':
            if a <5.0:
                return 'Derecha'
            else:
                return 'Izquierda'
         
        if robot == 'A' or robot == 'D':
            if a <5.0:
                return 'Derecha'
            else:
                if robot == 'D':
                    return 'Bajar'
                else:
                    return 'Subir'
        if robot == 'C' or robot =='F':
            if a <5.0:
                return 'Izquierda'
            else:
                if robot == 'F':
                    return 'Bajar'
                else:
                    return 'Subir'

                       
        """
        if robot == 'B' or robot == 'C' or robot == 'E' or robot == 'F':
            return 'Izquierda'
        if robot == 'A' or robot == 'C':
            return 'Subir'
        if robot == 'D' or robot == 'E':
            return 'Bajar'
        if A == B == C == D == F == E == 'limpio':
            return 'noOp'
        
        Original
         return ('limpiar' if situacion == 'sucio' else
                'irA' if robot == 'B' else
                'irB)
        """

class AgenteReactivoModeloDosCuartos(entornos6cuartos.Agente):
    """
    Un agente reactivo basado en modelo

    """
    def __init__(self):
        """
        Inicializa el modelo interno en el peor de los casos

        """
        self.modelo = ['A', "sucio", 'sucio', 'sucio', 'sucio', 'sucio', 'sucio']
        self.lugar = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}

    def programa(self, percepcion):
        robot, situacion = percepcion
        # Actualiza el modelo interno
        #robot = self.modelo[0]
        #print 'Percepcion: ', percepcion, '\t AgenteReactivoModeloDosCuartos'
        self.modelo[self.lugar[robot]] = situacion

        # Decide sobre el modelo interno
        A, B ,C, D, E, F= self.modelo[1], self.modelo[2], self.modelo[3], self.modelo[4], self.modelo[5], self.modelo[6]
        #print A, B, C, D, E, F
        """return ('noOp' if A == B ==C == D ==E == F == 'limpio' else
                'limpiar' if situacion == 'sucio' else
                'Derecha' if robot == 'B' or robot == 'A' or robot == 'D' or robot == 'E' else
                'Izquierda' if robot == 'B' or robot == 'C' or robot == 'E' or robot == 'F' else
                'Subir' if robot =='A' or robot =='C' else
                'Bajar' if robot =='D' or robot =='F' else 'noOp'
                )
        """
        a = random.random()*10
        #print a 
        #return 'noOp'
        #print 'Robot', robot, 'situacion: ', situacion

        if A == B ==C == D ==E == F == 'limpio':
            #print 'Robot', robot, 'situacion: ', situacion, 'regresa: ', 'noOp'
            return 'noOp'
        if A == 'sucio' and robot == 'A':
            #print 'Robot', robot, 'situacion: ', situacion, 'regresa: ', 'limpiar'
            return 'limpiar'
        if B == 'sucio' and robot == 'B':
            #print 'Robot', robot, 'situacion: ', situacion, 'regresa: ', 'limpiar'
            return 'limpiar'
        if C == 'sucio' and robot == 'C':
            #print 'Robot', robot, 'situacion: ', situacion, 'regresa: ', 'limpiar'
            return 'limpiar'
        if D == 'sucio' and robot == 'D':
            #print 'Robot', robot, 'situacion: ', situacion, 'regresa: ', 'limpiar'
            return 'limpiar'
        if E == 'sucio' and robot == 'E':
            #print 'Robot', robot, 'situacion: ', situacion, 'regresa: ', 'limpiar'
            return 'limpiar'
        if F == 'sucio' and robot == 'F':
            #print 'Robot', robot, 'situacion: ', situacion, 'regresa: ', 'limpiar'
            return 'limpiar'
        if situacion == 'sucio':
            #print 'Robot', robot, 'situacion: ', situacion, 'regresa: ', 'limpiar'
            return 'limpiar'
        
        if robot == 'B' or robot == 'E':
            if a <5.0:
                #print 'Robot', robot, 'situacion: ', situacion, 'regresa: Derecha'
                return 'Derecha'
            else:
                #print 'Robot', robot, 'situacion: ', situacion, 'regresa: Izquierda'
                return 'Izquierda'
         
        if robot == 'A' or robot == 'D':
            if a <5.0:
                #print 'Robot', robot, 'situacion: ', situacion, 'regresa: Derecha'
                return 'Derecha'
            else:
                if robot == 'D':
                    #print 'Robot', robot, 'situacion: ', situacion, 'regresa: Bajar'
                    return 'Bajar'
                else:
                    #print 'Robot', robot, 'situacion: ', situacion, 'regresa: Subir'
                    return 'Subir'
        if robot == 'C' or robot =='F':
            if a <5.0:
                #print 'Robot', robot, 'situacion: ', situacion, 'regresa: Derecha'
                return 'Izquierda'
            else:
                if robot == 'F':
                    #print 'Robot', robot, 'situacion: ', situacion, 'regresa: "Bajar"'
                    return 'Bajar'
                else:
                    #print 'Robot', robot, 'situacion: ', situacion, 'regresa: Su'
                    return 'Subir'

def test():
  
    print "Prueba del entorno de dos cuartos con un agente aleatorio"
    entornos6cuartos.simulador(DosCuartos(),
                       AgenteAleatorio(['Derecha', 'Izquierda', 'limpiar', 'Subir', 'Bajar', 'noOp']),
                               ['A', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio'],
                               100)
   
    print "Prueba del entorno de dos cuartos con un agente reactivo"
    entornos6cuartos.simulador(DosCuartos(),
                       AgenteReactivoDoscuartos(),
                               ('A', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio'),
                               100)
    
    print "Prueba del entorno de dos cuartos con un agente reactivo"
    entornos6cuartos.simulador(DosCuartos(),
                       AgenteReactivoModeloDosCuartos(),
                               ('A', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio'),
                               100)
    

if __name__ == '__main__':
    test()
