
#https://coderbyte.com/



#01-------------------------------------------------------
def FirstReverse(input_string):
  return input_string[::-1]
  
test_case = 'kruki i Kotki'
print(FirstReverse(test_case))



#02-------------------------------------------------------
def LetterChanges(str):
  in_list=list(str)
  out_list=[]
    
  for l in in_list:
    print(l,ord(l.lower()))
    if(ord(l.lower()) >= ord('a') and ord(l.lower()) <= ord('z')):
      print('in')
      c=chr(ord(l)+1)
      if(c.lower() in 'aeiou'):
        c=c.upper()
      out_list.append(c)
    else:
      out_list.append(l)
  # code goes here
  return ''.join(out_list)


test_case='fun times!Z'
print(LetterChanges(test_case))

def LetterChanges(str):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW"
    changes = "bcdEfghIjklmnOpqrstUvwxyzABCDEFGHIJKLMNOPQRSTUVWZ"
    mapping = { k:v for (k,v) in zip(test_case+letters,test_case+changes) }
    return "".join([ mapping[c] for c in str ])

test_case='fun times!Z'
print(LetterChanges(test_case))

#03-------------------------------------------------------

def SimpleAdding(num):
    s=0
    for n in range(num):
        s+=n+1

    return s

SimpleAdding(12)  

#04-------------------------------------------------------

def FirstFactorial(num):

    f=1
    for n in range(num):
        f*=n+1

    return f

FirstFactorial(4)

#05-------------------------------------------------------

def LongestWord(sen):
    letters='abcdefghijklmnopqrstuwxyz 1234567890'
    str_clean=''

    for l in sen:
        if l.lower() in letters:
            str_clean+=l

    return max(str_clean.split(), key=len)

test_case='ala ma kota'
print(LongestWord(test_case))

#06-------------------------------------------------------

def AlphabetSoup(str):
    return ''.join(filter(lambda x: x.isalpha(), sorted(str)))


test_case='ala ma kota'
print(AlphabetSoup(test_case))

#07-------------------------------------------------------

'''
#Scale Balancing

# Have the function ScaleBalancing(strArr) 
# read strArr which will contain two elements, 
# the first being the two positive integer weights on a balance scale (left and right sides) 
# and the second element being a list of available weights as positive integers.

# Your goal is to determine if you can balance the scale 
# by using the least amount of weights from the list, 
# but using at most only 2 weights. 

# For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then 
# this means there is a balance scale with a weight of 5 on the left side 
# and 9 on the right side. 
# It is in fact possible to balance this scale by adding a 6 
# to the left side from the list of weights and adding a 2 to the right side. 
# Both scales will now equal 11 and they are perfectly balanced. 

# Your program should return a comma separated string of the weights that were used
# from the list in ascending order, so for this example your program should return the string 2,6

There will only ever be one unique solution and the list of available weights will not be empty. It is also possible to add two weights to only one side of the scale to balance it. If it is not possible to balance the scale then your program should return the string not possible.
Examples
Input: ["[3, 4]", "[1, 2, 7, 7]"]
Output: 1
Input: ["[13, 4]", "[1, 2, 3, 6, 14]"]
Output: 3,6
'''

def ScaleBalancing(strArr):
    scale_l=eval(strArr[0])[0]
    scale_r=eval(strArr[0])[1]

    if scale_l==scale_r: 
        return ''
    
    weights=eval(strArr[1])

    scale_light=min(eval(strArr[0]))
    scale_heavy=max(eval(strArr[0]))

    #check single weight
    for w1 in weights:
        if scale_light+w1==scale_heavy:
            return str(w1)
    
    #check both weights
    for w1 in sorted(weights):
        #reset light/heavy
        weights2=eval(strArr[1])
        weights2.remove(w1)
        scale_light=min(eval(strArr[0]))
        scale_heavy=max(eval(strArr[0]))

        #update light/heavy
        if scale_light+w1>scale_heavy:
            scale_tmp=scale_heavy
            scale_heavy=scale_light+w1
            scale_light=scale_tmp
        else:
            scale_light+=w1

        for w2 in sorted(weights2):
            if scale_light+w2==scale_heavy:
                return min(str(w1),str(w2))+','+max(str(w1),str(w2))
    return 'not possible'

ScaleBalancing(["[13, 4]", "[1, 2, 3, 3, 4]"])
ScaleBalancing(["[5, 9]", "[1, 2, 6, 7]"])
ScaleBalancing(["[6, 2]", "[1, 10, 6, 5]"])




