from checkLogic import *
from drawing import *
from state import *
import random
import sys

def minIMax(trenutnoStanjePesaka: list[int], depth: int, alphaP: int, betaP: int, alphaZ: int, betaZ: int, naPotezu: int, trenutnoStanjeZidova: list[Label], pesakIliZid: int, fields: list[Label], a: list[int], walls: list[Label], frame: Frame) -> tuple[list[int], list[Label], int]:
    tuplic: tuple[list[int], list[Label], int]= [trenutnoStanjePesaka, trenutnoStanjeZidova, 0]
    fields2: list[Label] = []
    trenutnoStanjeZidova2: list[Label] = []
    if(pesakIliZid == 0):
        print("Pesak")
        if(krajnjeStanje(trenutnoStanjePesaka, a)[0]):
            p:list[int] = []
            trenutnoStanjePesaka.append(proceniStanjePesak(trenutnoStanjePesaka))
            for element in trenutnoStanjePesaka:
                p.append(element)
            tuplic[0] = p
            return tuplic
        movesPesak: list[list[int]] = moguciPoteziPesak(trenutnoStanjePesaka, trenutnoStanjeZidova, fields, a)
        if(depth == 0 or len(movesPesak) == 0):
            p:list[int] = []
            trenutnoStanjePesaka.append(proceniStanjePesak(trenutnoStanjePesaka))
            for element in trenutnoStanjePesaka:
                p.append(element)
            tuplic[0] = p
            return tuplic
        best: list[int] = []
        bestValue: int = 0
        for element in trenutnoStanjePesaka:
            best.append(element)
        if(trenutnoStanjePesaka[13] == 1):
            best.append(-sys.maxsize - 1)
            bestValue = -sys.maxsize - 1
            for p in movesPesak:
                fields2.clear()
                for label in fields:
                    fields2.append(label)
                    if (p[0] != trenutnoStanjePesaka[0] or p[1] != trenutnoStanjePesaka[1]):
                        if ((label.grid_info()['row'] - 1) / 2 == p[0] and (label.grid_info()['column']) / 2 == p[1]):
                            label.config(text='X1')
                        if ((label.grid_info()['row'] - 1) / 2 == trenutnoStanjePesaka[0] and (label.grid_info()['column']) / 2 == trenutnoStanjePesaka[1]):
                            label.config(text=(str(int((label.grid_info()['row']-1)/2)) + str(int(label.grid_info()['column']/2))))
                    elif(p[2] != trenutnoStanjePesaka[2] or p[3] != trenutnoStanjePesaka[3]):
                        if ((label.grid_info()['row'] - 1) / 2 == p[2] and (label.grid_info()['column']) / 2 == p[3]):
                            label.config(text='X2')
                        if ((label.grid_info()['row'] - 1) / 2 == trenutnoStanjePesaka[2] and (label.grid_info()['column']) / 2 == trenutnoStanjePesaka[3]):
                            label.config(text=(str(int((label.grid_info()['row']-1)/2)) + str(int(label.grid_info()['column']/2))))
                    elif(p[4] != trenutnoStanjePesaka[4] or p[5] != trenutnoStanjePesaka[5]):
                        if ((label.grid_info()['row'] - 1) / 2 == p[4] and (label.grid_info()['column']) / 2 == p[5]):
                            label.config(text='O1')
                        if ((label.grid_info()['row'] - 1) / 2 == trenutnoStanjePesaka[4] and (label.grid_info()['column']) / 2 == trenutnoStanjePesaka[5]):
                            label.config(text=(str(int((label.grid_info()['row']-1)/2)) + str(int(label.grid_info()['column']/2))))
                    elif(p[6] != trenutnoStanjePesaka[6] or p[7] != trenutnoStanjePesaka[7]):
                        if ((label.grid_info()['row'] - 1) / 2 == p[6] and (label.grid_info()['column']) / 2 == p[7]):
                            label.config(text='O2')
                        if ((label.grid_info()['row'] - 1) / 2 == trenutnoStanjePesaka[6] and (label.grid_info()['column']) / 2 == trenutnoStanjePesaka[7]):
                            label.config(text=(str(int((label.grid_info()['row']-1)/2)) + str(int(label.grid_info()['column']/2))))
                m: tuple[list[int], list[Label], int] = minIMax(p, depth, alphaP, betaP, alphaZ, betaZ, naPotezu, trenutnoStanjeZidova, (pesakIliZid + 1) % 2, fields2, a, walls, frame)
                p.append(m[0][14])
                if(p[14] > best[14]):
                    best = p
                if bestValue < m[2]:
                    bestValue = m[2]
                if best[14] >= betaP:
                    break #beta cut-off
                alphaP = max(alphaP, best[14])
        else:
            best.append(sys.maxsize)
            bestValue = sys.maxsize
            for p in movesPesak:
                fields2.clear()
                for label in fields:
                    fields2.append(label)
                    if (p[0] != trenutnoStanjePesaka[0] or p[1] != trenutnoStanjePesaka[1]):
                        if ((label.grid_info()['row'] - 1) / 2 == p[0] and (label.grid_info()['column']) / 2 == p[1]):
                            label.config(text='X1')
                        if ((label.grid_info()['row'] - 1) / 2 == trenutnoStanjePesaka[0] and (label.grid_info()['column']) / 2 == trenutnoStanjePesaka[1]):
                            label.config(text=(str(int((label.grid_info()['row']-1)/2)) + str(int(label.grid_info()['column']/2))))
                    elif(p[2] != trenutnoStanjePesaka[2] or p[3] != trenutnoStanjePesaka[3]):
                        if ((label.grid_info()['row'] - 1) / 2 == p[2] and (label.grid_info()['column']) / 2 == p[3]):
                            label.config(text='X2')
                        if ((label.grid_info()['row'] - 1) / 2 == trenutnoStanjePesaka[2] and (label.grid_info()['column']) / 2 == trenutnoStanjePesaka[3]):
                            label.config(text=(str(int((label.grid_info()['row']-1)/2)) + str(int(label.grid_info()['column']/2))))
                    elif(p[4] != trenutnoStanjePesaka[4] or p[5] != trenutnoStanjePesaka[5]):
                        if ((label.grid_info()['row'] - 1) / 2 == p[4] and (label.grid_info()['column']) / 2 == p[5]):
                            label.config(text='O1')
                        if ((label.grid_info()['row'] - 1) / 2 == trenutnoStanjePesaka[4] and (label.grid_info()['column']) / 2 == trenutnoStanjePesaka[5]):
                            label.config(text=(str(int((label.grid_info()['row']-1)/2)) + str(int(label.grid_info()['column']/2))))
                    elif(p[6] != trenutnoStanjePesaka[6] or p[7] != trenutnoStanjePesaka[7]):
                        if ((label.grid_info()['row'] - 1) / 2 == p[6] and (label.grid_info()['column']) / 2 == p[7]):
                            label.config(text='O2')
                        if ((label.grid_info()['row'] - 1) / 2 == trenutnoStanjePesaka[6] and (label.grid_info()['column']) / 2 == trenutnoStanjePesaka[7]):
                            label.config(text=(str(int((label.grid_info()['row']-1)/2)) + str(int(label.grid_info()['column']/2))))
                m: tuple[list[int], list[Label], int] = minIMax(p, depth, alphaP, betaP, alphaZ, betaZ, (naPotezu + 1)%2, trenutnoStanjeZidova, (pesakIliZid + 1)%2, fields2, a, walls, frame)
                p.append(m[0][14])
                if(p[14] < best[14]):
                    for element in p:
                        best[p.index(element)] = element
                if (m[2] < bestValue):
                    bestValue = m[2]
                if best[14] <= alphaP:
                    break # alpha cut-off
                betaP = min(betaP, best[14])
        tuplic[0] = best
        tuplic[1] = trenutnoStanjeZidova
        tuplic[2] = bestValue
    else:
        print("Zid")
        if(krajnjeStanje(trenutnoStanjePesaka, a)[0]):
            z: list[Label] = []
            trenutnoStanjeValue = proceniStanjeZid(trenutnoStanjeZidova)
            for element in trenutnoStanjeZidova:
                z.append(element)
            tuplic[1] = z
            tuplic[2] = trenutnoStanjeValue
            return tuplic
        movesZid:list[Label] = moguciPoteziZid(fields, trenutnoStanjeZidova, a, trenutnoStanjePesaka, walls, frame)
        if (naPotezu == 1):
            if (trenutnoStanjePesaka[10] == 0 and trenutnoStanjePesaka[11] == 0):
                return tuplic
        else:
            if (trenutnoStanjePesaka[8] == 0 and trenutnoStanjePesaka[9] == 0):
                return tuplic
        if (depth == 0 or len(movesZid) == 0):
            z: list[Label] = []
            trenutnoStanjeValue = proceniStanjeZid(trenutnoStanjeZidova)
            for element in trenutnoStanjeZidova:
                z.append(element)
            tuplic[1] = z
            tuplic[2] = trenutnoStanjeValue
            return tuplic
        best: list[Label] = []
        for element in trenutnoStanjeZidova:
            best.append(trenutnoStanjeZidova)
        bestValue: int = 0
        if(naPotezu == 1):
            bestValue = -sys.maxsize - 1
            for move in movesZid[::2]:
                trenutnoStanjeZidova2.clear()
                for zid in trenutnoStanjeZidova:
                    trenutnoStanjeZidova2.append(zid)
                trenutnoStanjeZidova2.append(move)
                if (move.cget('text') == "|"):
                    label = Label(frame, text='||', width=3)
                    trenutnoStanjeZidova2.append(label)
                    label.grid(row = move.grid_info()['row'] + 1, column = move.grid_info()['column'])
                    trenutnoStanjePesaka[10] = trenutnoStanjePesaka[10] - 1
                else:
                    label = Label(frame, text='=', width=3)
                    trenutnoStanjeZidova2.append(label)
                    label.grid(row = move.grid_info()['row'], column = move.grid_info()['column'] + 1)
                    trenutnoStanjePesaka[11] = trenutnoStanjePesaka[11] - 1
                trenutnoStanjeZidova2.append(movesZid[movesZid.index(move) + 1])
                m: tuple[list[int], list[Label], int] = minIMax(trenutnoStanjePesaka, depth - 1, alphaP, betaP, alphaZ, betaZ, (naPotezu + 1)%2, trenutnoStanjeZidova2, (pesakIliZid + 1) % 2, fields, a, walls, frame)
                label = trenutnoStanjeZidova2[len(trenutnoStanjeZidova2) - 2]
                label.grid_forget()
                moveValue = m[2]
                if (moveValue > bestValue):
                    best.append(move)
                    best.append(movesZid[movesZid.index(move) + 1])
                    best.append(movesZid[movesZid.index(move) + 2])
                    bestValue = moveValue
                if bestValue >= betaZ:
                    break #beta cut-off
                alphaZ = max(alphaZ, bestValue)
        else:
            bestValue = sys.maxsize
            for move in movesZid[::2]:
                trenutnoStanjeZidova2.clear()
                for zid in trenutnoStanjeZidova:
                    trenutnoStanjeZidova2.append(zid)
                trenutnoStanjeZidova2.append(move)
                if (move.cget('text') == "|"):
                    label = Label(frame, text='||', width=3)
                    trenutnoStanjeZidova2.append(label)
                    label.grid(row = move.grid_info()['row'] + 1, column = move.grid_info()['column'])
                    trenutnoStanjePesaka[8] = trenutnoStanjePesaka[8] - 1
                else:
                    label = Label(frame, text='=', width=3)
                    trenutnoStanjeZidova2.append(label)
                    label.grid(row = move.grid_info()['row'], column = move.grid_info()['column'] + 1)
                    trenutnoStanjePesaka[9] = trenutnoStanjePesaka[9] - 1
                trenutnoStanjeZidova2.append(movesZid[movesZid.index(move) + 1])
                m: tuple[list[int], list[Label], int] = minIMax(trenutnoStanjePesaka, depth - 1, alphaP, betaP, alphaZ, betaZ, (naPotezu + 1)%2, trenutnoStanjeZidova2, (pesakIliZid + 1) % 2, fields, a, walls, frame)
                label = trenutnoStanjeZidova2[len(trenutnoStanjeZidova2) - 2]
                label.grid_forget()
                moveValue = m[2]
                if (moveValue < bestValue): 
                    best.append(move)
                    best.append(movesZid[movesZid.index(move) + 1])
                    best.append(movesZid[movesZid.index(move) + 2])
                    bestValue = moveValue
                if bestValue <= alphaZ:
                    break # alpha cut-off
                betaZ = min(betaZ, bestValue)
        tuplic[0] = trenutnoStanjePesaka
        tuplic[1] = best
        tuplic[2] = bestValue
    print(trenutnoStanjePesaka)
    for element in trenutnoStanjeZidova:
        print(element.cget("text"))
    return tuplic

