import pygame
import math

# inicializar o pygame
pygame.init()

# definir as dimensões da janela
width = 500
height = 500

# criar uma janela
window = pygame.display.set_mode((width, height))

# definir as coordenadas do centro do quadrado
center_x = 250
center_y = 250

# definir as dimensões do quadrado
size = 100

# definir o ângulo de rotação em graus
angle_degrees = 0

# definir a quantidade de rotação por atualização em graus
rotation_speed = 1

# definir as coordenadas dos vértices do quadrado
vertices = [
    (center_x - size/2, center_y - size/2),
    (center_x + size/2, center_y - size/2),
    (center_x + size/2, center_y + size/2),
    (center_x - size/2, center_y + size/2)
]

# loop principal
while True:
    # lidar com eventos do pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # apagar a tela
    window.fill((255, 255, 255))

    # criar a matriz de rotação
    angle_radians = math.radians(angle_degrees)
    rotation_matrix = [
        [math.cos(angle_radians), -math.sin(angle_radians)],
        [math.sin(angle_radians), math.cos(angle_radians)]
    ]

    # rotacionar os vértices do quadrado em torno do centro
    rotated_vertices = []
    for vertex in vertices:
        # subtrair as coordenadas do centro do quadrado
        x = vertex[0] - center_x
        y = vertex[1] - center_y

        # multiplicar as coordenadas pela matriz de rotação
        x_new = x * rotation_matrix[0][0] + y * rotation_matrix[0][1]
        y_new = x * rotation_matrix[1][0] + y * rotation_matrix[1][1]

        # adicionar as coordenadas do centro de volta
        x_new += center_x
        y_new += center_y

        rotated_vertices.append((x_new, y_new))

    # desenhar o quadrado na nova posição
    pygame.draw.polygon(window, (0, 0, 255), rotated_vertices)

    # atualizar o ângulo de rotação
    angle_degrees += rotation_speed

    # atualizar a janela
    pygame.display.update()

    # limitar a taxa de atualização
    pygame.time.Clock().tick(60)
