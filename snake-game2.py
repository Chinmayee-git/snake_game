import random

import pygame

pygame.init()

screen = pygame.display.set_mode((500, 520))
clock = pygame.time.Clock()
FPS = 10
x, y = 40, 40
dx, dy = 20, 0
direction = 'right'
score = 0
me = [(x + 2, y + 2, 18, 18)]
fx = random.choice([i for i in range(0, 500, 20)])
fy = random.choice([i for i in range(0, 500, 20)])


class food():
    global fx, fy

    def eat(self):
        global fx, fy
        fx = random.choice([i for i in range(0, 500, 20)])
        fy = random.choice([i for i in range(0, 500, 20)])

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 0), (fx + 2, fy + 2, 18, 18), 0)


class snake():

    def body(self):
        global x, y, fx, fy, me, score
        if eatself():
            return []
        elif x == fx and y == fy:
            food().eat()
            me.append((x + 2, y + 2, 18, 18))
            score = score + 1
            return me
        elif True:
            me.pop(0)
            me.append((x + 2, y + 2, 18, 18))
            return me

    def direct(self):
        global dx, dy, direction
        if direction == 'right':
            dx = 20
            dy = 0
        elif direction == 'left':
            dx = -20
            dy = 0
        elif direction == 'up':
            dx = 0
            dy = -20
        elif direction == 'down':
            dx = 0
            dy = 20


def grid():
    for i in range(0, 500, 20):
        pygame.draw.line(screen, (128, 128, 128), (0, i), (500, i))
        pygame.draw.line(screen, (128, 128, 128), (i, 0), (i, 500))
    pygame.draw.line(screen, (128, 128, 128), (0, 500), (500, 500))
    screen.blit(pygame.font.Font('freesansbold.ttf', 20).render('Score : ' + str(score), True, (255, 255, 255)),
                (2, 502))


def eatself():
    if len(me) > 1:
        for pos1 in range(len(me)):
            for pos2 in range(pos1 + 1, len(me)):
                if me[pos1][0] == me[pos2][0] and me[pos1][1] == me[pos2][1]:
                    return True
    else:
        return False


def checkend():
    if x > 490 or x < 0 or y < 0 or y > 490 or eatself():
        return True
    else:
        return False


r = True
while r:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 'right'
            elif event.key == pygame.K_LEFT:
                direction = 'left'
            elif event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'
        if event.type == pygame.KEYUP:
            snake().direct()
    x = x + dx
    y = y + dy
    if not checkend():
        for i in snake().body():
            pygame.draw.rect(screen, (255, 0, 0), i, 0)
        food().draw()
    if checkend():
        screen.blit(pygame.font.Font('freesansbold.ttf', 40).render('GAME OVER!!', True, (255, 255, 255)), (120, 220))
    pygame.display.update()
