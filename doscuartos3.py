#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doscuartos.py.py
------------

Ejemplo de un entorno muy simple y agentes idem

"""

__author__ = 'juliowaissman'

import entornos3
from random import choice
import random


class DosCuartos(entornos3.Entorno):
    """
    Todo lo que envie.. supongo qeu se perdio...
    Clase para un entorno de dos cuartos. Muy sencilla solo regrupa métodos.

    El estado se define como 
                (robot, A, B)
    donde robot puede tener los valores "A", "B"
    A y B pueden tener los valores "limpio", "sucio"

    Las acciones válidas en el entorno son 
            "irA", "irB", "limpiar" y "noOp".
    Todas las acciones son válidas en todos los estados.

    Los sensores es una tupla 
                (robot, limpio?) 
    con la ubicación del robot y el estado de limieza

    """

    def transicion(self, estado, accion):
        if not self.accion_legal(estado, accion):
            raise ValueError("La accion no es legal para este estado")

        robot, A, B = estado

        return (('A', A, B) if accion == 'irA' else
                ('B', A, B) if accion == 'irB' else
                (robot, A, B) if accion == 'noOp' else
                ('A', 'limpio', B) if accion == 'limpiar' and robot == 'A' else
                ('B', A, 'limpio'))

    def sensores(self, estado):
        robot, A, B = estado
        if robot == 'A':
            return robot, A
        else: 
            return robot, B
        #return robot, A if robot == 'A' else B

    def accion_legal(self, estado, accion):
        return accion in ('irA', 'irB', 'limpiar', 'noOp')

    def desempeno_local(self, estado, accion):
        robot, A, B = estado
        return 0 if accion == 'noOp' and A == B == 'limpio' else -1


class AgenteAleatorio(entornos3.Agente):
    """
    Un agente que solo regresa una accion al azar entre las acciones legales

    """
    def __init__(self, acciones):
        self.acciones = acciones

    def programa(self, percepcion):
        return choice(self.acciones)


class AgenteReactivoDoscuartos(entornos3.Agente):
    """
    Un agente reactivo simple

    """

    def programa(self, percepcion):
        robot, situacion = percepcion[0], percepcion[1]
        #print 'Robot: ', percepcion
        a = random.random()*1
        """
        Sabe en que cuarto esta... pero no sabe si esta limpio o sucio. Asi que hice esto para que si no elije limpiar, se va al otro cuarto. 
        """
        if robot == 'A':
            if  0.0 < a < .5:
                return 'limpiar'
            else:
                return 'irB'
        else: #en caso que est[e en un cuarto, pero no puede saber si esta suicio o limpio. 
            if  0.0 < a < .5:
                return 'limpiar'
            else:
                return 'irB'
        
        """
        return ('limpiar' if situacion == 'sucio' else
                'irA' if robot == 'B' else
                'irB')
        """

class AgenteReactivoModeloDosCuartos(entornos3.Agente):
    """
    Un agente reactivo basado en modelo

    """
    def __init__(self):
        """
        Inicializa el modelo interno en el peor de los casos

        """
        self.modelo = ['A', 'sucio', 'sucio']
        self.lugar = {'A': 1, 'B': 2}

    def programa(self, percepcion):
        robot, situacion = percepcion

        # Actualiza el modelo interno
        self.modelo[0] = robot
        self.modelo[self.lugar[robot]] = situacion

        # Decide sobre el modelo interno
        A, B = self.modelo[1], self.modelo[2]
        return ('noOp' if A == B == 'limpio' else
                'limpiar' if situacion == 'sucio' else
                'irA' if robot == 'B' else
                'irB')


def test():
    """
    Prueba del entorno y los agentes

    """
    print "Prueba del entorno de dos cuartos con un agente aleatorio"
    entornos3.simulador(DosCuartos(),
                       AgenteAleatorio(['irA', 'irB', 'limpiar', 'noOp']),
                       ('A', 'sucio', 'sucio'), 100)

    print "Prueba del entorno de dos cuartos con un agente reactivo" 
    #Este es el que se modifica para ser modificado...
    entornos3.simulador(DosCuartos(),
                       AgenteReactivoDoscuartos(),
                       ('A', 'sucio', 'sucio'), 100)

    """print "Prueba del entorno de dos cuartos con un agente reactivo"
    entornos3.simulador(DosCuartos(),
                       AgenteReactivoModeloDosCuartos(),
                       ('A', 'sucio', 'sucio'), 100)
    """
if __name__ == '__main__':
    test()
"""
Como se ve el ajente racional,es mejor que el aleatorio. Ya que tiene menos pasos. 
"""