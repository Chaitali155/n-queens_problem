import random
import time

def fitness(chromosome, n):
    """Calculate the fitness of a chromosome.
    The fitness is the number of non-attacking pairs of queens."""
    non_attacking_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Check if queens are not attacking each other
            if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != abs(i - j):
                non_attacking_pairs += 1
    return non_attacking_pairs

def select_parents(population, fitnesses):
    """Select two parents using a weighted probability based on fitness."""
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    parent1 = random.choices(population, probabilities)[0]
    parent2 = random.choices(population, probabilities)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    """Perform a single-point crossover."""
    point = random.randint(1, len(parent1) - 2)  # Avoid trivial cases
    child = parent1[:point] + parent2[point:]
    return child

def mutate(chromosome, mutation_rate, n):
    """Mutate a chromosome with a given mutation rate."""
    if random.random() < mutation_rate:
        idx = random.randint(0, n - 1)
        chromosome[idx] = random.randint(0, n - 1)
    return chromosome

def genetic_algorithm(n, population_size=100, generations=1000, mutation_rate=0.1):
    """Solve the N-Queens problem using a genetic algorithm."""
    # Initialize the population randomly
    population = [[random.randint(0, n - 1) for _ in range(n)] for _ in range(population_size)]
    start_time = time.time()

    for generation in range(generations):
        # Calculate fitness for each individual
        fitnesses = [fitness(individual, n) for individual in population]
        max_fitness = max(fitnesses)

        # Check if we have found the solution
        if max_fitness == (n * (n - 1)) // 2:  # All pairs are non-attacking
            solution_idx = fitnesses.index(max_fitness)
            end_time = time.time()
            return population[solution_idx], generation, end_time - start_time

        # Select parents and generate new population
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population, fitnesses)
            child1 = mutate(crossover(parent1, parent2), mutation_rate, n)
            child2 = mutate(crossover(parent1, parent2), mutation_rate, n)
            new_population.extend([child1, child2])

        population = new_population

    # If no solution is found, return the best guess
    best_idx = fitnesses.index(max(fitnesses))
    end_time = time.time()
    return population[best_idx], generations, end_time - start_time

# Test the Genetic Algorithm for N-Queens
if __name__ == "__main__":
    n = 100  # You can test with 10, 50, or 100
    solution, generations, exec_time = genetic_algorithm(n)

    print(f"Genetic Algorithm for N={n}")
    print(f"Solution found in {generations} generations and {exec_time:.2f} seconds.")
    # print("Solution:", solution)
