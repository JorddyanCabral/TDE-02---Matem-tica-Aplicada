import pygame

# definindo as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

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

# criando os botões dos quadrantes
button_size = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
button1_rect = pygame.Rect(0, WINDOW_HEIGHT//2, *button_size)
button2_rect = pygame.Rect(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, *button_size)
button3_rect = pygame.Rect(0, 0, *button_size)
button4_rect = pygame.Rect(WINDOW_WIDTH//2, 0, *button_size)

# criando as superfícies dos botões
button1_surf = pygame.Surface(button_size)
button2_surf = pygame.Surface(button_size)
button3_surf = pygame.Surface(button_size)
button4_surf = pygame.Surface(button_size)

# preenchendo as superfícies dos botões
button1_surf.fill(RED)
button2_surf.fill(GREEN)
button3_surf.fill(BLUE)
button4_surf.fill(WHITE)

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
                square_rect = pygame.Rect(
                    0, WINDOW_HEIGHT//2, SQUARE_SIZE, SQUARE_SIZE)
            # verificando se o botão 2 foi clicado
            elif button2_rect.collidepoint(event.pos):
                square_rect = pygame.Rect(
                    WINDOW_WIDTH//2, WINDOW_HEIGHT//2, SQUARE_SIZE, SQUARE_SIZE)
            # verificando se o botão 3 foi clicado
            elif button3_rect.collidepoint(event.pos):
                square_rect = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
            # verificando se o botão 4 foi clicado
            elif button4_rect.collidepoint(event.pos):
                square_rect = pygame.Rect(
                    WINDOW_WIDTH//2, 0, SQUARE_SIZE, SQUARE_SIZE)

    # limpando a tela
    screen.fill(WHITE)

    # desenhando os botões dos quadrantes na tela
    screen.blit(button1_surf, button1_rect)
    screen.blit(button2_surf, button2_rect)
    screen.blit(button3_surf, button3_rect)
    screen.blit(button4_surf, button4_rect)

    # desenhando o quadrado preto na tela
    if 'square_rect' in locals():
        pygame.draw.rect(screen, BLACK, square_rect)

    # atualizando a janela
    pygame.display.update()

# finalizando o Pygame
pygame.quit()
