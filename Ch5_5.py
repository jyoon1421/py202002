
def flatten(data):
    result = []
    for element in data:
        if type(element) == list:
            result += flatten(element)
        else:
            result.append(element)
    return result

example = [ [1,2,3], [4,[5,6]],7,[8,9]]
print("원본:", example)
print("변환:", flatten(example))
