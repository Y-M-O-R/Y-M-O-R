x = 121

num_test = 123443212
num_test = str(num_test)
forwards = list(num_test)
backwards = forwards[::-1]

forwards = ''.join(forwards)
backwards = ''.join(backwards)

if forwards == backwards:
    print('win')
else:
    print('lose')