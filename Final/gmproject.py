from tkinter import N
import show 
import pygame, sys, random, time
from pygame.locals import *
import time
WINDOWX = 1920 
WINDOWY = 1080
FPS = 300 
TILEWIDTH = 50   
TILEHEIGHT = 50    
TILEFLOORHEIGHT = 49.8
#RGB values for colours
#            R    G    B
GRAY     = (100, 100, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
BLACK    = (  0,   0,   0)
BGMAIN = WHITE
BGTEXT = (255, 181, 181) 
BGHL = RED 
item_count = 0
key_count = 0
corr = 0
done = False



class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

def main():
    pygame.init()
    global di, s, finishFont, COLOR_INACTIVE, COLOR_ACTIVE, FONT, level, sprite, clock, TILEDICT, titleFont, textFont, c_forest, c_desertSprite, c_spaceSprite, SPRITEDICT, MAPWIDTH, MAPHEIGHT, difficulty
    clock = pygame.time.Clock()
    COLOR_INACTIVE = pygame.Color('lightskyblue3')
    COLOR_ACTIVE = pygame.Color('dodgerblue2')
    FONT = pygame.font.Font(None, 32)
#fonts and sprites are loaded
    finishFont = pygame.font.Font('./fonts/Galmuri.ttc', 30) 
    titleFont = pygame.font.Font('./fonts/ChangwonDangamAsac-Bold_0712.ttf', 50)
    textFont = pygame.font.Font('./fonts/ChangwonDangamAsac-Bold_0712.ttf', 30)
    c_forest = pygame.image.load('./sprites/daramgi.png')
    c_forest = pygame.transform.scale(c_forest, (50, 50))
    c_desertSprite = pygame.image.load('./sprites/fox.png')
    c_desertSprite = pygame.transform.scale(c_desertSprite, (50, 50))
    c_spaceSprite = pygame.image.load('./sprites/ufo.png')
    c_spaceSprite = pygame.transform.scale(c_spaceSprite, (50, 50))    

    SPRITEDICT = {'c_forest': c_forest, 'c_desert': c_desertSprite, 'c_space': c_spaceSprite}
    
    difficulty  = startup()
    sprite = how2play(difficulty)
    level, MAPWIDTH, MAPHEIGHT, di = loadLevelFile(difficulty)
    
    if di == 'easy':
        pygame.mixer.music.load('./sounds/Easy.mp3')
        wallSprite = pygame.image.load('./sprites/forest_wall.png')
        wallSprite = pygame.transform.scale(wallSprite, (50, 50))
        tileSprite = pygame.image.load('./sprites/forest_tile.png') 
        tileSprite = pygame.transform.scale(tileSprite, (50, 50))
        SideBlockSprite = pygame.image.load('./sprites/side_wall.png')
        SideBlockSprite = pygame.transform.scale(SideBlockSprite, (50, 50))
        boxSprite = pygame.image.load('./sprites/box.png')
        boxSprite = pygame.transform.scale(boxSprite, (50, 50))
        flipboxSprite = pygame.transform.flip(boxSprite, True, False)
        finishSprite = pygame.image.load('./sprites/exit.png')
        finishSprite = pygame.transform.scale(finishSprite, (50, 50))
        openboxSprite = pygame.image.load('./sprites/open_box.png')
        openboxSprite = pygame.transform.scale(openboxSprite, (50, 50))
        flipopenboxSprite = pygame.transform.flip(openboxSprite, True, False)
        keySprite = pygame.image.load('./sprites/key.png')
        keySprite = pygame.transform.scale(keySprite, (50, 50))
        itemSprite = pygame.image.load('./sprites/item_axe.png')
        itemSprite = pygame.transform.scale(itemSprite, (50, 50))
        virtual_block = pygame.image.load('./sprites/forest_virtual.png')
        virtual_block = pygame.transform.scale(virtual_block, (50, 50))
        howtoplay = pygame.image.load('./sprites/howtoplay_1.png')
        howtoplay = pygame.transform.scale(howtoplay, (1920, 1080))
        TILEDICT = {'#':wallSprite, ' ': tileSprite, '>': flipboxSprite, '<': boxSprite, 'f':flipopenboxSprite,
        'o':openboxSprite, 'g': SideBlockSprite, '$': finishSprite, 'k': keySprite, 'i' : itemSprite, 'v': virtual_block}
    elif di =='normal':
        pygame.mixer.music.load('./sounds/Normal.mp3')
        wallSprite = pygame.image.load('./sprites/desert_wall.png')
        wallSprite = pygame.transform.scale(wallSprite, (50, 50))
        tileSprite = pygame.image.load('./sprites/desert_back.png') 
        tileSprite = pygame.transform.scale(tileSprite, (50, 50))
        SideBlockSprite = pygame.image.load('./sprites/side_wall.png')
        SideBlockSprite = pygame.transform.scale(SideBlockSprite, (50, 50))
        boxSprite = pygame.image.load('./sprites/box.png')
        boxSprite = pygame.transform.scale(boxSprite, (50, 50))
        finishSprite = pygame.image.load('./sprites/exit.png')
        finishSprite = pygame.transform.scale(finishSprite, (50, 50))
        openboxSprite = pygame.image.load('./sprites/open_box.png')
        openboxSprite = pygame.transform.scale(openboxSprite, (50, 50))
        keySprite = pygame.image.load('./sprites/key.png')
        keySprite = pygame.transform.scale(keySprite, (50, 50))
        itemSprite = pygame.image.load('./sprites/item_desert.png')
        itemSprite = pygame.transform.scale(itemSprite, (50, 50))
        virtual_block = pygame.image.load('./sprites/desert_virtual.png')
        virtual_block = pygame.transform.scale(virtual_block, (50, 50))
        flipboxSprite = pygame.transform.flip(boxSprite, True, False)
        flipopenboxSprite = pygame.transform.flip(openboxSprite, True, False)
        TILEDICT = {'#':wallSprite, ' ': tileSprite, '>': flipboxSprite, '<': boxSprite, 'f':flipopenboxSprite,
        'o':openboxSprite, 'g': SideBlockSprite, '$': finishSprite, 'k': keySprite, 'i' : itemSprite, 'v': virtual_block}
    else:
        pygame.mixer.music.load('./sounds/Hard.mp3')
        wallSprite = pygame.image.load('./sprites/stone.png')
        wallSprite = pygame.transform.scale(wallSprite, (50, 50))
        tileSprite = pygame.image.load('./sprites/space_tile.png')
        tileSprite = pygame.transform.scale(tileSprite, (50, 50))
        SideBlockSprite = pygame.image.load('./sprites/side_wall.png')
        SideBlockSprite = pygame.transform.scale(SideBlockSprite, (50, 50))
        boxSprite = pygame.image.load('./sprites/box.png')
        boxSprite = pygame.transform.scale(boxSprite, (50, 50))
        finishSprite = pygame.image.load('./sprites/exit.png')
        finishSprite = pygame.transform.scale(finishSprite, (50, 50))
        openboxSprite = pygame.image.load('./sprites/open_box.png')
        openboxSprite = pygame.transform.scale(openboxSprite, (50, 50))
        keySprite = pygame.image.load('./sprites/key.png')
        keySprite = pygame.transform.scale(keySprite, (50, 50))
        itemSprite = pygame.image.load('./sprites/move.png')
        itemSprite = pygame.transform.scale(itemSprite, (50, 50))
        virtual_block = pygame.image.load('./sprites/desert_virtual.png')
        virtual_block = pygame.transform.scale(virtual_block, (50, 50))
        flipboxSprite = pygame.transform.flip(boxSprite, True, False)
        flipopenboxSprite = pygame.transform.flip(openboxSprite, True, False)
        TILEDICT = {'#':wallSprite, ' ': tileSprite, '>': flipboxSprite, '<': boxSprite, 'f':flipopenboxSprite, 
        'o':openboxSprite, 'g': SideBlockSprite, '$': finishSprite, 'k': keySprite, 'm' : itemSprite}

    pygame.mixer.music.play(-1, 0.0)
    blockSound = pygame.mixer.Sound('./sounds/blocked.mp3')

    #focusCamera(level)
    keyPressed = False
    box = False
    item = False
    wongame = False
    drawscreen(level)
    start = time.time()
    #s = time.time()
    while True:
        drawscreen(level)
    
        for event in pygame.event.get():            
            if event.type == KEYDOWN:    # Handle key presses
                if event.key == K_LEFT:
                    keyPressed = True
                    k_p = 'l'
                    box = quiz(level, 'left')
                    if validmove(level, 'left'):
                        level, wongame =  updatelevel(level, 'left')
                        if tele == True:
                            level = tele_level
                    else:
                        blockSound.play()

                elif event.key == K_RIGHT:
                    keyPressed = True
                    k_p = 'r'
                    box = quiz(level, 'right')
                    if validmove(level, 'right'):
                        level, wongame = updatelevel(level, 'right')
                        if tele == True:
                            level = tele_level
                    
                    else:
                        blockSound.play()
                elif event.key == K_UP:
                    keyPressed = True
                    k_p = 'u'
                    box = quiz(level, 'up')
                    if validmove(level, 'up'):
                        level, wongame = updatelevel(level, 'up')
                        if tele == True:
                            level = tele_level
        
                    else:
                        blockSound.play()
                elif event.key == K_DOWN:
                    keyPressed = True
                    k_p = 'd'
                    box = quiz(level, 'down')
                    if validmove(level, 'down'):
                        level, wongame = updatelevel(level, 'down')
                        if tele == True:
                            level = tele_level
    
                    else:
                        blockSound.play()

                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                else:
                    blockSound.play()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(FPS)
        if box == True:
            if k_p == 'r':
                quiz_gui('r')
            elif k_p == 'l':
                quiz_gui('l')
            elif k_p == 'u':
                quiz_gui('u')
            elif k_p == 'd':
                quiz_gui('d')
            box=False
        
        if corr >= 3:
            if wongame == True:
                end = time.time()
                time_record = round(end - start, 5)

                import csv
                if di == 'easy':
                    f = open('record_easy.csv', 'a', newline='')
                    wr = csv.writer(f)
                    wr.writerow([user, time_record])
                    f.close()
                elif di == 'normal':
                    f = open('record_normal.csv', 'a', newline='')
                    wr = csv.writer(f)
                    wr.writerow([user, time_record])
                    f.close()
                elif di == 'hard':
                    f = open('record_hard.csv', 'a', newline='')
                    wr = csv.writer(f)
                    wr.writerow([user, time_record])
                    f.close()

                endAnim(time_record)

        
def quiz_gui(x):
    global corr, level
    # k = show.k(difficulty, x)
    if show.k(difficulty, x):
        level = box_open(level, x)
        corr +=1

    
def ms(s):
    minu = int(s) // 60
    sec = float(s) % 60
    return minu, sec

def how2play(x):
    HOWPLAYSCREEN = pygame.display.set_mode((WINDOWX, WINDOWY))
    if x == 'easy':
        imp = pygame.image.load("./sprites/howtoplay_1.png").convert()
        k = 'c_forest'
    elif x == 'normal':
        imp = pygame.image.load("./sprites/howtoplay_2.png").convert()
        k = 'c_desert'
    else:
        imp = pygame.image.load("./sprites/howtoplay_3.png").convert()
        k = 'c_space'

    imp = pygame.transform.scale(imp, (1920, 1080))
    HOWPLAYSCREEN.fill(WHITE)
    done=False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return k
        HOWPLAYSCREEN.blit(imp, (0, 0))
        pygame.display.update()
        clock.tick(FPS)



def endAnim(x):
    import pandas_ranking
    arr =  pandas_ranking.ranking(di)
    minute, second = ms(x)
    wonSound = pygame.mixer.Sound('./sounds/Finish.mp3')
    wonSound.play()
    time.sleep(1)
    ENDSCREEN = pygame.display.set_mode((WINDOWX, WINDOWY))
    ENDSCREEN.fill(WHITE)
    endText = titleFont.render(f'Thank you for playing!', True, BGTEXT, WHITE) 
    endRect = endText.get_rect()
    endRect.center = (int(WINDOWX/2), int(WINDOWY/4)) 

    recordText = titleFont.render(f'{user}: {minute}분 {"{:.3f}".format(second)}초', True, BGTEXT, WHITE)
    recordRect = recordText.get_rect()
    recordRect.center = (int(WINDOWX/2), int(WINDOWY/2.5))  

    user1 = arr.iloc[0]['NAME']
    user2 = arr.iloc[1]['NAME']
    user3 = arr.iloc[2]['NAME']
    user4 = arr.iloc[3]['NAME']
    user5 = arr.iloc[4]['NAME']

    gtime1 = arr.iloc[0]['TIME']
    gtime2 = arr.iloc[1]['TIME']
    gtime3 = arr.iloc[2]['TIME']
    gtime4 = arr.iloc[3]['TIME']
    gtime5 = arr.iloc[4]['TIME']

    

    import numpy as np
    
    if np.isnan(gtime1): 
        user1 = 'x'
        minute1 = 0
        second1 = 0
    else:
        minute1, second1 = ms(gtime1)
    
    if np.isnan(gtime2):
        user2 = 'x'
        minute2 = 0
        second2 = 0
    else:
        minute2, second2 = ms(gtime2)
    
    if np.isnan(gtime3):
        user3 = 'x'
        minute3 = 0
        second4 = 0
    else:
        minute3, second3 = ms(gtime3)

    if np.isnan(gtime4):
        user4 = 'x'
        minute4 = 0
        second4 = 0
    else:
        minute4, second4 = ms(gtime4)
    
    if np.isnan(gtime5):
        user5 = 'x'
        minute5 = 0
        second5 = 0
    else:
        minute5, second5 = ms(gtime5)

    record1Text = finishFont.render(f'{user1}: {minute1}분 {"{:.3f}".format(second1)}초', True, BGTEXT, WHITE)
    record1Rect = record1Text.get_rect()
    record1Rect.center = (int(WINDOWX/2), int(2.8*WINDOWY/4.5))  
    record2Text = finishFont.render(f'{user2}: {minute2}분 {"{:.3f}".format(second2)}초', True, BGTEXT, WHITE)
    record2Rect = record2Text.get_rect()
    record2Rect.center = (int(WINDOWX/2), int(2.8*WINDOWY/4.2))  
    record3Text = finishFont.render(f'{user3}: {minute3}분 {"{:.3f}".format(second3)}초', True, BGTEXT, WHITE)
    record3Rect = record3Text.get_rect()
    record3Rect.center = (int(WINDOWX/2), int(2.8*WINDOWY/3.9))  
    record4Text = finishFont.render(f'{user4}: {minute4}분 {"{:.3f}".format(second4)}초', True, BGTEXT, WHITE)
    record4Rect = record4Text.get_rect()
    record4Rect.center = (int(WINDOWX/2), int(2.75*WINDOWY/3.6))  
    record5Text = finishFont.render(f'{user5}: {minute5}분 {"{:.3f}".format(second5)}초', True, BGTEXT, WHITE)
    record5Rect = record5Text.get_rect()
    record5Rect.center = (int(WINDOWX/2), int(2.7*WINDOWY/3.3))  





    while True:
        ENDSCREEN.blit(endText, endRect)
        ENDSCREEN.blit(recordText, recordRect)
        ENDSCREEN.blit(record1Text, record1Rect)
        ENDSCREEN.blit(record2Text, record2Rect)
        ENDSCREEN.blit(record3Text, record3Rect)
        ENDSCREEN.blit(record4Text, record4Rect)
        ENDSCREEN.blit(record5Text, record5Rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(FPS)
    
def quiz(level, direction):
    global key_count
    x, y = getplayerlocation(level)
    levtemp = []
    box = False
    boxSound = pygame.mixer.Sound('./sounds/boxopen.mp3')

    for elem in level:
        levlist = list(elem)
        levtemp.append(levlist)
    if direction == 'left':
        if levtemp[x - 1][y] == '<' or levtemp[x - 1][y] == '>':
            if key_count > 0:
                boxSound.play()
                box = True
                key_count-=1
                print('상자 오픈')
            
    if direction == 'right':
        if levtemp[x + 1][y] == '<' or levtemp[x + 1][y] == '>':
            if key_count > 0:
                boxSound.play()
                box = True
                key_count-=1
            
    if direction == 'up':
        if levtemp[x][y - 1] =='<' or levtemp[x][y - 1] == '>':
            if key_count > 0:
                boxSound.play()
                box = True
                key_count-=1
            
    if direction == 'down':
        if levtemp[x][y + 1] == '<' or levtemp[x][y + 1] == '>':
            if key_count > 0:
                boxSound.play()
                box = True
                key_count-=1
    return box


def crash_vblock(level, direction):
    global item_count
    levtemp = []
    crashsound = pygame.mixer.Sound('./sounds/Crash (mp3cut.net).mp3')
    x, y = getplayerlocation(level)
    for elem in level:
        levlist = list(elem)
        levtemp.append(levlist)
    wall = False

    if direction == 'left':
    	if levtemp[x-1][y] == 'v':
            if item_count > 0:
                item_count -= 1
                print('아이템 사용')
                crashsound.play() 
                wall = True 
    if direction == 'right':
        if levtemp[x+1][y] == 'v':
            if item_count > 0:
                item_count -= 1
                print('아이템 사용')
                crashsound.play() 	
                wall = True 
    if direction == 'up':
        if levtemp[x][y-1] =='v':
            if item_count > 0:
                item_count -= 1
                print('아이템 사용')
                crashsound.play() 	
                wall = True 
    if direction == 'down':
        if levtemp[x][y+1] == 'v':
            if item_count > 0:
                item_count -= 1
                print('아이템 사용')
                crashsound.play() 
                wall = True 
                
    return wall


def box_open(level, direction):
    x, y = getplayerlocation(level)
    levtemp = []
    levelmod = []
   
    for elem in level:
        levlist = list(elem)
        levtemp.append(levlist)

    if direction == 'l':
        levtemp[x - 1][y] = 'o'
    elif direction == 'r':
        levtemp[x + 1][y] = 'f'
    elif direction == 'u':
        levtemp[x][y - 1] = 'o'
    elif direction == 'd':
        levtemp[x][y + 1] = 'o'
        
    for elem in levtemp:
        levelmod.append(''.join(elem))
    
    return levelmod

def updatelevel(level, direction):
    x, y = getplayerlocation(level)
    levtemp = []
    levelmod = []
    wongame = False
   
    
    for elem in level:
        levlist = list(elem)
        levtemp.append(levlist)
        
    if direction == 'left':
    	if levtemp[x - 1][y] == '$':
            wongame = True
        	
    elif direction == 'right':
        if levtemp[x + 1][y] == '$':
            wongame = True
        	
    elif direction == 'up':
        if levtemp[x][y - 1] =='$':
            wongame = True
        	
    elif direction == 'down':
        if levtemp[x][y + 1] == '$':
            wongame = True
    
    
    if direction == 'left':
        levtemp[x - 1][y] = '@'
        levtemp[x][y] = ' '
    elif direction == 'right':
        levtemp[x + 1][y] = '@'
        levtemp[x][y] = ' '
    elif direction == 'up':
        levtemp[x][y - 1] = '@'
        levtemp[x][y] = ' '
    elif direction == 'down':
        levtemp[x][y + 1] = '@'
        levtemp[x][y] = ' '
    

    for elem in levtemp:
        levelmod.append(''.join(elem))
        
    return levelmod, wongame

def move(direction):
    x, y = getplayerlocation(level)
    levtemp = []
    levelmod = []
   
    
    for elem in level:
        levlist = list(elem)
        levtemp.append(levlist)
        
    if direction == 'left':
        levtemp[x - 1][y] = ' '
    elif direction == 'right':
        levtemp[x + 1][y] = ' '	
    elif direction == 'up':
        levtemp[x][y - 1] =' '
    elif direction == 'down':
        levtemp[x][y + 1] = ' '
    for i in range(len(levtemp)):
        for j in range(len(levtemp[10])):
            if levtemp[i][j] == 'm':
                item_x = i
                item_y = j
                

    levtemp[item_x][item_y] = '@'

    levtemp[x][y] = ' '
    
        	
    for elem in levtemp:
        levelmod.append(''.join(elem))
    #print(levelmod)
    return levelmod



def validmove(level, direction):
    global item_count, key_count, tele, tele_level
    tele = False
    x, y = getplayerlocation(level)
    itemSound = pygame.mixer.Sound('./sounds/Item.mp3')

    if direction == 'left':
        if corr >= 3:
            if level[x-1][y] == '$':
                return True
        if crash_vblock(level, 'left'):
            return True
        if level[x - 1][y] == ' ' or level[x - 1][y] == 'i' or level[x - 1][y] == 'k' or level[x - 1][y] == 'm':
            if level[x - 1][y] == 'i':
                itemSound.play()
                item_count += 1
                print('아이템 획득')
                print('아', item_count)

            if level[x - 1][y] == 'k':
                itemSound.play()
                key_count += 1
                print('키 획득')
            if level[x - 1][y] == 'm':
                tele_level = move('left')
                tele = True
            return True
        else:
            return False
    if direction == 'right':
        if corr >= 3:
            if level[x + 1][y] == '$':
                return True
        if crash_vblock(level, 'right'):
            return True
        if level[x + 1][y] == ' ' or level[x + 1][y] == 'i' or level[x + 1][y] == 'k' or level[x - 1][y] == 'm':
            if level[x + 1][y] == 'i':
                itemSound.play()
                item_count += 1
                print('아이템 획득')
                print('아', item_count)
            if level[x + 1][y] == 'k':
                itemSound.play()
                key_count += 1
                print('키 획득')
            if level[x + 1][y] == 'm':
                tele_level = move('right')
                tele = True
            return True
        else:
            return False
    if direction == 'up':
        if corr >= 3:
            if level[x][y - 1] == '$':
                return True
        if crash_vblock(level, 'up'):
            return True
        if level[x][y - 1] == ' ' or level[x][y - 1] == 'i' or level[x][y-1] == 'k' or level[x][y-1] == 'm':
            if level[x][y - 1] == 'i':
                itemSound.play()
                item_count += 1
                print('아이템 획득')
                print('아', item_count)
            if level[x][y - 1] == 'k':
                itemSound.play()
                key_count += 1
                print('키 획득')
            if level[x][y - 1] == 'm':
                tele_level = move('up')
                tele = True
            return True
        else:
            return False
    if direction == 'down':
        if corr >= 3:
            if level[x][y + 1] == '$':
                return True
        if crash_vblock(level, 'down'):
            return True
        if level[x][y + 1] == ' ' or level[x][y + 1] == 'i' or level[x][y+1] == 'k' or level[x - 1][y] == 'm':
            if level[x][y + 1] == 'i':
                itemSound.play()
                item_count += 1
                print('아이템 획득')
                print('아', item_count)
            if level[x][y + 1] == 'k':
                itemSound.play()
                key_count += 1
                print('키 획득')

            if level[x][y + 1] == 'm':
                tele_level = move('down')
                tele = True

            return True
        else:
            return False
    
def loadLevelFile(difficulty):
    levelFile = open('./levels/' + difficulty + '.txt', 'r')
    l = levelFile.readlines()
    level = []
    
    for i in l:
        level.append(i.strip('\n'))
    width = len(level) * TILEWIDTH
    height = (len(level[0]) - 1)*TILEFLOORHEIGHT + TILEHEIGHT
    return level, width, height, difficulty
    
def getplayerlocation(level):
    for x in range(len(level)):
        for y in range(len(level[x])):
            if level[x][y] == '@':
                return x, y

def drawscreen(level):			
    GAMESCREEN = pygame.display.set_mode((WINDOWX, WINDOWY))
    GAMESCREEN.fill(WHITE)
    playerpixx, playerpixy = getplayerlocation(level)
    playerx, playery = playerpixx * TILEWIDTH, playerpixy * TILEFLOORHEIGHT
    camx = 0
    camy = 0
    divx = int(MAPWIDTH/WINDOWX) + 1
    divy = int(MAPHEIGHT/WINDOWY) + 1
    paramx = int(MAPWIDTH/divx)
    paramy = int(MAPWIDTH/divy)
    totx = paramx
    toty = paramy
    while playerx > totx:
        totx += paramx
    camx = totx - paramx
    while playery > toty:
        toty += paramy
    camy = toty - paramy

    e = time.time()
    gametime = textFont.render(f'{int(e-s)}', True, BGTEXT, WHITE)
    timeRect = gametime.get_rect()
    timeRect.center = (int(1700), int(135))
    

    for x in range(len(level)):
        for y in range(len(level[x])):
            blockRect = pygame.Rect((x * TILEWIDTH - camx - 30, y * TILEFLOORHEIGHT - camy - 30, TILEWIDTH, TILEHEIGHT))
            tile = TILEDICT[' ']
            GAMESCREEN.blit(tile, blockRect)
            if level[x][y] in TILEDICT:
                tile = TILEDICT[level[x][y]]
                GAMESCREEN.blit(tile, blockRect)
            elif level[x][y] == '@':
                tile = SPRITEDICT[sprite]
                GAMESCREEN.blit(tile, blockRect)
                playerRect = blockRect
    GAMESCREEN.blit(gametime, timeRect)



def startup(): #initial display screen
    global done, user, s

    STARTSCREEN = pygame.display.set_mode((WINDOWX, WINDOWY))
    STARTSCREEN.fill(WHITE)
    easy = False
    pygame.display.set_caption('image')
    imp = pygame.image.load("bg.png").convert()
    STARTSCREEN.blit(imp, (0, 0))

    pygame.display.set_caption("Game")
    diffEasy = textFont.render('Forest (EASY)', True, BGTEXT, WHITE)
    diffMed = textFont.render('normal', True, BGTEXT, WHITE)
    diffHard = textFont.render('Hard', True, BGTEXT, WHITE)
    charSelect = textFont.render('Select Character', True, BGTEXT, WHITE)
    name = textFont.render('이름: ', True, BGTEXT, WHITE)
    Confirmed = textFont.render('Confirmed!', True, BGTEXT, WHITE)

    diffEasyRect = diffEasy.get_rect()
    diffMedRect = diffMed.get_rect()
    diffHardRect = diffHard.get_rect()
    charSelectRect = charSelect.get_rect()
    c_forestRect = c_forest.get_rect()
    c_desertSpriteRect = c_desertSprite.get_rect()
    c_spaceSpriteRect = c_spaceSprite.get_rect()
    nameRect = name.get_rect()
    ConfirmedRect = Confirmed.get_rect()

    diffEasyRect.center = (int(WINDOWX/4), int(1.8*WINDOWY/3))
    diffMedRect.center = (int(WINDOWX/2), int(1.8*WINDOWY/3))
    diffHardRect.center = (int(3*WINDOWX/4), int(1.8*WINDOWY/3))
    charSelectRect.center = (int(947), int(WINDOWY/4))
    nameRect.center = (int(WINDOWX/2.3), int(WINDOWY/1.95))
    ConfirmedRect= (int(WINDOWX/2.2), int(WINDOWY/2.01))
    c_forestRect.center = (int(WINDOWX/4), int(3*WINDOWY/4))
    c_desertSpriteRect.center = (int(2*WINDOWX/4), int(3*WINDOWY/4))
    c_spaceSpriteRect.center = (int(3*WINDOWX/4), int(3*WINDOWY/4))

    pygame.mixer.music.load('./sounds/Start .mp3')
    pygame.mixer.music.play(-1, 0.0)
    
    i = 0
    mousex = 0
    mousey = 0
    clicked = False

    while clicked != True:
        
        if i <= int(WINDOWX/2):
            i += 5
             
        else: 
            STARTSCREEN.blit(diffEasy, diffEasyRect)
            STARTSCREEN.blit(diffMed, diffMedRect)
            STARTSCREEN.blit(diffHard, diffHardRect)
        

        for event in pygame.event.get():
            if event.type == MOUSEMOTION :
                mousex, mousey = event.pos
                if diffEasyRect.collidepoint(mousex, mousey):
                    diffEasy = textFont.render('Forest (EASY)', True, BGHL, BLACK)
                        
                elif diffMedRect.collidepoint(mousex, mousey):
                    diffMed = textFont.render('Desert (NORMAL)', True, BGHL, BLACK)

                elif diffHardRect.collidepoint(mousex, mousey):
                    diffHard = textFont.render('Space (HARD)', True, BGHL, BLACK)
                else:
                    diffEasy = textFont.render('Forest (EASY)', True, BGTEXT, BLACK)
                    diffMed = textFont.render('Desert (NORMAL)', True, BGTEXT, BLACK)
                    diffHard = textFont.render('Space (HARD)', True, BGTEXT, BLACK)

            elif event.type == MOUSEBUTTONUP :
                mousex, mousey = event.pos
                if diffEasyRect.collidepoint(mousex, mousey):
                    difficulty = 'easy'
                    clicked = True

                elif diffMedRect.collidepoint(mousex, mousey):
                    difficulty = 'normal'

                    clicked = True

                elif diffHardRect.collidepoint(mousex, mousey):
                    difficulty = 'hard'
                    
                    clicked = True

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        #update screen and tick clock    
        pygame.display.update()
        clock.tick(FPS)

    while True:

        STARTSCREEN.fill(WHITE)
        STARTSCREEN.blit(charSelect, charSelectRect)
        STARTSCREEN.blit(name, nameRect)
    
        if done == True:
            STARTSCREEN.blit(Confirmed, ConfirmedRect)
        input_box1 = InputBox(WINDOWX/2.2, WINDOWY/2, 140, 32)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
                        

                user = input_box1.handle_event(event)
                print(user)

            input_box1.update()

            input_box1.draw(STARTSCREEN)

            pygame.display.flip()
        #clock.tick(30)

        for event in pygame.event.get():
            
            s = time.time()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    return difficulty
    
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        #update screen and tick clock    
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()

