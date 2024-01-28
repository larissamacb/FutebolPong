import pygame
pygame.init()

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Football Pong")

field = pygame.image.load("assets/assets/field.png")

score1 = 0
score1_img = pygame.image.load("assets/assets/score/0.png")
score2 = 0
score2_img = pygame.image.load("assets/assets/score/0.png")

win = pygame.image.load("assets/assets/win.png")

player1 = pygame.image.load("assets/assets/player1.png")
player1_y = 287
player1_moveup = False
player1_movedown = False

player2 = pygame.image.load("assets/assets/player2.png")
player2_y = 287

ball = pygame.image.load("assets/assets/ball.png")
ball_x = 617
ball_y = 337
ball_direction = -3
ball_direction_y = 1

def move_player():
    global player1_y

    if player1_moveup:
        player1_y -= 5
    else:
        player1_y += 0

    if player1_movedown:
        player1_y += 5
    else:
        player1_y += 0

    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

def move_player2():
    global player2_y
    player2_y = ball_y

def move_ball():
    global ball_x
    global ball_y
    global ball_direction
    global ball_direction_y
    global score1
    global score2
    global score1_img
    global score2_img

    ball_x += ball_direction
    ball_y += ball_direction_y

    if ball_x < 120:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_direction *= -1

    if ball_x > 1100:
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_direction *= -1


    if ball_y > 680:
        ball_direction_y *= -1
    elif ball_y <= 0:
        ball_direction_y *= -1

    if ball_x < -50:
        ball_x = 617
        ball_y = 337
        ball_direction *= -1
        ball_direction_y *= -1
        score2 += 1
        score2_img = pygame.image.load("assets/assets/score/" + str(score2) + ".png")

    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_direction *= -1
        ball_direction_y *= -1
        score1 += 1
        score1_img = pygame.image.load("assets/assets/score/" + str(score1) + ".png")


def draw():
    if score1 or score2 < 9:
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1150, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))
        move_ball()
        move_player()
        move_player2()
    else:
        window.blit(win, (300, 330))



loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False


    draw()
    pygame.display.update()

