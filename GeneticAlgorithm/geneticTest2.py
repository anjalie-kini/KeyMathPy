import os, datetime
import GeneticAlgorithm
from random import randint

def getInitialPopulation():
    TARGET_STRING = "Phillips Andover"
    popList = []
    for i in range(100):
        popList.append(GeneticAlgorithm.StringChromosome(randomRepresentation(len(TARGET_STRING)), list(TARGET_STRING)))
    return GeneticAlgorithm.Population(len(popList), 0.2, popList)

# Returns list of ASCII chars
def randomRepresentation(size):
    newRep = []
    for i in range(size):
        newRep.append(chr(randint(32, 126)))
    return newRep

####################################################################################################################
def main():
    print ("####### Current time at start = " + str(datetime.datetime.now())) 
    algo = GeneticAlgorithm.GeneticAlgorithm(GeneticAlgorithm.NPointCrossover(2), 0.9, GeneticAlgorithm.RandomCharMutation(), 0.02, GeneticAlgorithm.TournamentSelection(2))
    initialPop = getInitialPopulation()
    finalPopulation = algo.evolve(initialPop, GeneticAlgorithm.FixedGenerationCount(10000))
    best = finalPopulation.getFittestChromosome()
    print ("####### Current time at end = " + str(datetime.datetime.now())) 

if __name__ == '__main__':
    main()
