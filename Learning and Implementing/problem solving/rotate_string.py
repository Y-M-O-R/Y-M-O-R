s = "bbbacddceeb"
goal ="ceebbbbacdd"

#print(goal.index('b'))
pos = goal.index(s[0])
#print(pos)

new_s = goal[pos:] +goal[:pos]

print(goal[3])
print(goal[:3])
print(new_s)


if s == new_s:
    print('True')
else:
    print('False')