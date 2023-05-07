import random
import time
import matplotlib.pyplot as plt

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
n = 40
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

    # print("\nBrute Force:")
    # print("best_value = ", best_value)
    # print("prefer_items = ", best_solution)

def mybb():
    # zmienne globalne reprezentujące kolejno aktualną wartość, aktualną wagę i maksymalną znalezioną do tej pory wartość
    global items, n, capacity

    root = Node(0,0,0)

    solution = []
    best_solution = []
    best_value = 0

    def calc_low_bound(n_samples: int):
        global items, capacity
        nonlocal best_solution
        max_val = 0
        for i in range(n_samples):
            temp_val = 0
            temp_weight=0
            temp_sol = []
            for i in range(len(items)):
                if random.random() > 0.3:
                    if temp_weight + items[i].weight <= capacity:
                        temp_val += items[i].value
                        temp_weight += items[i].weight
                        temp_sol.append(i)
                        if temp_val > max_val:
                            max_val = temp_val
                            best_solution = temp_sol
        # print("Low bound: ", max_val)
        return max_val


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


    # print("\nB&B:")
    best_value = calc_low_bound(2*n)
    recursive_tree(root)
    #
    # print("best_value = ", best_value)
    # print("prefer_items = ", best_solution)

def beam_search():
    # zmienne globalne reprezentujące kolejno aktualną wartość, aktualną wagę i maksymalną znalezioną do tej pory wartość
    global items, n, capacity

    root = Node(0,0,0)

    solution = []
    best_solution = []
    best_value = 0
    cut_prob = 0.3

    def calc_low_bound(n_samples: int):
        global items, capacity
        nonlocal best_solution
        max_val = 0
        for i in range(n_samples):
            temp_val = 0
            temp_weight=0
            temp_sol = []
            for i in range(len(items)):
                if random.random() > 0.3:
                    if temp_weight + items[i].weight <= capacity:
                        temp_val += items[i].value
                        temp_weight += items[i].weight
                        temp_sol.append(i)
                        if temp_val > max_val:
                            max_val = temp_val
                            best_solution = temp_sol
        # print("Low bound: ", max_val)
        return max_val


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
        if random.random() > cut_prob and best_value < calc_upp_bound(Node(node.weight, node.value, node.level + 1)):
            recursive_tree(Node(node.weight, node.value, node.level + 1))
        return

    # print("\nBeam Search:")
    best_value = calc_low_bound(2 * n)
    recursive_tree(root)

    # print("best_value = ", best_value)
    # print("prefer_items = ", best_solution)


ns = []
bf_times_for_n = []
bb_times_for_n = []
bs_times_for_n = []

for n in range(3, 40):
    print("Obliczanie dla", n, "przedmiotów...")

    ns.append(n)
    bf_times = []
    bs_times = []
    bb_times = []
    for m in range(20):

        items = []
        capacity = random.randint(5 * n, 10 * n)  # pojemnosc (capacity)

        for i in range(n):
            items.append(Item(random.randint(1, 30), random.randint(1, 30)))
        items.sort(key=lambda x: x.ratio, reverse=True)

        if n < 20:
            start_time = time.time()
            brute_force()
            end_time = time.time()
            elapsed_time = end_time - start_time
            bf_times.append(elapsed_time)

        if n < 30:
            start_time = time.time()
            mybb()
            end_time = time.time()
            elapsed_time = end_time - start_time
            bb_times.append(elapsed_time)

        start_time = time.time()
        beam_search()
        end_time = time.time()
        elapsed_time = end_time - start_time
        bs_times.append(elapsed_time)

    if n < 20:
        bf_mean_time = sum(bf_times) / len(bf_times)
        bf_times_for_n.append(bf_mean_time)

    if n < 30:
        bb_mean_time = sum(bb_times) / len(bb_times)
        bb_times_for_n.append(bb_mean_time)

    bs_mean_time = sum(bs_times) / len(bs_times)
    bs_times_for_n.append(bs_mean_time)

plt.plot(ns[:len(bf_times_for_n)], bf_times_for_n, label="bf")
plt.plot(ns[:len(bb_times_for_n)], bb_times_for_n, label="bb")
plt.plot(ns, bs_times_for_n, label="bs")
plt.show()


