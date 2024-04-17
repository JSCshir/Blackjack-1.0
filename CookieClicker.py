import pygame
from pygame.locals import *
import random

pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Cookie Clicker')

pos = []
count = 0
mult = 1
cost = 25

clicked = False
run = True
font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 20) 
    

def backdrop():
    bg = (240,190,100)
    screen.fill(bg)
    numberOfStars = random.randint(35, 55)    
    for i in range(numberOfStars):            
        a = random.randint(3, 12)
        x = random.randint(5, screen_width - 12)
        y = random.randint(5, screen_height - 12)         
        starRect = pygame.Rect(x, y, a, a) 
        pygame.draw.rect(screen, "White", starRect)
    
    #cookie
    cookie = (150,60,0)
    pygame.draw.circle(screen, cookie, (screen_width//4, screen_height//4 + 50), screen_width//4 - 25)



def display_click_upgrade():
    #box
    upgrade_box = Rect(screen_width//2 + 50, screen_height//2 + 150, 190, 50)
    upgrade_text = 'Upgrade Click'
    upgrade_image = font.render(upgrade_text, True, (0, 68, 156))
    pygame.draw.rect(screen, (224, 255, 161), upgrade_box)
    screen.blit(upgrade_image, (screen_width//2 + 50, screen_height//2 + 160))

    #multiplier
    multiplier = 'x' + str(round(mult,2)) 
    mult_amt = font.render(multiplier, True, (0,0,0))
    screen.blit(mult_amt, (screen_width//2 + 50, screen_height//2 + 120))
   
    #cost
    cost1 = '$' + str(round(cost)) 
    cost_amt = font.render(cost1, True, (0,0,0))
    screen.blit(cost_amt, (screen_width//2 + 50, screen_height//2 + 200))


def display_count():
    num_cookies = str(round(count)) + ' cookies!'
    cookie_count = font.render(num_cookies, True, (0,0,0))
    screen.blit(cookie_count, (screen_width//4 - 75, screen_height//4 - 100))


while run:   
    backdrop()
    display_count()
    display_click_upgrade()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clciked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if (cell_x < 225 and cell_x > 25) and (cell_y < 275 and cell_y > 75):
                count+=round(1*mult)
            if (cell_x < (screen_width - 10) and cell_x > 300) and (cell_y < 450 and cell_y > 400) and count >= cost:
                mult = mult*1.11
                count -= cost
                cost = cost*1.1
            
    pygame.display.update()
                
pygame.quit()
