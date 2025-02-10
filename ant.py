import pygame
import random

# setup
pygame.init()

(sizeX, sizeY) = (100, 100)
boxSize = 15
tickSpeed = 120
fullColor = (30, 30, 30)
emptyColor = (200, 200, 200)
backgroundColor = (255, 255, 255)

table = [[False for _ in range(sizeX+10)] for _ in range(sizeY+10)]

for i in range(int(sizeX/2)):
    for j in range(int(sizeY/2)):
        # table[i+int(sizeX/4)][j+int(sizeX/4)] = bool(random.getrandbits(1))
        pass


antX = int(sizeX/2)
antY = int(sizeY/2)
antDir = 0

screen = pygame.display.set_mode((sizeX * boxSize, sizeY * boxSize))
pygame.display.set_caption('automatAnt')
screen.fill(backgroundColor)
clock = pygame.time.Clock()


def moveNflip():
    global antX, antY, antDir, table
    tile = table[antX][antY]
    if tile is True:
        antDir += 3
    else:
        antDir -= 3
    if antDir == -3:
        antDir = 9
    antDir = abs(antDir) % 12
    table[antX][antY] = not tile
    if tile is False:
        pygame.draw.rect(screen, fullColor,
                         pygame.Rect(antX*boxSize, antY*boxSize, boxSize, boxSize), 0)
    if tile is True:
        pygame.draw.rect(screen, backgroundColor,
                         pygame.Rect(antX*boxSize, antY*boxSize, boxSize, boxSize), 0)
        pygame.draw.rect(screen, emptyColor,
                         pygame.Rect(antX*boxSize, antY*boxSize, boxSize, boxSize), 2)
    if antDir == 0:
        antY -= 1
    elif antDir == 3:
        antX += 1
    elif antDir == 6:
        antY += 1
    elif antDir == 9:
        antX -= 1
    else:
        print("error")
    antX %= sizeX
    antY %= sizeY


def drawAllTable():
    screen.fill(backgroundColor)
    for i in range(sizeX):
        for j in range(sizeY):
            if table[i][j]:
                pygame.draw.rect(screen, fullColor,
                                 pygame.Rect(i*boxSize, j*boxSize, boxSize, boxSize), 0)
            else:
                pygame.draw.rect(screen, emptyColor,
                                 pygame.Rect(i*boxSize, j*boxSize, boxSize, boxSize), 2)


def drawAnt(antX, antY, antDir):
    antColor = (0, 252, 0)
    if antDir == 0:
        pygame.draw.rect(screen, antColor,
                         pygame.Rect(antX*boxSize+boxSize/4, antY*boxSize, boxSize/2, boxSize))
    elif antDir == 3:
        pygame.draw.rect(screen, antColor,
                         pygame.Rect(antX*boxSize, antY*boxSize+boxSize/4, boxSize, boxSize/2))
    elif antDir == 6:
        pygame.draw.rect(screen, antColor,
                         pygame.Rect(antX*boxSize+boxSize/4, antY*boxSize, boxSize/2, boxSize))
    elif antDir == 9:
        pygame.draw.rect(screen, antColor,
                         pygame.Rect(antX*boxSize, antY*boxSize+boxSize/4, boxSize, boxSize/2))


def XY2Tile(in_xy):
    in_x, in_y = in_xy
    out_x = int(in_x / boxSize)
    out_y = int(in_y / boxSize)
    return (out_x, out_y)


def main():
    global antX, antY
    running = True
    pause = True
    drawAllTable()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# keyboard input
            if event.type == pygame.KEYDOWN:
                pause = not pause
# mouse input
        leftButtonDown, midButtonDown, rightButtonDown = pygame.mouse.get_pressed()
        if leftButtonDown:
            tx, ty = XY2Tile(pygame.mouse.get_pos())
            table[tx][ty] = True
            drawAllTable()
        elif rightButtonDown:
            tx, ty = XY2Tile(pygame.mouse.get_pos())
            table[tx][ty] = False
            drawAllTable()
        elif midButtonDown:
            antX, antY = XY2Tile(pygame.mouse.get_pos())
            drawAllTable()
            drawAnt(antX, antY, antDir)

# graphics
        if not pause:
            moveNflip()
        drawAnt(antX, antY, antDir)
        pygame.display.flip()
        clock.tick(tickSpeed)


main()