def ScaleBalancing2(strArr):
    s_l=min(eval(strArr[0]))
    s_h=max(eval(strArr[0]))
    weights=eval(strArr[1])

    scales_w1=[s for s in map(lambda x: (min(s_l+x,s_h), max(s_l+x,s_h), x), sorted(weights))]

    for s in scales_w1:
        if s[0]==s[1]:
            return str(s[2])
        else:
            #for each not used weight
            for w in [w for w in weights if w!=s[2]]:
                if s[0]+w==s[1]:
                    return str(min(w, s[2]))+','+str(max(w, s[2]))

    return 'not possible'

ScaleBalancing2(["[13, 4]", "[1, 2, 3, 3, 4]"])
ScaleBalancing2(["[5, 9]", "[1, 2, 6, 7]"])
ScaleBalancing2(["[6, 2]", "[1, 10, 6, 5]"])



#08-------------------------------------------------------
'''
Have the function VowelSquare(strArr) 
take the strArr parameter being passed which will be a 2D matrix of some arbitrary size
filled with letters from the alphabet, 
and determine if a 2x2 square composed entirely of vowels exists in the matrix. 
For example: strArr is ["abcd", "eikr", "oufj"] then this matrix looks like the following:

a b c d
e i k r
o u f j

Within this matrix there is a 2x2 square of vowels starting in the second row and first column, 
namely, ei, ou. If a 2x2 square of vowels is found 
your program should return the top-left position (row-column) of the square, 
so for this example your program should return 1-0. 
If no 2x2 square of vowels exists, then return the string not found. 
If there are multiple squares of vowels, return the one that is at the most top-left 
position in the whole matrix. The input matrix will at least be of size 2x2. 
'''

from collections import defaultdict

def VowelSquare(strArr):

    vovels = ['a','e','i','o','u']

    row_candidates = defaultdict(set)

    for r, row in enumerate(strArr):
        for c, col in enumerate(row[:-1]):
            if col in vovels and row[c+1] in vovels:
                row_candidates[r].add(c)

    for r, candidates in row_candidates.items():
        common_candidate=candidates.intersection(row_candidates.get(r+1, {}))
        if len(common_candidate) > 0:
            return str(r) + '-' + str(min(common_candidate))

    return 'not found'

VowelSquare(["abcd", "eikr", "oufj"])
VowelSquare(["aqrst", "ukaei", "ffooo"])


#09-------------------------------------------------------
'''
Have the function CorrectPath(str) read the str parameter being passed, 
which will represent the movements made in a 5x5 grid of cells starting from the top left position. 
The characters in the input string will be entirely composed of: r, l, u, d, ?. 
Each of the characters stand for the direction to take within the grid, 
for example: r = right, l = left, u = up, d = down. 
Your goal is to determine what characters the question marks should be 
in order for a path to be created to go from the top left of the grid 
all the way to the bottom right without touching previously travelled on cells in the grid.

For example: if str is "r?d?drdd" then your program should output the final correct string 
that will allow a path to be formed from the top left of a 5x5 grid to the bottom right. 
For this input, your program should therefore return the string rrdrdrdd. 
There will only ever be one correct path and there will always be at least one question mark 
within the input string.

Examples
Input: "???rrurdr?"
Output: dddrrurdrd
Input: "drdr??rrddd?"
Output: drdruurrdddd
'''

from copy import deepcopy

def CorrectPath(str):
    move_values = {'r':(0,1), 'l':(0,-1), 'd':(1,0), 'u':(-1,0), '?':(0,0)}
    move_values_inverse = {v: k for k, v in move_values.items()}

    path = [move_values[m] for m in list(str)]
    paths = [path]
    
    #create all paths permutations
    for move_no, move in enumerate(list(str)):
        if move == '?':
            copy1, copy2, copy3 = deepcopy(paths), deepcopy(paths), deepcopy(paths)
            
            for path in paths: path[move_no] = move_values['r']
            for path in copy1: path[move_no] = move_values['l']
            for path in copy2: path[move_no] = move_values['d']
            for path in copy3: path[move_no] = move_values['u']

            paths.extend(copy1)
            paths.extend(copy2)
            paths.extend(copy3)

    #eliminate out of matrix paths and visited paths
    for path in paths:
        visited = {}
        pos_x, pos_y = 0, 0

        for move in path:
            visited[(pos_x, pos_y)] = True
            pos_x += move[0]
            pos_y += move[1]

            if max(pos_x, pos_y) > 4 or min(pos_x, pos_y) < 0:
                break

            if (pos_x, pos_y) in visited:
                break
        else:
            if (pos_x, pos_y) == (4,4):
                return ''.join([move_values_inverse[k] for k in path])
    
    return 'not found'

from itertools import product

