import sys

import PyQt5
from PyQt5 import QtGui

from components.deapBackend.geneticAlgo import GeneticAlgorithm
from containers.Generate import Generate


def geneticAlgoTest():
    anewApp = PyQt5.QtWidgets.QApplication(sys.argv)
    result = Generate()


if __name__ == "__main__":
    geneticAlgoTest()