import pygame
from globalvars import *
from classes import *

pygame.init()
Screen = pygame.display.set_mode(WINDOWSIZE)
Clock = pygame.time.Clock()
Running = True

# !CONST
WINDOWSIZE = pygame.Vector2(1024, 576)
SCREENSIZE = pygame.Vector2(1920, 1080)
FPS_LIMIT = 60

SQUARESIZE = 16
NUMSQUARE = (int)(WINDOWSIZE.x / SQUARESIZE)
# !CONST

# VARS
CAMERA_OFFSET = pygame.Vector2(0, 0)

showGrid = True
DeltaTime = 0

# !VARS


# Methods
def moveCamera(moveSpeed,CAMERA_OFFSET):

    keyPressed = pygame.key.get_pressed()

    if (keyPressed[pygame.K_RIGHT]):
        CAMERA_OFFSET.x += moveSpeed * DeltaTime
    if (keyPressed[pygame.K_LEFT]):
        CAMERA_OFFSET.x -= moveSpeed * DeltaTime
    if (keyPressed[pygame.K_UP]):
        CAMERA_OFFSET.y -= moveSpeed * DeltaTime
    if (keyPressed[pygame.K_DOWN]):
        CAMERA_OFFSET.y += moveSpeed * DeltaTime
# !Methods




while Running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    CAMERA_OFFSET = moveCamera(200, CAMERA_OFFSET)

    # clear screen
    Screen.fill("white")
    if(showGrid):
        for X in range(0, (int)(SCREENSIZE.x), SQUARESIZE):
            pygame.draw.line(Screen, "Black", ((float)(X) - CAMERA_OFFSET, 0), ((float)(X) - CAMERA_OFFSET.x, SCREENSIZE.y))
        for Y in range(0, (int)(SCREENSIZE.y), SQUARESIZE):
            pygame.draw.line(Screen, "Black", (0, Y - CAMERA_OFFSET), (SCREENSIZE.x, Y - Camera_Offset))

    # update screen
    pygame.display.flip()

    DeltaTime = Clock.tick(FPS_LIMIT) * 0.001

pygame.quit()