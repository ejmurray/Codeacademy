players = ['Smauel', 'Maxwell', 'Peter', 'Lizzi', 'Jack', 'Oliver', 'Abinav']
number = 1
print 'You have...'
for p in players:
    if p == 'Lizzi':
        print 'The only girl in the team!' # (It actually is.)
        # break
    print 'Player ' + str(number) + ': ' + p
    number += 1
else:
    print 'A fine team selection!'
