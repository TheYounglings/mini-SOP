import queue
import gridBlock

class pathFinding:
    def __init__(self):
        pass

    def Djikstra(self, start : gridBlock, endId : int):
        Q = queue.PriorityQueue()
        Q.put((0, start, -1))
        D = {}
        while not Q.empty():
            a, b, c = Q.get()
            D[b.id] = c
            if (b.id == endId): break
            for i in b.neigbours:
                Q.put((a+i.travelTime, i, )
        