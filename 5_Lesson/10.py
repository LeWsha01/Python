

def penultimate_len(string):
    string = string.split()[::-1]
    print(len(string[1]))


penultimate_len('In the end the winner is still the last man standing')