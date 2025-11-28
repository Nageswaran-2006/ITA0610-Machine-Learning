data = [
    (['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'], 'No'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change'], 'Yes'),
]

hypothesis = ['Ø'] * len(data[0][0])

for attributes, output in data:
    if output == 'Yes':  # only positive examples
        for i in range(len(attributes)):
            if hypothesis[i] == 'Ø':                  
                hypothesis[i] = attributes[i]
            elif hypothesis[i] != attributes[i]:        
                hypothesis[i] = '?'
print("Final Hypothesis:", hypothesis)
