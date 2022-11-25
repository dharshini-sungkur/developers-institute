
def display_board(answers):
    board = "\nTIC TAC TOE"
    board += "\n" + "*" * 17
    board += "\n" + "*   " + answers[0] + " | " + answers[1] + " | " + answers[2] + "   *" 
    board += "\n" + "*  ---|---|---  *" 
    board += "\n" + "*   " + answers[3] + " | " + answers[4] + " | " + answers[5] + "   *" 
    board += "\n" + "*  ---|---|---  *" 
    board += "\n" + "*   " + answers[6] + " | " + answers[7] + " | " + answers[8] + "   *" 
    board += "\n" + "*" * 17 + "\n"
    print(board)
    
def valid_position(location):
    while True:
        try:
            position = int(input(f"Enter {location} (1-3): "))    
        except:
            continue
        else:
            if position >= 1 and position <= 3:
                break 
    return position
            
def get_position(row, column):
    position = 0
    column -= 1
    match row:
        case 1:
            position = column
        case 2:
            position = column + 3
        case 3:
            position = column + 6
    return position
        
def player_input(player,answers):
    display_board(answers)
    print(f"Player {player}'s turn...\n")
    row = valid_position("row")
    column = valid_position("column")
    answers[get_position(row, column)] = player
    
def check_win(game, answers):
    game = True
    player = " "
    if answers[0] == answers[1] == answers[2]:
        player = answers[0]
    elif answers[3] == answers[4] == answers[5]:
        player = answers[3] 
    elif answers[6] == answers[7] == answers[8]:
        player = answers[6]   
         
    elif answers[0] == answers[3] == answers[6]:
        player = answers[0]  
    elif answers[1] == answers[4] == answers[7]:
        player = answers[1] 
    elif answers[2] == answers[5] == answers[8]:
        player = answers[2] 
                 
    elif answers[0] == answers[4] == answers[8]:
        player = answers[4]  
    elif answers[2] == answers[4] == answers[6]:
        player = answers[4] 
    
    if player != " ":
        game = False
        display_board(answers)
        print(f"Win! Player {player} has won...\n")
        
    return game

def play():
    game = True
    count = 0
    answers = []
    for i in range(0,9):   
        answers.append(" ")
        
    print("Welcome to TIC TAC TOE!")
    
    while game and count < 9:
        if count % 2 == 0:
            player_input("O", answers)
        else:
            player_input("X", answers)
        game = check_win(game, answers)
        count += 1
        if count == 9:
            display_board(answers)
            print("Tie! No player has won...\n")
            
play()
