import random
import sys
import time
import pygame


def Score ():
	global Player2_score
	global Sets_Won2
	global Sets_Won1
	global Player1_score
	if Player2_score >= 11:
		ball.x = screen_width / 2 - 15
		ball.y = screen_height / 2 - 15
		Player1.x = screen_width - 100
		Player1.y = screen_height / 2 - 25
		Player2.x = 80
		Player2.y = screen_height / 2
		Sets_Won2 += 1
		Player1_score = 0
		Player2_score = 0
		pygame.mixer.Sound.play(Set_Sound)

	elif Player1_score >= 11:
		ball.x = screen_width / 2 - 15
		ball.y = screen_height / 2 - 15
		Player1.x = screen_width - 100
		Player1.y = screen_height / 2 - 25
		Player2.x = 80
		Player2.y = screen_height / 2
		Sets_Won1 += 1
		Player1_score = 0
		Player2_score = 0
		pygame.mixer.Sound.play(Set_Sound)

	if Sets_Won1 >= 3:
		ball.x = screen_width / 2 - 15
		ball.y = screen_height / 2 - 15
		Player1.x = screen_width - 100
		Player1.y = screen_height / 2 - 25
		Player2.x = 80
		Player2.y = screen_height / 2
		WINNER_GREEN_TEXT = winner_text.render(f"{WE}", False, 'green')
		screen.blit(WINNER_GREEN_TEXT, (screen_width / 2 - 320, screen_height / 2 - 64))

	if Sets_Won2 >= 3:
		ball.x = screen_width / 2 - 15
		ball.y = screen_height / 2
		Player1.x = screen_width - 100
		Player1.y = screen_height / 2 - 25
		Player2.x = 80
		Player2.y = screen_height / 2
		WINNER_BLUE_TEXT = winner_text.render(f"{WB}", False, 'blue')
		screen.blit(WINNER_BLUE_TEXT, (screen_width / 2 - 320, screen_height / 2 - 64))

def Player1_Ani():

	Player1.y += Player1y_speed
	Player1.x += Player1x_speed

	if Player1.top <= 0:
		Player1.top = 0 + 5

	if Player1.bottom >= screen_height:
		Player1.bottom = screen_height - 5

	if Player1.right >= screen_width:
		Player1.right = screen_width - 5

	if Player1.left <= screen_width / 2:
		Player1.left = screen_width / 2 + 5

def Player2_Ani():

	Player2.y += Player2y_speed
	Player2.x += Player2x_speed
	if Player2.top <= 0:
		Player2.top = 0 + 5

	if Player2.bottom >= screen_height:
		Player2.bottom = screen_height - 5

	if Player2.left <= 0:
		Player2.left = 5

	if Player2.right >= screen_width / 2:
		Player2.right = screen_width  /2 - 5

def Ball_Ani():

	global Bally_speed, Ballx_speed
	ball.x += Ballx_speed
	ball.y += Bally_speed
	if ball.top <= 0:
		Bally_speed *= -1
		pygame.mixer.Sound.play(Bounce_Edge)
	if ball.bottom >= screen_height:
		Bally_speed *= -1
		pygame.mixer.Sound.play(Bounce_Edge)
	if ball.left <= 0:
		Ballx_speed *= -1
		pygame.mixer.Sound.play(Bounce_Edge)
	if ball.right >= screen_width:
		Ballx_speed *= -1
		pygame.mixer.Sound.play(Bounce_Edge)

