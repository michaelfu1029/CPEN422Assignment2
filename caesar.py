import numpy as np


ciphertext = 'KYLZLUWCPLEYIIZRQCFZRPEYIIZPZWXLFQFZLLQCDTLHYTEYTNXOQQRWLLYFZNURZPLYKQZPNYKAZPHYTNWOQXXYLWPLFZLLFQJZHHYTIZKZAQZNWEQZPOQXXYLLFQFZLLQCPFYYOFWPFQZXIYTCKUTNNHXYLKYLWFQCQRNWQXXYLJQGTZCCQNNQXNZPLIZCEFBTPLDQUYCQFQJQKLIZXEYIIZHYTOKYJRYWKLWKAJWLFFWPLQZPRYYKZLLFQIZCEFFZCQEYIIZWLJZPZLLFQACQZLEYKEQCLAWMQKDHLFQGTQQKYUFQZCLPEYIIZZKXWFZXLYPWKALJWKONQEYIIZLJWKONQEYIIZNWLLNQDZLFYJWJYKXQCJFZLHYTCQZLHYTOKYJLFQPYKAEYIIZRQCFZRPWMQFQZCXPYIQLFWKANWOQWLEYIIZPZWXZNWEQ'
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(1, len(alphabet)):
    plaintext = ""
    for letter in ciphertext:
        plaintext += alphabet[(alphabet.index(letter) + i) % 26]
    print("Shift is: " + str(i))
    print(plaintext)