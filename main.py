# Example file showing a basic pygame "game loop"
import pygame
import queue
import enemy
import gridBlock
import pathFinding
from building import Building
from random import randint
from tower import Tower

# pygame setup
pygame.init()

w,h = 1000, 500

screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
running = True


boardBlock = []
enemyList = []
enemy1SpawnRate = 1000 # 1/enemy1SpawnRate
enemy2SpawnRate = 250 # 1/enemy2SpawnRate
spawnPoint = (-1, -1)

selected = (-1, -1)
def select(pos : tuple[int, int]):
    global selected
    x,y = pos
    print("selecting:",x//50, y//50)
    boardBlock[y//50][x//50].select()
    if selected != (-1, -1):
        selx, sely = selected
        boardBlock[sely][selx].deselect()
    selected = (x//50, y//50)

def build_slow():
    global selected
    if selected == (-1, -1):
        return
    selx, sely = selected
    print("building slow at:", selx, sely)
    boardBlock[sely][selx].build_slow()
    boardBlock[sely][selx].deselect()
    selected = (-1, -1)

t = 0
for i in range(0, h, 50):
    l = []
    for j in range(0, w, 50):
        l.append(gridBlock.GridBlock(t, j+3, i+3, 1, 45, pygame.Color("lightblue"), Building.none))
        t += 1
    boardBlock.append(l)

boardBlock[3][3].make_spawn()
spawnPoint = (3, 3)
boardBlock[h//50-3][w//50-3].make_goal()
goalPoint = (w//50-3, h//50-3)

towerList : list[Tower] = []
game_over_bool = False

def build_wall():
    global selected
    if selected == (-1, -1):
        return False
    selx,sely = selected
    print("trying to build wall at:",selx, sely)
    if not boardBlock[sely][selx].build_wall():
        return False
    boardBlock[sely][selx].deselect()
    selected = (-1, -1)
    spawnx, spawny = spawnPoint
    if pathFinding.djikstra(spawnx, spawny, boardBlock) == -2:
        boardBlock[sely][selx].remove_building()
        return False
    return True

def build_tower():
    global selected
    if selected == (-1, -1):
        return False
    selx,sely = selected
    print("trying to build tower at:",selx, sely)
    if not boardBlock[sely][selx].build_tower():
        return False
    boardBlock[sely][selx].deselect()
    selected = (-1, -1)
    spawnx, spawny = spawnPoint
    if pathFinding.djikstra(spawnx, spawny, boardBlock) == -2:
        boardBlock[sely][selx].remove_building()
        return False
    towerList.append(Tower(selx*50+25, sely*50+25, 100, 2, 30))
    boardBlock[sely][selx].tower_id = len(towerList) - 1
    return True

def destroy_building():
    global selected
    if selected == (-1, -1):
        return False
    selx, sely = selected
    print("trying to destroy building at:",selx, sely)
    a = boardBlock[sely][selx].remove_building()
    boardBlock[sely][selx].deselect()
    if a != -1:
        towerList.pop(a)
    selected = (-1, -1)

def game_over():
    global game_over_bool
    print("Game Over")
    game_over_bool = True
    text = pygame.font.SysFont("Arial", 50).render("GAME OVER", True, (255, 0, 0))
    textrect = text.get_rect()
    textrect.center = (w // 2, h // 2)
    screen.blit(text, textrect)
cnt = 0
while running:
    cnt += 1
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            select(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            print("user pressed key:", event.key)
            if event.key == pygame.K_1:
                build_slow()
            if event.key == pygame.K_2:
                build_wall()
            if event.key == pygame.K_3:
                build_tower()
            if event.key == 8: # delete, on my computer at least
                destroy_building()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("lightblue")

    n = 0
    while n <= w:
        pygame.draw.line(screen, "black", (n, 0), (n, h), width=5)
        n += 50

    n = 0

    while n <= h:
        pygame.draw.line(screen, "black", (0, n), (w, n), width=5)
        n += 50



    # RENDER YOUR GAME HERE
    for i in range(len(boardBlock)):
        for j in range(len(boardBlock[i])):
            boardBlock[i][j].render(screen)

    if randint(1, enemy1SpawnRate) == 1:
        sx, sy = spawnPoint
        sx *= 50
        sx += 25
        sy *= 50
        sy += 25
        enemyList.append(enemy.Enemy(sx, sy, 1, 100+cnt//100))

    if randint(1, enemy2SpawnRate) == 1:
        sx, sy = spawnPoint
        sx *= 50
        sx += 25
        sy *= 50
        sy += 25
        enemyList.append(enemy.Enemy(sx, sy, 1, 20+cnt//100, False))

    dead = queue.Queue()
    for i in range(len(enemyList)):
        if cnt%30 == 0 and enemyList[i].move(boardBlock, goalPoint):
            game_over()
        enemyList[i].render(screen)
        if not enemyList[i].alive():
            dead.put(i)

    while not dead.empty():
        i = dead.get()
        enemyList.pop(i)

    for i in range(len(towerList)):
        towerList[i].shoot(enemyList, goalPoint)

    if game_over_bool:
        game_over()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()









