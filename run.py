import random

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value/weight
    def __str__(self):
        return "Weights: " + self.weight + " Vales:" + self.value
class Node:
    def __init__(self, weight, value, level):
        self.weight = weight
        self.value = value
        self.level = level

items = []
n = random.randint(4, 7)  # liczba przedmiotow (number of items)
capacity = random.randint(5 * n, 10 * n)  # pojemnosc (capacity)

for i in range(n):
    items.append(Item(random.randint(1,30), random.randint(1,30)))
items.sort(key=lambda x: x.ratio, reverse=True)


print("knapsack capacity: " + str(capacity))
for item in items:
    print(f"({item.weight}, {item.value})", end=" ")

def brute_force():
    # zmienne globalne reprezentujące kolejno aktualną wartość, aktualną wagę i maksymalną znalezioną do tej pory wartość
    global items, n, capacity

    root = Node(0,0,0)

    solution = []
    best_solution = []
    best_value = 0

    def recursive_tree(node : Node):
        global items, n, capacity
        nonlocal solution, best_solution, best_value
        if node.level == len(items):
            if node.value > best_value:
                best_value = node.value
                best_solution = solution.copy()
            return
        if node.weight + items[node.level].weight <= capacity:
            solution.append(node.level)
            recursive_tree(Node(node.weight + items[node.level].weight,
                                node.value + items[node.level].value,
                                node.level + 1))
            solution.pop()
        else:
            if node.value > best_value:
                best_value = node.value
                best_solution = solution.copy()
        recursive_tree(Node(node.weight, node.value, node.level + 1))
        return

    recursive_tree(root)

    print("\nBrute Force:")
    print("best_value = ", best_value)
    print("prefer_items = ", best_solution)

def mybb():
    # zmienne globalne reprezentujące kolejno aktualną wartość, aktualną wagę i maksymalną znalezioną do tej pory wartość
    global items, n, capacity

    root = Node(0,0,0)

    solution = []
    best_solution = []
    best_value = 0

    def calc_upp_bound(node : Node):
        nonlocal solution
        global items, capacity
        bound = 0
        abstract_weight = node.weight
        for i in range(len(solution)):
            bound += items[i].value
        for i in range(node.level, len(items)):
            if capacity <= abstract_weight + items[i].weight:
                abstract_weight += items[i].weight
                bound += items[i].value
            else:
                bound += ((capacity-abstract_weight) / items[i].weight) * items[i].value
                break
        return bound

    def recursive_tree(node : Node):
        global items, n, capacity
        nonlocal solution, best_solution, best_value
        if node.level == len(items):
            if node.value > best_value:
                best_value = node.value
                best_solution = solution.copy()
            return
        if node.weight + items[node.level].weight <= capacity:
            solution.append(node.level)
            recursive_tree(Node(node.weight + items[node.level].weight,
                                  node.value + items[node.level].value,
                                  node.level + 1))
            solution.pop()
        else:
            if node.value > best_value:
                best_value = node.value
                best_solution = solution.copy()
        if best_value < calc_upp_bound(Node(node.weight, node.value, node.level + 1)):
            recursive_tree(Node(node.weight, node.value, node.level + 1))
        return

    recursive_tree(root)

    print("\nB&B:")
    print("best_value = ", best_value)
    print("prefer_items = ", best_solution)


brute_force()
mybb()