#def minIMaxPesak(trenutnoStanje: list[int], depth: int) -> list[int]:
#    moves: list[list[int]] = moguciPoteziPesak(trenutnoStanje)
#    if (depth == 0 or moves.len() == 0):
#        p: list[int] = []
#        trenutnoStanje.append(proceniStanjePesak(trenutnoStanje))
#        for element in trenutnoStanje:
#            p.append(element)
#        return p
#    best = trenutnoStanje
#    if(trenutnoStanje[13] == 1):
#        best.append(sys.maxSize)
#        for p in moves:
#            m: list[int] = minIMaxPesak(p, depth - 1)
#            p.append(m[14])
#            if (p[14] > best[14]):
#                best = p
#    else:
#        best.append(sys.maxSize)
#        for p in moves:
#            m = minIMaxPesak(p, depth - 1)
#            p.append(m[14])
#            if (p[14] < best[14]):
#                best = p
#    return best

#def minIMaxZid(trenutnoStanje: list[Label], depth: int, naPotezu: int) -> tuple[list[Label], int]:
#    moves: list[list[Label]] = moguciPoteziZid(trenutnoStanje)
#    if (depth == 0 or moves.len() == 0):
#        p: list[Label] = []
#        trenutnoStanjeValue = proceniStanjeZid(trenutnoStanje)
#        for element in trenutnoStanje:
#            p.append(element)
#        return tuple[p, trenutnoStanjeValue]
#    best = trenutnoStanje
#    bestValue: int()
#    if(naPotezu == 1):
#        bestValue = sys.maxSize
#        for p in moves:
#            m: tuple[list[Label], int] = minIMaxPesak(p, depth - 1)
#            pValue = m[1]
#            if (pValue > bestValue):
#                best = p
#    else:
#        bestValue = -sys.maxsize - 1
#        for p in moves:
#            m = minIMaxPesak(p, depth - 1)
#            pValue = m[1]
#            if (pValue < bestValue):
#                best = p
#    return tuple[best, bestValue]

