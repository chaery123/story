import random
from tkinter import font
import pygame
#################################################### 기본 초기화 
pygame.init() # 초기화

# 화면 크기 
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀
pygame.display.set_caption("케이크 피하기")

# FPS
clock = pygame.time.Clock()

###################################################

# 1. 사용자 게임 초기화

# 배경
background = pygame.image.load("C:\\Users\\skybi\\Desktop\\pythonworkspace\\pygame_basis\\backg.png")


# 캐릭터
character = pygame.image.load("C:\\Users\\skybi\\Desktop\\pythonworkspace\\pygame_basis\\cha.png")
character_size = character.get_rect().size
character_width = character_size[0] # 가로
character_height = character_size[1] # 세로
character_x_pos = (screen_width / 2) - (character_width / 2 ) # 위치 (가로 절반) 
character_y_pos = screen_height - character_height

# 이동할 좌표 
to_x = 0
character_speed = 10


# 폰트 
game_font = pygame.font.Font(None, 40) # None은 디폴트 나옴
over_font = pygame.font.Font(None, 90)
game_over = over_font.render('GAME OVER', True, (255,0,0))



# 포인트
point = 0
font_point = pygame.font.Font(None, 50)

# 총 시간
total_time = 30

# 시작 시간
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴

# 당근
carrot = pygame.image.load("C:\\Users\\skybi\\Desktop\\pythonworkspace\\pygame_basis\\carrot.png")
carrot_size = carrot.get_rect().size
carrot_width = carrot_size[0] # 가로
carrot_height = carrot_size[1] # 세로
carrot_x_pos = random.randint(0, screen_width - carrot_width)
carrot_y_pos = 0
carrot_speed = 10

# 케이크 
cake = pygame.image.load("C:\\Users\\skybi\\Desktop\\pythonworkspace\\pygame_basis\\cake.png")
cake_size = cake.get_rect().size
cake_width = cake_size[0] # 가로
cake_height = cake_size[1] # 세로
cake_x_pos = random.randint(0, screen_width - cake_width)
cake_y_pos = 0
cake_speed = 10



# 이벤트 루프 
running = True # 진행중인지
while running:
    dt = clock.tick(30) # 초당 프레임 수
    
    # 2. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생하는가
            running = False
        
        if event.type == pygame.KEYDOWN: # 키 누름
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            

        if event.type == pygame.KEYUP: # 키 안누름
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                to_x = 0
           
    
    # 3. 위치 정의
    character_x_pos += to_x 


    if character_x_pos < 0: # 화면 밖으로 안나가게
        character_x_pos = 0
    elif  character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    cake_y_pos += cake_speed

    if cake_y_pos > screen_height:
        cake_y_pos = 0
        cake_x_pos = random.randint(0, screen_width - cake_width)
    
    
    carrot_y_pos += carrot_speed

    if carrot_y_pos > screen_height:
        carrot_y_pos = 0
        carrot_x_pos = random.randint(0, screen_width - carrot_width)



    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    cake_rect = cake.get_rect()
    cake_rect.left = cake_x_pos
    cake_rect.top = cake_y_pos
    
    carrot_rect = carrot.get_rect()
    carrot_rect.left = carrot_x_pos
    carrot_rect.top = carrot_y_pos

    # 충돌 체크
    if character_rect.colliderect(cake_rect):
        running = False
    
    elif character_rect.colliderect(carrot_rect):
         point += 1
         carrot_x_pos = random.randint(0, screen_width - carrot_width )
         carrot_y_pos = 0

    #5. 그리기
    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(cake, (cake_x_pos, cake_y_pos))
    screen.blit(carrot, (carrot_x_pos, carrot_y_pos))

    # 타이머
    # 경과시간
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 초 단위로 표시하려고 나눔

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0))
    # 출력할 글자, True, 색상
    screen.blit(timer, (10, 10))


    # 포인트
    text_point = font_point.render(str(point), True, (130,130,130))
    screen.blit(text_point, (230, 30))


    # 시간 다 되면 게임 종료
    if total_time - elapsed_time <= 0:
        
        running = False

    pygame.display.update() # 계속해서 호출해야함. 다시 그리기

# 종료시 게임오버 띄우기
game_over_rect = game_over.get_rect(center=(int(screen_width /2), int(screen_height / 2)))
screen.blit(game_over, game_over_rect)
pygame.display.update()

# 끝나기 전 대기
pygame.time.delay(500)

pygame.quit()


