seconds = 10
for number in range(10):
    seconds -= 1

if seconds:
    print('Wait', seconds, 'seconds')
else:
    print('The term is over in', seconds, 'seconds')
