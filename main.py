import numpy as np
import random
from tqdm import tqdm
import matplotlib.pyplot as plt

def ChooseStartNode(start_node_pheromones):
    choices = np.arange(0, len(start_node_pheromones))

    choice = random.choices(choices, start_node_pheromones, k=1)[0]

    return choice

def GeneratePath(distances, pheromones, start_node):

    path = [start_node]

    available_nodes = np.arange(0, len(distances)).tolist()

    current_node = start_node

    while(len(available_nodes) > 1):
        
        available_pheromones = []
        available_nodes.remove(current_node)

        for x in available_nodes:
            available_pheromones.append(pheromones[current_node][x])

        next_node = random.choices(available_nodes, weights=available_pheromones, k=1)[0]

        path.append(next_node)

        current_node = next_node

    return path

def GetFitness(path, distances):
    fitness = 0

    for x in range(len(path) - 1):
        fitness += distances[path[x]][path[x+1]]

    return fitness

def generate_distance_matrix(size):

    b = np.random.randint(0,100,size=(size,size))
    mat = (b + b.T)
    np.fill_diagonal(mat, 0)

    return mat

def main(e, ants, distances):

    start_node_pheromones = np.random.rand(1, len(distances))[0]
    pheromones = np.random.rand(len(distances), len(distances))

    fitness_list = []

    iterations = 1000

    for i in tqdm(range(iterations)):

        total_fitness = 0

        start_node_pheromones_update = np.zeros((1, (len(distances))))[0]
        pheromones_update = np.zeros((len(distances), (len(distances))))
        
        for a in range(ants):

            start_node = ChooseStartNode(start_node_pheromones)

            path = GeneratePath(distances, pheromones, start_node)
            fitness = GetFitness(path, distances)
            total_fitness += fitness
            oneover = 1/fitness

            start_node_pheromones_update[path[0]] += oneover
            for x in range(len(path) - 1):
                pheromones_update[path[x]][path[x+1]] += oneover
        

        pheromones = np.add(pheromones, pheromones_update)
        start_node_pheromones = np.add(start_node_pheromones, start_node_pheromones_update)

        pheromones = pheromones * e
        start_node_pheromones = start_node_pheromones * e

        fitness_list.append(total_fitness/ants)


    print(path)

    return fitness_list

if __name__ == '__main__':

    distances = generate_distance_matrix(10)

    results = []

    evaporation = [0.3, 0.6, 0.9]
    ants = [300, 600, 900]

    for e in evaporation:
        for ant in ants:
            results.append(main(e, ant, distances))

    fig = plt.figure(figsize=(7,5))
    fig.patch.set_facecolor('white')
    fig.suptitle('ACO for TSP (10 cities, 1000 iterations)', fontsize=14)
    
    ax1 = fig.add_subplot(3, 3, 1)
    ax1.plot(np.arange(len(results[0])), results[0])
    ax1.set_xlabel('Iterations')
    ax1.set_ylabel('Fitness')
    ax1.set_title('0.3 evaporation rate, 300 ants')

    ax2 = fig.add_subplot(3, 3, 2)
    ax2.plot(np.arange(len(results[1])), results[1])
    ax2.set_xlabel('Iterations')
    ax2.set_ylabel('Fitness')
    ax2.set_title('0.3 evaporation rate, 600 ants')

    ax3 = fig.add_subplot(3, 3, 3)
    ax3.plot(np.arange(len(results[2])), results[2])
    ax3.set_xlabel('Iterations')
    ax3.set_ylabel('Fitness')
    ax3.set_title('0.3 evaporation rate, 900 ants')

    ax4 = fig.add_subplot(3, 3, 4)
    ax4.plot(np.arange(len(results[3])), results[3])
    ax4.set_xlabel('Iterations')
    ax4.set_ylabel('Fitness')
    ax4.set_title('0.6 evaporation rate, 300 ants')

    ax5 = fig.add_subplot(3, 3, 5)
    ax5.plot(np.arange(len(results[4])), results[4])
    ax5.set_xlabel('Iterations')
    ax5.set_ylabel('Fitness')
    ax5.set_title('0.6 evaporation rate, 600 ants')

    ax6 = fig.add_subplot(3, 3, 6)
    ax6.plot(np.arange(len(results[5])), results[5])
    ax6.set_xlabel('Iterations')
    ax6.set_ylabel('Fitness')
    ax6.set_title('0.6 evaporation rate, 900 ants')
    
    ax7 = fig.add_subplot(3, 3, 7)
    ax7.plot(np.arange(len(results[6])), results[6])
    ax7.set_xlabel('Iterations')
    ax7.set_ylabel('Fitness')
    ax7.set_title('0.9 evaporation rate, 300 ants')

    ax8 = fig.add_subplot(3, 3, 8)
    ax8.plot(np.arange(len(results[7])), results[7])
    ax8.set_xlabel('Iterations')
    ax8.set_ylabel('Fitness')
    ax8.set_title('0.9 evaporation rate, 600 ants')

    ax9 = fig.add_subplot(3, 3, 9)
    ax9.plot(np.arange(len(results[8])), results[8])
    ax9.set_xlabel('Iterations')
    ax9.set_ylabel('Fitness')
    ax9.set_title('0.9 evaporation rate, 900 ants')

    plt.tight_layout()
    plt.show()

