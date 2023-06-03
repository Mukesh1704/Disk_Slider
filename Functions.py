import main as m
import pygame
from main import Player2
from main import Player1
from main import ball
from main import screen_height
from main import screen_width
import random


def Score ():
	global Player2_score
	global Sets_Won2
	global Sets_Won1
	global Player1_score

	if m.Player2_score >= 5:
		ball.x = m.screen_width / 2 - 15
		ball.y = m.screen_height / 2 - 15
		Player1.x = m.screen_width - 100
		Player1.y = m.screen_height / 2 - 25
		Player2.x = 80
		Player2.y = screen_height / 2
		m.Sets_Won2 += 1
		m.Player1_score = 0
		m.Player2_score = 0
		pygame.mixer.Sound.play(m.Set_Sound)

	elif Player1_score >= 5:
		m.ball.x = m.screen_width / 2 - 15
		m.ball.y = m.screen_height / 2 - 15
		m.Player1.x = m.screen_width - 100
		m.Player1.y = m.screen_height / 2 - 25
		m.Player2.x = 80
		m.Player2.y = screen_height / 2
		Sets_Won1 += 1
		Player1_score = 0
		Player2_score = 0
		pygame.mixer.Sound.play(m.Set_Sound)

	if Sets_Won1 >= 3:
		m.ball.x = m.screen_width / 2 - 15
		m.ball.y = m.screen_height / 2 - 15
		m.Player1.x = m.screen_width - 100
		m.Player1.y = screen_height / 2 - 25
		m.Player2.x = 80
		m.Player2.y = screen_height / 2
		WINNER_GREEN_TEXT = m.winner_text.render(f"{m.WE}", False, 'green')
		m.screen.blit(WINNER_GREEN_TEXT, (m.screen_width / 2 - 320, screen_height / 2 - 64))

	if Sets_Won2 >= 3:
		m.ball.x = m.screen_width / 2 - 15
		m.ball.y = m.screen_height / 2
		m.Player1.x = m.screen_width - 100
		m.Player1.y = m.screen_height / 2 - 25
		m.Player2.x = 80
		m.Player2.y = screen_height / 2
		WINNER_BLUE_TEXT = m.winner_text.render(f"{m.WB}", False, 'blue')
		m.screen.blit(WINNER_BLUE_TEXT, (m.screen_width / 2 - 320, screen_height / 2 - 64))

def Player1_Ani():
	m.Player1.y += m.Player1y_speed
	m.Player1.x += m.Player1x_speed

	if m.Player1.top <= 0:
		m.Player1.top = 0 + 5

	if m.Player1.bottom >= m.screen_height:
		m.Player1.bottom = m.screen_height - 5

	if m.Player1.right >= m.screen_width:
		m.Player1.right = m.screen_width - 5

	if m.Player1.left <= m.screen_width / 2:
		m.Player1.left = m.screen_width / 2 + 5

def Player2_Ani():
	m.Player2.y += m.Player2y_speed
	m.Player2.x += m.Player2x_speed
	if m.Player2.top <= 0:
		m.Player2.top = 0 + 5

	if m.Player2.bottom >= screen_height:
		m.Player2.bottom = screen_height - 5

	if m.Player2.left <= 0:
		m.Player2.left = 5

	if m.Player2.right >= m.screen_width / 2:
		m.Player2.right = m.screen_width / 2 - 5

def Ball_Ani():
	global Bally_speed, Ballx_speed
	m.ball.x += Ballx_speed
	m.ball.y += Bally_speed
	if m.ball.top <= 0:
		Bally_speed *= -1
		pygame.mixer.Sound.play(m.Bounce_Edge)
	if m.ball.bottom >= screen_height:
		Bally_speed *= -1
		pygame.mixer.Sound.play(m.Bounce_Edge)
	if m.ball.left <= 0:
		Ballx_speed *= -1
		pygame.mixer.Sound.play(m.Bounce_Edge)
	if m.ball.right >= m.screen_width:
		Ballx_speed *= -1
		pygame.mixer.Sound.play(m.Bounce_Edge)

def Collision():
	global Bally_speed
	global Ballx_speed

	if m.ball.colliderect(Player1):

		if m.ball.right >= Player1.left and m.old_shape_Ball.right <= m.old_shape_P1.left:
			ball.right = Player1.left
			Ballx_speed += -10
			Bally_speed += random.choice((-0.1, 0.1))


		if ball.left <= Player1.right and m.old_shape_Ball.left >= m.old_shape_P1.right:
			ball.left = Player1.right
			Ballx_speed += 10
			Bally_speed += random.choice((-0.1, 0.1))


		if ball.top <= Player1.bottom and m.old_shape_Ball.top >= m.old_shape_P1.bottom:
			ball.top = Player1.bottom
			Bally_speed += -10
			Bally_speed += random.choice((-0.1, 0.1))

		if ball.bottom >= Player1.top and m.old_shape_Ball.bottom <= m.old_shape_P1.top:
			ball.bottom = Player1.top
			Bally_speed += 10
			Bally_speed += random.choice((-0.1, 0.1))

	if ball.colliderect(Player2):

		if ball.right >= Player2.left and m.old_shape_Ball.right <= m.old_shape_P2.left:
			ball.right = Player2.left
			Ballx_speed += -10
			Bally_speed += random.choice((-0.1, 0.1))


		if ball.left <= Player2.right and m.old_shape_Ball.left >= m.old_shape_P2.right:
			ball.left = Player2.right
			Ballx_speed += 10
			Bally_speed += random.choice((-0.1, 0.1))


		if ball.top <= Player2.bottom and m.old_shape_Ball.top >= m.old_shape_P2.bottom:
			ball.top = Player2.bottom
			Bally_speed += 10
			Bally_speed += random.choice((-0.1, 0.1))

		if ball.bottom >= Player2.top and m.old_shape_Ball.bottom <= m.old_shape_P2.top:
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

	if ball.colliderect(m.Goal1):

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
		pygame.mixer.Sound.stop(m.Ball_movement)

		if Player2_score <= 4:
			pygame.mixer.Sound.play(m.Score_Sound)

	elif ball.colliderect(m.Goal2):
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
		pygame.mixer.Sound.stop(m.Ball_movement)
		if Player1_score <= 4:
			pygame.mixer.Sound.play(m.Score_Sound)

def Ball_Start():
	global Bally_speed
	global Ballx_speed
	global current_time
	global countdown

	current_time = pygame.time.get_ticks()
	TImer_font = pygame.font.Font("freesansbold.ttf", 64)

	if current_time - m.countdown < 700:
		Three = TImer_font.render("3", False, (255, 255, 255))
		m.screen.blit(Three, (screen_width / 2 - 32, screen_height / 2 - 32))
	if 700 < current_time - m.countdown < 1400:
		Two = TImer_font.render("2", False, (255, 255, 255))
		m.screen.blit(Two, (screen_width / 2 - 32, screen_height / 2 - 32))

	if 1400 < current_time - m.countdown < 2100:
		One = TImer_font.render("1", False, (255, 255, 255))
		m.screen.blit(One, (screen_width / 2 - 32, screen_height / 2 - 32))

	if current_time - countdown < 2100:
		Ballx_speed = 0
		Bally_speed = 0
	else:
		Ballx_speed = 6 * random.choice((-1, 1))
		Bally_speed = 6 * random.choice((-1, 1))
		countdown = None
