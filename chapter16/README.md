# Chapter 16: Create games with pygame

Use the following in the prompt

```
# import pygame
import pygame

# initialize pygame
pygame.init()

# the size of pygame screen
size = (800, 600)

# initialize the screen
surface = pygame.display.set_mode(size)

pygame.display.set_caption('An awesome game by Rob')

red = (255, 0, 0)
start = (0,0)
end = (500, 300)
pygame.draw.line(surface, red, start, end)
<rect(0, 0, 501, 301)>

# show it on the screen
pygame.display.flip()
```

Using images in your game
```
cheeseImage = pygame.image.load('cheese.png')
```

Added the following to make sure the screen doesn't close
```
        is_running = True
        while is_running:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   is_running = False
```                   

Look at the final game in directory chapter 11 Complete Game
