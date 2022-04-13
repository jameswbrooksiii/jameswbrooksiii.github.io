from Trees import *
import time

text = open('SciFiLiBooks.txt', 'r').read()
splitbooks = text.split("\n")
r = Node(splitbooks[0])
i = 1
for i in range(len(splitbooks)):
    r = insert(r, splitbooks[i])

inorder(r)
print("-------------------------")
search(r, "Halo: The Fall of Reach")
