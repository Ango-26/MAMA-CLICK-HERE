# idea to make an avoid avalanche rock game, probs include main menu, main character should be a ball
# also add a score counter in which the score is the time (s), you have survived for
# add coin counter

# warning sign before rocks occur u know like duck life



# THE CLASSES
#_____________________________________________________________________
class terminalformat:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Colours:
    WHITE = (255,255,255)
    BLACK = (0, 0, 0)
    RED = (255,0,0)
    BLUE = (0,0,255)
    LIME = (0,255,0)
    YELLOW = (255,255,0)
    CYAN = (0,255,255)
    MAGENTA = (255,0,255)
    SILVER = (192,192,192)
    GRAY = (128,128,128)
    MAROON = (128,0,0)
    OLIVE = (128,128,0)
    GREEN = (0,128,0)
    PURPLE = (128,0,128)
    TEAL = (0,128,128)
    NAVYBLUE = (0,0,128)
    SPRINGGREEN = (0,255,127)
    FORESTGREEN = (34,139,34)
    CHARTREUSE = (127,255,0)
    TURQUOISE = (64,224,208)
    DARKTURQUOISE = (0,206,209)
    CORNFLOWERBLUE = (100,149,237)
    LIGHTSKYBLUE = (135,206,250)
    AQUAMARINE = (127,255,212)
    GOLD = (255,215,0)
    GOLDENROD = (218,165,32)
    ORANGE = (255,165,0)
    CRIMSON = (220,20,60)
    LIGHTSALMON = (255,160,122)
    DARKGREEN = (0,100,0)
    VIOLET = (238,130,238)
    DEEPPINK = 	(255,20,147)
    PINK = (255,192,203)
    HOTPINK = (255,105,180)




class Ball:
    COLOUR = Colours.WHITE
    VEL = 4
    MAX_VEL = 5

    def __init__(self, x, y,radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.rect(
            pygame.draw.circle(win, self.COLOUR, (self.x, self.y), self.radius)

    def move(self, left=True):
        if left:
            self.x -= self.VEL
        else:
            self.x += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1  # might need to make -1 to 0

#________________________________________________________________________
#MAIN
#____________________________________________________________________
import pygame
pygame.init()
import sys


background_colour = (100,100,100)
WIDTH,HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Avalanche!')
screen.fill(background_colour)
pygame.display.flip()


SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE = 100  # need to make an if stattemtns which says if >= , then u win and end game.





#____________________________________________________________________________

# GAME LOOP
#____________________________________________________________________________
run = True
while run:
    FPS = 60
    pygame.clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

#_________________________________________________

# WORKING ON IT

#_________________________________________________

#def draw(win, paddles, ball, left_score, right_score):
    #win.fill(BLACK)

    #right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    #win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    #win.blit(right_score_text, (WIDTH * (3/4) -
                                #right_score_text.get_width()//2, 20))
