#Testing enumerate function
champions = ['Anquetil', 'Merckx', 'Hinault', 'Indurain']
for k,v in enumerate(champions):
    print("[", k, "]", v)
print("\n")

#Testing reversed function
for i in reversed(range(0,51, 5)):
    print(i, end=" ")
print("\n")

for i in sorted(set(champions)):
    print(i)