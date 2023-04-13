import pygame

# definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# definindo as dimensões da janela
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# definindo as dimensões do quadrado
SQUARE_SIZE = 50

# inicializando o Pygame
pygame.init()

# criando a janela
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Quadrantes")

# criando os botões
button1_rect = pygame.Rect(0, WINDOW_HEIGHT - 50, WINDOW_WIDTH // 2, 50)
button2_rect = pygame.Rect(
    WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50, WINDOW_WIDTH // 2, 50)
button3_rect = pygame.Rect(0, 0, WINDOW_WIDTH // 2, 50)
button4_rect = pygame.Rect(WINDOW_WIDTH // 2, 0, WINDOW_WIDTH // 2, 50)

# loop principal do programa
running = True
while running:
    # verificando se o usuário quer fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verificando se o botão 1 foi clicado
            if button1_rect.collidepoint(event.pos):
                pygame.draw.rect(
                    screen, BLACK, (0, WINDOW_HEIGHT // 2, SQUARE_SIZE, SQUARE_SIZE))
            # verificando se o botão 2 foi clicado
            elif button2_rect.collidepoint(event.pos):
                pygame.draw.rect(screen, BLACK, (WINDOW_WIDTH //
                                 2, WINDOW_HEIGHT // 2, SQUARE_SIZE, SQUARE_SIZE))
            # verificando se o botão 3 foi clicado
            elif button3_rect.collidepoint(event.pos):
                pygame.draw.rect(
                    screen, BLACK, (0, 0, SQUARE_SIZE, SQUARE_SIZE))
            # verificando se o botão 4 foi clicado
            elif button4_rect.collidepoint(event.pos):
                pygame.draw.rect(screen, BLACK, (WINDOW_WIDTH //
                                 2, 0, SQUARE_SIZE, SQUARE_SIZE))

    # limpando a tela
    screen.fill(WHITE)

    # desenhando os botões na tela
    pygame.draw.rect(screen, RED, button1_rect)
    pygame.draw.rect(screen, GREEN, button2_rect)
    pygame.draw.rect(screen, BLUE, button3_rect)
    pygame.draw.rect(screen, BLACK, button4_rect)

    # atualizando a janela
    pygame.display.update()

# finalizando o Pygame
pygame.quit()
