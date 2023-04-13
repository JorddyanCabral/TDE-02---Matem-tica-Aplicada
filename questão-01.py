import pygame

# inicializar o pygame
pygame.init()

# definir as dimensões da janela
width = 500
height = 500

# criar uma janela
window = pygame.display.set_mode((width, height))

# definir a posição inicial do objeto
x = 100
y = 100

# definir a direção da translação
dx = 5
dy = 5

# loop principal
while True:
    # lidar com eventos do pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # apagar a tela
    window.fill((255, 255, 255))

    # atualizar a posição do objeto
    x += dx
    y += dy
    print(x)
    print(y)

    # atualização da posição do objeto para o ponto inicial caso chegue próximo a borda esquerda
    if x >= 450 or y >= 450:
        x = 100
        y = 100
    # desenhar o objeto na nova posição
    pygame.draw.circle(window, (0, 0, 255), (x, y), 50)

    # atualizar a janela
    pygame.display.update()
    # limitar a taxa de atualização
    pygame.time.Clock().tick(20)
