def find_strings(input_list):
    results = {}
    for input in input_list:
        # create empty array with 26 elements
        count = [0] * 26

        for letter in input:
            # get the alphabet index of each letter
            index = ord(letter) - ord('a')
            count[index] += 1
        
        # generate the Hash Map's key
        key = tuple(count)

        if key in results:
            results[key].append(input)
        else:
            results[key] = [input]

    return results.values()

strings = ['fuel', 'feul', 'break', 'braek', 'brake', 'random']
matches = list(find_strings(strings))

query = 'brake'

for possible_match in matches:
    if query in possible_match: print(possible_match)