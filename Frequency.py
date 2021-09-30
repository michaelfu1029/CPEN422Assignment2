import numpy as np


ciphertext = 'KYLZLUWCPLEYIIZRQCFZRPEYIIZPZWXLFQFZLLQCDTLHYTEYTNXOQQRWLLYFZNURZPLYKQZPNYKAZPHYTNWOQXXYLWPLFZLLFQJZHHYTIZKZAQZNWEQZPOQXXYLLFQFZLLQCPFYYOFWPFQZXIYTCKUTNNHXYLKYLWFQCQRNWQXXYLJQGTZCCQNNQXNZPLIZCEFBTPLDQUYCQFQJQKLIZXEYIIZHYTOKYJRYWKLWKAJWLFFWPLQZPRYYKZLLFQIZCEFFZCQEYIIZWLJZPZLLFQACQZLEYKEQCLAWMQKDHLFQGTQQKYUFQZCLPEYIIZZKXWFZXLYPWKALJWKONQEYIIZLJWKONQEYIIZNWLLNQDZLFYJWJYKXQCJFZLHYTCQZLHYTOKYJLFQPYKAEYIIZRQCFZRPWMQFQZCXPYIQLFWKANWOQWLEYIIZPZWXZNWEQ'
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def getCounts(cipher):
    counts = []
    for letter in alphabet:
        counts.append(ciphertext.count(letter))
        
    return counts

counts = getCounts(ciphertext)

sortedCounts = np.sort(counts)
indexes = np.argsort(counts)

testPlain = [' '] * len(ciphertext)

alphabetDict = {}
for letter in alphabet:
    alphabetDict[letter] = ' '
    
def guessLetter(cipherLetter, plainLetter):
    for i in range(len(ciphertext)):
        if ciphertext[i] == cipherLetter:
            testPlain[i] = plainLetter
            
    alphabetDict[cipherLetter] = plainLetter
    
    
    
def makeAnswer(testPlain):
    return "".join(l for l in testPlain)
    
'''

16 Q = E Frequency
11 L = T Frequency
25 Z = A Frequency
24 Y = O Frequency

10 K = N Guess _OT NOT 

15 P = S Guess TEA__OON teaspoon
17 R = P

5  F = H Guess T_E THE

2  C = R Guess PE_HAPS PERHAPS

14 O = K Guess _EEP KEEP

22 W = I Guess _T IT

20 U = F Guess _IRST FIRST

13 N = L Guess HA_F HALF

23 X = D Guess SAI_ SAID

0  A = G Guess LON_ LONG

7  H = Y Guess AS LONG AS _O_ LIKED -> YOU
19 T = U 

3  D = B Guess _UT BUT

4  E = C Guess _OULD COULD

9  J = W Guess _AY WAY

8  I = M Guess _ANAGE MANAGE

6  G = Q Guess _UARRELLED QUARRELLED

1  B = J Guess _UST JUST

12 M = V Guess GI_EN GIVEN
'''