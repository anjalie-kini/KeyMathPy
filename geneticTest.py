import os, datetime
import geneticAlgorithm
from random import randint
import copy

class StringChromosome(Chromosome):
	def __init__(self, rep, target):
		this.target = target
        super(rep)

	def fitness(self):
	    f=0 # best fitness
		myRep = getRepresentation()
	    for i in range(len(target)):
			f = f - abs(ord(target[i]) - ord(myRep[i]))
		return f
		
	def checkValidity(self, rep):
	    for c in rep:
		    if (ord(c) < 32 or ord(c) > 126):
			    raise Exception("Invalid char in representation: " + str(c))
	
	def newFixedLengthChromosome(rep)
	    return StringChromosome(rep, target)

		    
class RandomCharMutation(MutationPolicy):
    def __init__(self):
        pass
		
	def mutate(original):
        characters = original.getRepresentation()
		mutationIndex = randint(len(characters))
		mutatedRep = copy.copy(characters)
		# Desired ASCII range has start=27, end=132
		newValue = 32 + randint(127-32)
		mutatedRep.set(mutationIndex, newValue)
		return original.newFixedLengthChromosome(mutatedRep)
		
class OnePointCrossover(CrossoverPolicy):
    def __init__(self):
        pass

	def crossover(self, firstChromo, secondChromo):
        firstLength = firstChromo.getLength();
        if (firstLength != secondChromo.getLength()) {
            raise Exception("Length of first chromosome (" + str(firstLength) + ") does not match length of the second: " + str(secondChromo.getLength()))
        }

        // representations of the parents
        parent1Rep = firstChromo.getRepresentation();
        parent2Rep = secondChromo.getRepresentation();

        // and the children
        child1Rep = [];
        child2Rep = [];

        // select a crossover point at random 
        crossoverIndex = 1 + (randInt(0, length-2));

        // copy the first part
        for i in range(crossoverIndex) {
            child1Rep.add(parent1Rep[i]);
            child2Rep.add(parent2Rep[i]);
        }
        // and switch the second part
        for (i in range(crossoverIndex, firstLength) {
            child1Rep.add(parent2Rep[i]);
            child2Rep.add(parent1Rep[i]);
        }

        return ChromosomePair(firstChromo.newFixedLengthChromosome(child1Rep),
                              secondChromo.newFixedLengthChromosome(child2Rep));
							  
class TournamentSelection(SelectionPolicy):
    def __init__(self, arity):
        self.numberToDraw = arity

    def select(self, population):
        return ChromosomePair(tournament(population), tournament(population))

    def tournament(self, inPopulation):
        if (len(inPopulation) < this.numberToDraw):
            raise Exception("Size of population (" + len(inPopulation) + ") must be at least: " + str(numberToDraw))
        tournamentPopulation = Population(this.numberToDraw)
        myChromosomes = copy.deepcopy(inPopulation)
        for i in range(this.numberToDraw):
            rando = randint(0, len(myChromosomes))
            tournamentPopulation.add(myChromosomes[rando])
            myChromosomes.pop(rando)
        return tournamentPopulation.getFittestChromosome()

    def getArity(self):
        return selfnumberToDraw

    def setArity(self, arity):
        self.numberToDraw = arity
		
class FitnessCondition(StoppingCondition):
    def __init__(self, threshold):
        self.generationNum = 0
		self.fitnessThreshold = threshold

	def isSatisfied(self, population):
	    fittestChr = population.getFittestChromosome()
		if (generationNum == 1 or generationNum % 10 == 0):
		    print('Generation #' + str(generationNum) + ": " + str(fittestChr))
		generationNum = generationNum + 1

		fittestFitness = fittestChr.getFitness()
		if (fittestFitness < fitnessThreshold):
		    return True
		else
			return False

def getInitialPopulation():
    TARGET_STRING = "Phillips Andover"
    popList = []
	for i in range(100):
	    popList.add(StringChromosome(randomRepresentation(len(TARGET_STRING)), TARGET_STRING)
	return popList

def randomRepresentation(size):
	newRep = []
    for i in size:
		newRep.add(32 + randint(127-32))
	return newRep

####################################################################################################################
def main():
    print ("####### Current time = " + str(datetime.datetime.now())) 
	algo = GeneticAlgorithm(OnePointCrossover(), 0.9, RandomCharMutation(), 0.03, TournamentSelection(2))
	initialPop = getInitialPopulation()
	finalPopulation = algo.evolve(initial, FitnessCondition(0.0001))
    best = finalPopulation.getFittestChromosome()

if __name__ == '__main__':
    main()
