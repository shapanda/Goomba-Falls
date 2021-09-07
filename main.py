import pygame
import random


def main():
    pygame.init()

    scr = pygame.display.set_mode((800, 600))
    # Title Etc
    pygame.display.set_caption("Goomba Falls")
    # make colors
    SKYBLUE = (135, 206, 255)

    # makes a variable called game, and gives it the bool value "true"
    game = True
    # sets the background initially as black
    background = SKYBLUE
    # make mario
    mario_img = pygame.image.load("mario.png")
    mario = pygame.transform.scale(mario_img, (65, 75))
    m_x = 360
    m_y = 450
    m_x_change = 0
    alive = True
    mario_border_x = m_x + 65
    mario_border_y = m_y + 75

    # Raining Goombas
    goomba_img = pygame.image.load("goomba.png")
    goomba = pygame.transform.scale(goomba_img, (50, 50))
    g_x = random.randint(30, 770)
    g_x_border = g_x + 50
    g_y = 30
    g_y_border = g_y + 50
    g_y_change = .1

    # Icon for Window
    pygame.display.set_icon(goomba_img)

    # ground setup
    ground_y = 525
    ground_x = 0
    ground_img = pygame.image.load("Ground.png")
    ground_s = pygame.transform.scale(ground_img, (800, 75))

    def player():
        scr.blit(mario, (m_x, m_y))

    def enemy():
        scr.blit(goomba, (g_x, g_y))

    def ground():
        scr.blit(ground_s, (ground_x, ground_y))

    clock = pygame.time.Clock()
    # while game is equal to true, this loop will run
    while game:
        clock.tick(60)
        if g_y >= 525:
            g_x = random.randint(30, 770)
            g_y = 30
            g_y_change = 0.1
        scr.fill(background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # Makes it so that we can click X at the top right to quit out.
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:

                    m_x_change = -8

                elif event.key == pygame.K_RIGHT:

                    m_x_change = 8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    m_y_change = 0
                elif event.key == pygame.K_LEFT:
                    m_x_change = 0
                elif event.key == pygame.K_DOWN:
                    m_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    m_x_change = 0
        g_y = g_y + g_y_change
        g_y_change = g_y_change + .4
        m_x += m_x_change
        if m_x <= 0:
            m_x = 0
        elif m_x >= 750:
            m_x = 750

        ground()
        enemy()
        player()

        pygame.display.update()
        # Makes sure to make mario lose a life when he collides with one of the goombas
        if g_x >= m_x >= g_x_border and g_y >= m_y >= g_y_border:
            alive = False
        if m_x >= g_x >= mario_border_x and m_y >= g_y >= mario_border_y:
            alive = False
        if alive == False:
            game = False


pygame.quit()
if __name__ == "__main__":
    main()
