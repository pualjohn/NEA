import pygame
import random
from random import randrange

pygame.font.init()

screen = pygame.display.set_mode((500, 600))


brimstoneIMG=pygame.image.load('brimstone.png')
breachIMG=pygame.image.load('breach.png')
sageIMG=pygame.image.load('sage.png')
phoniexIMG=pygame.image.load('phoenix.png')
astraIMG=pygame.image.load('killjoy.png')
neonIMG=pygame.image.load('neon.png')
cypherIMG=pygame.image.load('cypher.png')
viperIMG=pygame.image.load('viper.png')
killjoyIMG=pygame.image.load('killjoy.png')

x = 0
y = 0
dif = 500 / 9
val = 0

grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
 

font1 = pygame.font.SysFont("comicsans", 20)
font2 = pygame.font.SysFont("comicsans", 20)
def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif
 

def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (0, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (0, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)  
 
      
def draw():   
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
 
                
                pygame.draw.rect(screen, (0, 255, 255), (i * dif, j * dif, dif + 1, dif + 1))
 
                
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
             
    for i in range(10):
        if i % 3 == 0 :
            thick = 6
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)     
 
     
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))   
#def newnumber():
 #   new= randrange(9)
  #  if new >=0 and new<=0:
   #     randnumber=2
    #else:
     #   randnumber=4
    #randrow = randrange(2,2,4)
    #randcolumn=randrange(9)
    #while grid[randrow][randcolumn]>0:
     #   randrow=randrange(9)
      #  randcolumn=randrange(9)
    #grid[randrow][randcolumn]= randnumber



def raise_error1():
    text1 = font1.render("WRONG !!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
def raise_error2():
    text1 = font1.render("Wrong !!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
 

def valid(m, i, j, val):
    for it in range(9):
        if m[i][it]== val:
            return False
        if m[it][j]== val:
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if m[i][j]== val:
                return False
    return True
 

def solve(grid, i, j):
     
    while grid[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()   
    for it in range(1, 10):
        if valid(grid, i, j, it)== True:
            grid[i][j]= it
            global x, y
            x = i
            y = j
           
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j)== 1:
                return True
            else:
                grid[i][j]= 0
           
            screen.fill((25, 255, 25))
         
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)   
    return False 
 

def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))       
    screen.blit(text2, (20, 540))
 

def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))   
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

while run:
     
    
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False 
           
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
         
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1   
            if event.key == pygame.K_1:
                val = phoniexIMG
                screen.blit(phoniexIMG, (x * dif + 15, y * dif + 15))
            if event.key == pygame.K_2:
                val = neonIMG
                screen.blit(neonIMG, (x * dif + 15, y * dif + 15))
            if event.key == pygame.K_3:
                val = cypherIMG
                screen.blit(cypherIMG, (x * dif + 15, y * dif + 15))
            if event.key == pygame.K_4:
                val = brimstoneIMG
                screen.blit(brimstoneIMG, (x * dif + 15, y * dif + 15))
            if event.key == pygame.K_5:
                val = breachIMG
                screen.blit(breachIMG, (x * dif + 15, y * dif + 15))
            if event.key == pygame.K_6:
                val = killjoyIMG
                screen.blit(killjoyIMG, (x * dif + 15, y * dif + 15))
            if event.key == pygame.K_7:
                val = viperIMG
                screen.blit(viperIMG, (x * dif + 15, y * dif + 15))
            if event.key == pygame.K_8:
                val = sageIMG
                screen.blit(sageIMG, (x * dif + 15, y * dif + 15))
            if event.key == pygame.K_9:
                val = astraIMG
                screen.blit(astraIMG, (x * dif + 15, y * dif + 15))
            if event.key == pygame.K_RETURN:
                flag2 = 1  
            
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                grid =[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                grid =[
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]
    if flag2 == 1:
        if solve(grid, 0, 0)== False:
            error = 1
        else:
            rs = 1
        flag2 = 0   
    if val != 0:           
        draw_val(val)
        print(x)
        print(y)
        if valid(grid, int(x), int(y), val)== True:
            grid[int(x)][int(y)]= val
            flag1 = 0
        else:
            grid[int(x)][int(y)]= 0
            raise_error2()  
        val = 0   
       
    if error == 1:
        raise_error1() 
    if rs == 1:
        result()       
    draw() 
    if flag1 == 1:
        draw_box()      
    instruction()   
 
    
    pygame.display.update() 
 
   
pygame.quit()     

