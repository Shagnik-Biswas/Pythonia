# Stone-Paper-Scissor
# This is a game of stone paper scissor. There will be two player joining this game. Each can play any round of game. If they play more than 5 round of game then the first player to win 5 round will be the WINNER.
# Otherwise if they play less than 5 rounds then whoever wins the most round between them will be the winner.
# Players can stop at any round and if they won equal round of game, then the game will be considered as a DRAW.
# Each Player will have equal amout of rounds as this is the game's rule.

# The Rules Of The Games:
# Stone Wins against Scissor BUT Loses to Paper.
# Paper Wins against Stone BUT Loses to Scissor.
# Scissor Wins against Paper but Loses to Stone.
# If Two Player draw same items between each other, it will be considered a Draw.

player1 = ["stone","paper","scissor","stone", "paper","stone","paper","paper","stone","paper"]
player2 = ["paper","stone", "paper","paper","scissor", "scissor","stone","stone","paper","scissor"]

winner = []

for i in range(len(player1)):
    if winner.count('player1') < 5 and winner.count('player2') < 5:
        if player1[i] != player2[i]:
          if player1[i] == 'stone':
              if player2[i] == 'paper':
                  winner += ['player2']
              else:
                  winner += ['player1']
          elif player1[i] == 'paper':
              if player2[i] == 'scissor':
                  winner += ['player2']
              else:
                  winner += ['player1']
          elif player1[i] == 'scissor':
              if player2[i] == 'stone':
                  winner += ['player2']
              else:
                  winner += ['player1']

player1_round = winner.count('player1')
player2_round = winner.count('player2')

if player1_round == player2_round:
    print(f'It\'s a Draw. Total {len(winner)} Round Of Games Played. Both Player Won {player1_round} rounds.')
else:
    print(f'Total {len(winner)} Round Of Games Played. Player1 Won {player1_round} round and Player2 Won {player2_round}. So The Winner is: {max(winner, key=winner.count)}.')
