
def game(number):

    numberOfSticks = number

    while numberOfSticks > 0:
        player1 = int(input(f'Where are {numberOfSticks} sticks left. Player1 how many sticks do you want to take: '))
        while player1 >= 4 or player1 <= 0:
            player1 = int(input(f'Where are {numberOfSticks} sticks left. Player1 how many sticks do you want to take: '))
        numberOfSticks -= player1
        if numberOfSticks <= 0:
            loser = 'player1'
            break 
        
        
        player2 = int(input(f'Where are {numberOfSticks} sticks left. Player2 how many sticks do you want to take: '))
        while player2 >= 4 or player2 <= 0:
            player2 = int(input(f'Where are {numberOfSticks} sticks left. Player2 how many sticks do you want to take: '))
        numberOfSticks -= player2
        if numberOfSticks <= 0:
            loser = 'player2'
            break
        
    print(f'{loser} has lost the game {numberOfSticks}')

game(10)