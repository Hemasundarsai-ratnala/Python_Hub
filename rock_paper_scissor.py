p1 = input("Enter [ rock, paper, scissor]:")
p2 = input("Enter [ rock, paper, scissor]:")
if p1 == 'rock' and p2 == 'paper':
    print('Player 2 Won')
if p1 == 'paper' and p2 == 'scissor':
    print('Player 2 Won')
if p1 == 'scissor' and p2 == 'paper':
    print('Player 1 Won')
if p1 == 'paper' and p2 == 'rock':
    print('Player 1 Won')  
if p1 == 'scissor' and p2 == 'rock':
    print('Player 2 Won')
if p1 == 'rock' and p2 == 'scissor':
    print('Player 1 Won')
if p1 == 'scissor' and p2 == 'scissor':
    print('Draw')
if p1 == 'paper' and p2 == 'paper':
    print('Draw')
if p1 == 'rock' and p2 == 'rock':
    print('Draw')
