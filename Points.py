import random
import math 
import matplotlib.pyplot as plt
import numpy as np
from numpy import inf
import time

class Point: 
  
    # default constructor 
    def __init__(self, tuples, name): 
        self.tuples = tuples
        self.name = name

    def printPoint(self):
        print(self.name, "= (",self.tuples[0], ", " ,self.tuples[1],")")

class Candidate:

    def __init__(self, arr):
        self.arr = arr 
        self.intersection = 0
        self.perimeter = 0

    def setIntersection(self, intersection):
        self.intersection = intersection

    def setPerimeter(self, perimeter):
        self.perimeter = perimeter

    def addPoint(self, point):
        self.arr.append(point)



def inArray(l, p):

    for point in l:
        if point.tuples[0] == p.tuples[0] and point.tuples[1] == p.tuples[1]:
            return True
    return False
    

def setPoints(n,m1,m2):    
    
    l = []
    for i in range(n):
        new_point = (random.randrange(m1, m2), random.randrange(m1, m2))
        name = "p" + str(i + 1)
        p = Point(new_point, name)

        while inArray(l, p):
            
            new_point = (random.randrange(m1, m2), random.randrange(m1, m2))
            name = "p" + str(i + 1)
            p = Point(new_point, name)

        l.append(p)

    return l

def printArrayPoints(l):
    for i in range(len(l)):
        l[i].printPoint()
    print("\n")

def calculateDistance(p1,p2):
    return (math.sqrt(((p1.tuples[0] - p2.tuples[0]) ** 2) + (p1.tuples[1] - p2.tuples[1]) ** 2)) ** 2

def orientation(p, q, r):
      
    val = ((q.tuples[1] - p.tuples[1]) * (r.tuples[0] - q.tuples[0])) - ((q.tuples[0] - p.tuples[0]) * (r.tuples[1] - q.tuples[1]))
    if val == 0 : return 0
    return 1 if val > 0 else -1
  
def segmentIntersects(p1,p2,p3,p4):


    d1 = orientation(p1, p2, p3)
    d2 = orientation(p1, p2, p4)
    d3 = orientation(p3, p4, p1)
    d4 = orientation(p3, p4, p2)
    
    if ((d1 != d2) and (d3 != d4)): return True
    elif (d1 == 0) and inBox(p1,p2,p3): return True
    elif (d2 == 0) and inBox(p1,p2,p4): return True
    elif (d3 == 0) and inBox(p3,p4,p1): return True
    elif (d4 == 0) and inBox(p3,p4,p2): return True
    else: return False

def inBox(p, q, r):

    if r.tuples[0] <= max(p.tuples[0], q.tuples[0]) and r.tuples[0] >= min(p.tuples[0], q.tuples[0]) and r.tuples[1] <= max(p.tuples[1], q.tuples[1]) and r.tuples[1] >= min(p.tuples[1], q.tuples[1]):
        return True
    return False


def random_candidate(candidate):

    aux = candidate.arr[:]
    random.shuffle(aux)

    cand = Candidate(aux)
    cand.addPoint(cand.arr[0])
    return cand

def nearestNeighbourFirst(candidate):
    
    l = Candidate([])
    distanceArray = 0
    l.arr.append(candidate.arr[0])
    nearest = ()

    for i in range(len(candidate.arr)-1):    
        for p2 in candidate.arr:
            if not inArray(l.arr, p2):
                d1 = calculateDistance(l.arr[i], p2)
                if distanceArray  == 0:
                    distanceArray = d1
                    nearest = p2

                elif d1 < distanceArray:
                    distanceArray  = d1
                    nearest = p2
        if nearest:
            l.arr.append(nearest)
        distanceArray = 0
        nearest = ()

    return l

def areDiferent(p1,p2,p3,p4):
    return (p1.tuples[0] == p3.tuples[0] and p1.tuples[1] == p3.tuples[1]) or (p1.tuples[0] == p4.tuples[0] and p1.tuples[1] == p4.tuples[1]) or (p2.tuples[0] == p3.tuples[0] and p2.tuples[1] == p3.tuples[1] ) or (p2.tuples[0] == p4.tuples[0] and p2.tuples[1] == p4.tuples[1])


def getPerimeter(candidate):
    p = 0
    i = 0
    while i < len(candidate.arr)-1:

        p += (calculateDistance(candidate.arr[i], candidate.arr[i+1])) ** 2
        i += 1

    return p

