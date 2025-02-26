import pygame

# when pygame is going to be used, always start with this command
print('Setup Start!')
pygame.init()
# create the variable and it receives the following code, to generate the screen (dimensions always on x and y and inside parentesis ())
screen = pygame.display.set_mode(size=(600, 480))
print('Setup End!')

# loop to keep the window opened
print('Loop Start!')
while True:
    # check for all
    for event in pygame.event.get():  # pygame.event.get() gets all events from a queue
        if event.type == pygame.QUIT:
            pygame.quit()  # close window
            quit()  # end pygame
