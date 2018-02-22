import os, datetime
import GeneticAlgorithm
from random import randint
import copy

# Represented by a list of characters
class StringChromosome(GeneticAlgorithm.Chromosome):
    def __init__(self, rep, target):
        self.target = target
        super().__init__(rep)

	# Computed as "distance" from target string
    def getFitness(self):
        # Compute once
        if (self.fitness == GeneticAlgorithm.Chromosome.NO_FITNESS):
            f=0 # Best fitness
            myRep = self.getRepresentation()
            listTgt = list(self.target)
            for i in range(len(listTgt)):
                # print('listTgt[i]=' + str(listTgt[i]) + ", myRep[i]=" + str(myRep[i]))
                f = f - abs(ord(listTgt[i]) - ord(myRep[i]))
            self.fitness = f
        return self.fitness

	# All chars must be in ASCII range
    def checkValidity(self, inRep):
        for c in inRep:
            if (ord(c) < 32 or ord(c) > 126):
                raise Exception("Invalid char in representation: " + str(c))

    def isSame(self, another):
        rep1 = self.getRepresentation()
        rep2 = another.getRepresentation()
        if (cmp(rep1, rep2) == 0):
            return True
        else:
            return False

    def newFixedLengthChromosome(self, rep):
        return StringChromosome(rep, self.target)

# Mutation of a random char in the array
class RandomCharMutation(GeneticAlgorithm.MutationPolicy):
    def __init__(self):
        pass

    def mutate(self, original):
        characters = original.getRepresentation()
        mutationIndex = randint(0, len(characters)-1)
        mutatedRep = copy.copy(characters)
        # Desired ASCII range
        newValue = randint(32, 126)
        mutatedRep[mutationIndex] = chr(newValue)
        return original.newFixedLengthChromosome(mutatedRep)

# One point crossover policy. A random crossover point is selected and the
# first part from each parent is copied to the corresponding child, and the
# second parts are copied crosswise.
# The chromosomes must have the same length
class OnePointCrossover(GeneticAlgorithm.CrossoverPolicy):
    def __init__(self):
        pass

    def crossover(self, firstChromo, secondChromo):
        firstLength = firstChromo.getLength()
        if (firstLength != secondChromo.getLength()):
            raise Exception("Length of first chromosome (" + str(firstLength) + ") does not match length of the second: " + str(secondChromo.getLength()))

        # Representations of the parents
        parent1Rep = firstChromo.getRepresentation();
        parent2Rep = secondChromo.getRepresentation();

        # and the children
        child1Rep = [];
        child2Rep = [];

        # Select a crossover point at random
        crossoverIndex = 1 + (randint(0, firstLength-2))

        # Copy the first part
        for i in range(crossoverIndex):
            child1Rep.append(parent1Rep[i])
            child2Rep.append(parent2Rep[i])

        # and switch the second part
        for i in range(crossoverIndex, firstLength):
            child1Rep.append(parent2Rep[i])
            child2Rep.append(parent1Rep[i])

        return GeneticAlgorithm.ChromosomePair(firstChromo.newFixedLengthChromosome(child1Rep), secondChromo.newFixedLengthChromosome(child2Rep));

# Tournament selection scheme. Each of the two selected chromosomes is selected
# based on n-ary tournament -- this is done by drawing a predetermined random
# number of chromosomes without replacement from the population, and then
# selecting the fittest chromosome among them.
class TournamentSelection(GeneticAlgorithm.SelectionPolicy):
    def __init__(self, arity):
        self.numberToDraw = arity

    def select(self, population):
        return GeneticAlgorithm.ChromosomePair(self.tournament(population), self.tournament(population))

    def tournament(self, inPopulation):
        if (inPopulation.getPopulationSize() < self.numberToDraw):
            raise Exception("Size of population (" + str(inPopulation.getPopulationSize()) + ") must be at least: " + str(numberToDraw))
        tournamentPopulation = GeneticAlgorithm.Population(self.numberToDraw, 0.2)
        myChromosomes = copy.deepcopy(inPopulation.getChromosomes())
        for i in range(self.numberToDraw):
            rando = randint(0, len(myChromosomes)-1)
            tournamentPopulation.addChromosome(myChromosomes[rando])
            myChromosomes.pop(rando)
        retVal = tournamentPopulation.getFittestChromosome()
        # print("tournament winner: " + str(retVal))
        return retVal

    def getArity(self):
        return self.numberToDraw

    def setArity(self, arity):
        self.numberToDraw = arity

# Stop when the fittest chromosome in the population reaches a threshold
class FitnessCondition(GeneticAlgorithm.StoppingCondition):
    def __init__(self, threshold):
        self.generationNum = 0
        self.fitnessThreshold = threshold

    def isSatisfied(self, population):
        fittestChr = population.getFittestChromosome()
        if (self.generationNum % 10 == 0):
            print('%%% Generation #' + str(self.generationNum) + ": (" + str(datetime.datetime.now()) + ") fittest=" + str(fittestChr))
        self.generationNum = self.generationNum + 1

        fittestFitness = fittestChr.getFitness()
        if (fittestFitness > self.fitnessThreshold):
            return True
        else:
            return False

def getInitialPopulation():
    TARGET_STRING = "Phillips Andover"
    popList = []
    for i in range(100):
        popList.append(StringChromosome(randomRepresentation(len(TARGET_STRING)), list(TARGET_STRING)))
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
    algo = GeneticAlgorithm.GeneticAlgorithm(OnePointCrossover(), 0.9, RandomCharMutation(), 0.03, TournamentSelection(2))
    initialPop = getInitialPopulation()
    finalPopulation = algo.evolve(initialPop, FitnessCondition(-3))
    best = finalPopulation.getFittestChromosome()
    print ("####### Current time at end = " + str(datetime.datetime.now()))

if __name__ == '__main__':
    main()