def findSegmentsIntersects(points):

    c = []
    count = 0

    tmp = points.arr[:]

    cand = Candidate(tmp)

    for i in range(len(points.arr) - 1):
        for j in range(len(points.arr) - 3 - i):
            if not areDiferent(points.arr[i], points.arr[i+1], points.arr[j+i+2], points.arr[j+i+3]):
                aux = segmentIntersects(points.arr[i], points.arr[i+1], points.arr[j+i+2], points.arr[j+i+3])
                if aux: 

                    tmp2 = cand.arr[j+i+2]
                    tmp3 = cand.arr[i+1]
                    cand.arr[i+1] = tmp2
                    cand.arr[j+i+2] = tmp3

                    diff = (j+i+2) - (i+1)
                    
                    if diff > 2:
                        iti = 0
                        itj = 0
                        stop = (diff-1)/2
                        while iti < stop:
                            tmp2 = cand.arr[i+2+iti]
                            tmp3 = cand.arr[i+j+1+itj]
                            cand.arr[i+j+1+itj] = tmp2
                            cand.arr[i+2+iti] = tmp3
                            iti += 1
                            itj -= 1

                    count += 1
                    cand.setPerimeter(getPerimeter(cand))  
                    cand.setIntersection(totalSegmentsIntersect(cand))


                    c.append(cand)
                    

                    tmp = points.arr[:]
                    cand = Candidate(tmp)

    points.intersection = count

    return c
    



def totalSegmentsIntersect(points):

    count = 0

    for i in range(len(points.arr) -1):
        for j in range(len(points.arr) - 3 - i):
            if not areDiferent(points.arr[i], points.arr[i+1], points.arr[j+i+2], points.arr[j+i+3]):
                aux = segmentIntersects(points.arr[i], points.arr[i+1], points.arr[j+i+2], points.arr[j+i+3])
                if aux: 

                    count += 1
                    
    return count


def bestImprovementFirst(candidate):

    global bests 

    arr = findSegmentsIntersects(candidate)
    if len(arr) == 0: return candidate

    perimeter = arr[0].perimeter
    aux = arr[0]
    for candidate in arr:

        if candidate.perimeter < perimeter: 
            perimeter = candidate.perimeter
            aux = candidate


    if aux.perimeter > candidate.perimeter:
        return candidate

    bests += 1
    return bestImprovementFirst(aux)


def firstImprovement(candidate):
    
    global firsts
    
    arr = findSegmentsIntersects(candidate)
    if len(arr) == 0: return candidate

    firsts += 1
    return firstImprovement(arr[0])


def lessImprovementFirst(candidate):

    global lesss

    arr = findSegmentsIntersects(candidate)
    if len(arr) == 0: return candidate

    inter = arr[0].intersection
    aux = arr[0]
    for candidate in arr:

        if candidate.intersection < inter: 
            intersection = candidate.intersection
            aux = candidate

    if aux.intersection > candidate.intersection:
        return candidate

    lesss += 1
    return lessImprovementFirst(aux)


def randomImprovement(candidate):

    global randoms
    
    arr = findSegmentsIntersects(candidate)
    if len(arr) == 0: return candidate

    randoms += 1 
    return randomImprovement(random.choice(arr))



def simulatedAnnealing(initial_state, alpha, initial_temp, final_temp):
    
    global sa

    #initial_temp = 100
    #final_temp = 1
    #alpha = 1
    
    current_temp = initial_temp


    current_state = initial_state
    solution = current_state

    while current_temp > final_temp:

        arrayNeighbours = findSegmentsIntersects(current_state)
        if len(arrayNeighbours) < 1:
                return solution

        neighbor = random.choice(arrayNeighbours)


        cost_cs = totalSegmentsIntersect(current_state)
        cost_neighbor = totalSegmentsIntersect(neighbor)
        cost_diff = cost_cs - cost_neighbor


        if cost_diff > 0:
            solution = neighbor
            current_state = neighbor
            
        else:
            if random.uniform(0, 1) < math.exp(-cost_diff / current_temp):
                solution = neighbor
                current_state = neighbor
                
        sa += 1
        
        current_temp -= alpha

        print("Current Temp: " , current_temp)
        print("Current cost: " , cost_neighbor)
        print("Previous cost: " , cost_cs)
        print("Alpha: ", alpha)
        print("")

    return solution


