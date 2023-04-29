import random

class Node_Tree:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.items = []

class Priority_Queue:
    def __init__(self, k):
        self.pqueue = []
        self.length = 0
        self.k = k

    def insert(self, Node_Tree):
        i = 0
        while i < len(self.pqueue):
            if self.pqueue[i].bound > Node_Tree.bound:
                break
            i += 1
        self.pqueue.insert(i, Node_Tree)
        if self.length < self.k:
            self.length += 1
        else:
            self.pqueue.pop(0)

    def remove(self):
        try:
            result = self.pqueue.pop()
            self.length -= 1
        except:
            print("Priority queue is empty, cannot pop from empty list.")
        else:
            return result

def get_bound(Node_Tree):
    if Node_Tree.weight >= capacity:
        return 0
    else:
        result = Node_Tree.profit
        j = Node_Tree.level + 1
        totweight = Node_Tree.weight
        while j <= n - 1 and totweight + weights[j] <= capacity:
            totweight = totweight + weights[j]
            result = result + values[j]
            j += 1
        k = j
        if k <= n - 1:
            result = result + (capacity - totweight) * p_per_weight[k]
        return result

p_per_weight = []
weights = []
values = []
n = 5
capacity = random.randint(5 * n, 10 * n)

for i in range(n):
    weights.append(random.randint(1, 30))

for i in range(n):
    values.append(random.randint(1, 30))

p_per_weight = [i / j for i, j in zip(values, weights)]

print("knapsack capacity: " + str(capacity))
print("weights: " + str(weights))
print("values: " + str(values))

nodes_generated = 0
k = 10
p_queue = Priority_Queue(k)
root = Node_Tree(-1, 0, 0)
nodes_generated += 1
maxprofit = 0
root.bound = get_bound(root)

p_queue.insert(root)
  # Ustal wartość parametru k dla metody Beam Search
temp_nodes = []

while p_queue.length != 0:

    root = p_queue.remove()

    if root.bound > maxprofit:
        u = Node_Tree(0, 0, 0)
        nodes_generated += 1
        u.level = root.level + 1
        u.profit = root.profit + values[u.level]
        u.weight = root.weight + weights[u.level]
        u.items = root.items.copy()
        u.items.append(u.level)
        u.bound = get_bound(u)

        if u.weight <= capacity and u.profit > maxprofit:
            maxprofit = u.profit
            bestitems = u.items

        if u.bound > maxprofit:
            temp_nodes.append(u)

        u2 = Node_Tree(u.level, root.profit, root.weight)
        nodes_generated += 1
        u2.bound = get_bound(u2)
        u2.items = root.items.copy()
        if u2.bound > maxprofit:
            temp_nodes.append(u2)

    temp_nodes.sort(key=lambda x: x.bound, reverse=True)
    for node in temp_nodes[:k]:
        p_queue.insert(node)
    temp_nodes.clear()

print("best_value =", maxprofit, "nodes generated =", nodes_generated)
print("bestitems =", bestitems)