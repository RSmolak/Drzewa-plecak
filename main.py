import random

class Node:
    def __init__(self, c_value, w_value):
        self.c_value = c_value
        self.w_value = w_value


n = 6
capacity = random.randint(5*n, 10*n)
c_value_list = []  # Wektor wartości
w_value_list = []  # Wektor wag

solutions = []
left = []
value = 0
weight = 0

max_value = 0

for i in range(n):
    left.append(Node(random.randint(1, 30), random.randint(1, 30)))


def recursiveTree():
    global value, weight, max_value
    for i in range(n):
        if weight+left[i].w_value > capacity:
            return

        solutions.append(left[i])
        left.remove(left[i])
        
        value += solutions[-1].c_value
        weight += solutions[-1].w_value


        if weight > capacity or len(left) == 0:
            return
        recursiveTree()
        if value > max_value:
            max_value = value
        removed_node = solutions.pop(-1)
        left.append(removed_node)
        value -= removed_node.c_value
        weight -= removed_node.w_value


recursiveTree()
print(value, weight, max_value, capacity)


