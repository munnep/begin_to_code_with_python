# EG16-02 Image Drawing

import pygame

class ImageDemo:

    @staticmethod
    def do_image_demo():
        init_result = pygame.init()
        if init_result[1] != 0:
            print('pygame not installed properly')
            return

        width = 800
        height = 600
        size = (width, height)

        surface = pygame.display.set_mode(size)
        pygame.display.set_caption('Image example')

        white = (255, 255, 255)
        surface.fill(white)

        cheeseImage = pygame.image.load('Cheese.png')

        cheesePos = (0,0)
        surface.blit(cheeseImage, cheesePos)
        pygame.display.flip()
        
        is_running = True
        while is_running:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   is_running = False
        
ImageDemo.do_image_demo()

