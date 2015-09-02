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


class DosCuartos(entornos6cuartos.Entorno):

    def transicion(self, estado, accion):
        if not self.accion_legal(estado, accion):
            print "La accion no es legal para este estado"
            return estado
        
        robot, A, B, C, D, F, E = estado[0], estado[1], estado[2], estado[3], estado[4], estado[5], estado[6]
        #A =
        #B = estado[2]
        #C = estado[3]
        #D = estado[4]
        #E = estado[5]
        #F = estado[6]
        #print 'Robot: ',robot,'A:',A,'B:',B,'C:',C,'D:',D,'E:',E,'F:',F, 'Accion:', accion
        #return estado
        if accion == 'Derecha':
            if robot == 'A':
                return ('B', A, B, C, D, E, F)
            if robot == 'B':
                return ('C', A, B, C, D, E, F)
            if robot == 'D':
                return ('E', A, B, C, D, E, F)
            if robot == 'E':
                return ('F', A, B, C, D, E, F)
            else:
                return estado
        """
        En caso de la accion de la izquierda...
        (robot == 'C' or robot == 'B' or robot == 'F' or robot == 'E')
        """
        if accion == 'Izquierda':
            if robot == 'E':
                return ('D', A, B, C, D, E, F)
            if robot == 'F':
                return ('E', A, B, C, D, E, F)
            if robot == 'B':
                return ('A', A, B, C, D, E, F)
            if robot == 'C':
                return ('B', A, B, C, D, E, F)
            else: 
                return estado
        """
        En caso de la accion Subir..
        """
        if accion == 'Subir':
            if robot == 'C':
                return ('F', A, B, C, D, E, F)
            if robot == 'A':
                return ('D', A, B, C, D, E, F)
            else:
                return estado
        """
        En caso de la accion Bajar..
        """
        if accion == 'Bajar':
            if robot == 'D':
                return ('A', A, B, C, D, E, F)
            if robot == 'F':
                return ('C', A, B, C, D, E, F)
            else:
                return estado
        """
        En caso de la accion Limpiar
        """
        if accion == 'limpiar':
            if robot == 'A' and A == 'sucio':
                return ('A','limpio', B, C, D, E ,F)
            if robot =='B' and B == 'sUcio':
                return ('B', A, 'limpio', C, D, E, F)
            if robot == 'C' and C == 'sucio':
                return ('C', A, B, 'limpio', D, E ,F)
            if robot == 'D' and D == 'sucio':
                return ('D', A, B, C, 'limpio', E, F)
            if robot == 'E' and E == 'sucio':
                return ('E', A, B, C, D, 'limpio', F)
            if robot == 'F' and F == 'sucio':
                return ('F', A, B, C, D, E, 'limpio')
            else:
                return estado
        if accion == 'noOp':
            return estado


    def sensores(self, estado):

        robot = estado
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
        return accion in ('Derecha', 'Izquierda', 'limpiar', 'Subir','Bajar','noOp')

    def desempeno_local(self, estado, accion):
        robot, A, B,C,D,E,F = estado
        return 0 if accion == 'noOp' and A == B == C == D == E == F == 'limpio' else -1


class AgenteAleatorio(entornos6cuartos.Agente):
    """
    Un agente que solo regresa una accion al azar entre las acciones legales

    """
    def __init__(self, acciones):
        self.acciones = acciones

    def programa(self, percepcion):
        return choice(self.acciones)


class AgenteReactivoDoscuartos(entornos6cuartos.Agente):
    """
    Un agente reactivo simple

    """

    def programa(self, percepcion):
        robot = percepcion
        situacion = percepcion
       # print 'Percepcion: ', percepcion
      #  return 'noNe'

        if situacion == 'sucio':
            return 'limpiar'
        if robot == 'B' or robot == 'A' or robot == 'D' or robot == 'E':
            return 'Derecha'
        if robot == 'B' or robot == 'C' or robot == 'E' or robot == 'F':
            return 'Izquierda'
        if robot == 'A' or robot == 'C':
            return 'Subir'
        if robot == 'D' or robot == 'E':
            return 'Bajar'
        return 'noOp'

        """
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
        self.modelo[0] = robot
        self.modelo[self.lugar[robot]] = situacion

        # Decide sobre el modelo interno
        A, B ,C, D, E, F= self.modelo[1], self.modelo[2], self.modelo[3], self.modelo[4], self.modelo[5], self.modelo[6]
        return ('noOp' if A == B ==C == D ==E == F == 'limpio' else
                'limpiar' if situacion == 'sucio' else
                'Derecha' if robot == 'B' or robot == 'A' or robot == 'D' or robot == 'E' else
                'Izquierda' if robot == 'B' or robot == 'C' or robot == 'E' or robot == 'F' else
                'Subir' if robot =='A' or robot =='C' else
                'Bajar' if robot =='D' or robot =='F' else
                'noOp'
                )


def test():
  
    print "Prueba del entorno de dos cuartos con un agente aleatorio"
    """entornos6cuartos.simulador(DosCuartos(),
                       AgenteAleatorio(['Derecha', 'Izquierda', 'limpiar', 'Subir', 'Bajar', 'noOp']),
                               ['A', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio'],
                               10)"""
   
    print "Prueba del entorno de dos cuartos con un agente reactivo"
    entornos6cuartos.simulador(DosCuartos(),
                       AgenteReactivoDoscuartos(),
                               ('A', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio'),
                               100)
 

    print "Prueba del entorno de dos cuartos con un agente reactivo"
    """entornos6cuartos.simulador(DosCuartos(),
                       AgenteReactivoModeloDosCuartos(),
                               ('A', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio'),
                               10)
    """

if __name__ == '__main__':
    test()
