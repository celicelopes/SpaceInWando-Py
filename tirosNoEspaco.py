import pygame, random, math, sys
from pygame import mixer

#iniciar modulos
pygame.init()
mixer.init()

#carrega musica
mixer.music.load('fundo_de_tela.wav')
#repete a musica pra sempre
mixer.music.play(-1)

#variavel
score = 0
check = False
bala_x= 386
bala_y= 490
nave_x = 370
nave_y = 480
largura = 800
altura = 600

#tela setup
tela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Jogo maneiro de tiro')

#carregar icone
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

fundo_de_tela = pygame.image.load('bg.png')
nave_imagem = pygame.image.load('wando.png')
bala_imagem = pygame.image.load('bullet.png')

velocidade = 0
rodando = True

font = pygame.font.SysFont('Arial',32,'bold')


while rodando:
    
    tela.blit(fundo_de_tela,(0,0))

    for event in pygame.event.get():
        #botão de fechar
        if event.type == pygame.QUIT:
            rodando = False
            pygame.quit()
            sys.exit()
        
    #controle da movimentação
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocidade-=5
            if event.key == pygame.K_RIGHT:
                velocidade+=5
            if event.key == pygame.K_SPACE:
                if check is False:
                    bala_som = mixer.Sound('laser.wav')
                    bala_som.play()
                    check = True
                    bala_x=nave_x+99/2
                
            
        if event.type==pygame.KEYUP:
            velocidade=0
            
    nave_x+=velocidade
        
    if nave_x <=0:
        nave_x = 0
    elif nave_x>= largura-99:
        nave_x = largura-99
        
    #lógica da bala
    if bala_y<=0:
        bala_y = nave_y
        check = False
    if check:
        tela.blit(bala_imagem,(bala_x,bala_y))
        bala_y-=50
                
    #desenhando a nave
    tela.blit(nave_imagem,(nave_x,nave_y))
    pygame.display.update()
    