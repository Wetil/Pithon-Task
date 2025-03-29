def rps_game_winner(list):
    if(len(list) > 2):
        raise Exception("WrongNumberOfPlayersError")
    else:
        if(list[0][1] == list[1][1]):
            print(*list[0])
        elif(list[0][1] == "R" and list[1][1] == "S"):
            print(*list[0])
        elif (list[0][1] == "R" and list[1][1] == "P"):
            print(*list[1])
        elif (list[0][1] == "S" and list[1][1] == "P"):
            print(*list[0])
        elif (list[0][1] == "S" and list[1][1] == "R"):
            print(*list[1])
        elif (list[0][1] == "P" and list[1][1] == "R"):
            print(*list[0])
        elif (list[0][1] == "P" and list[1][1] == "S"):
            print(*list[1])
        else:
            raise Exception("NoSuchStrategyError")

rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) #=> WrongNumberOfPlayersError
rps_game_winner([['player1', 'P'], ['player2', 'A']]) #=> NoSuchStrategyError
rps_game_winner([['player1', 'P'], ['player2', 'S']]) #=> 'player2 S'
rps_game_winner([['player1', 'P'], ['player2', 'P']]) #=> 'player1 P'
