# Advent of Code 2022, Day 21 Part 1 and 2
# Michael Chen
# 12/31/2022

def monkey(func:str, library:dict):
    """Executes `func`, a key to a function defined as a string in `library`."""

    expr = library[func]
    if type(expr) is int:
        return expr

    # Assuming all func calls two other func.
    func1, op, func2 = expr.split(' ')

    eval_str = 'monkey("' +func1+ '",library)' + op + 'monkey("'+func2+'",library)'
    return eval(eval_str)

def find_humn(library:dict):
    """Starts at 'root' in library and finds the humn value needed to set both
    sides of 'root' equal to each other."""

    library['root'] = library['root'].replace('+','=')

    # jiggle is used to find which side is affected by 'humn'.
    jiggle = library.copy()
    jiggle['humn'] = library['humn'] + 1

    def reverse_op():
        match op:
            case '+':
                return target - monkey(other_func, library)
            case '-':
                if func == func1:
                    return target + monkey(other_func, library)
                else:
                    return monkey(other_func, library) - target
            case '*':
                return target / monkey(other_func, library)
            case '/':
                if func == func1:
                    return target * monkey(other_func, library)
                else:
                    return monkey(other_func, library) / target
            case '=':
                return monkey(other_func, library)

    func = 'root'
    while func != 'humn':
        expr = library[func]
        func1, op, func2 = expr.split(' ')

        if monkey(func1, library) != monkey(func1, jiggle):
            func = func1
            other_func = func2
        else:
            func = func2
            other_func = func1

        target = reverse_op()

    return target


if __name__ == "__main__":

    start = 'root'

    with open('input.txt') as f:
        input1 = f.read().strip()
    lines = input1.split('\n')

    library = {}
    for line in lines:
        key, colon, val = line.partition(': ')
        library[key] = int(val) if val.isnumeric() else val

    print("'root' yells: ", monkey('root',library))
    print("'humn' yells: ",find_humn(library))




