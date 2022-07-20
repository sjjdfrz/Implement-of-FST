from FST_Machine import *

set0 = 'abcdefghijklmnopqrstuvwxyz'
set1 = 'zxo'
set2 = 'sc'
set3 = 'aeiou'
set4 = 'bcdfghjklmnpqrstvwxyz'
set5 = 'abcdgijklmnpqrtuvw'
set6 = 'abcdeghijklmnopqrstuvwxyz'
set7 = 'abdefghijklmnopqrtuvwxyz'
set8 = 'abcdefghijklmnopqrtuvwxyz'

fst = FST()

fst.add_state('q0', False, True)
fst.add_state('q1', False, False)
fst.add_state('q2', False, False)
fst.add_state('q3', False, False)
fst.add_state('q4', False, False)
fst.add_state('q5', False, False)
fst.add_state('q6', False, False)
fst.add_state('q7', False, False)
fst.add_state('q8', False, False)
fst.add_state('q9', False, False)
fst.add_state('q10', False, False)
fst.add_state('q11', False, False)
fst.add_state('q12', False, False)
fst.add_state('q13', False, False)
fst.add_state('q14', False, False)
fst.add_state('q15', False, False)
fst.add_state('q16', False, False)
fst.add_state('q17', False, False)
fst.add_state('q18', False, False)
fst.add_state('q19', False, False)
fst.add_state('q20', False, False)
fst.add_state('q21', False, False)
fst.add_state('q22', False, False)
fst.add_state('q23', False, False)
fst.add_state('q24', False, False)
fst.add_state('qf', True, False)

fst.add_set_transition(set0, 'q0', 'q0')

fst.add_set_transition(set1, 'q0', 'q1')
fst.add_transition('λ', 'e', 'q1', 'q2')
fst.add_transition('λ', 's', 'q2', 'qf')

fst.add_set_transition(set2, 'q0', 'q3')
fst.add_transition('h', 'h', 'q3', 'q4')
fst.add_transition('λ', 'e', 'q4', 'q5')
fst.add_transition('λ', 's', 'q5', 'qf')

fst.add_transition('s', 's', 'q0', 'q6')
fst.add_transition('s', 's', 'q6', 'q7')
fst.add_transition('λ', 'e', 'q7', 'q8')
fst.add_transition('λ', 's', 'q8', 'qf')

fst.add_set_transition(set3, 'q0', 'q9')
fst.add_transition('y', 'y', 'q9', 'q10')
fst.add_transition('λ', 's', 'q10', 'qf')

fst.add_set_transition(set4, 'q0', 'q11')
fst.add_transition('y', 'i', 'q11', 'q12')
fst.add_transition('λ', 'e', 'q12', 'q13')
fst.add_transition('λ', 's', 'q13', 'qf')

fst.add_transition('f', 'v', 'q0', 'q14')
fst.add_transition('e', 'e', 'q14', 'q15')
fst.add_transition('λ', 'e', 'q14', 'q16')
fst.add_transition('λ', 's', 'q15', 'qf')
fst.add_transition('λ', 's', 'q16', 'qf')

fst.add_set_transition(set5, 'q0', 'q17')
fst.add_transition('λ', 's', 'q17', 'qf')

fst.add_set_transition(set6, 'q0', 'q18')
fst.add_transition('e', 'e', 'q18', 'q19')
fst.add_transition('λ', 's', 'q19', 'qf')

fst.add_set_transition(set7, 'q0', 'q20')
fst.add_transition('h', 'h', 'q20', 'q21')
fst.add_transition('λ', 's', 'q21', 'qf')

fst.add_set_transition(set8, 'q0', 'q22')
fst.add_transition('s', 's', 'q22', 'q23')
fst.add_transition('λ', 'e', 'q23', 'q24')
fst.add_transition('λ', 's', 'q24', 'qf')

myFile = open('C:/Users/Sajjadf/Desktop/test.txt', 'r')
list1 = myFile.readlines()
list2 = []
for noun in list1:
    list2.append(noun.rstrip('\n'))

for word in list2:
    print(fst.parse_input(fst.getInitial(), word, ''))
    fst.outStrings.clear()
    if len(fst.outStrings) == 0:
        fst.outStrings.append("FAIL")

# fst2 = FST()
#
# fst2.add_state('q0', False, True)
# fst2.add_state('q1', False, False)
# fst2.add_state('qf', True, False)
#
# fst2.add_set_transition(set0, 'q0', 'q0')
# fst2.add_transition('s', 's', 'q0', 'q1')
# fst2.add_set_transition(set8, 'q0', 'qf')
# fst2.add_transition('λ', 'λ', 'q1', 'qf')
# fst2.add_transition('s', 'λ', 'q1', 'qf')
#
#
# print(fst2.parse_input(fst2.getInitial(), 'chess', ''))
