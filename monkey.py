'''
Hill Climbing (Genetic Algorithm):
Hill Climbing is the most simple implementation of a Genetic Algorithm.
It completely gets rid of the concepts like population and crossover,
instead focusing on the ease of implementation. It has faster iterations
compared to more traditional genetic algorithms, but in return it is less thorough.

How does it work?
Hill Climbing works in a very simple way. We can actually show it in a step-by-step list.
1. Start with an empty or random solution. This is called our best solution
2. Make a copy of the solution and mutate it slightly
3. Evaluate the new solution. If it's better than the best solution, we replace the best solution with this one
4. Go to step two and repeat
So basically to evolve a solution to a problem, you need to write three functions.
1. Create a random solution
2. Evaluate a solution and return a score
3. Mutate a solution in a random way
'''

#Infinite Monkey problem 

import random
import string

#This function returns a random solution with 29 chars length
def generate_random_solution(length=29):
    return [random.choice(string.printable) for _ in range(length)]

#The target of the algorithm is producing the string "me thinks it is like a weasel"
#so we need to create a evaluation function that is going to return a distance metric
#between two strings
#The function below will return the absolute difference of our solution to the target

def evaluate(solution):
    target = list("me thinks it is like a weasel")
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        diff += abs(ord(s) - ord(t))
    return diff

#In genetic algorithms, mutating a solution means randomly changing it in a small way
#In this context, it means changing one of the letters randomly

def mutate_solution(solution):
    index = random.randint(0, len(solution) - 1)
    solution[index] = random.choice(string.printable)
    
#Basic outline aka skeleton

best = generate_random_solution()
best_score = evaluate(best)

while True:
    print("Best score so far", best_score, "Solution", "".join(best))
    if best_score == 0:
        break
    new_solution = list(best)
    mutate_solution(new_solution)
    score = evaluate(new_solution)
    if evaluate(new_solution) < best_score:
        best = new_solution
        best_score = score
    
