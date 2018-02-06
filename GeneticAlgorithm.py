def fitnessFunction():
    ## User inputs their own fitness function
    ## Outputs score by which to compare members of the population
    ## If not a score, then at the very least there needs to be a compare fucntion and then individual members can be
    ## compared to find the fittest (but this seems very inefficient)

def mutation():
    ## Randomly mutates a member of the population with probability ___%
    ## Also add chance of random mutation during crossover?
    ## Mutation would mean switching out a trait? Needs to be inputted by user as it would depend on their individuals

def crossover():
    ## Crosses over traits of two members of population to make child member
    ## "The speciation heuristic penalizes crossover between candidate solutions that are too similar;
    ## this encourages population diversity and helps prevent premature convergence to a less optimal solution."
    ## Needs to be inputted by individual becauase depends on their individual

def initializePopulation():
    ## Should (randomly?) initialize individuals based on user input
    ## Might need to seed solutions in areas where optimal solution is likely to be found?

def selection():
    ## Selects top __% of population to be carried into next generation
    ## Based on fitness function
    ## Depending on size of the population, might need to only check random portion of population
    ## Should bring over small percent of less fit members for genetic diversity

def newGeneration():
    ##Implements selection, crossover, and mutation to generate new population

def averageFitness():
    ## Calculates average fitness of entire population

def checkTerminate():
    ## Determines whether or not new population should be generated
    ## There are a few criteria often used to determine whether termination is necessary:
    ## (a) Average fitness has reached a certain benchmark
    ## (b) Number of generations is specified by User
    ## (c) Highest ranking member's fitness has reached a plateau
    ## (d) Computation time is reached
    ## Or some combination of the above methods