def moguciPoteziPesak(trenutnoStanje: list[int], zidovi: list[Label], fields: list[Label], a: list[int]) -> list[list[int]]:
    moves: list[list[int]] = []
    if (trenutnoStanje[trenutnoStanje[13] * 4] == 1):
        if trenutnoStanje[trenutnoStanje[13] * 4 + 1] == 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 1] == int((a[1] - 3) / 2):
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 1] == 2:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 1] == (int(a[1]/2) - 3) - 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        else:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
    elif (trenutnoStanje[trenutnoStanje[13] * 4] == 2):
        if trenutnoStanje[trenutnoStanje[13] * 4 + 1] == 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 1] == int((a[1] - 3) / 2):
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 1] == 2:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 1] == int((a[1] - 3) / 2) - 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        else:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
    elif (trenutnoStanje[trenutnoStanje[13] * 4] == int((a[0] - 3) / 2) - 1):
        if trenutnoStanje[trenutnoStanje[13] * 4 + 1] == 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 1] == int((a[1] - 3) / 2):
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 1] == 2:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 1] == int((a[1] - 3) / 2) - 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        else:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
    elif (trenutnoStanje[trenutnoStanje[13] * 4] == int((a[0] - 3) / 2)):
        if trenutnoStanje[trenutnoStanje[13] * 4 + 1] == 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 1] == int((a[1] - 3) / 2):
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 1] == 2:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 1] == int((a[1] - 3) / 2) - 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        else:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
    else:
        if (trenutnoStanje[trenutnoStanje[13] * 4 + 1] == 1):
            move: list[int] = []
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif (trenutnoStanje[trenutnoStanje[13] * 4 + 1] == int((a[1] - 3) / 2)):
            move: list[int] = []
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif (trenutnoStanje[trenutnoStanje[13] * 4 + 1] == 2):
            move: list[int] = []
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif (trenutnoStanje[trenutnoStanje[13] * 4 + 1] == int((a[1] - 3) / 2) - 1):
            move: list[int] = []
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        else:
            move: list[int] = []
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4], trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] - 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4] = trenutnoStanje[trenutnoStanje[13] * 4] + 1
                move[trenutnoStanje[13] * 4 + 1] = trenutnoStanje[trenutnoStanje[13] * 4 + 1] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
    if (trenutnoStanje[trenutnoStanje[13] * 4 + 2] == 1):
        if trenutnoStanje[trenutnoStanje[13] * 4 + 3] == 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 3] == int((a[1] - 3) / 2):
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 3] == 2:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 3] == (int(a[1]/2) - 3) - 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        else:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
    elif (trenutnoStanje[trenutnoStanje[13] * 4 + 2] == 2):
        if trenutnoStanje[trenutnoStanje[13] * 4 + 3] == 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 3] == int((a[1] - 3) / 2):
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 3] == 2:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 3] == int((a[1] - 3) / 2) - 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        else:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
    elif (trenutnoStanje[trenutnoStanje[13] * 4 + 2] == int((a[0] - 3) / 2) - 1):
        if trenutnoStanje[trenutnoStanje[13] * 4 + 3] == 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 3] == int((a[1] - 3) / 2):
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 3] == 2:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 3] == int((a[1] - 3) / 2) - 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        else:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
    elif (trenutnoStanje[trenutnoStanje[13] * 4 + 2] == int((a[0] - 3) / 2)):
        if trenutnoStanje[trenutnoStanje[13] * 4 + 3] == 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 3] == int((a[1] - 3) / 2):
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 3] == 2:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif trenutnoStanje[trenutnoStanje[13] * 4 + 3] == int((a[1] - 3) / 2) - 1:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        else:
            move: list[int] = []
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
    else:
        if (trenutnoStanje[trenutnoStanje[13] * 4 + 3] == 1):
            move: list[int] = []
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif (trenutnoStanje[trenutnoStanje[13] * 4 + 3] == int((a[1] - 3) / 2)):
            move: list[int] = []
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif (trenutnoStanje[trenutnoStanje[13] * 4 + 3] == 2):
            move: list[int] = []
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        elif (trenutnoStanje[trenutnoStanje[13] * 4 + 3] == int((a[1] - 3) / 2) - 1):
            move: list[int] = []
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
        else:
            move: list[int] = []
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 2, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3], trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (not proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 2, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a) and proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2], trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] - 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] - 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
            if (proveraPromenePesaka(trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1, trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1, trenutnoStanje[13] * 2 + 1, trenutnoStanje, zidovi, fields, a)):
                for element in trenutnoStanje:
                    move.append(element)
                move[trenutnoStanje[13] * 4 + 2] = trenutnoStanje[trenutnoStanje[13] * 4 + 2] + 1
                move[trenutnoStanje[13] * 4 + 3] = trenutnoStanje[trenutnoStanje[13] * 4 + 3] + 1
                move[13] = (trenutnoStanje[13] + 1) % 2
            if move:
                move1: list[int] = []
                for element in move:
                    move1.append(element)
                moves.append(move1)
                move.clear()
    return moves

