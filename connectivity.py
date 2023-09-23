'''
NOME - TIA
Filipe Costa Pereira - 32106521
Guilherme Guimarães Chiarelli - 32036647
Maisa Folgueral - 32121385

This file implements graph connectivity
methods and search algorithm

History
Date: 2023-09-20
Author: Filipe, Guilherme, Maisa
'''

from collections import deque
import math


class Connectivity:

  
  def __init__(self, graph):
    self.n = graph.n
    self.adj = graph.adj


  # Breadth-first search (BFS)
  def bfs(self, n):
    queue = deque()
    visited = [False] * self.n
    visited[n] = True
    queue.append(n)
    while queue:
      n = queue.popleft()
      for m in range(self.n):
        if not visited[m] and self.adj[n][m] != math.inf:
          queue.append(m)
          visited[m] = True
    return visited

  
  def is_disconnected(self):
    visited = self.bfs(0)
    total_visited = visited.count(True)
    if total_visited == self.n:
      return False
    return True