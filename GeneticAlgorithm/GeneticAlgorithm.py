from random import random
from random import randint
from abc import abstractmethod
import copy
import os, datetime
import math


# Implementation of a genetic algorithm. 
class GeneticAlgorithm:
    # Create a new genetic algorithm.
    # crossoverRate: The crossover rate as a percentage (0-1 inclusive)
    # mutationRate: The mutation rate as a percentage (0-1 inclusive)
    def __init__(self, crossoverPolicy, crossoverRate, mutationPolicy, mutationRate, selectionPolicy):
        if (crossoverRate < 0 or crossoverRate > 1):
            raise Exception("Invalid crossoverRate: " + str(crossoverRate))
        if (mutationRate < 0 or mutationRate > 1):
            raise Exception("Invalid mutationRate: " + str(mutationRate))

        self.crossoverPolicy = crossoverPolicy
        self.crossoverRate = crossoverRate
        self.mutationPolicy = mutationPolicy
        self.mutationRate = mutationRate
        self.selectionPolicy = selectionPolicy

    def getCrossoverPolicy(self):
        return self.crossoverPolicy

    def getCrossoverRate(self):
        return self.crossoverRate

    def getMutationPolicy(self):
        return self.mutationPolicy

    def getMutationRate(self):
        return self.mutationRate

    def getSelectionPolicy(self):
        return self.selectionPolicy

    # Evolve the given population. Evolution stops when the stopping condition
    # is satisfied. Updates generationCount with the number of generations evolved 
    # before the StoppingCondition is satisfied
    def evolve(self, initialPopulation, stoppingCondition):
        currentPopulation = initialPopulation
        generationCount = 0
        while (not stoppingCondition.isSatisfied(currentPopulation)):
            currentPopulation = self.nextGeneration(currentPopulation)
            generationCount = generationCount + 1
        return currentPopulation

    # Evolve the given population into the next generation.
    # Get nextGeneration population to fill from currentPopulation, using its nextGeneration method
    # Loop until new generation is filled:
    #  Apply configured SelectionPolicy to select a pair of parents from currentPopulation
    #  With probability = crossoverRate, apply configured CrossoverPolicy to parents
    #  With probability = getMutationRate, apply configured MutationPolicy to each offspring
    #  Add offspring individually to nextGeneration, space permitting
    # Return nextGeneration</li>
    def nextGeneration(self, currentPopulation):
        nextGeneration = currentPopulation.nextGeneration()
        while (nextGeneration.getPopulationSize() < nextGeneration.getPopulationLimit()):
            # select parent chromosomes
            pair = self.getSelectionPolicy().select(currentPopulation)

            # crossover?
            if (random() < self.getCrossoverRate()):
                pair = self.getCrossoverPolicy().crossover(pair.getFirst(), pair.getSecond())

            # mutate?
            if (random() < self.getMutationRate()):
                # apply mutation policy
                pair = ChromosomePair(self.getMutationPolicy().mutate(pair.getFirst()), self.getMutationPolicy().mutate(pair.getSecond()))

            # add the first chromosome to the population
            nextGeneration.addChromosome(pair.getFirst())
            # still room for the second chromosome?
            if (nextGeneration.getPopulationSize() < nextGeneration.getPopulationLimit()):
                # add the second chromosome to the population
                nextGeneration.addChromosome(pair.getSecond())
        return nextGeneration


