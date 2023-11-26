import math


class Colouring:


  def __init__(self, graph):
    self.graph = graph
    self.sorted_vertices = self.get_sorted_vertices()
    self.sorted_matrix = self.get_sorted_matrix()

  
  def get_neighbors(self, v):
    neighbors = []
    for w in range(self.graph.n):
      if self.sorted_matrix[v][w] != math.inf:
        neighbors.append(w)
    return neighbors


  def get_sorted_vertices(self):
    vertices = []

    for i in range(self.graph.n):
      vertex = {
        'index': i,
        'degree': self.graph.get_vertex_degree(i)
      }
      vertices.append(vertex)

    sorted_vertices = sorted(vertices, key=lambda x: x['degree'], reverse=True)

    return sorted_vertices

  
  def get_sorted_matrix(self):
    sorted_matrix = [[math.inf for _ in range(self.graph.n)] for _ in range(self.graph.n)]

    for i in range(self.graph.n):
      old_i = self.sorted_vertices[i]['index']
      for j in range(self.graph.n):
        old_j = self.sorted_vertices[j]['index']
        if self.graph.adj[old_i][old_j] != math.inf:
          sorted_matrix[i][j] = self.graph.adj[old_i][old_j]
          sorted_matrix[j][i] = self.graph.adj[old_i][old_j]

    return sorted_matrix


  def find_class_colouring(self):
    C = [[] for i in range(self.graph.n)] # vetor de classes de cores Ci

    W = [i for i in range(self.graph.n)] # W = V (W variável auxiliar)

    k = 0 # indicador da classe atual de cor

    # Enquanto nem todos os vértices foram inseridos nas classes corretas
    while(W):

      # Para os vértices que ainda não foram encontradas classes de cores
      W_aux = W.copy()
      for i in W:

        # Interseccao
        n_i = set(self.get_neighbors(i))
        c_k = set(C[k])
        intersec = list(n_i.intersection(c_k))

        # Se nenhum vizinho de vi fizer parte da classe atual k 
        if len(intersec) == 0:
          C[k].append(i) # O vértice vi pode ser ‘pintado’ com a mesma cor da classe k
          W_aux.remove(i) # Retira esse vértice vi de W (W eh atualizado na copia para nao ocasionar problemas no loop)

      W = W_aux

      k += 1 # segue para a próxima classe de cores k

    return C


  def show_classes(self):
    classes = self.find_class_colouring()
    for i in range(len(classes)):
      if classes[i]:
        print("Classe ", i+1)
        for country in classes[i]:
          country_name = self.graph.vect[country].name
          print(f"\t {country_name}")
      