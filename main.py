from constants import *
from camera import camera
from wizard import wizard
from groups import all_sprites, player_group, map_sprites, forest_group
from map_generation import load_level, gen_map, add_forest
import pprint
running = True

to_up = False
to_left = False
to_right = False
to_down = False

load_level("data/level.txt")
add_forest()
gen_map()
# print(len(level))
# for i in level:
#     print(i)
pos = (0, 0)
while running:
    SCREEN.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_left = True
            if event.key == pygame.K_d:
                to_right = True
            if event.key == pygame.K_s:
                to_down = True
            if event.key == pygame.K_w:
                to_up = True
            if event.key == pygame.K_h:
                shaking = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                to_left = False
            if event.key == pygame.K_d:
                to_right = False
            if event.key == pygame.K_s:
                to_down = False
            if event.key == pygame.K_w:
                to_up = False
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            wizard.do_attack = True

    camera.update(wizard)
    for i in all_sprites:
        camera.apply(i)

    wizard.update(to_right, to_left, to_up, to_down, pos)
    map_sprites.draw(SCREEN)
    #
    # for i in forest_group:
    #     i.draw_rect()
    forest_group.draw(SCREEN)
    # print(len(forest_group))
    player_group.draw(SCREEN)
    # all_sprites.draw(screen)
    # wizard.draw_healbar()
    pygame.display.flip()
    clock.tick(FPS)
