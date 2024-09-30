import queue
import gridBlock

# returns direction of next block on optimal route
# -1 on goal, 1 <-, 2 ^, 3 ->, 4 v
def djikstra(x : int, y : int, board : list[list[gridBlock.GridBlock]]):
    q = queue.PriorityQueue()
    M = [[-1 for i in range(len(board[0]))] for j in range(len(board))]
    q.put((0, x, y, -1))
    while not q.empty():
        a, b, c, d = q.get()

        if M[c][b] != -1:
            continue
        M[c][b] = a

        if board[c][b].is_goal():
            return d

        if b != 0:
            qd = d
            if d == -1: qd = 1
            if board[c][b-1].travelTime != -1:
                qa = a + board[c][b-1].travelTime
                q.put((qa, b-1, c, qd))
        if c != 0:
            qd = d
            if d == -1: qd = 2
            if board[c-1][b].travelTime != -1:
                qa = a + board[c-1][b].travelTime
                q.put((qa, b, c-1, qd))
        if b != len(board[c]) - 1:
            qd = d
            if d == -1: qd = 3
            if board[c][b+1].travelTime != -1:
                qa = a + board[c][b+1].travelTime
                q.put((qa, b+1, c, qd))
        if c != len(board) - 1:
            qd = d
            if d == -1: qd = 4
            if board[c+1][b].travelTime != -1:
                qa = a + board[c+1][b].travelTime
                q.put((qa, b, c+1, qd))
    return -2

def heuristic(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)

def Astar(x : int, y : int, gx : int, gy : int, board : list[list[gridBlock.GridBlock]]):
    q = queue.PriorityQueue()
    M = [[False for i in range(len(board[0]))] for j in range(len(board))]
    Cost = [[-1 for i in range(len(board[0]))] for j in range(len(board))]
    q.put((0, x, y, -1))
    while not q.empty():
        a, b, c, d = q.get()

        if b == gx and c == gy:
            return d

        if M[c][b]: continue
        M[c][b] = True

        a = Cost[c][b]

        if b != 0:
            qd = d
            if d == -1: qd = 1
            if board[c][b-1].travelTime != -1:
                qa = a + heuristic(b-1, c, gx, gy) + 1
                q.put((qa, b-1, c, qd))
                Cost[c][b-1] = a + 1

        if b != len(board[c]) - 1:
            qd = d
            if d == -1: qd = 3
            if board[c][b+1].travelTime != -1:
                qa = a + heuristic(b+1, c, gx, gy) + 1
                q.put((qa, b+1, c, qd))
                Cost[c][b+1] = a + 1

        if c != 0:
            qd = d
            if d == -1: qd = 2
            if board[c-1][b].travelTime != -1:
                qa = a + heuristic(b, c-1, gx, gy) + 1
                q.put((qa, b, c-1, qd))
                Cost[c-1][b] = a + 1

        if c != len(board) - 1:
            qd = d
            if d == -1: qd = 4
            if board[c+1][b].travelTime != -1:
                qa = a + heuristic(b, c+1, gx, gy) + 1
                q.put((qa, b, c+1, qd))
                Cost[c+1][b] = a + 1

    return -2

