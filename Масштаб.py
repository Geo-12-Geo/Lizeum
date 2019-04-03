import pygame

pygame.init()
size = w, h = 501, 501
screen = pygame.display.set_mode(size)

running = True
rects = list(map(lambda x: list(map(float(x[1:-1].replace(',', '.').split(';'))),
                                input().split(', '))))
k = 10
dk = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            k += dk
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            k -= dk if 0 < (k - dk) else 0

    screen.fill(pygame.Color('black'))
    pygame.draw.polygon(screen, pygame.Color('white'),
                        list(map(lambda x: [int(w // 2 + x[0] * k),
                                            int(h // 2 - x[1] * k)],
                                 rects)), 2)
    pygame.display.flip()

pygame.quit()
