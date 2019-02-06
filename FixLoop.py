def list_animals(animals):
    list = ''
    l=1
    for i in animals:
        list += str(l) + '. ' + i + '\n'
        l += 1
    return list