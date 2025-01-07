import copy
import sys
import pygame
import time
from pygame.locals import *


def createGrid(theSizeOfGrid):
    _size = theSizeOfGrid

    _arrTemp = []
    _default = []
    nextState = []

    i = 0
    j = 0

    for i in range(_size + 2):
        _arrTemp.append(-1)


    _default.append(_arrTemp)

    for j in range(_size):
        arr_1d = []
        arr_1d.append(-1)

        for k in range(_size):
            arr_1d.append(0)
        arr_1d.append(-1)
        # print(len(arr_1d))
        _default.append(arr_1d)

    k = 0

    _default.append(_arrTemp)

    return _default


def editGrid(theWindow, default):
    _theWindow = theWindow
    _default = default
    middleClick = False
    xStartOffset = 1
    yStartOffset = 1
    while True:

        for event in pygame.event.get():

            leftClick, middleClick, rightClick, = pygame.mouse.get_pressed(3)

            if middleClick:
                # print("Middle click")
                break


            if leftClick:
                coord = pygame.mouse.get_pos()
                # print(coord)

                xpos = coord[0]
                ypos = coord[1]

                cellCoordX = int(xpos / 10) * 10
                cellCoordY = int(ypos / 10) * 10

                if not(cellCoordX < 0 or cellCoordX > 990 or cellCoordY < 0 or cellCoordY > 990):

                    cellToUpdate = pygame.draw.rect(_theWindow, (0, 0, 255),
                                                    [(1 + cellCoordX), (1 + cellCoordY), 9, 9], )

                    pygame.display.update(cellToUpdate)

                    # _default[(cellCoordY + 1)][(cellCoordX + 1)] = 1
                    # print(cellCoordX, cellCoordY)
                    _default[(int(cellCoordY / 10) + 1)][(int(cellCoordX / 10) + 1)] = 1

            if rightClick:
                coord = pygame.mouse.get_pos()

                xpos = coord[0]
                ypos = coord[1]

                cellCoordX = int(xpos / 10) * 10
                cellCoordY = int(ypos / 10) * 10

                if not (cellCoordX < 0 or cellCoordX > 990 or cellCoordY < 0 or cellCoordY > 990):

                    cellToUpdate = pygame.draw.rect(_theWindow, (255, 255, 255),
                                                [(1 + cellCoordX), (1 + cellCoordY), 9, 9], )

                    pygame.display.update(cellToUpdate)

                    # _default[(cellCoordY + 1)][(cellCoordX + 1)] = 1

                    _default[(int(cellCoordY / 10) + 1)][(int(cellCoordX / 10) + 1)] = 0


        if middleClick:
            print("Middle click")
            break

    return _theWindow, _default


def createBoard():
    pygame.init()

    window = pygame.display.set_mode((1000, 1000))

    window.fill((255, 0, 255))
    cells = []

    y = 1

    for i in range(100):
        x = 1
        for j in range(100):
            pygame.draw.rect(window, (255, 255, 255), [x, y, 9, 9], )
            x += 10

        y += 10

    pygame.display.update()

    time.sleep(1)
    return window


def updateTiles(theWindow, currentState, blank):
    _theWindow = theWindow

    _currentState = currentState

    _blank = blank

    nextState = copy.deepcopy(_blank)

    cellsUpdate = []
    xOffset = 1
    yOffset = 1

    for k in range(1, (len(_currentState) - 1)):
        for l in range(1, (len(_currentState[0]) - 1)):

            neighborsAlive = 0

            if _currentState[k][l - 1] == 1:
                neighborsAlive += 1

            if _currentState[k][l + 1] == 1:
                neighborsAlive += 1

            if _currentState[k + 1][l] == 1:
                neighborsAlive += 1

            if _currentState[k + 1][l - 1] == 1:
                neighborsAlive += 1

            if _currentState[k + 1][l + 1] == 1:
                neighborsAlive += 1

            if _currentState[k - 1][l] == 1:
                neighborsAlive += 1

            if _currentState[k - 1][l - 1] == 1:
                neighborsAlive += 1

            if _currentState[k - 1][l + 1] == 1:
                neighborsAlive += 1

            if _currentState[k][l] == 1 and neighborsAlive <= 1:
                nextState[k][l] = 0


            elif _currentState[k][l] == 1 and neighborsAlive >= 4:
                nextState[k][l] = 0

            elif _currentState[k][l] == 1 and (neighborsAlive == 2 or neighborsAlive == 3):
                nextState[k][l] = 1

            elif _currentState[k][l] == 0 and neighborsAlive == 3:
                nextState[k][l] = 1
                # print("h")
            else:
                pass
            # cellTrack += 1
            # if nextState[k][l] != _currentState[k][l]:

            if nextState[k][l] == 1:
                cellsUpdate.append(pygame.draw.rect(_theWindow, (0, 0, 255), [xOffset, yOffset, 9, 9], ))
            else:
                cellsUpdate.append(pygame.draw.rect(_theWindow, (255, 255, 255), [xOffset, yOffset, 9, 9], ))
            xOffset += 10

            # print(str(nextState[k][l]), end=" ")
        # print("\n")
        xOffset = 1
        yOffset += 10

    # print("\n")

    pygame.display.update(cellsUpdate)
    time.sleep(.1)
    _currentState = copy.deepcopy(nextState)

    return _currentState, _theWindow

    # shuffle next and current state


def main():
    sizeOfGrid = 100

    default = createGrid(sizeOfGrid)

    blank = copy.deepcopy(default)

    theWindow = createBoard()

    theWindow, theCurrentState = editGrid(theWindow, default)

    while True:

        theCurrentState, theWindow = updateTiles(theWindow, theCurrentState, blank)

        for event in pygame.event.get():
        
            if pygame.mouse.get_pressed(3)[1]:
                theWindow, default = editGrid(theWindow, theCurrentState)






if __name__ == "__main__":
    main()