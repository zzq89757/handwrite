import numpy as np
class Astar:
    def find_path_by_astar(self, graph:np.ndarray, start, end):
        '''
        graph: a numpy array , 1 means point can move, otherwise 0
        start: start point
        end: end point
        '''
        
        # 