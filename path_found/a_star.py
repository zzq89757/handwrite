import numpy as np
class Astar:
    def find_path_by_astar(self, graph:np.ndarray, start:tuple, end:tuple):
        '''
        graph: a numpy array , 1 means point can move, otherwise 0
        start: start point
        end: end point
        '''
        
        # distance = |x1 - x2| + |y1 -y2|
        distance = lambda start, end:abs(start[0] - end[0]) + abs(start[1] - end[1])
        # calc step have moved and distance
        step_array = graph
        current_pos = start
        move_step = 0
        while (current_pos != end):
            x = current_pos[1]
            y = current_pos[0]
            left_pos = (y, x - 1)
            right_pos = (y, x + 1)
            up_pos = (y - 1, x)
            down_pos = (y + 1, x)
            left_dis = (move_step, 100000) if x == 0 or not graph[left_pos] else (move_step, distance(left_pos, end)) 
            right_dis = (move_step, 100000) if x == len(graph[0]) - 1 or (not graph[right_pos]) else (move_step, distance(right_pos, end))
            up_dis = (move_step, 100000) if y == 0 or not graph[up_pos] else (move_step, distance(up_pos, end))
            down_dis = (move_step, 100000) if y== len(graph) - 1 or not graph[down_pos] else (move_step, distance(down_pos, end))
            # find 
            min_dis = min(left_dis, right_dis, up_dis, down_dis, key=lambda x:x[0] + x[1])
            if min_dis == left_dis:
                current_pos = left_pos
            elif min_dis == right_dis:
                current_pos = right_pos
            elif min_dis == up_dis:
                current_pos = up_pos
            else:
                current_pos = down_pos
            graph[current_pos] = 0
            move_step += 1
            print(current_pos)
        print(graph)
                


if __name__ == "__main__":
    graph = np.array([[1]*10]*10)
    graph[(4, 9)] = 0
    graph[(4, 9)] = 0
    start = (3, 4)
    end = (7, 9)
    a = Astar()
    a.find_path_by_astar(graph, start, end)
        
        
        
