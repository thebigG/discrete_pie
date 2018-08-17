import math
import itertools
import random
import fractions
"""
This module is a collection of a few functions, data structres and classes that were inspired by concepts I learned
in Discrete Mathematics II(CS-206). The goal with this little module is to make some of these concepts practical and fun!
Because they are! Hope you like it!
"""



rand_machine  = random.Random()

class subject:
     pass 



class pie:
    """
    pie is a data structure that represents a pie. This pie is slices size big.
    Input slices in the following form: [(label_1, weight), (label_2, weight), (label_n, weight)]
    For example the following discrete_pie.pie([("A", 4), ("B", 4), ("C", 7)])
    Will create the a pie instance which, under the hood, looks like this:
    ('A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C')
    Which is essentially the labels repeated weight times inside of a tuple
    Having data in this format, hopefully, allows you to experiment when picking a slice of the pie.
    Think of this as the partitioning rule in the flesh!
    """
    def __init__(self, slices):

        pie = []
        self.meta_pie = {}
        for (label,weight) in slices:
            self.meta_pie.update({label: weight})
            for i in [label] * weight:
                pie.append(i)
        self.pie = tuple(pie)
    def get_weight(self,label):
        """
        Get the weight of the piece with name label
        """
        return self.meta_pie[label]
    def get_slices(self):
        return self.meta_pie
    def pick_slice(self):
        """
        Pick a slice of the pie at random
        """
        return self.pie[rand_machine.randint(0, len(self.pie) - 1)]





class dice:
    """
    This class represents a dice. By default, this dice has 6 sides.
    However, this can be set to however many number of sides you'd like.
    The hope with this class is that it feels like a data structure, rather than just a random number generator.
    This is why this dice has state. The current dice can be seen as a tupple of length sides.
    For example in the case of a 6-sided dice, the dice field will yield a tuple like this:(1,2,3,4,5,6)
    At the beginning, when no rolls have been made, the state will be "Idle".
    When roll() has been called at least once, then state will be the last number that was shown on the dice.
    If roll_n_times() was called last, the state will be a n-sized tuple where every element is the result from each rolll.
    Play with it! Hope you like it!
    """
    def __init__(self ,sides = 6):
        self.sides = sides
        self.dice  = []
        for i in range(1, sides+1, 1):
            self.dice.append(i)
        self.dice = tuple(self.dice)
        self.state = "Idle"
    def roll(self):
        self.state =  self.dice[rand_machine.randint(0, self.sides-1)]
        return self.state
    def roll_n_times(self, n):
        self.state  = tuple(self.dice[rand_machine.randint(0, self.sides-1)]  for i in range(1,n+1, 1))
        return self.state

    def get_state():
        return self.state



class coin:
    """
    Very similar to dice--a coin with state.
    However, unlike dice, coin ALWAYS has two sides.
    Sadly, python does not have private fields...so I had to use name mangling.
    The field __coin holds the coin data, but please, DO NOT touch this variable.
    If you wish to build on top of this and make it better and you HAVE to modify __coin, then that's  fine.
    But as a user of this module, do not touch __coin. Modifying it could break this whole thing.
    """
    __coin = ("H", "T")
    def __init__(self):
        self.state = "Idle"
        return
    def toss(self):
        self.state  = self.__coin[rand_machine.randint(0,1)]
        return self.state
    def toss_n_times(self, n):
        self.state = tuple([self.__coin[rand_machine.randint(0,1)] for i in range(1, n+1, 1)])
        return self.state










def product(iter):
    """
    Just like the built-in function sum, only that this multiplies the iteratable!
    """
    product = 1
    for num in iter:
        product *= num
    return product

def get_factorials(n):
    """
    Gets a list of all the factorials from 1 to n!
    n = 3 will return [1, 2, 6]
    n = 4 will return [1, 2, 6, 24]
    n  = 5 will return [1, 2, 6, 24, 120]
    and so on...
    """
    return[math.factorial(i) for i in range(1, n+1, 1)]


