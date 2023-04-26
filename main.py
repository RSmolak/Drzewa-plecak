import random
class Node:
    def __init__(self, c_value, w_value):
        self.c_value = c_value
        self.w_value = w_value
        self.index = 0

    def __str__(self):
        return (f"{self.index}) val: {self.c_value} weight: {self.w_value}")


n = 14  # ilosc przedmiotow
capacity = random.randint(5 * n, 10 * n)  # pojemnosc plecaka
c_value_list = []  # Wektor wartości
w_value_list = []  # Wektor wag

solutions = []
left = []
best_sol = []
value = 0
weight = 0
optim_found = False

max_value = 0

# Generujemy listę przedmiotów i dodajemy je do wektora left
for i in range(n):
    left.append(Node(random.randint(1, 30), random.randint(1, 30)))
    left[-1].index = i
    print(left[-1])
    # print(f"{i}) Waga: {left[-1].w_value} wartość: {left[-1].c_value}")  # Wypisanie przedmiotów


def recursive_tree():
    # zmienne globalne reprezentujące kolejno aktualną wartość, aktualną wagę i maksymalną znalezioną do tej pory wartość
    global value, weight, max_value, optim_found, best_sol

    for i in range(len(left)):
        # Jeśli znajdziemy optymalne rozwiązanie wychodzimy z rekurencji
        if optim_found:
            return

        solutions.append(left[i])
        left.remove(left[i])

        value += solutions[-1].c_value
        weight += solutions[-1].w_value

        # Jeżeli żaden przedmiot już się nie zmieści
        if weight > capacity and i == len(left) - 1:
            left.append(solutions.pop())
            value -= left[-1].c_value
            weight -= left[-1].w_value
            return
        # Jeżeli nie ma już przedmiotów
        elif len(left) == 0:
            max_value = value
            best_sol = solutions.copy()
            optim_found = True
            return
        # Jeżeli wybrany przedmiot się nie mieści
        elif weight > capacity:
            left.append(solutions.pop())
            value -= left[-1].c_value
            weight -= left[-1].w_value
            continue  # To szukamy czy następny z left się zmieści

        recursive_tree()
        if value > max_value:
            max_value = value
            best_sol = solutions.copy()
        left.append(solutions.pop())
        value -= left[-1].c_value
        weight -= left[-1].w_value


recursive_tree()
print(f"pojemność: {capacity}\nmax_value: {max_value}\nRozwiazanie:")
for i in range(len(best_sol)):
    print(best_sol[i])