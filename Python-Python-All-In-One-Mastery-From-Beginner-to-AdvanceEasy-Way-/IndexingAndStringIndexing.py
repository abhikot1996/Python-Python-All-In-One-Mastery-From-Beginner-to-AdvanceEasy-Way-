"""
Indexing And String Indexing
Apposite string indexing start with -1
E.g
  0  1  2  3  4  5  6  7  (Left to Right String idexing)
" G  a  n  g  s  t  e  r " (String)
 -1 -2 -3 -4 -5 -6 -7 -8  (Right to Left String idexing)
"""
# E.g 1),
# (If want to print single character at time)
name = "Gangster"
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[-7])
print(name[-8])

# E.g 2),
print(name[-8])
print(name[-7])
print(name[-6])
print(name[-5])
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])

# E.g 3),
# (If want to print multiple character at time)
print(name[0:4])

#E.g 4)
# (If don't want to print multiple characters from string)
#print(name[0:7:2])
# or
# print(name[0::2])
#Syntax 1,
# print(name[StartPoint:EndPoint:StepSize])
# Syntax 2,
# print(name[StartPoint::StepSize])
print(name[0::2])
#   0  1  2  3  4  5  6  7  (Left to Right String indexing)
# " G  a  n  g  s  t  e  r " (String)
# (o/p) G n s e
#       0 2 4 6

#E.g 5)
string='1 2 3 4 5 6 7 8 9' #(Python treats space as a charcater)
print(string[0::3])

