#Initalizing Tour de France winners
winners = {'Anquetil': 5, 'Armstrong': 7, 'Merckx': 5, 'Hinault': 5, 'Indurain': 5, 'Froome': 3, 'Thys': 3}

print('Tours won by Indurain:', winners['Indurain'])

print('Tours won by Armstrong:', winners['Armstrong'])

print('Amstrong was doped and trapped')
del winners['Armstrong']

if ('Amstrong' in winners):
    print('Tours won by Armstrong:', winners['Armstrong'], end="\n\n")
else:
    print('Tours won by Armstrong 0', end="\n\n")

#Iterate over dictionary keys
for winner, times in winners.items():
    print(winner, "won", times, "Tour de France")