def CorrectPath(str):
    moves = {'r':(0,1), 'l':(0,-1), 'd':(1,0), 'u':(-1,0)}
    moves_inverse = {v: k for k, v in moves.items()}

    path = [moves.get(m, None) for m in list(str)]
    unknown_moves = [move_no for move_no, move in enumerate(path) if move is None]
    
    # iterate all permutation on moves in unknown (?) poitions 
    for perutation in product(moves.values(), repeat=len(unknown_moves)):
        # for each permutation create path
        for i, move in enumerate(perutation):
            path[unknown_moves[i]]=move
        
        # check path for: 
        # a) in matrix bounds 
        # b) single visit in each cell 
        # c) proper final position

        pos_x, pos_y = 0, 0
        visited = {(pos_x, pos_y):True}

        for move in path:
            pos_x += move[0]
            pos_y += move[1]

            if max(pos_x, pos_y) > 4 or min(pos_x, pos_y) < 0:
                break

            if (pos_x, pos_y) in visited:
                break

            visited[(pos_x, pos_y)] = True
        else:
            if (pos_x, pos_y) == (4,4):
                return ''.join([moves_inverse[k] for k in path])
                
    

def CorrectPath(str):
    moves = {'r':(0,1), 'l':(0,-1), 'd':(1,0), 'u':(-1,0)}
    
    unknown_moves = [m for m in list(str) if m == '?']
    
    # iterate all permutation on moves with unknown (?) direction 
    for permutation in product(moves, repeat=len(unknown_moves)):
        permutation = list(permutation)
        
        path=''
        pos = (0, 0)
        visited = [pos]

        for move in list(str):
            if move == '?': move = permutation.pop()
            pos = tuple(sum(x) for x in zip(pos, moves[move])) 
        
            if pos in visited: break
            if max(pos) > 4 or min(pos) < 0: break

            path += move
            visited.append(pos)
        else:
            if pos == (4,4):
                return path
                
    
CorrectPath('rrrrddd?')


CorrectPath('drdr??rrddd?')

          # 'drdruurrdddd'

CorrectPath('rrrrddd?')
CorrectPath('???rrurdr?')

#10-------------------------------------------------------

'''
Have the function FindIntersection(strArr) read the array of strings stored in strArr 
which will contain 2 elements: 
the first element will represent a list of comma-separated numbers sorted in ascending order, 
the second element will represent a second list of comma-separated numbers (also sorted). 
Your goal is to return a comma-separated string containing the numbers that
 occur in elements of strArr in sorted order. If there is no intersection, return the string false.

For example: if strArr contains ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"] 
the output should return "1,4,13" because those numbers appear in both strings. 
The array given will not be empty, 
and each string inside the array will be of numbers sorted in ascending order
and may contain negative numbers.

Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13
Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10
'''


def FindIntersection(strArr):
    a, b = map(lambda x: set([x]) if type(x)==int else set(x), map(eval, strArr))
    return ','.join(map(str, sorted(a.intersection(b)))) or 'false'

FindIntersection(["2, 3, 4", "1"])
FindIntersection(["2, 3, 4", "2"])
FindIntersection(["2, 3, 4", "4,2"])


#11-------------------------------------------------------
'''
Have the function QuestionsMarks(str) take the str string parameter,
 which will contain single digit numbers, letters, and question marks, 
 and check if there are exactly 3 question marks 
 between every pair of two numbers that add up to 10. 
 If so, then your program should return the string true, 
 otherwise it should return the string false. 
 If there aren't any two numbers that add up to 10 in the string, 
 then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true 
because there are exactly 3 question marks between 6 and 4, 
and 3 question marks between 5 and 5 at the end of the string. 

Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true

'''

def QuestionsMarks(strArg):
    has_adding_digits = False
    for pos1, letter1 in enumerate(list(strArg[:-1])):
        for pos2, letter2 in enumerate(list(strArg[pos1+1:]), pos1+1):

            between = strArg[pos1+1:pos2]
            print(pos1, pos2, letter1, letter2, letter1.isdigit() and letter2.isdigit(), between)

            if not (letter1.isdigit() and letter2.isdigit()):
                continue

            if int(letter1)+int(letter2) != 10:
                continue

            has_adding_digits = True
            between = strArg[pos1+1:pos2]
            count = len([l for l in list(between) if l == '?'])

            print(pos1, pos2, between, count)

            if count != 3:
                return 'false'

    return 'true' if has_adding_digits else 'false'



def QuestionsMarks(strArg):
    dig_pos = [i for i, letter in enumerate(list(strArg)) if letter.isdigit()]
    dig_val = [int(strArg[d]) for d in dig_pos]
    
    pos = zip(dig_pos[:-1], dig_pos[1:])
    val = zip(dig_val[:-1], dig_val[1:])
    pairs = {pos:val for pos, val in zip(pos, val) if sum(val) == 10}

    if len(pairs) == 0:
        return 'false'

    for pos in pairs:
        mid = strArg[pos[0]+1:pos[1]]
        if mid.count('?') != 3:
            return 'false'
    else:
        return 'true'
    
