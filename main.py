import pygame

pygame.init()
screen = pygame.display.set_mode((450, 450))
clock = pygame.time.Clock()
running = True
pos = (0,0)
inputNumber = ""
currentSelection = (0,0)
cursorPosition = [0,0]
setNumber = False

def is_valid_sudoku(board):
    def is_valid_unit(unit):
        unit = [x for x in unit if x != ""]
        return len(set(unit)) == len(unit)

    def is_valid_rows(board):
        for row in board:
            if not is_valid_unit(row):
                return False
        return True

    def is_valid_columns(board):
        for col in zip(*board):
            if not is_valid_unit(col):
                return False
        return True

    def is_valid_subgrids(board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not is_valid_unit(subgrid):
                    return False
        return True

    return is_valid_rows(board) and is_valid_columns(board) and is_valid_subgrids(board)
def textCoordinates (x,y,distort) :
    return [x+(50/distort),y+(50/distort)]
def cursor (x,y) :
    color = (0,0,255)
    position = (x,y)
    pygame.draw.circle(screen,color,position,2)
def rendertext (x,y,text) :
    color = (0,0,255)
    font = pygame.font.Font ('freesansbold.ttf',20)
    position = (x,y)
    screen.blit(font.render(text,True,color),position)
def createMatrix () :
    matrix = []
    for i in range(9) :
        matrix.append([])
        for j in range (9) :
            matrix[i].append("")
    return matrix
def blockIterate (number,matrix,x,y) :
    if x in range (0,3) :
        istart = 0
        iend = 3
    if x in range (3,6) :
        istart = 3
        iend = 6
    if x in range (6,9) :
        istart = 6
        iend = 9
    if y in range (0,3) :
        jstart = 0
        jend = 3
    if y in range (3,6) :
        jstart = 3
        jend = 6
    if y in range (6,9) :
        jstart = 6
        jend = 9
    for i in range(istart,iend) :
        for j in range(jstart,jend) :
            if matrix[i][j] == str(number) :
                return True
    return False
def checkNumber (number,matrix,x,y) :
    if blockIterate(number,matrix,x,y) == True :
        return False
    for i in range(9) :
        if matrix[i][y] == str(number) or matrix[x][i] == str(number) :
            return False
    return True
def checkMatrix (matrix) :
    for i in range(9) :
        for j in range(9) :
            if matrix[i][j] == "" :
                return False
    return True
def find_empty_cell (matrix) :
    for i in range(9) :
        for j in range(9) :
            if matrix[i][j] == "" :
                return [i,j]
    return [-1,-1]
def Solve (sudoku) :
    if is_valid_sudoku(sudoku) == False :
        return False
    if checkMatrix(sudoku) :
        return True
    row,col = find_empty_cell(sudoku)[0],find_empty_cell(sudoku)[1]
    if row == -1 or col == -1 :
        return True

    for num in range(1,10) :
        if checkNumber(num,sudoku,row,col) :
            sudoku[row][col] = str(num)
            if Solve(sudoku) :
                return True
            sudoku[row][col] = ""
    return False

sudoku = createMatrix()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                cursorPosition[0] += 50
            if event.key == pygame.K_LEFT :
                cursorPosition[0] -= 50
            if event.key == pygame.K_UP :
                cursorPosition[1] -= 50
            if event.key == pygame.K_DOWN :
                cursorPosition[1] += 50
            if event.key == pygame.K_0 :
                inputNumber = "0"
                setNumber = True
            if event.key == pygame.K_1 :
                inputNumber = "1"
                setNumber = True
            if event.key == pygame.K_2 :
                inputNumber = "2"
                setNumber = True
            if event.key == pygame.K_3 :
                inputNumber = "3"
                setNumber = True
            if event.key == pygame.K_4 :
                inputNumber = "4"
                setNumber = True
            if event.key == pygame.K_5 :
                inputNumber = "5"
                setNumber = True
            if event.key == pygame.K_6 :
                inputNumber = "6"
                setNumber = True
            if event.key == pygame.K_7 :
                inputNumber = "7"
                setNumber = True
            if event.key == pygame.K_8 :
                inputNumber = "8"
                setNumber = True
            if event.key == pygame.K_9 :
                inputNumber = "9"
                setNumber = True
            if event.key == pygame.K_SPACE :
                if Solve(sudoku) == False :
                    pygame.quit()
                Solve(sudoku)
    screen.fill("white")
    if cursorPosition[0] < 0 :
        cursorPosition[0] = 0
    if cursorPosition[0] > 400 :
        cursorPosition[0] = 400
    if cursorPosition[1] < 0 :
        cursorPosition[1] = 0
    if cursorPosition[1] > 400 :
        cursorPosition[1] = 400
    pos = textCoordinates(cursorPosition[0],cursorPosition[1],2)
    cursor(pos[0],pos[1])
    for i in range(0,450,50) :
        if i % 150 == 0 :
            pygame.draw.line(screen, "black", (i, 0), (i, 450), 2)
            pygame.draw.line(screen, "black", (0, i), (450, i), 2)
        pygame.draw.line(screen, "black", (i, 0), (i, 450), 1)
        pygame.draw.line(screen, "black", (0, i), (450, i), 1)
        for j in range (0,450,50) :
            rendertext(textCoordinates(i, j, 2.5)[0], textCoordinates(i, j, 2.5)[1], sudoku[round(i/50)][round(j/50)])
            if setNumber :
                sudoku[round(cursorPosition[0]/50)][round(cursorPosition[1]/50)] = inputNumber
                setNumber = False


    pygame.display.flip()
pygame.quit()