def Collision():

	global Bally_speed
	global Ballx_speed

	if ball.colliderect(Player1):

		if ball.right >= Player1.left and old_shape_Ball.right <= old_shape_P1.left:
			ball.right = Player1.left
			Ballx_speed += -10
			Bally_speed += random.choice((-0.1, 0.1))


		if ball.left <= Player1.right and old_shape_Ball.left >= old_shape_P1.right:
			ball.left = Player1.right
			Ballx_speed += 10
			Bally_speed += random.choice((-0.1, 0.1))


		if ball.top <= Player1.bottom and old_shape_Ball.top >= old_shape_P1.bottom:
			ball.top = Player1.bottom
			Bally_speed += -10
			Bally_speed += random.choice((-0.1, 0.1))

		if ball.bottom >= Player1.top and old_shape_Ball.bottom <= old_shape_P1.top:
			ball.bottom = Player1.top
			Bally_speed += 10
			Bally_speed += random.choice((-0.1, 0.1))

	if ball.colliderect(Player2):

		if ball.right >= Player2.left and old_shape_Ball.right <= old_shape_P2.left:
			ball.right = Player2.left
			Ballx_speed += -10
			Bally_speed += random.choice((-0.1, 0.1))


		if ball.left <= Player2.right and old_shape_Ball.left >= old_shape_P2.right:
			ball.left = Player2.right
			Ballx_speed += 10
			Bally_speed += random.choice((-0.1, 0.1))


		if ball.top <= Player2.bottom and old_shape_Ball.top >= old_shape_P2.bottom:
			ball.top = Player2.bottom
			Bally_speed += 10
			Bally_speed += random.choice((-0.1, 0.1))

		if ball.bottom >= Player2.top and old_shape_Ball.bottom <= old_shape_P2.top:
			ball.bottom = Player2.top
			Bally_speed += -10
			Bally_speed += random.choice((-0.1, 0.1))

def Goaal():

	global Player1_score
	global Player2_score
	global Ballx_speed
	global Bally_speed
	global screen_height
	global countdown
	global New_Play
	global Current_second

	if ball.colliderect(Goal1):

		Player2_score += 1
		ball.x = screen_width / 2 - 15
		ball.y = screen_height / 2 - 15

		Player1.x = screen_width - 100
		Player1.y = screen_height / 2 - 25

		Player2.x = 80
		Player2.y = screen_height / 2

		New_Play = pygame.time.get_ticks()
		Ballx_speed = 0
		Bally_speed = 0
		countdown = pygame.time.get_ticks()
		pygame.mixer.Sound.stop(Ball_movement)

		if Player2_score <= 11:
			pygame.mixer.Sound.play(Score_Sound)

	elif ball.colliderect(Goal2):
		Player1_score += 1
		ball.x = screen_width / 2 - 15
		ball.y = screen_height / 2 - 15
		Player1.x = screen_width - 100
		Player1.y = screen_height / 2 - 25
		Player2.x = 80
		Player2.y = screen_height / 2
		New_Play = pygame.time.get_ticks()
		Ballx_speed = 0
		Bally_speed = 0
		countdown = pygame.time.get_ticks()
		pygame.mixer.Sound.stop(Ball_movement)
		if Player1_score <= 11:
			pygame.mixer.Sound.play(Score_Sound)

def Ball_Start():

	global Bally_speed
	global Ballx_speed
	global current_time
	global countdown

	current_time = pygame.time.get_ticks()
	TImer_font = pygame.font.Font("freesansbold.ttf", 32)

	if current_time - countdown < 700:
		Three = TImer_font.render("3", False, white)
		screen.blit(Three, (screen_width / 2 - 8, screen_height / 2 + 128))
	if 700 < current_time - countdown < 1400:
		Two = TImer_font.render("2", False, white)
		screen.blit(Two, (screen_width / 2 - 8, screen_height / 2 + 128))

	if 1400 < current_time - countdown < 2100:
		One = TImer_font.render("1", False, white)
		screen.blit(One, (screen_width / 2 - 8, screen_height / 2 + 128))

	if current_time - countdown < 2100:
		Ballx_speed = 0
		Bally_speed = 0
	else:
		Ballx_speed = 6 * random.choice((-1, 1))
		Bally_speed = 6 * random.choice((-1, 1))
		countdown = None



# Pygame Setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# Screen Initials
screen_width = 1800
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
FPS = 60

# Background Color
bg_color = (random.uniform(20,40), random.uniform(20,40), random.uniform(20,40))

# The Objects for the collision Rects
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)

Player1 = pygame.Rect(screen_width - 100, screen_height / 2 - 25, 50, 50)
Player2 = pygame.Rect(80, screen_height / 2, 50, 50)

Goal1 = pygame.Rect(screen_width - 10, 260, 10, 400)
Goal2 = pygame.Rect(2.4, 260, 10, 400)

# assigning each Player and the ball a x and y speed which will increment their Position
Player1y_speed = 0
Player1x_speed = 0

Player2y_speed = 0
Player2x_speed = 0

Ballx_speed = 0
Bally_speed = 0

# old Rects for Collisions
old_shape_Ball = ball.copy()
old_shape_P1 = Player1.copy()
old_shape_P2 = Player2.copy()
tolerance = 2


