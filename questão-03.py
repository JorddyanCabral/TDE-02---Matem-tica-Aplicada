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

# definindo o ponto central de escala
SCALE_CENTER = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

# inicializando o Pygame
pygame.init()

# criando a janela
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Escala de objeto")

# criando o botão de trocar escala
font = pygame.font.SysFont(None, 20)
button_text = font.render("Trocar Escala", True, WHITE)
button_rect = button_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-20))

# definindo as coordenadas do objeto
vertices = [(WINDOW_WIDTH/2-OBJECT_SIZE/2, WINDOW_HEIGHT/2-OBJECT_SIZE/2),
            (WINDOW_WIDTH/2+OBJECT_SIZE/2, WINDOW_HEIGHT/2-OBJECT_SIZE/2),
            (WINDOW_WIDTH/2+OBJECT_SIZE/2, WINDOW_HEIGHT/2+OBJECT_SIZE/2),
            (WINDOW_WIDTH/2-OBJECT_SIZE/2, WINDOW_HEIGHT/2+OBJECT_SIZE/2)]

# definindo o fator de escala inicial
scale_factor = 2

# criando a matriz de transformação de escala inicial
T = np.array([[scale_factor, 0, (1-scale_factor)*SCALE_CENTER[0]],
              [0, scale_factor, (1-scale_factor)*SCALE_CENTER[1]],
              [0, 0, 1]])

# realizando a escala do objeto inicial
new_vertices = []
for vertex in vertices:
    v = np.array([vertex[0], vertex[1], 1])
    new_v = T.dot(v)
    new_vertices.append((new_v[0], new_v[1]))

# função para atualizar a escala do objeto


def update_scale():
    global scale_factor, T, new_vertices
    # atualizando o fator de escala
    scale_factor = 1 + (scale_factor % 4)
    # criando a nova matriz de transformação de escala
    T = np.array([[scale_factor, 0, (1-scale_factor)*SCALE_CENTER[0]],
                  [0, scale_factor, (1-scale_factor)*SCALE_CENTER[1]],
                  [0, 0, 1]])
    # realizando a escala do objeto com a nova matriz de transformação
    new_vertices = []
    for vertex in vertices:
        v = np.array([vertex[0], vertex[1], 1])
        new_v = T.dot(v)
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
                update_scale()

    # limpando a tela
    screen.fill(BLACK)

    # desenhando o objeto na tela
    pygame.draw.polygon(screen, GREEN, new_vertices)
    # desenhando o botão na tela
    pygame.draw.rect(screen, WHITE, button_rect)
    screen.blit(button_text, button_rect)

    # atualizando a tela
    pygame.display.flip()

pygame.quit()
