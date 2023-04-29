import random


class Node_Tree:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit    #current profit obtained in a given node
        self.weight = weight    #current backpack weight obtained in a given node
        self.items = []         #list of indexes of items that are placed in the backpack so far



class Priority_Queue:
    def __init__(self):
        self.pqueue = []    #list that holds tree nodes, decreasing estimate(bound)
        self.length = 0

    def insert(self, Node_Tree):
        i = 0
        while i < len(self.pqueue):
            if self.pqueue[i].bound > Node_Tree.bound:
                break
            i += 1
        self.pqueue.insert(i, Node_Tree)
        self.length += 1

    def print_pqueue(self):
        for i in list(range(len(self.pqueue))):
            print("pqueue", i, "=", self.pqueue[i].bound)

    def remove(self):
        try:
            result = self.pqueue.pop()  #smallest estimate
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
values = []  # wartosc (value)
n = 3  # liczba przedmiotow (number of items)
capacity = random.randint(5 * n, 10 * n)  # pojemnosc (capacity)

for i in range(n):
    weights.append(random.randint(1, 30))

for i in range(n):
    values.append(random.randint(1, 30))

p_per_weight = [i / j for i, j in zip(values, weights)]

print("knapsack capacity: " + str(capacity))
print("weights: " + str(weights))
print("values: " + str(values))


nodes_generated = 0
p_queue = Priority_Queue()

root = Node_Tree(-1, 0, 0)  # root initialized to be the root with level = 0, profit = $0, weight = 0
nodes_generated += 1
maxprofit = 0  # maxprofit initialized to $0
root.bound = get_bound(root)
# print("root.bound = ", root.bound)


p_queue.insert(root)

while p_queue.length != 0:

    root = p_queue.remove()  # remove Node_Tree with best bound
    #    print("\nNode removed from p_queue.")
    #    print("Priority Queue: ")
    #    p_queue.print_pqueue()

    #    print("\nmaxprofit = ", maxprofit)
    #    print("Parent Node_Tree: ")
    #    print("root.level = ", root.level, "root.profit = ", root.profit, "root.weight = ", root.weight, "root.bound = ", root.bound, "root.items = ", root.items)

    if root.bound > maxprofit:  # check if Node_Tree is still promising
        # set u to the child that includes the next item
        u = Node_Tree(0, 0, 0)
        nodes_generated += 1
        u.level = root.level + 1
        u.profit = root.profit + values[u.level]
        u.weight = root.weight + weights[u.level]
        # take root's list and add u's list
        u.items = root.items.copy()
        u.items.append(u.level)  # adds next item
        #        print("child that includes the next item: ")
        #        print("Child 1:")
        #        print("u.level = ", u.level, "u.profit = ", u.profit, "u.weight = ", u.weight)
        #        print("u.items = ", u.items)
        if u.weight <= capacity and u.profit > maxprofit:
            # update maxprofit
            maxprofit = u.profit
            #            print("\nmaxprofit updated = ", maxprofit)
            bestitems = u.items
        #            print("bestitems = ", bestitems)
        u.bound = get_bound(u)
        #        print("u.bound = ", u.bound)
        if u.bound > maxprofit:
            p_queue.insert(u)
        #            print("Node_Tree u1 inserted into p_queue.")
        #            print("Priority Queue : ")
        #            p_queue.print_pqueue()
        # set u to the child that does not include the next item
        u2 = Node_Tree(u.level, root.profit, root.weight)
        nodes_generated += 1
        u2.bound = get_bound(u2)
        u2.items = root.items.copy()
        #        print("child that doesn't include the next item: ")
        #        print("Child 2:")
        #        print("u2.level = ", u2.level, "u2.profit = ", u2.profit, "u2.weight = ", u2.weight, "u2.bound = ", u2.bound)
        #        print("u2.items = ", u2.items)
        if u2.bound > maxprofit:
            p_queue.insert(u2)
#            print("Node_Tree u2 inserted into p_queue.")
#            print("Priority Queue : ")
#            p_queue.print_pqueue()





print("best_value = ", maxprofit, "nodes generated = ", nodes_generated)
print("bestitems = ", bestitems)