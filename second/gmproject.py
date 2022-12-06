import show 
import pygame, sys, random, time
from pygame.locals import *
import time
WINDOWX = 1920 #x and y coordinates of window
WINDOWY = 1080
FPS = 300 #refresh rate of screen
TILEWIDTH = 50   #50
TILEHEIGHT = 50    # 85
TILEFLOORHEIGHT = 49.8
#RGB values for colours
#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)
BGMAIN = WHITE # 원래 BLACK
BGTEXT = (255, 120, 255) # 원래 GREEN
BGHL = RED # 원래 WHITE
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
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    #print(self.text)
                    return self.text
                    #self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

def main():
    pygame.init()
    global s, e, finishFont, COLOR_INACTIVE, COLOR_ACTIVE, FONT, level, sprite, clock, TILEDICT, titleFont, textFont, c_forest, c_desertSprite, c_spaceSprite, SPRITEDICT, MAPWIDTH, MAPHEIGHT, difficulty
    clock = pygame.time.Clock()
    COLOR_INACTIVE = pygame.Color('lightskyblue3')
    COLOR_ACTIVE = pygame.Color('dodgerblue2')
    FONT = pygame.font.Font(None, 32)
#fonts and sprites are loaded
    finishFont = pygame.font.Font(None, 30) 
    titleFont = pygame.font.Font('./fonts/ChangwonDangamAsac-Bold_0712.ttf', 50)
    textFont = pygame.font.Font('./fonts/ChangwonDangamAsac-Bold_0712.ttf', 30)
    c_forest = pygame.image.load('./sprites/daramgi.png')
    c_forest = pygame.transform.scale(c_forest, (50, 50))
    c_desertSprite = pygame.image.load('./sprites/fox.png')
    c_desertSprite = pygame.transform.scale(c_desertSprite, (50, 50))
    c_spaceSprite = pygame.image.load('./sprites/ufo.png')
    c_spaceSprite = pygame.transform.scale(c_spaceSprite, (50, 50))    
    # TILEDICT = {'#':wallSprite, ' ': blockSprite, '<': boxSprite, 'o':openboxSprite, 'g': grassSprite, '$': goalSprite, 'k': keySprite, 'i' : itemSprite, 'v': crash_block}
    SPRITEDICT = {'c_forest': c_forest, 'c_desert': c_desertSprite, 'c_space': c_spaceSprite}
    
    difficulty, sprite = startup()
    level, MAPWIDTH, MAPHEIGHT, di = loadLevelFile(difficulty)
    # print(di)
    if di == 'easy':
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
        TILEDICT = {'#':wallSprite, ' ': tileSprite, '>': flipboxSprite, '<': boxSprite, 'f':flipopenboxSprite,'o':openboxSprite, 'g': SideBlockSprite, '$': finishSprite, 'k': keySprite, 'i' : itemSprite, 'v': virtual_block}
    elif di =='normal':
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
        TILEDICT = {'#':wallSprite, ' ': tileSprite, '>': flipboxSprite, '<': boxSprite, 'f':flipopenboxSprite,'o':openboxSprite, 'g': SideBlockSprite, '$': finishSprite, 'k': keySprite, 'i' : itemSprite, 'v': virtual_block}
    else:
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
        TILEDICT = {'#':wallSprite, ' ': tileSprite, '>': flipboxSprite, '<': boxSprite, 'f':flipopenboxSprite, 'o':openboxSprite, 'g': SideBlockSprite, '$': finishSprite, 'k': keySprite, 'm' : itemSprite}

    pygame.mixer.music.load('./sounds/Easy.mp3')
    pygame.mixer.music.play(-1, 0.0)
    blockSound = pygame.mixer.Sound('./sounds/01blocked.wav')

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
        # if keyPressed == True:
        #     drawscreen(level)
        #     keyPressed = False
        # getxy(playerRect)
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
                        # item = get_item(level, 'left')
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
                    #    item = get_item(level, 'right')
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
                        # item = get_item(level, 'up')
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
                        # item = get_item(level, 'down')
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
                # print(f"{end - start:.5f} sec")
                import csv
                f = open('record.csv','a', newline='')
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


