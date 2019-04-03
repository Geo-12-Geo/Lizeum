import pygame

pygame.init()
w, hue = map(int, input().split())
size = (width, width) = (300, 300)
screen = pygame.display.set_mode(size)


def draw():
    a = ((width / 2 - w * 0.75, width / 2 - w * 0.25), (w, w))

    pygame.draw.rect(screen, pygame.Color(hue, 100, 75, 100).hsva, a, 0)
    the_first_polygon_poins = [(width / 2 - w * 0.75, width / 2 - w * 0.25),
                               (width / 2 + w * 0.25, width / 2 - w * 0.25),
                               (width / 2 + w * 0.75, width / 2 - w * 0.75),
                               (width / 2 - w * 0.25, width / 2 - w * 0.75)]

    pygame.draw.polygon(screen,
                        pygame.Color(hue, 100, 100, 100).hsva,
                        the_first_polygon_poins, 0)

    the_second_polygon_poins = [(width / 2 + w * 0.25, width / 2 - w * 0.25),
                                (width / 2 + w * 0.25, width / 2 + w * 0.75),
                                (width / 2 + w * 0.75, width / 2 + w * 0.25),
                                (width / 2 + w * 0.75, width / 2 - w * 0.75)]

    pygame.draw.polygon(screen,
                        pygame.Color(hue, 100, 50, 100).hsva,
                        the_second_polygon_poins, 0)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
