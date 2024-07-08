import numpy as np
import heapq

class Astar:
    def find_path_by_astar(self, graph: np.ndarray, start: tuple, end: tuple):
        '''
        graph: a numpy array, 1 means point can move, otherwise 0
        start: start point (y, x)
        end: end point (y, x)
        '''
        
        # Heuristic function: Manhattan distance
        def heuristic(start, end):
            return abs(start[0] - end[0]) + abs(start[1] - end[1])

        # Priority queue
        open_list = []
        heapq.heappush(open_list, (0 + heuristic(start, end), 0, start))  # (f, g, position)

        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start, end)}

        while open_list:
            current = heapq.heappop(open_list)[2]
            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path

            y, x = current
            neighbors = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]
            for neighbor in neighbors:
                ny, nx = neighbor
                if 0 <= ny < graph.shape[0] and 0 <= nx < graph.shape[1] and graph[ny, nx] == 1:
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                        heapq.heappush(open_list, (f_score[neighbor], tentative_g_score, neighbor))

        return None  # No path found

if __name__ == "__main__":
    graph = np.array([[1]*10]*10)
    graph[(4, 9)] = 0
    graph[(5, 9)] = 0
    start = (3, 4)
    end = (7, 9)
    a = Astar()
    path = a.find_path_by_astar(graph, start, end)
    if path:
        print("Path found:")
        print(path)
    else:
        print("No path found.")
