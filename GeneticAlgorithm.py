from random import random
from abc import abstractmethod
import copy
import os, datetime


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
    
    def getCrossoverPolicy(self):
        return self.crossoverPolicy
    
    def getCrossoverRate(self):
        return self.crossoverRate
    
    def evolve(self, initialPopulation, stoppingCondition):
        currentPopulation = initialPopulation
        generationCount = 0
        while (not stoppingCondition.isSatisfied(currentPopulation)):
            currentPopulation = nextGeneration(currentPopulation)
            generationCount = generationCount + 1
        return currentPopulation
    
    
    def nextGeneration(self, currentPopulation):
        nextGeneration = currentPopulation.nextGeneration()
        while (nextGeneration.getPopulationSize() < nextGeneration.getPopulationLimit()):
            # select parent chromosomes
            pair = self.getSelectionPolicy().select(currentPopulation)
            
            # crossover?
            if (random() < getCrossoverRate()):
                pair = self.getCrossoverPolicy().crossover(pair.getFirst(), pair.getSecond())
            
            # mutation?
            if (random() < getMutationRate()):
                # apply mutation policy
                pair = self.getMutationPolicy().mutate(pair.getFirst())
                pair = self.getMutationPolicy().mutate(pair.getSecond())
            
            # add the first chromosome to the population
            nextGeneration.addChromosome(pair.getFirst())
            # still placefor the second chromosome?
            if (nextGeneration.getPopulationSize() < nextGeneration.getPopulationLimit()):
                # add the second chromosome to the population
                nextGeneration.addChromosome(pair.getSecond())
        
    return nextGeneration



class Population:
    def __init__(self, populationLimit, chromosomes):
        if (populationLimit < 0):
            raise Exception("Invalid populationLimit: " + str(populationLimit))
        if (populationLimit < 0):
            raise Exception("Invalid populationLimit: " + str(populationLimit))
        if (len(chromosomes) > populationLimit):
            raise Exception("Size of population (" + len(chromosomes) + ") exceeds populationLimit: " + str(populationLimit))
        
        self.populationLimit = populationLimit
        self.chromosomes = copy.deepcopy(chromosomes)
    
    def getPopulationLimit(self):
        return self.populationLimit
    
    def getChromosomes(self):
        return self.chromosomes
    
    def addChromosome(self, newChromosome):
        if (len(chromosomes) >= populationLimit):
            raise Exception("Size of population (" + len(chromosomes) + ") exceeds populationLimit: " + str(populationLimit))
        self.chromosomes.add(newChromosome)
    
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
    
    def getPopulationSize(self):
        return len(chromosomes)



# Immutable, so their fitness is also immutable and can be cached
class Chromosome:
    NO_FITNESS = -1000000
        
        def __init__(self, rep):
        self.representation = copy.copy(rep)
    
    # Changes a randomly chosen element of the representation
    #  to a random value distributed in [0,1]
    def getFitness(self):
        if (self.fitness == NO_FITNESS)
            self.fitness = fitness()
        return self.fitness
        
        def compareTo(self, another):
            if self.fitness > another.getFitness():
                return 1
                elif self.fitness < another.getFitness():
                    return -1
                else
                    return 0
            
            # should be true if identical representation,
            def isSame(self, another):
                        return False
                    
                    def findSameChromosome(self, population):
                        for anotherChr in population:
                    if (self.isSame(anotherChr):
                        return anotherChr
                        
                        return None
                        
                        def searchForFitnessUpdate(self, population):
                        sameChr = self.findSameChromosome(population)
                        if (sameChr != None):
                        self.fitness = sameChr.getFitness()
                        
                        def getRepresentation(self):
                        return self.representation
                        
                        def getLength(self):
                        return getRepresentation().size()
                        
                        def __str__(self):
                        return ("F: " + str(self.getFitness()) +
                                ", R: " + str(self.getRepresentation()))
                        
                        def __repr__(self):
                        return ("Fitness: " + str(self.getFitness()) +
                                ", Representation: " + str(self.getRepresentation()))
                        
                        
                        class ChromosomePair:
                        def __init__(self, chr1, chr2):
                        self.first = chr1
                        self.second = chr2
                        
                        def getFirst(self):
                        return self.first
                        
                        def getSecond(self):
                        return self.second
                        
                        def __str__(self):
                        return ("C1: " + str(first) +
                                ", C2: " + str(second))
                        
                        def __repr__(self):
                        return ("Chromosome1: " + str(first) +
                                ", Chromosome2: " + str(second))
                        
                        
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
                        
                        