def endAnim(x):
    import pandas_ranking
    arr =  pandas_ranking.ranking()
    minute, second = ms(x)
    wonSound = pygame.mixer.Sound('./sounds/correct.wav')
    wonSound.play()
    time.sleep(1)
    ENDSCREEN = pygame.display.set_mode((WINDOWX, WINDOWY))
    ENDSCREEN.fill(BGMAIN)
    endText = titleFont.render(f'Thank you for playing!', True, BGTEXT, BGMAIN) 
    endRect = endText.get_rect()
    endRect.center = (int(WINDOWX/2), int(WINDOWY/4)) 

    recordText = titleFont.render(f'{user}: {minute}분 {second}초', True, BGTEXT, BGMAIN)
    recordRect = recordText.get_rect()
    recordRect.center = (int(WINDOWX/2), int(WINDOWY/2))  

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

    


    
    if gtime1.isnan():
        user1 = 'x'
        minute1 = 0
        second1 = 0
    else:
        minute1, second1 = ms(gtime1)
    
    if gtime2.isnan():
        user2 = 'x'
        minute2 = 0
        second2 = 0
    else:
        minute2, second2 = ms(gtime2)
    
    if gtime3.isnan():
        user3 = 'x'
        minute3 = 0
        second4 = 0
    else:
        minute3, second3 = ms(gtime3)

    if gtime4.isnan():
        user4 = 'x'
        minute4 = 0
        second4 = 0
    else:
        minute4, second4 = ms(gtime4)
    
    if gtime5.isnan():
        user5 = 'x'
        minute5 = 0
        second5 = 0
    else:
        minute5, second5 = ms(gtime5)

    record1Text = finishFont.render(f'{user1}: {minute1}분 {second1}초', True, BGTEXT, BGMAIN)
    record1Rect = record1Text.get_rect()
    record1Rect.center = (int(WINDOWX/2), int(WINDOWY/2.4))  
    record2Text = finishFont.render(f'{user2}: {minute2}분 {second2}초', True, BGTEXT, BGMAIN)
    record2Rect = record2Text.get_rect()
    record2Rect.center = (int(WINDOWX/2), int(WINDOWY/2.8))  
    record3Text = finishFont.render(f'{user3}: {minute3}분 {second3}초', True, BGTEXT, BGMAIN)
    record3Rect = record3Text.get_rect()
    record3Rect.center = (int(WINDOWX/2), int(WINDOWY/3.2))  
    record4Text = finishFont.render(f'{user4}: {minute4}분 {second4}초', True, BGTEXT, BGMAIN)
    record4Rect = record4Text.get_rect()
    record4Rect.center = (int(WINDOWX/2), int(WINDOWY/3.6))  
    record5Text = finishFont.render(f'{user5}: {minute5}분 {second5}초', True, BGTEXT, BGMAIN)
    record5Rect = record5Text.get_rect()
    record5Rect.center = (int(WINDOWX/2), int(WINDOWY/4))  





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

    for elem in level:
        levlist = list(elem)
        levtemp.append(levlist)
    if direction == 'left':
        if levtemp[x - 1][y] == '<' or levtemp[x - 1][y] == '>':
            if key_count > 0:
                box = True
                key_count-=1
                print('상자 오픈')
            
    if direction == 'right':
        if levtemp[x + 1][y] == '<' or levtemp[x + 1][y] == '>':
            if key_count > 0:
                box = True
                key_count-=1
            
    if direction == 'up':
        if levtemp[x][y - 1] =='<' or levtemp[x][y - 1] == '>':
            if key_count > 0:
                box = True
                key_count-=1
            
    if direction == 'down':
        if levtemp[x][y + 1] == '<' or levtemp[x][y + 1] == '>':
            if key_count > 0:
                box = True
                key_count-=1
    # print('후', key_count)
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
                # time.sleep(1) # wait and
                # crashsound.stop()		
                wall = True 
    return wall