# Sound
Bounce_Edge = pygame.mixer.Sound("Bounce.ogg")
Score_Sound = pygame.mixer.Sound("Point.ogg")
Player_movement = pygame.mixer.Sound('Player_Movement.ogg')
Set_Sound = pygame.mixer.Sound('Set_won.ogg')
Ball_movement = pygame.mixer.Sound('Ball_Movement.ogg')


# Score
Player1_score = 0
Player2_score = 0

# Sets
Sets_Won1 = 0
Sets_Won2 = 0

# Text
WB = 'Winner is Blue'
WE = 'Winner is Green'
winner_text = pygame.font.Font("freesansbold.ttf", 90)
game_Text = pygame.font.Font("freesansbold.ttf", 32)

# Countdown
Current_second = 0
New_Play = 0
countdown = True

# Decoration
C1 = pygame.surface.Surface((100, 100))
C2 = pygame.surface.Surface((98, 98))
C1r = pygame.transform.rotate(C1, 0)
C2r = pygame.transform.rotate(C2, 0)
C1r.fill('white')
C2r.fill(bg_color)

# Caption
pygame.display.set_caption("Rectslider")

# Colors
green = (0, 150, 0)
blue = (0, 0, 200)
red = (150, 0, 0)
yellow = (75, 75, 0)
black = (0,0,0)
white = (255,255,255)

while True:
	last_time = time.time()
	dt = time.time() - last_time

	for Event in pygame.event.get():
		if Event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif Event.type == pygame.KEYDOWN:
			Player_movement.play(-1)

			if Event.key == pygame.K_UP:
				Player1y_speed -= 10
			if Event.key == pygame.K_DOWN:
				Player1y_speed += 10
			if Event.key == pygame.K_RIGHT:
				Player1x_speed += 10
			if Event.key == pygame.K_LEFT:
				Player1x_speed -= 10


			if Event.key == pygame.K_w:
				Player2y_speed -= 10
			if Event.key == pygame.K_s:
				Player2y_speed += 10
			if Event.key == pygame.K_d:
				Player2x_speed += 10
			if Event.key == pygame.K_a:
				Player2x_speed -= 10

		elif Event.type == pygame.KEYUP:
			Player_movement.stop()
			if Event.key == pygame.K_UP:
				Player1y_speed += 10
			if Event.key == pygame.K_DOWN:
				Player1y_speed -= 10
			if Event.key == pygame.K_RIGHT:
				Player1x_speed -= 10
			if Event.key == pygame.K_LEFT:
				Player1x_speed += 10




			if Event.key == pygame.K_w:
				Player2y_speed += 10
			if Event.key == pygame.K_s:
				Player2y_speed -= 10
			if Event.key == pygame.K_d:
				Player2x_speed -= 10
			if Event.key == pygame.K_a:
				Player2x_speed += 10

	Goaal()
	Player1_Ani()
	Player2_Ani()
	Ball_Ani()
	Collision()


	screen.fill(bg_color)

	# Drawing
	pygame.draw.aaline(screen, (200, 200, 200), (screen_width / 2, 0), (screen_width / 2, screen_height))
	screen.blit(C1r, (screen_width / 2 - 50, screen_height / 2 - 50))
	screen.blit(C2r, (screen_width / 2 - 49, screen_height / 2 - 49))

	pygame.draw.rect(screen, (0, 100, 0), Player1)
	pygame.draw.rect(screen, (0, 0, 100), Player2)
	pygame.draw.rect(screen, (255, 255, 255), ball)
	pygame.draw.rect(screen, (0, 100, 0), Goal1)
	pygame.draw.rect(screen, (0, 0, 100), Goal2)

	Player1_Text = game_Text.render(f"{Player1_score}", False, green)
	screen.blit(Player1_Text, (screen_width - 33, 77))

	Player2_Text = game_Text.render(f"{Player2_score}", False, blue)
	screen.blit(Player2_Text, (33, 77))

	Set1_Text = game_Text.render(f"{Sets_Won1}", False, green)
	screen.blit(Set1_Text, (screen_width - 33, 33))

	Set2_Text = game_Text.render(f"{Sets_Won2}", False, blue)
	screen.blit(Set2_Text, (33, 33))
	Score()
	if countdown:
		Ball_Start()
	Current_second = pygame.time.get_ticks()

	pygame.display.flip()
	clock.tick(FPS)
