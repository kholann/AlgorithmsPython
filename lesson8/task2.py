# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter
import heapq

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, code_dict, path):
        self.left.walk(code_dict, path + "0")
        self.right.walk(code_dict, path + "1")

class Leaf:
    def __init__(self, value):
        self.value = value

    def walk(self, code_dict, path):
        code_dict[self.value] = path
        return path

def Huffman(s):
    lst = []

    for i, item in Counter(s).items():
        lst.append((item, len(lst), Leaf(i)))

    iteration = len(lst)
    heapq.heapify(lst)
    while len(lst) > 1:
        first = heapq.heappop(lst)
        second = heapq.heappop(lst)
        heapq.heappush(lst, (first[0] + second[0], iteration, Node(first[2], second[2])))
        iteration += 1

    code_dict = {}
    if lst:
        lst[0][2].walk(code_dict, "")
    return code_dict

S = input('Введите строку из трех слов: ')

S = Counter(S)
print(f'Counter in string: {S}')

encode_S = Huffman(S)
print(f'String in Huffman: {encode_S}')

for key, value in encode_S.items():
    print(f'Key: {key}: value: {value}')

# Введите строку из трех слов: Hello my world
# Counter in string: Counter({'l': 3, 'o': 2, ' ': 2, 'H': 1, 'e': 1, 'm': 1, 'y': 1, 'w': 1, 'r': 1, 'd': 1})
# String in Huffman: {'l': '00', 'd': '010', 'o': '011', ' ': '100', 'H': '1010', 'e': '1011', 'm': '1100', 'y': '1101', 'w': '1110', 'r': '1111'}
# Key: l: value: 00
# Key: d: value: 010
# Key: o: value: 011
# Key:  : value: 100
# Key: H: value: 1010
# Key: e: value: 1011
# Key: m: value: 1100
# Key: y: value: 1101
# Key: w: value: 1110
# Key: r: value: 1111