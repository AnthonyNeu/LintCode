"""
An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis. 
People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). 
They cannot select which specific animal they would like. 
Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.

Example
int CAT = 0
int DOG = 1

enqueue("james", DOG);
enqueue("tom", DOG);
enqueue("mimi", CAT);
dequeueAny();  // should return "james"
dequeueCat();  // should return "mimi"
dequeueDog();  // should return "tom"
Challenge
Can you do it with single Queue?
"""

# use two queues
from collections import deque
class AnimalShelter(object):
    def __init__(self):
        # do some intialize if necessary
        self.dogs = deque([])
        self.cats = deque([])
        self.order = 0
    """
    @param {string} name
    @param {int} type, 1 if Animal is dog or 0
    @return nothing
    """
    def enqueue(self, name, type):
        # Write yout code here
        if type == 1:
            self.dogs.append((name, self.order))
            self.order += 1
        elif type == 0:
            self.cats.append((name, self.order))
            self.order += 1

    # return a string
    def dequeueAny(self):
        # Write your code here
        if not self.dogs and not self.cats:
            return None
        if not self.dogs:
            cat = self.cats.popleft()
            return cat[0]
        if not self.cats:
            dog = self.dogs.popleft()
            return dog[0]
        dog = self.dogs[0]
        cat = self.cats[0]
        if dog[1] > cat[1]:
            self.cats.popleft()
            return cat[0]
        else:
            self.dogs.popleft()
            return dog[0]

    # return a string
    def dequeueDog(self):
        # Write your code here
        if self.dogs:
            dog = self.dogs.popleft()
            return dog[0]
        else:
            return None

    # return a string
    def dequeueCat(self):
        # Write your code here
        if self.cats:
            cat = self.cats.popleft()
            return cat[0]
        else:
            return None
