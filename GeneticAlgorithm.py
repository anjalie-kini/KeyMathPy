from random import random
from abc import abstractmethod
import copy
import os, datetime
import math


class GeneticAlgorithm:
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

    def evolve(self, initialPopulation, stoppingCondition):
        currentPopulation = initialPopulation
        generationCount = 0
        while (not stoppingCondition.isSatisfied(currentPopulation)):
            currentPopulation = self.nextGeneration(currentPopulation)
            generationCount = generationCount + 1
        return currentPopulation


    def nextGeneration(self, currentPopulation):
        nextGeneration = currentPopulation.nextGeneration()
        while (nextGeneration.getPopulationSize() < nextGeneration.getPopulationLimit()):
            # select parent chromosomes
            pair = self.getSelectionPolicy().select(currentPopulation)

            # crossover?
            if (random() < self.getCrossoverRate()):
                pair = self.getCrossoverPolicy().crossover(pair.getFirst(), pair.getSecond())

            # mutation?
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



class Population:
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


