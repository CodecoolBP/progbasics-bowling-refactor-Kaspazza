def score(game):
    global last
    result, frame, first_half = 0, 1, True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += value(game[i])
        if frame < 10 and game[i] in ('/', 'X', 'x') :
                result += value(game[i + 1])
                if game[i] in ('X', 'x'):
                    if game[i + 2] == '/':
                        result += 10 - value(game[i + 1])
                    else:
                        result += value(game[i + 2])
        last = value(game[i])
        if first_half:
            first_half = False
        else:
            first_half = True
            frame += 1
        if game[i] in ('X', 'x'):
            first_half = True
            frame += 1
    return result


def value(char):
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    if char in numbers:
        return int(char)
    elif char in ('X', 'x', '/'):
        return 10
    elif char == '-':
        return 0