def permute_n(n):
    """
    returns a list with all permutations from 1 through n
    for instance permute_n(3) would return the following list:
        [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    """
    return [i for i in itertools.permutations(range(1,n+1,1))]

def n_choose_k_slices(n, k = None, result = False):
    """
    This function returns a list of all of the parts(partition rule) that make up n_choose_k from 0 to k
    in the format of a tuple: (n, i, result )
    for instance:
        n_choose_k_slices(3, 2)
        will return the list [(3, 0, 1), (3, 1, 3), (3, 2, 3)]
        if k is not given(k == None):
            it is assumed that k ==  n
            which will return ALL of the partitions which would be [(3, 0, 1), (3, 1, 3), (3, 2, 3), (3, 3, 1)]
    """
    slices = []
    if k == None:
        for i in range(n+1):
            if result == False:
                slices.append((n,i,n_choose_k(n, i)))
            else:
                slices.append(n_choose_k(n, i))
    else:
        for i in range(k+1):
            if result == False:
                slices.append((n,i,n_choose_k(n, i)))
            else:
                slices.append(n_choose_k(n, i))
    return slices



def n_choose_k(n, k):
    return int((math.factorial(n)/(( math.factorial(k)) * (math.factorial(n-k) ))))


def find_factor(n):
     """
     this function gives you all of the factors of n in a list
     """
     factor_values = []
     for i in range(1, n +1):
         if n % i == 0:
             factor_values.append(i)
     return factor_values

def get_fraction(decimal):
    return (Fraction(decimal).limit_denominator())



def is_before_greater(list, i):
    pivot = list[i]
    is_greater = True
    for item in range(i):
        if list[item] < pivot:
            is_greater = False
            break
    return is_greater

def is_before_less(list, i):
    pivot = list[i]
    is_less = True
    for item in range(i):
        if list[item] > pivot:
            is_less = False
            break
    return is_less



def is_zig_zag(nums):
    zig_zag  =True
    for num in range(1,len(nums)):
        if not(is_before_less(nums, num) or is_before_greater(nums, num)):
            zig_zag = False
            break
    return zig_zag



def zig_zag_count(num):
    """
    This function generates permutatons from 1 to num(inclusive) and counts how many of those permuutations are zigzags.
    """
    nums = range(1, num +1)
    nums_permutations = itertools.permutations(nums, len(nums))
    count  = 0
    times_called  = 0
    for permutation in nums_permutations:
        if is_zig_zag(permutation):
            count += 1
    # print("times called:", times_called)
    return count

def zig_zag_permutations(num):
    """
    This function generates permutatons from 1 to num(inclusive) and returns the permutations which are zigzags.
    For instance the call zig_zag_permutations(3)
    yields [(1, 2, 3), (2, 1, 3), (2, 3, 1), (3, 2, 1)]
    """
    nums = range(1, num +1)
    nums_permutations = itertools.permutations(nums, len(nums))
    zig_zags  = []
    for permutation in nums_permutations:
        if is_zig_zag(permutation):
            zig_zags.append(permutation)
    return zig_zags





def generate_path(point):
    index = point[0]
    # print("index:", index)
    p = point[1][index[0]]
    q = point[1][index[1]]
    r = point[1][index[2]]
    path  =[]
    while p > 0 or q> 0 or r > 0:
        # print("current step:", (p,q,r))
        path.append((p,q,r))
        if p>0:
            p -= 1
            continue
        elif q>0:
            q -= 1
            continue
        elif r>0:
            r -= 1
            continue
    # paths.append((0,0,0))

    return (path, len(path))



def go_back_to_origin(p, q, r):
    paths = []
    path_count  =  0
    choice_combinations  = itertools.permutations((0,1,2), 3)
    for set in choice_combinations:
        # print("current set:", set)
        paths.append(generate_path([set, [p,q,r]])[0])
    return (paths, path_count)