def algoritamZaTrazenje(trenutnePozicije: list[int], startnePozicije: list[int]) -> int :
    return 

def proceniStanjePesak(a: list[int], startnePozicije: list[int]) -> int :
    distance1 : int
    distance2 : int
    distance1 = algoritamZaTrazenje([a[4], a[5]], [startnePozicije[8], startnePozicije[9], startnePozicije[10], startnePozicije[11]])
    distance2 = algoritamZaTrazenje([a[6], a[7]], [startnePozicije[8], startnePozicije[9], startnePozicije[10], startnePozicije[11]])
    return random.choice(a)

#def maxStanjePesak(listaStanjaPesaka: list[int]) -> int :
#    maxi = listaStanjaPesaka[0]
#    for i in listaStanjaPesaka:
#        if i > maxi:
#            maxi = i
#    return maxi

#def minStanjePesak(listaStanjaPesaka: list[int]) -> int :
#    mini = listaStanjaPesaka[0]
#    for i in listaStanjaPesaka:
#        if i < mini:
#            mini = i
#    return mini
def nadjiZid(lista: list[Label], k1: int, k2: int) -> Label:
    for x in lista:
        if(x.grid_info()['row'] == k1 and x.grid_info()['column'] == k2):
            return x

def moguciPoteziZid(fields: list[Label], zidovi: list[Label], a: list[int], b: list[int], walls: list[Label], frame: Frame) -> list[Label] :
    lista: list[Label] = []
    for w in walls:
        if(w.cget('text') == "|" or w.cget('text')=="_"):
            lista.append(w)

    listica : list[Label] = []
    for x in lista:
        if (x.cget("text") == "|" and b[b[13]*2 + 8] > 0):
            if(x.grid_info()['row'] != a[0] - 2):
                koord1 = int((x.grid_info()['row'] - 1)/2)
                koord2 = int((x.grid_info()['column']-1)/2)
                koord3 = int((x.grid_info()['row'] - 1)/2)
                koord4 = int((x.grid_info()['column']+1)/2)
                koord5 = int((x.grid_info()['row'] + 1)/2)
                koord6 = int((x.grid_info()['column']-1)/2)
                koord7 = int((x.grid_info()['row'] + 1)/2)
                koord8 = int((x.grid_info()['column']+1)/2)
                if(proveraPromeneZida([koord1, koord2, koord3, koord4, koord5, koord6, koord7, koord8, 0], fields, zidovi, a, walls, frame)):
                    listica.append(x)
                    listica.append(nadjiZid(lista, koord5*2 + 1, koord6*2+1))
        elif (b[b[13]*2 + 9] > 0):
            if(x.grid_info()['column'] != a[1] - 3):
                koord1 = int((x.grid_info()['row'])/2 - 1)
                koord2 = int((x.grid_info()['column'])/2)
                koord3 = int((x.grid_info()['row'])/2 - 1)
                koord4 = int((x.grid_info()['column'] + 2)/2)
                koord5 = int((x.grid_info()['row'])/2 )
                koord6 = int((x.grid_info()['column'])/2)
                koord7 = int((x.grid_info()['row'])/2)
                koord8 = int((x.grid_info()['column']+2)/2)
                if(proveraPromeneZida([koord1, koord2, koord3, koord4, koord5, koord6, koord7, koord8, 0], fields, zidovi, a, walls, frame)):
                    listica.append(x)
                    listica.append(nadjiZid(lista, koord7*2, koord8*2))
    
    return listica

