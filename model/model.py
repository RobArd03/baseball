import copy

import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = []
        self._idMap = {}
        self._bestPath = []
        self._bestScore = 0

    def buildGraph(self, year: int):
        self._graph.clear()
        self.addAllNodes(year)
        for node in self._nodes:
            self._idMap[node.ID] = node
        DAO.setPesi(year, self._idMap)
        self.addAllEdges(year)

    def getNumAllNodes(self):
        return len(self._nodes)

    def getAllNodes(self, year):
        return DAO.getAllNodes(year)

    def addAllNodes(self, year: int):
        self._nodes = DAO.getAllNodes(year)
        self._graph.add_nodes_from(self._nodes)

    def addAllEdges(self, year: int):

        self._graph.clear_edges()

        for i in range(0, len(self._nodes)-1):
            for j in range(i+1, len(self._nodes)-1):

                n1 = self._nodes[i]
                n2 = self._nodes[j]

                pesoV0 = self._idMap[n1.ID].peso
                pesoV1 = self._idMap[n2.ID].peso

                self._graph.add_edge(n1, n2, weight = pesoV0+pesoV1)

    @staticmethod
    def getYear() -> list:
        list = []
        for i in range(1980, 2020):
            list.append(i)
        list.sort( reverse=True )
        return list

    def adiacenti(self, v0) -> list:
        list =[]
        for n in self._graph.neighbors(v0):
            list.append((n , self._graph[v0][n]['weight']))
        listOrdinata = sorted( list, key=lambda x: x[1], reverse=True )
        return listOrdinata

    def calcolaPercorso(self, v0):
        parziale = []
        parziale.append(v0)
        self.ricorsione(parziale)
        return self._bestPath, self._bestScore

    def ricorsione(self, parziale):
        if len(parziale) > 1:
            if parziale[-1].peso < parziale[-2].peso:
                score = self.getBestScore(parziale)
                if score > self._bestScore:
                    self._bestPath = copy.deepcopy(parziale)
                    self._bestScore = score

        for n in self._graph.neighbors(parziale[-1]):
            if n not in parziale:
                if n.peso < parziale[-1].peso:
                    parziale.append(n)
                    self.ricorsione(parziale)
                    parziale.pop()

    def getBestScore(self, parziale):
        score = 0
        for p in parziale:
            score += p.peso
        return score





