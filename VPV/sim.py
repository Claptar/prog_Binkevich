import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

WIN_WIDTH = 480
WIN_HEIGHT = 800

def add_ball(space):
    """Add a ball to the given space at a random position"""
    mass = 1
    radius = 4
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
    body = pymunk.Body(mass, inertia)
    x = random.randint(120, 380)
    body.position = x, 550
    shape = pymunk.Circle(body, radius, (0, 0))
    space.add(body, shape)
    shape.elasticity = 1.0
    return shape


def add_static_L(space):
    body1 = pymunk.Body(body_type = pymunk.Body.STATIC) # 1
    body2 = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body3 = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body1.position = (0, 400)
    body2.position = (480, 400)
    body3.position = (240, 0)
    l1 = pymunk.Segment(body3, (-240, 0), (240, 0), 50) # 2
    l2 = pymunk.Segment(body1, (0, -400), (0, 2000), 5)
    l3 = pymunk.Segment(body2, (0, -400), (0, 2000), 5)
    l1.elasticity = 1.0
    l2.elasticity = 1.0
    l3.elasticity = 1.0

    space.add(l1, l2, l3) # 3
    return l1, l2, l3


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -1000.0)

    lines = add_static_L(space)
    balls = []
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    draw_options.shape_dynamic_color = (0, 0, 255)

    ticks_to_next_ball = 10
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)

        ticks_to_next_ball -= 1
        if ticks_to_next_ball <= 0:
            ticks_to_next_ball = 25
            ball_shape = add_ball(space)
            balls.append(ball_shape)

        space.step(1/50.0)
        if len(balls) > 2:
            print(balls[1].body._get_velocity()[1])
        screen.fill((255, 255, 255))
        space.debug_draw(draw_options)

        pygame.display.flip()
        clock.tick(50)

if __name__ == '__main__':
    main()
