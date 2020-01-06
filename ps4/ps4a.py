

def get_permutations(sequence):

    if len(sequence) == 1:
        return list(sequence)
    else:
        list_result = get_permutations(sequence[1:])
        result = []
        for string in list_result:
            for i in range(len(string)+1):
                #print(string)
                string_copy = list(string)
                string_copy.insert(i, sequence[0])
                #print(string_copy)
                string_permutation = ''.join(string_copy)
                #print(string_permutation)
                result.append(string_permutation)
        return result
            
if __name__ == '__main__':
    get_permutations('abc')

