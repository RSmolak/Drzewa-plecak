import random


class Node:
    def __init__(self, value, weight, upp_bound, level):
        self.value = value
        self.weight = weight
        self.upper_bound = upp_bound
        self.level = level

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
    def __str__(self):
        return "value: "+ str(self.value) + " weight: "+ str(self.weight)

def calculate_bound(node: Node):
    global items, solution_perm
    bound = 0
    for i in range(node.level):
        if solution_perm[i] == 1:
            bound+=items[i].value
    for i in range(node.level, len(items)):
        if node.weight + items[i].weight < capacity:
            bound+=items[i].value
    return bound


def bb(node: Node):
    global items, solution_perm, best

    if node.level >= len(items):
        best = node.upper_bound
        return

    node1 = Node(node.value + items[node.level].value, node.weight + items[node.level].weight, node.upper_bound, node.level+1)
    node2 = Node(node.value, node.weight, node.upper_bound, node.level+1)

    if node1.weight > capacity:
        bound1 = 0
    else:
        bound1 = calculate_bound(node1)
    bound2 = calculate_bound(node2)

    print(bound1, bound2)

    if bound1>=bound2:
        solution_perm[node.level] = 1
        node.bound = bound1
        bb(node1)
    else:
        node.bound = bound2
        bb(node2)
    return




n = 4
solution_perm = [0 for taken in range(n)]
items = [Item(random.randint(1,30), random.randint(1,30)) for item in range(n)]
capacity = random.randint(5*n, 10*n)
items.sort(key=lambda item: item.value / item.weight, reverse=True)
best = 0

root = Node(0, 0, 0, 0)
bb(root)


print("items:")
for i in items:
    print(i)


print("capacity: " ,capacity)
print("best: "+ str(best))
print("picked items:")
for i in range(len(items)):
    if solution_perm == 1:
        print(items[i])




