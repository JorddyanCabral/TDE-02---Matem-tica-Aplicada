import pygame
import numpy as np

# definindo as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# definindo as dimensões da janela
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# definindo as dimensões do objeto
OBJECT_SIZE = 100

# definindo o ponto central de reflexão
REFLECTION_CENTER = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

# inicializando o Pygame
pygame.init()

# criando a janela
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Reflexão de objeto")

# criando o botão de trocar eixo
font = pygame.font.SysFont(None, 20)
button_text = font.render("Trocar Eixo", True, WHITE)
button_rect = button_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-20))

# definindo as coordenadas do objeto
vertices = [(WINDOW_WIDTH/2-OBJECT_SIZE/2, WINDOW_HEIGHT/2-OBJECT_SIZE/2),
            (WINDOW_WIDTH/2+OBJECT_SIZE/2, WINDOW_HEIGHT/2-OBJECT_SIZE/2),
            (WINDOW_WIDTH/2+OBJECT_SIZE/2, WINDOW_HEIGHT/2+OBJECT_SIZE/2),
            (WINDOW_WIDTH/2-OBJECT_SIZE/2, WINDOW_HEIGHT/2+OBJECT_SIZE/2)]

# definindo a matriz de transformação de reflexão inicial
reflection_axis = np.array([[1, 0, 0],
                            [0, -1, 2*REFLECTION_CENTER[1]],
                            [0, 0, 1]])

# realizando a reflexão do objeto inicial
new_vertices = []
for vertex in vertices:
    v = np.array([vertex[0], vertex[1], 1])
    new_v = reflection_axis.dot(v)
    new_vertices.append((new_v[0], new_v[1]))

# função para atualizar o eixo de reflexão do objeto


def update_reflection_axis():
    global reflection_axis, new_vertices
    # criando a nova matriz de transformação de reflexão
    reflection_axis = np.array([[1, 0, 0],
                                [0, -1, 2*REFLECTION_CENTER[1]],
                                [0, 0, 1]])
    # realizando a reflexão do objeto com a nova matriz de transformação
    new_vertices = []
    for vertex in vertices:
        v = np.array([vertex[0], vertex[1], 1])
        new_v = reflection_axis.dot(v)
        new_vertices.append((new_v[0], new_v[1]))


# loop principal do programa
running = True
while running:
    # verificando se o usuário quer fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verificando se o botão foi clicado
            if button_rect.collidepoint(event.pos):
                update_reflection_axis()

    # limpando a tela
    screen.fill(BLACK)

    # desenhando o objeto original na tela
    pygame.draw.polygon(screen, GREEN, vertices, 1)

    # desenhando o objeto refletido na tela
    pygame.draw.polygon(screen, WHITE, new_vertices)

    # atualizando a tela
    pygame.display.update()

# encerrando o Pygame
pygame.quit()
