#!/usr/bin/env python3
import random
import numpy as np

# Parameters
NUM_ANTENNAS = 10  # Number of antennas
FREQUENCY_RANGE = (1000, 2000)  # Frequency range in MHz
POPULATION_SIZE = 100  # Population size
MUTATION_RATE = 0.1  # Probability of mutation
CROSSOVER_RATE = 0.7  # Probability of crossover
NUM_GENERATIONS = 1000  # Number of generations

# Fitness function: Minimize interference and optimize frequencies
def fitness(chromosome):
    """
    Fitness function to evaluate how well the antenna frequencies are optimized.
    The goal is to minimize the frequency overlap (interference).
    """
    interference = 0
    for i in range(NUM_ANTENNAS):
        for j in range(i + 1, NUM_ANTENNAS):
            if abs(chromosome[i] - chromosome[j]) < 50:  # Arbitrary interference threshold
                interference += 1
    return 1 / (1 + interference)  # Inverse of interference, higher is better

# Create initial population
def create_population():
    population = []
    for _ in range(POPULATION_SIZE):
        chromosome = [random.randint(FREQUENCY_RANGE[0], FREQUENCY_RANGE[1]) for _ in range(NUM_ANTENNAS)]
        population.append(chromosome)
    return population

# Selection: Tournament selection
def tournament_selection(population):
    tournament_size = 5
    selected_parents = []
    for _ in range(2):  # Select two parents
        tournament = random.sample(population, tournament_size)
        tournament.sort(key=lambda x: fitness(x), reverse=True)  # Sort by fitness
        selected_parents.append(tournament[0])
    return selected_parents

# Crossover: One-point crossover
def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1[:], parent2[:]  # No crossover, return copies of parents

    crossover_point = random.randint(1, NUM_ANTENNAS - 1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

# Mutation: Random mutation
def mutate(chromosome):
    if random.random() > MUTATION_RATE:
        return chromosome  # No mutation

    mutation_point = random.randint(0, NUM_ANTENNAS - 1)
    mutation_value = random.randint(FREQUENCY_RANGE[0], FREQUENCY_RANGE[1])
    chromosome[mutation_point] = mutation_value
    return chromosome

# Main Genetic Algorithm
def genetic_algorithm():
    population = create_population()

    for generation in range(NUM_GENERATIONS):
        new_population = []
        
        # Evaluate the population's fitness
        population.sort(key=lambda x: fitness(x), reverse=True)

        # Elitism: Carry over the best individual to the next generation
        new_population.append(population[0])

        # Selection, Crossover, and Mutation
        while len(new_population) < POPULATION_SIZE:
            parents = tournament_selection(population)
            offspring1, offspring2 = crossover(parents[0], parents[1])
            new_population.append(mutate(offspring1))
            if len(new_population) < POPULATION_SIZE:
                new_population.append(mutate(offspring2))
        
        population = new_population

        # Print the best solution every 100 generations
        if generation % 100 == 0:
            print(f"Generation {generation}: Best Fitness = {fitness(population[0])}")
            print(f"Best Solution: {population[0]}")

    return population[0]

# Run the genetic algorithm
if __name__ == "__main__":
    best_solution = genetic_algorithm()
    print(f"\nBest Solution: {best_solution}")
    print(f"Fitness of Best Solution: {fitness(best_solution)}")
