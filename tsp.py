import random

from main import EvolutionaryAlgorithm


class TSP(EvolutionaryAlgorithm):

    def __init__(
        self,
        filename,
        selection_scheme,
        population_size,
        max_generations,
    ):
        super().__init__(
            selection_scheme,
            population_size,
            max_generations,
        )
        self.population_size = population_size
        self.max_generations = max_generations
        self.filename = filename
        self.selection_scheme = selection_scheme
        self.name = ""
        self.comment1 = ""
        self.comment2 = ""
        self.type = ""
        self.dimension = 0
        self.edgeWeightType = ""
        self.nodeCoordSelection = ""
        self.node_coords = []
        self.distance_matrix = []
        self.read_file()

    def read_file(self):
        with open(self.filename, "r") as f:
            self.name = f.readline().strip()
            self.comment1 = f.readline().strip()
            self.comment2 = f.readline().strip()
            self.type = f.readline().strip()
            self.dimension = int(f.readline().strip().split()[2])
            self.edgeWeightType = f.readline().strip()
            self.nodeCoordSelection = f.readline().strip()

            line = f.readline().strip()
            while line != "EOF":
                self.node_coords.append(list(map(float, line.split())))
                line = f.readline().strip()

        self.distance_matrix = [
            [0 for _ in range(self.dimension)] for _ in range(self.dimension)
        ]
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.distance_matrix[i][j] = self.euclidean_distance(
                    self.node_coords[i], self.node_coords[j]
                )

    def euclidean_distance(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def chromosome(self) -> list:
        arr = [i for i in range(self.dimension)]
        random.shuffle(arr)
        return arr

    def evaluate_fitness(self, chromosome) -> float:
        fitness = 0
        for i in range(self.dimension - 1):
            fitness += self.distance_matrix[chromosome[i]][chromosome[i + 1]]
        fitness += self.distance_matrix[chromosome[self.dimension - 1]][chromosome[0]]
        return fitness

    def compute_population_fitness(self) -> dict:
        fitness_dictionary = {}
        for individual, chromosome in self.population.items():
            fitness_dictionary[individual] = self.evaluate_fitness(chromosome)
        self.fitness_dictionary = fitness_dictionary
        return fitness_dictionary


filename = "qa194.tsp"
selection_scheme = 1
population_size = 30
max_generations = 50

tsp = TSP(
    filename=filename,
    selection_scheme=selection_scheme,
    population_size=population_size,
    max_generations=max_generations,
)

ch = tsp.chromosome()

print(tsp.initialize_population())
print(tsp.compute_population_fitness())
