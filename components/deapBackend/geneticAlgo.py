import random
import time

from PyQt5 import QtCore
from deap import creator, base, tools

from components import Settings
from components.deapBackend.chromosome import Chromosome


class GeneticAlgorithm(QtCore.QThread):
    statusSignal = QtCore.pyqtSignal(str)
    # Genetic algorithm variable details
    detailsSignal = QtCore.pyqtSignal(list)
    # Running process type
    operationSignal = QtCore.pyqtSignal(int)
    # List of chromosomes for preview
    dataSignal = QtCore.pyqtSignal(list)

    def __init__(self, scenario):
        self.averageFitness = 0
        self.pastAverageFitness = 0
        self.running = True
        self.data = {
            'rooms': [],
            'instructors': [],
            'sections': [],
            'subjects': []
        }
        self.tournamentSize = .04
        self.elitePercent = .05
        self.mutationRate = .10
        self.lowVariety = 55
        self.highestFitness = 0
        self.lowestFitness = 100
        self.scenario = scenario
        self.IND_INIT_SIZE = 100
        self.settings = Settings.getSettings()
        self.stopWhenMaxFitnessAt = self.settings['maximum_fitness']
        self.toolbox = base.Toolbox()
        super().__init__()

    def initialization(self):
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", Chromosome, fitness=creator.FitnessMax)

        self.toolbox.register("attr_item", random.randrange, 20)
        self.toolbox.register("individual", creator.Individual.create, self.scenario)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        self.pop = self.toolbox.population(n=50)
        self.dataSignal.emit([self.pop[0]])
        pass

    def run(self):
        self.statusSignal.emit('Initializing')
        self.initialization()
        generation = 0
        runThread = True
        while (runThread):
            time.sleep(10000)
