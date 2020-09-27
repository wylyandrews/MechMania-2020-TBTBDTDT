
class Graph():
    def __init__(self, board):
        self.barriers = []
        self.set_barriers(board)
    def get_barriers(self):
        return self.barriers
    def set_barriers(self, board):
        for x in range(board.width):
            for y in range(board.height):
                tile = board.grid[x][y]
                if tile.type == "VOID" or tile.type == "IMPASSIBLE":
                    self.barriers.append(tile)


    def heuristic(self, start, goal):
        return start.manhatten_distance(goal)

    def move_cost(self, a, b):
        for barrier in self.barriers:
            if b in barrier:
                return 100 #Extremely high cost to enter barrier squares
        return 1 #Normal movement cost

    def get_vertex_neighbours(self, pos, board):
        n = []
        #Moves allow link a chess king
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            x2 = pos.x + dx
            y2 = pos.y + dy
            if x2 < 0 or x2 >= board.width or y2 < 0 or y2 >= board.height:
                continue
            n.append((x2, y2))
        return n

    def AStarSearch(self, start, end, board):
    
        G = {} #Actual movement cost to each position from the start position
        F = {} #Estimated movement cost of start to end going via this position
    
        #Initialize starting values
        G[start] = 0 
        F[start] = heuristic(start, end)
    
        closedVertices = set()
        openVertices = set([start])
        cameFrom = {}
    
        while len(openVertices) > 0:
            #Get the vertex in the open list with the lowest F score
            current = None
            currentFscore = None
            for pos in openVertices:
                if current is None or F[pos] < currentFscore:
                    currentFscore = F[pos]
                    current = pos
    
            #Check if we have reached the goal
            if current == end:
                #Retrace our route backward
                path = [current]
                while current in cameFrom:
                    current = cameFrom[current]
                    path.append(current)
                path.reverse()
                return path, F[end] #Done!
    
            #Mark the current vertex as closed
            openVertices.remove(current)
            closedVertices.add(current)
    
            #Update scores for vertices near the current position
            for neighbour in get_vertex_neighbours(current, board):
                if neighbour in closedVertices: 
                    continue #We have already processed this node exhaustively
                candidateG = G[current] + move_cost(current, neighbour)
    
                if neighbour not in openVertices:
                    openVertices.add(neighbour) #Discovered a new vertex
                elif candidateG >= G[neighbour]:
                    continue #This G score is worse than previously found
    
                #Adopt this G score
                cameFrom[neighbour] = current
                G[neighbour] = candidateG
                H = heuristic(neighbour, end)
                F[neighbour] = G[neighbour] + H
 
	    raise RuntimeError("A* failed to find a solution")