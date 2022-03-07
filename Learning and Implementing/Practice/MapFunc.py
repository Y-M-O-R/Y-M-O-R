# Practice Map Function
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sets = {1, 2, 3, 4, 5, 6, 7, 8, 9}
dicts = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four ': 4,
    'five ': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
tuples = (1, 2, 3, 4, 5, 6, 7, 8, 9)


def power_to(x):  # changes contents in data type to power of themselves
    return x ** x


# lists
lists = list(map(power_to, lists))
print(f'list, {lists} ,type, {type(lists)}')
lists = list(map(str, lists))
print(lists)

# sets
sets = set(map(power_to, sets))
print(f'sets, {sets}, type,{type(sets)}')

# dicts

dicts = list(map(power_to, dicts.values()))
print(f'dicts, {dicts}, type, {type(dicts)}')

# tuples

tuples = tuple(map(power_to, tuples))
print(f'tuples, {tuples}, type, {type(tuples)}')
