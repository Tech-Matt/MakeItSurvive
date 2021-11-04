import sys, pygame
pygame.init()

def step_forward(rectangle, step):
    rectangle.y -= step
def step_backward(rectangle, step):
    rectangle.y += step
def step_left(rectangle, step):
    rectangle.x -= step
def step_right(rectangle, step):
    rectangle.x += step

size = width, height = 1000, 600

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode(size)

#The bug
bug = pygame.Rect(width/2, height/2, 10, 20)

#MAIN LOOP
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() 

        keys = pygame.key.get_pressed() #Array con lo stato pressed, non pressed dei tasti

        if keys[pygame.K_UP]:
            step_forward(bug, 5)
        elif keys[pygame.K_DOWN]:
            step_backward(bug, 5)
        elif keys[pygame.K_LEFT]:
            step_left(bug, 5)
        elif keys[pygame.K_RIGHT]:
            step_right(bug, 5)
            
        
        pygame.draw.rect(screen, RED, bug)
        
        pygame.display.update()
        screen.fill(WHITE)