# A collection of chromosomes/individuals that facilitates generational evolution.
class Population:
    # thresholdRate: The percentage (0-1 inclusive) of the best chromosomes retained in the next generation
    def __init__(self, populationLimit, thresholdRate, chromosomes=None):
        if (populationLimit < 0):
            raise Exception("Invalid populationLimit: " + str(populationLimit))
        if (thresholdRate >= 1):
            raise Exception("Invalid thresholdRate: " + str(thresholdRate))
        if (chromosomes is not None and len(chromosomes) > populationLimit):
            raise Exception("Size of population (" + len(chromosomes) + ") exceeds populationLimit: " + str(populationLimit))
        self.populationLimit = populationLimit
        self.thresholdRate = thresholdRate
        if (chromosomes is not None):
            self.chromosomes = copy.deepcopy(chromosomes)
        else:
            self.chromosomes = []

    def getPopulationLimit(self):
        return self.populationLimit

    def getThresholdRate(self):
        return self.thresholdRate

    def getChromosomes(self):
        return self.chromosomes

    def addChromosome(self, newChromosome):
        if (len(self.chromosomes) >= self.populationLimit):
            raise Exception("Size of population (" + len(self.chromosomes) + ") exceeds populationLimit: " + str(self.populationLimit))
        self.chromosomes.append(newChromosome)

    def getFittestChromosome(self):
        bestSoFar = self.chromosomes[0]
        for nextChromosome in self.chromosomes:
            if (nextChromosome.compareTo(bestSoFar) > 0):
                bestSoFar = nextChromosome
        return bestSoFar

    def setPopulationLimit(self, limit):
        if (limit < 0):
            raise Exception("Invalid populationLimit input: " + str(limit))
        if (len(chromosomes) > limit):
            raise Exception("Size of population (" + len(chromosomes) + ") exceeds input limit: " + str(limit))
        self.populationLimit = limit

    # Select proportion of best chromosomes based on thresholdRate
    def nextGeneration(self):
        # initialize a new generation with the same parameters
        nextGeneration = Population(self.getPopulationLimit(), self.getThresholdRate());
        oldChromosomes = self.getChromosomes();
        oldChromosomes.sort(key = lambda x: x.fitness, reverse=True);

        # find last "not good enough" chromosome
        boundIndex = int(math.ceil((1.0 - self.getThresholdRate()) * len(oldChromosomes)))
        for i in range(boundIndex, len(oldChromosomes)):
            nextGeneration.addChromosome(oldChromosomes[i])
        return nextGeneration;

    def getPopulationSize(self):
        return len(self.chromosomes)



# Immutable, so their fitness is also immutable and can be cached
class Chromosome:
    NO_FITNESS = -1000000

    def __init__(self, rep):
        self.representation = copy.copy(rep)
        self.fitness = Chromosome.NO_FITNESS

    @abstractmethod
    def getFitness(self):
        pass

    def compareTo(self, another):
        if self.fitness > another.getFitness():
            return 1
        elif self.fitness < another.getFitness():
            return -1
        else:
            return 0

    @abstractmethod
    def isSame(self, another):
        pass

    def findSameChromosome(self, population):
        for anotherChr in population:
            if (self.isSame(anotherChr)):
                return anotherChr
        return None

    def searchForFitnessUpdate(self, population):
        sameChr = self.findSameChromosome(population)
        if (sameChr != None):
            self.fitness = sameChr.getFitness()

    def getRepresentation(self):
        return self.representation

    def getLength(self):
        return len(self.getRepresentation())

    def __str__(self):
        return ("F: " + str(self.getFitness()) + ", R: " + str(self.getRepresentation()))

    def __repr__(self):
        return ("Fitness: " + str(self.getFitness()) + ", Representation: " + str(self.getRepresentation()))


class ChromosomePair:
    def __init__(self, chr1, chr2):
        self.first = chr1
        self.second = chr2

    def getFirst(self):
        return self.first

    def getSecond(self):
        return self.second

    def __str__(self):
        return ("C1: " + str(first) + ", C2: " + str(second))

    def __repr__(self):
        return ("Chromosome1: " + str(first) + ", Chromosome2: " + str(second))


class CrossoverPolicy:
    @abstractmethod
    def crossover(self, firstChromosome, secondChromosome):
        pass

class MutationPolicy:
    # Changes a randomly chosen element of the representation 
    @abstractmethod
    def mutate(self, originalChromosome):
        pass

class SelectionPolicy:
    @abstractmethod
    def select(self, population):
        pass

class StoppingCondition:
    @abstractmethod
    def isSatisfied(self, population):
        pass

