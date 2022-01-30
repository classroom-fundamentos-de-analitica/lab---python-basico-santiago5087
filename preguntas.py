"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

from calendar import month
import csv
from pickle import FALSE

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    with open('data.csv', newline='') as csvfile:
        dataCSVFile = csv.reader(csvfile, delimiter='	')
        totalSum = 0
        for row in dataCSVFile:
            totalSum += int(row[1])
        return totalSum

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open('data.csv', newline='') as csvfile:
        dataCSVFile = csv.reader(csvfile, delimiter='	')
        letters = [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0]]
        lettersTupple = []
        for row in dataCSVFile:
            for letter in letters:
                if (letter[0] == row[0]):
                    letter[1] += 1
        for itemLetter in letters:
            lettersTupple.append((itemLetter[0], itemLetter[1]))
        return lettersTupple


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open('data.csv', newline='') as csvfile:
        dataCSVFile = csv.reader(csvfile, delimiter='	')
        letters = [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0]]
        lettersTupple = []
        for row in dataCSVFile:
            for letter in letters:
                if (letter[0] == row[0]):
                    letter[1] += int(row[1])
        for itemLetter in letters:
            lettersTupple.append((itemLetter[0], itemLetter[1]))
        print(lettersTupple)
        return lettersTupple

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open('data.csv', newline='') as csvfile:
        dataCSVFile = csv.reader(csvfile, delimiter='	')
        months = [["01", 0], ["02", 0], ["03", 0], ["04", 0], ["05", 0], ["06", 0], ["07", 0], ["08", 0], ["09", 0], ["10", 0], ["11", 0], ["12", 0]]
        monthsTupple = []
        for row in dataCSVFile:
            for uniqueMonth in months:
                if (uniqueMonth[0] == row[2].split('-')[1]):
                    uniqueMonth[1] += 1
        for uniqueMonth in months:
            monthsTupple.append((uniqueMonth[0], uniqueMonth[1]))
        return monthsTupple

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('data.csv', newline='') as csvfile:
        dataCSVFile = csv.reader(csvfile, delimiter='	')
        letters = [["A", 0, 100000], ["B", 0, 100000], ["C", 0, 100000], ["D", 0, 100000], ["E", 0, 100000]]
        lettersTupple = []
        for row in dataCSVFile:
            for letter in letters:
                if (letter[0] == row[0]):
                    if (int(row[1]) > letter[1]):
                        letter[1] = int(row[1])
                    if (int(row[1]) < letter[2]):
                        letter[2] = int(row[1])
        for itemLetter in letters:
            lettersTupple.append((itemLetter[0], itemLetter[1], itemLetter[2]))
        return lettersTupple

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open('data.csv', newline='') as csvfile:
        dataCSVFile = csv.reader(csvfile, delimiter='	')
        myDict = [
            ["aaa", 100000, 0],
            ["bbb", 100000, 0],
            ["ccc", 100000, 0],
            ["ddd", 100000, 0],
            ["eee", 100000, 0],
            ["fff", 100000, 0],
            ["ggg", 100000, 0],
            ["hhh", 100000, 0],
            ["iii", 100000, 0],
            ["jjj", 100000, 0]
        ]
        myDictTupple = []
        for row in dataCSVFile:
            for myDictItem in myDict:
                itemsDictRow = row[4].split(',')
                for keyItemRow in itemsDictRow:
                    print(keyItemRow)
                    if (myDictItem[0] == keyItemRow.split(':')[0]):
                        if (int(keyItemRow.split(':')[1]) < myDictItem[1]):
                            myDictItem[1] = int(keyItemRow.split(':')[1])
                        if (int(keyItemRow.split(':')[1]) > myDictItem[2]):
                            myDictItem[2] = int(keyItemRow.split(':')[1])
        for itemmyDict in myDict:
            myDictTupple.append((itemmyDict[0], itemmyDict[1], itemmyDict[2]))
        return myDictTupple

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open('data.csv', newline='') as csvfile:
        dataCSVFile = csv.reader(csvfile, delimiter='	')
        myNumbers = [[0, []], [1, []], [2, []], [3, []], [4, []], [5, []], [6, []], [7, []], [8, []], [9, []]]
        myNumbersTupple = []
        for row in dataCSVFile:
            for myItemNumber in myNumbers:
                if (myItemNumber[0] == int(row[1])):
                    myItemNumber[1].append(row[0])
        for myItemNumbers in myNumbers:
            myNumbersTupple.append((myItemNumbers[0], myItemNumbers[1]))
        return myNumbersTupple

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv', newline='') as csvfile:
        dataCSVFile = csv.reader(csvfile, delimiter='	')
        myNumbers = [[0, []], [1, []], [2, []], [3, []], [4, []], [5, []], [6, []], [7, []], [8, []], [9, []]]
        myNumbersTupple = []
        for row in dataCSVFile:
            for myItemNumber in myNumbers:
                if (myItemNumber[0] == int(row[1])):
                    exist = False
                    for letter in myItemNumber[1]:
                        if (letter == row[0]):
                            exist = True
                    if (exist == False):
                        myItemNumber[1].append(row[0])
        for myItemNumbers in myNumbers:
            myNumbersTupple.append((myItemNumbers[0], sorted(myItemNumbers[1])))
        return myNumbersTupple

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open('data.csv', newline='') as csvfile:
        dataCSVFile = csv.reader(csvfile, delimiter='	')
        myDict = {
            "aaa": 0,
            "bbb": 0,
            "ccc": 0,
            "ddd": 0,
            "eee": 0,
            "fff": 0,
            "ggg": 0,
            "hhh": 0,
            "iii": 0,
            "jjj": 0
        }
        for row in dataCSVFile:
            for myDictItem in myDict:
                itemsDictRow = row[4].split(',')
                for keyItemRow in itemsDictRow:
                    if (myDictItem == keyItemRow.split(':')[0]):
                        myDict[myDictItem] += 1
        return myDict

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open('data.csv', newline='') as csvfile:
        dataCSVFile = csv.reader(csvfile, delimiter='	')
        lettersTupple = []
        for row in dataCSVFile:
            itemsLength1 = len(row[3].split(','))
            itemsLength2 = len(row[4].split(','))
            lettersTupple.append((row[0], itemsLength1, itemsLength2))
        return lettersTupple

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open('data.csv', newline='') as csvfile:
        dataCSVFile = csv.reader(csvfile, delimiter='	')
        lettersDict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0
        }
        for row in dataCSVFile:
            items = row[3].split(',')
            for letter in items:
                lettersDict[letter] += int(row[1])
        return lettersDict

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open('data.csv', newline='') as csvfile:
        dataCSVFile = csv.reader(csvfile, delimiter='	')
        lettersDict = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0
        }
        for row in dataCSVFile:
            items = row[4].split(',')
            for letterKey in lettersDict:
                if (letterKey == row[0]):
                    for myItem in items:
                        lettersDict[letterKey] += int(myItem.split(':')[1])
        return lettersDict