import math
import random

player, opponent = 'x', 'o'

def evaluate(state):
    if winner(state) == player:
        score = +1
    elif winner(state) == opponent:
        score = -1
    else:
        score = 0

    return score

def winner(state):
    for row in state:
        if row.count(row[0]) == len(row) and row[0] != 0:
            return row[0]

    for col in range(len(state)):
        if state[0][col] == state[1][col] == state[2][col] != 0:
            return state[0][col]

    if state[0][0] == state[1][1] == state[2][2] != 0:
        return state[0][0]

    if state[0][2] == state[1][1] == state[2][0] != 0:
        return state[0][2]

    return None

def empty_cells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells

def valid_move(x, y):
    if [x, y] in empty_cells(state):
        return True
    else:
        return False

def set_move(x, y, player):
    if valid_move(x, y):
        state[x][y] = player
        return True
    else:
        return False

def alphabeta(state, depth, alpha, beta, player):
    if player == opponent:
        best = [-1, -1, -math.inf]
    else:
        best = [-1, -1, +math.inf]

    if depth == 0 or winner(state) != None:
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = alphabeta(state, depth - 1, alpha, beta, opponent)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == opponent:
            if score[2] > best[2]:
                best = score
            beta = min(beta, best[2])
        else:
            if score[2] < best[2]:
                best = score 
            alpha = max(alpha, best[2])

        if alpha >= beta:
            break

    return best

def get_best_move(state, player):
    if len(empty_cells(state)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = alphabeta(state, 9, -math.inf, +math.inf, player)
        x, y  = move[0], move[1]

    return x, y

def print_state(state):
    for row in state:
        print("| ", end="")
        print(*row, sep=" | ", end=" |")
        print()

def get_user_move(state):
    while True:
        print("Enter your move:")
        x = int(input("X: ")) 
        y = int(input("Y: "))

        if valid_move(x, y):
            return [x, y] 
        else:
            print("Invalid move")

def choice(seq):
    return random.choice(seq)

# Rest of code remains the same...

if __name__ == "__main__":
    
    state = [[0, 0, 0], 
             [0, 0, 0], 
             [0, 0, 0]]

    print("Tic Tac Toe with AI")
    print("You are X and AI is O")
    print("")        

    while len(empty_cells(state)) > 0:
        move_x, move_y = get_best_move(state, opponent)
        set_move(move_x, move_y, opponent)

        print_state(state)

        if winner(state) != None:
            break
        
        move_x, move_y = get_user_move(state)
        set_move(move_x, move_y, player)

        print_state(state)

        if winner(state) != None:
            break

    if winner(state) == player:
        print("You Win!")
    elif winner(state) == opponent:   
        print("You Lose!")
    else:
        print("Draw!")