QuestionsMarks('9???1???9???1???9')

QuestionsMarks('5??aaaaaaaaaaaaaaaaaaa?5?a??5')

QuestionsMarks('1???9')

QuestionsMarks('')

QuestionsMarks('acc?7??sss?3rr1??????5')
QuestionsMarks('aa6?9')
QuestionsMarks('1abcd2')

QuestionsMarks('acc?7???3rr1??????5')
QuestionsMarks('acc?7??sss?3rr1??????5')




#11-------------------------------------------------------
'''
Have the function ClosestEnemyII(strArr) 
read the matrix of numbers stored in strArr which will be a 2D matrix 
that contains only the integers 1, 0, or 2. 
Then from the position in the matrix where a 1 is, 
return the number of spaces either left, right, down, or up you must move 
to reach an enemy which is represented by a 2. 
You are able to wrap around one side of the matrix to the other as well. 
For example: if strArr is ["0000", "1000", "0002", "0002"] 
then this looks like the following:

0 0 0 0
1 0 0 0
0 0 0 2
0 0 0 2

For this input your program should return 2 
because the closest enemy (2) is 2 spaces away from the 1 
by moving left to wrap to the other side and then moving down once. 
The array will contain any number of 0's and 2's, but only a single 1.
It may not contain any 2's at all as well, 
where in that case your program should return a 0.

Examples
Input: ["000", "100", "200"]
Output: 1
Input: ["0000", "2010", "0000", "2002"]
Output: 2
'''

def ClosestEnemyII(strArr):
    m = [list(r) for r in strArr]
    
    pos_foes = []
    
    for ir, r in enumerate(m):
        for ic, c in enumerate(r):
            if c == '1':
                pos_friend = (ir, ic)
            if c == '2':
                pos_foes.append((ir, ic))

    if len(pos_foes) == 0:
        return 0

    r, c = len(m), len(m[0])
    min_dist = r + c

    for pos_foe in pos_foes:
        dist_r = min([abs((pos_friend[0] + s) % r - (pos_foe[0] + s) % r) for s in range(r)])
        dist_c = min([abs((pos_friend[1] + s) % c - (pos_foe[1] + s) % c) for s in range(c)])
        if dist_r + dist_c < min_dist:
            min_dist = dist_r + dist_c

    return min_dist         

ClosestEnemyII(["0000000", "0001000", "0000000", "0000000", "0000000", "2000000", "0000000"])
ClosestEnemyII(["0000", "2010", "0000", "2002"])
ClosestEnemyII(["000", "100", "200"])



#12-------------------------------------------------------

'''
Have the function EquivalentKeypresses(strArr) read the array of strings stored in strArr 
which will contain 2 strings representing two comma separated lists of keypresses. 
Your goal is to return the string true if the keypresses produce the same printable string 
and the string false if they do not. 
A keypress can be either a printable character or a backspace represented by -B. 
You can produce a printable string from such a string of keypresses 
by having backspaces erase one preceding character.

For example: if strArr contains ["a,b,c,d", "a,b,c,c,-B,d"] 
the output should return true because those keypresses produce the same printable string.
The array given will not be empty. The keypresses will only contain letters from the alphabet and backspaces.

Examples
Input: ["a,b,c,d", "a,b,c,d,-B,d"]
Output: true
Input: ["c,a,r,d", "c,a,-B,r,d"]
Output: false
'''

def EquivalentKeypresses(strArr):
    a, b =  map(lambda x: x.split(','), strArr)

    print(a, b)

    mark_for_deletion = []
    for pos, key_press in enumerate(a):
        if key_press == '-B':
            mark_for_deletion.extend([pos-1, pos])
    a = [l for p, l in enumerate(a) if not p in mark_for_deletion and l != '']
    
    mark_for_deletion = []
    for pos, key_press in enumerate(b):
        if key_press == '-B':
            mark_for_deletion.extend([pos-1, pos])
    b = [l for p, l in enumerate(b) if not p in mark_for_deletion and l != '']

    print(a, b)
    print(len(a), len(b))
    return 'true' if a == b else 'false'



EquivalentKeypresses(["", "-B,-B,-B"])
EquivalentKeypresses(["q,w,e,r,t,y", "-B,-B,q,w,w,-B,e,r,t,y"])
EquivalentKeypresses(["p,o,i,n,-B,t", "-B,p,o,i,t"])
EquivalentKeypresses(["s,t,r,e,e,t", "-B,s,s,-B,t,r,e,e,t"])
EquivalentKeypresses(["a,b,c,d", "a,b,c,d,-B,e"])