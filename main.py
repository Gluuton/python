import pygame

pygame.init()


# !CONST
WINDOWSIZE = pygame.Vector2(1024, 576)
SCREENSIZE = pygame.Vector2(1920, 1080)
FPS_LIMIT = 60

SQUARESIZE = 16
NUMSQUARE = (int)(WINDOWSIZE.x / SQUARESIZE)


# !CONST

# VARS
Camera_Offset = pygame.Vector2(0, 0)

showGrid = True
DeltaTime = 0

# !VARS


# Methods
def moveCamera(moveSpeed, CAM_OFF):

    keyPressed = pygame.key.get_pressed()

    if (keyPressed[pygame.K_RIGHT]):
        CAM_OFF.x += moveSpeed * DeltaTime
    if (keyPressed[pygame.K_LEFT]):
        CAM_OFF.x -= moveSpeed * DeltaTime
    if (keyPressed[pygame.K_UP]):
        CAM_OFF.y -= moveSpeed * DeltaTime
    if (keyPressed[pygame.K_DOWN]):
        CAM_OFF.y += moveSpeed * DeltaTime
    
    CAM_OFF.x = max(0, min(CAM_OFF.x, SCREENSIZE.x - WINDOWSIZE.x))
    CAM_OFF.y = max(0, min(CAM_OFF.y, SCREENSIZE.y - WINDOWSIZE.y))
# !Methods



Screen = pygame.display.set_mode(WINDOWSIZE)
Clock = pygame.time.Clock()
Running = True

while Running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    moveCamera(200, Camera_Offset)

    # clear screen
    Screen.fill("white")
    if(showGrid):
        for X in range(0, (int)(SCREENSIZE.x), SQUARESIZE):
            pygame.draw.line(Screen, "Black", ((X - Camera_Offset.x), 0), (X - Camera_Offset.x, SCREENSIZE.y))
        for Y in range(0, (int)(SCREENSIZE.y), SQUARESIZE):
            pygame.draw.line(Screen, "Black", (0, Y - Camera_Offset.y), (SCREENSIZE.x, Y - Camera_Offset.y))

    # update screen
    pygame.display.flip()

    DeltaTime = Clock.tick(FPS_LIMIT) * 0.001

pygame.quit()