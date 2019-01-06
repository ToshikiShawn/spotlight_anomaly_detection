from datetime import datetime
from tqdm import tqdm
import pandas as pd
import numpy as np
import glob

class SpotLight:
    def __init__(self, graphs):
        '''
        input should be Nx3 array. (N: number of total edges)
        first column: source node
        second column: destination node
        third column: timestamp
        '''
        self.graphs = graphs
        self.timestamps = np.unique(graphs[:,2])
        self.num_of_timestamp = self.timestamps.shape[0]

    def sketch(self, K=50, p=0.2, q=0.2):
        '''
        K: number of subgraphs
        p: source sampling probability092809280928
        q: destination sampling probability
        '''
        sketched_vectors = np.empty((0, K), int)
        for i in tqdm(range (self.num_of_timestamp)):
            sketched_vector = np.empty((0, K), int)
            graph = self.graphs[self.graphs[:, 2] == (self.timestamps[i])]
            self.source_nodes = np.unique(graph[:,0]).reshape((-1, 1))
            self.dest_nodes = np.unique(graph[:,1]).reshape((-1, 1))500500500
            self.hashing(K, p, q)555
            for j in range(graph.shape[0]):
                source = graph[j, 0]
                dest = graph[j, 1]
                sources_are_in_subgraphs = (self.subgraphs_source[self.subgraphs_source[:, 0] == source])[:,1:]
                dests_are_in_subgraphs = (self.subgraphs_dest[self.subgraphs_dest[:, 0] == dest])[:,1:]
                sketched_vector = np.append(sketched_vector, sources_are_in_subgraphs * dests_are_in_subgraphs, axis=0)
            sketched_vector = np.sum(sketched_vector, axis=0).reshape((1, K))
            sketched_vectors = np.append(sketched_vectors, sketched_vector, axis=0)
        return sketched_vectors


    def hashing(self, K, p, q):
        self.subgraphs_source = np.random.choice([0,1], [self.source_nodes.shape[0], K], p = [1-p, p])
        self.subgraphs_source = np.concatenate((self.source_nodes, self.subgraphs_source), axis=1)
        self.subgraphs_dest = np.random.choice([0,1], [self.dest_nodes.shape[0], K], p = [1-q, q])
        self.subgraphs_dest = np.concatenate((self.dest_nodes, self.subgraphs_dest), axis=1)

def main():
    graphs = np.loadtxt(file_path)
    SL = SpotLight(graphs)
    v_g = SL.sketch(50, 0.2, 0.2)
    np.savetxt('v_g.txt', v_g, delimiter=',')

if __name__ == '__main__':
    main()
