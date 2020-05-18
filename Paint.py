import pygame


class Paint:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.draw_on = False
        self.last_pos = (0, 0)
        self.color = (255, 255, 0)
        self.radius = 10

    def __runPaint__(self):
        self.run = True

        while self.run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.draw_on = True

                if event.type == pygame.MOUSEBUTTONUP:
                    self.draw_on = False

                if event.type == pygame.MOUSEMOTION:
                    if(self.draw_on):
                        pygame.display.update(pygame.draw.circle(self.screen, self.color, event.pos, 5))

                if event.type == pygame.QUIT:
                    raise SystemExit

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.draw_on = False
                        self.run = False
                        return self.screen


                
            


paintBlock = Paint()
scr = paintBlock.__runPaint__()
print(pygame.surfarray.pixel2d(scr))