def plotCandidate(candidate):

    x_coordinates = []
    y_coordinates = []

    for point in candidate.arr:
        x_coordinates.append(point.tuples[0])
        y_coordinates.append(point.tuples[1])


    plt.scatter(x_coordinates, y_coordinates)
    plt.plot(x_coordinates, y_coordinates)

    i = 0

    while i < len(x_coordinates):
        plt.annotate(candidate.arr[i].name, (x_coordinates[i], y_coordinates[i]))
        i += 1
    plt.show()

if __name__ == "__main__":

    bests = 0
    randoms = 0
    lesss = 0
    firsts = 0
    sa = 0


    print("Quantos pontos queres gerar?")
    n = int(input())

    print("Indique o valor do m:")
    m1 = int(input())

    points = setPoints(n,-m1,m1) 

    cand = Candidate(points)
    t = Candidate([])
    t.arr = cand.arr[:]
    t2 = Candidate([])


    #t2.addPoint(t2.arr[0])

    printArrayPoints(t2.arr)
    
    menu = {}
    menu['1']="Usar Permutação Qualquer dos Pontos"
    menu['2']="Usar Nearest Neighbour First"
    menu['3']="Exit"

    menu2 = {}
    menu2['1']="Ver Plot"
    menu2['2']="Testar Best Improvement First"
    menu2['3']="Testar First Improvement"
    menu2['4']="Testar Less Improvement"
    menu2['5']="Testar Random Improvement"
    menu2['6']="Testar Simulated Annealing"
    menu2['7']="Testar ACO"
    menu2['8']="Voltar ao menu anterior"

    while True: 
        options = menu.keys()
        options2 = menu2.keys()
        
        
        for entry in options: 
            print (entry, menu[entry])

        selection = input("Please Select:") 

        if selection == '1':

            t2 = random_candidate(t)
            printArrayPoints(t2.arr)
            plotCandidate(t2)

        elif selection == '2': 

            start = time.time()
            t2 = nearestNeighbourFirst(t)
            end = time.time()
            print("")
            print("Time elapsed: " , end - start)
            print("")
            t2.addPoint(t2.arr[0])
            printArrayPoints(t2.arr)
            plotCandidate(t2)

        elif selection == '3':
            break
        
        else: 
            print("Unknown Option Selected!")

        while True: 
            for entry2 in options2: 
                print (entry2, menu2[entry2])

            selection2 = input("Please Select:") 
            
            if selection2 =='1': 

                plotCandidate(t2)

            elif selection2 == '2':
                start = time.time()
                per = bestImprovementFirst(t2)
                end = time.time()
                print("")
                print("Time elapsed: " , end - start)
                print("Iterations: " ,bests)
                print("")
                bests = 0
                #printArrayPoints(per.arr)
                plotCandidate(per)
            elif selection2 == '3':
                start = time.time()
                first = firstImprovement(t2)
                end = time.time()
                print("")
                print("Time elapsed: " , end - start)
                print("Iterations: " ,firsts)
                print("")
                firsts = 0
                #printArrayPoints(first.arr)
                plotCandidate(first)
            elif selection2 == '4':
                start = time.time()
                less = lessImprovementFirst(t2)
                end = time.time()
                print("")
                print("Time elapsed: " , end - start)
                print("Iterations: " ,lesss)
                print("")
                lesss = 0
                #printArrayPoints(less.arr)
                plotCandidate(less)
            elif selection2 == '5':
                start = time.time()
                rand = randomImprovement(t2)
                end = time.time()
                print("")
                print("Time elapsed: " , end - start)
                print("Iterations: " ,randoms)
                print("")
                randoms = 0
                #printArrayPoints(rand.arr)
                plotCandidate(rand)
            elif selection2 == '6':

                print("Indique o alpha")
                alpha = float(input())
                print("Indique a temperatura inicial:")
                initial_temp = float(input())
                print("Indique a temperatura final:")
                final_temp = float(input())
                start = time.time()
                sim_annealing = simulatedAnnealing(t2, alpha, initial_temp, final_temp)
                end = time.time()
                print("")
                print("Time elapsed: " , end - start)
                print("Iterations: " ,sa)
                print("")
                sa = 0
                #printArrayPoints(sim_annealing.arr)
                plotCandidate(sim_annealing)


            elif selection2 == '8':
                break
            else: 
                print("Unknown Option Selected!")



    

    
    