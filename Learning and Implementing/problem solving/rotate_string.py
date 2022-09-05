class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        print(-2)
        if len(s) == len(goal):  # s and goal are similar string's
            print(-1)
            if s[0] in goal:  # locate starting point of goal if any
                if s[0] == s[-1]: #
                    count = s.count(s[0]) # how many of first letter's are there
                    s_index_range = 0
                    for i in range(len(s)):
                        if s[i] == s[0]:
                            s_index_range+=1
                        else:
                            break

                    goal_start_point = goal.index(s[0]) + count-s_index_range
                    max_str = len(s)
                    print('maxstring', max_str)
                    s_start_point = 0
                    goal_shift = False  # if s continues into beginning of goal
                    print(0)
                    for element in range(max_str):
                        print(1)
                        if s_start_point != len(s) - 1:  # not all elements of s have been checked
                            print(2)
                            if goal_start_point < max_str and goal_shift == False:  # keep the index within goal
                                if s[s_start_point] == goal[goal_start_point]:  # if s and gaol are in sequence
                                    print('run')
                                    print(
                                        f's[{s[s_start_point]}] s[start]:{s_start_point}, goal[{goal[goal_start_point]}] goal[start]:{goal_start_point}, ')
                                    print()
                                    s_start_point += 1
                                    goal_start_point += 1
                                else:  # s and goal are not in sequence
                                    print('s and goal are not in the same sequence 1 s_start', s_start_point,
                                          s[s_start_point], 'goal', goal_start_point, goal[goal_start_point])
                                    return False
                            else:  # goal index to great
                                print(3)
                                if goal_shift == False:
                                    goal_start_point = 0  # change goal index to beginning
                                goal_shift = True  # s continues into beginng of goal

                            if goal_shift:  # if s continues into the beginning of goal

                                print('mew')
                                print(goal_start_point)
                                if s[s_start_point] == goal[goal_start_point]:  # if s and gaol are in sequence
                                    s_start_point += 1
                                    goal_start_point += 1
                                else:  # s and goal are not in sequence
                                    print('1s and goal are not in the same sequence ', s_start_point, 'goal',
                                          goal_start_point)

                                    return False
                        else:  # s and goal are the same (but shifted)
                            print('ding-ding')
                            return True


                else:






                    max_str = len(s)
                    print('maxstring', max_str)
                    goal_start_point = goal.index(s[0])
                    s_start_point = 0
                    goal_shift = False # if s continues into beginning of goal
                    print(0)
                    for element in range(max_str):
                        print(1)
                        if s_start_point != len(s) - 1:  # not all elements of s have been checked
                            print(2)
                            if goal_start_point < max_str and goal_shift == False:  # keep the index within goal
                                if s[s_start_point] == goal[goal_start_point]:  # if s and gaol are in sequence
                                    print('run')
                                    print(f's[{s[s_start_point]}] s[start]:{s_start_point}, goal[{goal[goal_start_point]}] goal[start]:{goal_start_point}, ')
                                    print()
                                    s_start_point += 1
                                    goal_start_point += 1
                                else:  # s and goal are not in sequence
                                    print('s and goal are not in the same sequence 1 s_start', s_start_point,
                                          s[s_start_point], 'goal', goal_start_point, goal[goal_start_point])
                                    return False
                            else:  # goal index to great
                                print(3)
                                if goal_shift == False:
                                    goal_start_point = 0  # change goal index to beginning
                                goal_shift = True # s continues into beginng of goal

                            if  goal_shift:   # if s continues into the beginning of goal

                                print('mew')
                                print(goal_start_point)
                                if s[s_start_point] == goal[goal_start_point]:  # if s and gaol are in sequence
                                    s_start_point += 1
                                    goal_start_point += 1
                                else:  # s and goal are not in sequence
                                    print('1s and goal are not in the same sequence ', s_start_point, 'goal',
                                          goal_start_point)

                                    return False
                        else:  # s and goal are the same (but shifted)
                            print('ding-ding')
                            return True

            else:  # no starting point loacted for goal
                print('s has no location at goal')
                return False

        else:  # s and goal two different string's
            print('s and goal are not the same length')
            return False

        # if s[0] in goal:
        #    pos = goal.index(s[0])

        #    new_s = goal[pos:] +goal[:pos]
        #    print(goal[pos:])
        #    print(goal[pos])

        #    if s == new_s:
        #        return True
        # else:
        #    print(2)
        #    return False


rotate = Solution()
if rotate.rotateString('bqqutquvbtgouklsayfvzewpnrbwfcdmwctusunasdbpbmhnvy', 'wpnrbwfcdmwctusunasdbpbmhnvybqqutquvbtgouklsayfvze'):
    print(True)
elif not rotate.rotateString('bqqutquvbtgouklsayfvzewpnrbwfcdmwctusunasdbpbmhnvy', 'wpnrbwfcdmwctusunasdbpbmhnvybqqutquvbtgouklsayfvze'):
    print(False)
else:
    print(False, 23)
print('exit')
"bbbacddceeb"
"ceebbbbacdd"

"bqqutquvbtgouklsayfvzewpnrbwfcdmwctusunasdbpbmhnvy"
"wpnrbwfcdmwctusunasdbpbmhnvybqqutquvbtgouklsayfvze"