#현재 사용 안됨
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
    #print(levtemp)

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
                #print(item_x)

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
    if direction == 'left':
        if corr >= 3:
            if level[x-1][y] == '$':
                return True
        if crash_vblock(level, 'left'):
            return True
        if level[x - 1][y] == ' ' or level[x - 1][y] == 'i' or level[x - 1][y] == 'k' or level[x - 1][y] == 'm':
            if level[x - 1][y] == 'i':
                item_count += 1
                print('아이템 획득')
                print('아', item_count)

            if level[x - 1][y] == 'k':
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
                item_count += 1
                print('아이템 획득')
                print('아', item_count)
            if level[x + 1][y] == 'k':
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
                item_count += 1
                print('아이템 획득')
                print('아', item_count)
            if level[x][y - 1] == 'k':
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
                item_count += 1
                print('아이템 획득')
                print('아', item_count)
            if level[x][y + 1] == 'k':
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
    GAMESCREEN.fill(BGMAIN)
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
    gametime = textFont.render(f'{int(e-s)}', True, BGTEXT, BGMAIN)
    #gametime = textFont.render('effef', True, BGTEXT, BGMAIN)
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
#title text
    STARTSCREEN = pygame.display.set_mode((WINDOWX, WINDOWY))
    # STARTSCREEN.fill(BGMAIN)

    pygame.display.set_caption('image')
 
    # create a surface object, image is drawn on it.
    imp = pygame.image.load("back.png").convert()
    
    # Using blit to copy content from one surface to other
    STARTSCREEN.blit(imp, (0, 0))

    # STARTSCREEN.bilt(backGround)
    pygame.display.set_caption("Game")
    diffEasy = textFont.render('Forest (EASY)', True, BGTEXT, BGMAIN)
    diffMed = textFont.render('normal', True, BGTEXT, BGMAIN)
    diffHard = textFont.render('Hard', True, BGTEXT, BGMAIN)
    charSelect = textFont.render('Select Character', True, BGTEXT, BGMAIN)
    name = textFont.render('이름: ', True, BGTEXT, BGMAIN)
    Confirmed = textFont.render('Confirmed!', True, BGTEXT, BGMAIN)

    diffEasyRect = diffEasy.get_rect()
    diffMedRect = diffMed.get_rect()
    diffHardRect = diffHard.get_rect()
    charSelectRect = charSelect.get_rect()
    c_forestRect = c_forest.get_rect()
    c_desertSpriteRect = c_desertSprite.get_rect()
    c_spaceSpriteRect = c_spaceSprite.get_rect()
    nameRect = name.get_rect()
    ConfirmedRect = Confirmed.get_rect()
    
    diffEasyRect.center = (int(WINDOWX/4), int(2*WINDOWY/3))
    diffMedRect.center = (int(WINDOWX/2), int(2*WINDOWY/3))
    diffHardRect.center = (int(3*WINDOWX/4), int(2*WINDOWY/3))
    charSelectRect.center = (int(WINDOWX/2), int(WINDOWY/4))
    nameRect.center = (int(WINDOWX/2.1), int(WINDOWY/1.95))
    ConfirmedRect= (int(WINDOWX/2), int(WINDOWY/2.01))
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
        # STARTSCREEN.fill(BGMAIN)
        if i <= int(WINDOWX/2):
            i += 5
             
        else: 
            STARTSCREEN.blit(diffEasy, diffEasyRect)
            STARTSCREEN.blit(diffMed, diffMedRect)
            STARTSCREEN.blit(diffHard, diffHardRect)
        #on mouse click 
        #event capture
        for event in pygame.event.get():
            if event.type == MOUSEMOTION :
                mousex, mousey = event.pos
                if diffEasyRect.collidepoint(mousex, mousey):
                    diffEasy = textFont.render('Forest (EASY)', True, BGHL, BGMAIN)
                        
                elif diffMedRect.collidepoint(mousex, mousey):
                    diffMed = textFont.render('Desert (NORMAL)', True, BGHL, BGMAIN)

                elif diffHardRect.collidepoint(mousex, mousey):
                    diffHard = textFont.render('Space (HARD)', True, BGHL, BGMAIN)
                else:
                    diffEasy = textFont.render('Forest (EASY)', True, BGTEXT, BGMAIN)
                    diffMed = textFont.render('Desert (NORMAL)', True, BGTEXT, BGMAIN)
                    diffHard = textFont.render('Space (HARD)', True, BGTEXT, BGMAIN)

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
        STARTSCREEN.fill(BGMAIN)
        STARTSCREEN.blit(charSelect, charSelectRect)
        STARTSCREEN.blit(name, nameRect)
        STARTSCREEN.blit(c_forest, c_forestRect)
        STARTSCREEN.blit(c_spaceSprite, c_spaceSpriteRect)
        STARTSCREEN.blit(c_desertSprite, c_desertSpriteRect)
        if done == True:
            STARTSCREEN.blit(Confirmed, ConfirmedRect)
        input_box1 = InputBox(WINDOWX/2, WINDOWY/2, 140, 32)
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
            if event.type == MOUSEMOTION :
                mousex, mousey = event.pos

            elif event.type == MOUSEBUTTONUP :
                mousex, mousey = event.pos
                clicked = True
                if clicked == True:
                    s = time.time()
                    if c_forestRect.collidepoint(mousex, mousey):
                        pygame.mixer.music.stop()
                        return difficulty, 'c_forest'
                    elif c_desertSpriteRect.collidepoint(mousex, mousey):
                        pygame.mixer.music.stop()
                        return difficulty, 'c_desert'
                    elif c_spaceSpriteRect.collidepoint(mousex, mousey):
                        pygame.mixer.music.stop()
                        return difficulty, 'c_space'
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
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