# Represented by a list of characters
class StringChromosome(Chromosome):
    def __init__(self, rep, target):
        self.target = target
        super().__init__(rep)

    # Computed as "distance" from target string
    def getFitness(self):
        # compute once
        if (self.fitness == Chromosome.NO_FITNESS):
            f=0 # best fitness
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
class RandomCharMutation(MutationPolicy):
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
class OnePointCrossover(CrossoverPolicy):
    def __init__(self):
        pass

    def crossover(self, firstChromo, secondChromo):
        firstLength = firstChromo.getLength()
        if (firstLength != secondChromo.getLength()):
            raise Exception("Length of first chromosome (" + str(firstLength) + ") does not match length of the second: " + str(secondChromo.getLength()))

        # representations of the parents
        parent1Rep = firstChromo.getRepresentation();
        parent2Rep = secondChromo.getRepresentation();
        # and the children
        child1Rep = [];
        child2Rep = [];

        # select a crossover point at random 
        crossoverIndex = 1 + (randint(0, firstLength-2))
        # copy the first part
        for i in range(crossoverIndex):
            child1Rep.append(parent1Rep[i])
            child2Rep.append(parent2Rep[i])
        # and switch the second part
        for i in range(crossoverIndex, firstLength):
            child1Rep.append(parent2Rep[i])
            child2Rep.append(parent1Rep[i])
        return ChromosomePair(firstChromo.newFixedLengthChromosome(child1Rep), secondChromo.newFixedLengthChromosome(child2Rep));

# N-point crossover policy. For each iteration a random crossover point is 
# selected and the first part from each parent is copied to the corresponding 
# child, and the second parts are copied crosswise.
# The chromosomes must have the same length
class NPointCrossover(CrossoverPolicy):
    def __init__(self, crossoverPoints):
        if (crossoverPoints <= 0):
            raise Exception("Number of crossover points must be positive: " + str(crossoverPoints))
        self.crossoverPoints = crossoverPoints

    def getCrossoverPoints(self):
        return self.crossoverPoints
        
    def crossover(self, firstChromo, secondChromo):
        firstLength = firstChromo.getLength()
        if (firstLength != secondChromo.getLength()):
            raise Exception("Length of first chromosome (" + str(firstLength) + ") does not match length of the second: " + str(secondChromo.getLength()))
        if (self.crossoverPoints >= firstLength):
            raise Exception("Length of first chromosome (" + str(firstLength) + ") is smaller than desired number of crossover points: " + str(self.crossoverPoints))

        # representations of the parents
        parent1Rep = firstChromo.getRepresentation();
        parent2Rep = secondChromo.getRepresentation();
        # and the children
        child1Rep = []
        child2Rep = []
        c1 = child1Rep
        c2 = child2Rep

        remainingPoints = self.crossoverPoints
        lastIndex = 0
        for i in range(self.crossoverPoints):
            # select a crossover point at random 
            crossoverIndex = 1 + lastIndex + randint(0, firstLength-lastIndex-remainingPoints)

            # copy the current segment
            for j in range(lastIndex, crossoverIndex):
                c1.append(parent1Rep[j])
                c2.append(parent2Rep[j])
    
            # and swap the children for the next segment
            tmp = c1
            c1 = c2
            c2 = tmp

            lastIndex = crossoverIndex
            remainingPoints = remainingPoints-1
        
        for j in range(lastIndex, firstLength):
            c1.append(parent1Rep[j])
            c2.append(parent2Rep[j])
    
        return ChromosomePair(firstChromo.newFixedLengthChromosome(child1Rep), secondChromo.newFixedLengthChromosome(child2Rep));
        
        
# Tournament selection scheme. Each of the two selected chromosomes is selected
# based on n-ary tournament -- this is done by drawing a predetermined random
# number of chromosomes without replacement from the population, and then 
# selecting the fittest chromosome among them.
class TournamentSelection(SelectionPolicy):
    def __init__(self, arity):
        self.numberToDraw = arity

    def select(self, population):
        return ChromosomePair(self.tournament(population), self.tournament(population))

    def tournament(self, inPopulation):
        if (inPopulation.getPopulationSize() < self.numberToDraw):
            raise Exception("Size of population (" + str(inPopulation.getPopulationSize()) + ") must be at least: " + str(numberToDraw))
        tournamentPopulation = Population(self.numberToDraw, 0.2)
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
class FitnessCondition(StoppingCondition):
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

# Stop after a fixed number of generations
class FixedGenerationCount(StoppingCondition):
    def __init__(self, maxGen):
        self.generationNum = 0
        self.maxGenerations = maxGen

    def isSatisfied(self, population):
        fittestChr = population.getFittestChromosome()
        if (self.generationNum % 10 == 0):
            print('%%% Generation #' + str(self.generationNum) + ": (" + str(datetime.datetime.now()) + ") fittest=" + str(fittestChr))
        self.generationNum = self.generationNum + 1

        if (self.generationNum > self.maxGenerations):
            return True
        else:
            return False