def proceniStanjeZid(trenutnoStanjeZidova: list[Label]) -> int :
    b = [12, 14, 7, 89, 33, 102, 34, 67, 89, 30, 11, 6, 45]
    return random.choice(b)

def maxStanje(listaStanja: list[int]) -> int :
    maxi = listaStanja[0]
    for m in listaStanja:
        if m > maxi:
            maxi = m
    return maxi

def minStanje(listaStanja: list[int]) -> int :
    mini = listaStanja[0]
    for m in listaStanja:
        if m < mini:
            mini = m
    return mini

def potezRacunara(trenutnoStanjePesaka: list[int], depth: int, naPotezu: int, trenutnoStanjeZidova: list[Label], pesakIliZid: int, fields: list[Label], a: list[int], walls: list[Label], frame: Frame, buttonStart: Button):

    potez: tuple[list[int], list[Label], int] = minIMax(trenutnoStanjePesaka, depth, -sys.maxsize - 1, sys.maxsize, -sys.maxsize - 1, sys.maxsize, naPotezu, trenutnoStanjeZidova, pesakIliZid, fields, a, walls, frame)
    for i in range(4, 8):
        if(potez[0][i] != trenutnoStanjePesaka[i]):
            if(i==4 or i==5):
                iscrtajPesaka([potez[0][i], potez[0][i+1], 3], fields, trenutnoStanjePesaka)
            else:
                iscrtajPesaka([potez[i], potez[i+1], 4], fields, trenutnoStanjePesaka)

    potez[1].pop()
    potez[1].pop()
    l1 = potez[1].pop()
    bojaZida = 0
    koord1: int = 0
    koord2: int = 0
    koord3: int = 0
    koord4: int = 0
    koord5: int = 0
    koord6: int = 0
    koord7: int = 0
    koord8: int = 0
    if (l1.cget("text") == "||"):
        koord1 = int((l1.grid_info()['row']-1)/2)
        koord2 = int((l1.grid_info()['column']-1)/2)
        koord3 = int((l1.grid_info()['row']-1)/2)
        koord4 = int((l1.grid_info()['column']+1)/2)
        koord5 = int((l1.grid_info()['row']+1)/2)
        koord6 = int((l1.grid_info()['column']-1)/2)
        koord7 = int((l1.grid_info()['row']+1)/2)
        koord8 = int((l1.grid_info()['column']+1)/2)
    else:
        koord1 = int((l1.grid_info()['row']-2)/2)
        koord2 = int((l1.grid_info()['column'])/2)
        koord3 = int((l1.grid_info()['row']-2)/2)
        koord4 = int((l1.grid_info()['column'])/2)
        koord5 = int((l1.grid_info()['row'])/2)
        koord6 = int((l1.grid_info()['column']+2)/2)
        koord7 = int((l1.grid_info()['row'])/2)
        koord8 = int((l1.grid_info()['column']+2)/2)
        bojaZida = 1
    if (trenutnoStanjePesaka[bojaZida * 2 + 10]):
        iscrtajZid([koord1, koord2, koord3, koord4, koord5, koord6, koord7, koord8, bojaZida], frame, walls, trenutnoStanjeZidova)
    #trenutnoStanjePesaka[10 + bojaZida] -= 1
    x = krajnjeStanje(trenutnoStanjePesaka, a)
    if (x[0]):
        if (x[1] == 1 or x[1] == 2):
            if (trenutnoStanjePesaka[12] == 0):
                messagebox.showinfo('Igra je zavrsena', 'Cestitamo, pobedili ste!!!')
            else: messagebox.showinfo('Igra je zavrsena', 'Cestitamo, pobedio je igrac 1!!!')
            buttonStart.pack_forget()
            return
        else:
            if (trenutnoStanjePesaka[12] == 0):
                messagebox.showinfo('Igra je zavrsena', 'Dobro ste igrali, ali racunar je bio bolji!!!')
            else: messagebox.showinfo('Igra je zavrsena', 'Cestitamo, pobedio je igrac 2!!!')
            buttonStart.pack_forget()
            return