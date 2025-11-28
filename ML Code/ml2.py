import csv

def read_data(filename):
    with open(filename) as f:
        data = [row for row in csv.reader(f)]
    return data

def candidate_elimination(data):
    # Initialize S with the most specific hypothesis
    S = ['Ø'] * (len(data[0]) - 1)

    # Initialize G with the most general hypothesis
    G = ['?'] * (len(data[0]) - 1)

    for row in data:
        attributes, output = row[:-1], row[-1]

        if output == "Yes":  # Positive Example
            # Remove those hypotheses from G that are inconsistent
            for i in range(len(G)):
                if G[i] != '?' and G[i] != attributes[i]:
                    G[i] = '?'

            # Generalize S
            for i in range(len(S)):
                if S[i] == 'Ø':
                    S[i] = attributes[i]
                elif S[i] != attributes[i]:
                    S[i] = '?'

        else:  # Negative Example
            # Specialize G
            for i in range(len(G)):
                if G[i] == '?':
                    if S[i] != attributes[i]:
                        G[i] = S[i]
                else:
                    G[i] = '?'

    return S, G


# Load data & run CE Algorithm
data = read_data("training.csv")
S_final, G_final = candidate_elimination(data)

print("Final Specific Boundary (S): ", S_final)
print("Final General Boundary (G): ", G_final)
