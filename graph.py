'''
NOME - TIA
Filipe Costa Pereira - 32106521
Guilherme Guimarães Chiarelli - 32036647
Maisa Folgueral - 32121385

This file implements graph class.
It is important to take note that
this is an undirected and weighted graph.

Date: 2023-09-20, 2023-09-21, 2023-09-22
Author: Filipe, Guilherme, Maisa
Description: Implementation the first part project

Date: 2023-11-10
Author: Filipe, Maisa, Guilherme
Description: Added information on the vertex, implementation the vertex degree, find paths between countries
'''

from connectivity import Connectivity
from vertex import Vertex
from colouring import Colouring
import math


class Graph:

  
  def __init__(self):
    self.n = 0 # Number of vertices
    self.m = 0 # Number of edges
    self.adj = []
    self.vect = []

  
  def get_vertex_name(self, v):
    return self.vect[v].name

    
  def count_vertex_edges(self, v):
    edges = 0
    for i in range(self.n):
      if self.adj[v][i] != math.inf:
        edges += 1
    return edges

  
  def insert_vertex(self, name, iso_code, population, area, population_density, coastline, gdp):
    self.vect.append(Vertex(name, iso_code, population, area, population_density, coastline, gdp)) # add vertex data
    self.adj.append([math.inf for i in range(self.n+1)]) # add row
    for i in range(self.n):
      self.adj[i].append(math.inf) # add col
    self.n += 1

  
  def remove_vertex(self, v):
    edges = self.count_vertex_edges(v)
    self.vect.pop(v) # remove vertex data
    self.adj.pop(v) # remove row
    for row in self.adj:
      row.pop(v) # remove col
    self.m -= edges
    self.n -= 1

  
  def insert_edge(self, v, w, label):
    if self.adj[v][w] == math.inf and self.adj[w][v] == math.inf:
      self.adj[v][w] = label
      self.adj[w][v] = label
      self.m += 1

  
  def remove_edge(self, v, w):
    if self.adj[v][w] != math.inf and self.adj[w][v] != math.inf:
      self.adj[v][w] = math.inf
      self.adj[w][v] = math.inf
      self.m -= 1

  
  def show_min(self):
    print(f"n: {self.n}", end=" ")
    print(f"m: {self.m} \n")
    for v in range(self.n):
      for w in range(self.n):
        print(f" {self.adj[v][w]} ", end="")
      print("\n")
    print("End of graph.")


  def get_connectivity_type(self):
    if Connectivity(self).is_disconnected():
      return 1
    return 0


  def makeGraphFromFile(self, filename):
    f = open(filename, 'r')
    f.readline() # skip graph type
    
    # extract vertex data
    n = int(f.readline().strip()) # number of vertices
    for i in range(n):
      data = f.readline().strip()
      pos = data.find(' ') # find pos of first space
      country_info = data[pos+1:].split(';')
      self.insert_vertex(
        name = country_info[0],
        iso_code = country_info[1],
        population = country_info[2],
        area = country_info[3],
        population_density = country_info[4],
        coastline = country_info[5],
        gdp = country_info[6]
      )
      
    # extract edge data
    m = int(f.readline().strip()) # number of edges
    for i in range(m):
      data = f.readline().strip()
      src, des, wgt = data.split(' ')
      self.insert_edge(int(src), int(des), float(wgt))
    f.close()


  def makeFileFromGraph(self, filename):
    file = open(filename, 'w')
    lines = []
    lines.append(str(2)) # graph type
    lines.append(str(self.n)) # number of vertices
  
    # all vertices data
    for i in range(self.n):
      line = str(i) + ' '
      line += self.vect[i].name + '-'
      line += self.vect[i].iso_code
      lines.append(line)
      
    lines.append(str(self.m)) # number of edges
  
     # all edges data
    start = 0
    for i in range(self.n):
      for j in range(start, self.n):
        if self.adj[i][j] != math.inf:
          line = str(i) + ' ' 
          line += str(j) + ' ' 
          line += str(self.adj[i][j])
          lines.append(line)
      start += 1

    # add breaklines
    total_lines = len(lines)
    for i in range(total_lines):
      if i == total_lines-1:
        # nao adiciona na ultima linha
        break
      lines[i] += '\n'
    file.writelines(lines)
    file.close()

  
  def get_vertex_degree(self, v):
    res = 0
    for w in range(self.n):
      if self.adj[v][w] != math.inf:
        res += 1
    return res


  def find_routes(self, source, destiny):
    routes = []
    visited = set()
    self.dfs(source, destiny, visited, [source], routes)
    return routes

  
  def find_best_route(self, source, destiny):
    routes = self.find_routes(source, destiny)
    min_length = min(map(len, routes))
    min_arrays = [arr for arr in routes if len(arr) == min_length]
    return min_arrays


  def dfs(self, current, destiny, visited, current_path, routes):
    if current == destiny:
        routes.append(list(current_path))
        return

    visited.add(current)

    for neighbor in range(self.n):
      if self.adj[current][neighbor] != math.inf and neighbor not in visited:
        current_path.append(neighbor)
        self.dfs(neighbor, destiny, visited, current_path, routes)
        current_path.pop()
  
    visited.remove(current)


  def show_class_colouring(self):
    c = Colouring(self)
    c.show_classes()