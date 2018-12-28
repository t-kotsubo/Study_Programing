pairs = {3:"C", 1:"A", 2:"B"}
pairs[3] = 'D'
pairs[4] = 'E'

# print(pairs[1])

for pair in pairs:
    print(str(pair)+'のペアは'+ pairs[pair] + 'です')