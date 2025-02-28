import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        # create the variable, and it receives the following code, to generate the screen (dimensions always on x and y and inside parentesis ())
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # check for all
            # for event in pygame.event.get():  # pygame.event.get() gets all events from a queue
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # close window
            #         quit()  # end pygame
