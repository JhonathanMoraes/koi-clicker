import pygame

class Progress_bar(object):
    def __init__(self, pos, tamanho, cooldown, running=False, progress=0, orientacao='horizontal'):
        self.pos = pos
        self.tamanho = tamanho
        self.cooldown = cooldown
        self.running = running
        self.progress = progress
        self.orientacao = orientacao

    def draw(self, surface):
        if self.progress < 100:
            pygame.draw.rect(surface, (0, 0, 0), self.pos + tuple(self.tamanho))
            ratio = self.progress / 100
            if self.orientacao == 'horizontal':
                pygame.draw.rect(surface, (10, 240, 20), self.pos + tuple([int(self.tamanho[0] * ratio), self.tamanho[1]]))
            else:
                pygame.draw.rect(surface, (10, 240, 20), self.pos + tuple([self.tamanho[0], int(self.tamanho[1] * ratio)]))

            self.progress += 10 / self.cooldown

        elif self.progress >= 100:
            self.running = False
            self.progress = 0
            return True
        
        return False