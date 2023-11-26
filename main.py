'''
NOME - TIA
Filipe Costa Pereira - 32106521
Guilherme Guimarães Chiarelli - 32036647
Maisa Folgueral - 32121385

This is the main file where everything
of the project run.

History
Date: 2023-09-20, 2023-09-21, 2023-09-22
Author: Filipe, Guilherme, Maisa
Description: Implementation the first part project

Date: 2023-11-03
Author: Filipe, Maisa
Description: Added more information about the countries on txt 

Date: 2023-11-10
Author: Filipe, Maisa, Guilherme
Description: Added information on the vertex, implementation the vertex degree, find paths between countries
'''

from graph import Graph
from tabulate import tabulate


def showFileContent(filename):
  f = open(filename, 'r')

  print('\n\n')
  print('Tipo do Grafo: ', f.readline())

  print('\n\n')
  print('Vertices: ')
  head = ["Indice", "Pais", "Codigo ISO"]
  content = []
  n = int(f.readline())
  for i in range(n):
    data = f.readline().strip()
    pos = data.find(' ') # find pos of first space
    name, iso = data[pos+1:].split('-')
    content.append([i, name, iso])
  print(tabulate(content, headers=head, tablefmt="grid", numalign="left", stralign="left"))

  print('\n\n')
  print('Arestas: ')
  head = ["Origem", "Destino", "Peso (km)"]
  content = []
  m = int(f.readline())
  for i in range(m):
    data = f.readline().strip()
    src, des, wgt = data.split(' ')
    content.append([src, des, wgt])
  print(tabulate(content, headers=head, tablefmt="grid",  numalign="left", stralign="left"))
  f.close()


def insert_vertex_aux(g):
  while(True):
    name = input("Digite o nome do pais: ")
    if name == '':
      print('Nome invalido!')
      continue
    iso_code = input("Digite a sigla do pais (ISO): ").upper()
    if iso_code == '':
      print('Sigla invalida!')
      continue
    g.insert_vertex(name, iso_code)
    break


def insert_edge_aux(g):
  while(True):
    source = int(input("Digite o indice de origem: "))
    if source == '':
      print('Origem invalida!')
      continue
    destiny = int(input("Digite o indice de destino: "))
    if destiny == '':
      print('Destino invalido!')
      continue
    weight = float(input("Digite o peso da aresta: "))
    if weight == '':
      print('Peso invalido!')
      continue
    g.insert_edge(source, destiny, weight)
    break


def remove_vertex_aux(g):
  while(True):
    index = int(input("Digite o indice: "))
    if index == '':
      print('Indice invalido!')
      continue
    g.remove_vertex(index)
    break


def remove_edge_aux(g):
  while(True):
    source = int(input("Digite o indice de origem: "))
    if source == '':
      print('Origem invalida!')
      continue
    destiny = int(input("Digite o indice de destino: "))
    if destiny == '':
      print('Destino invalido!')
      continue
    g.remove_edge(source, destiny)
    break


def get_connectivity_aux(g):
  if g.get_connectivity_type() == 1:
    print("Desconexo")
  else:
    print("Conexo")


def get_vertex_degree_aux(self, g):
  while(True):
    indice = int(input("Digite o indice do pais: "))
    if indice == '':
      print('Indice invalido!')
      continue
    print(g.get_vertex_degree(indice))
    break


def find_paths_between_countries_aux(g):
  routes = []
  while(True):
    source = int(input("Digite o indice de origem: "))
    if source == '':
      print('Origem invalida!')
      continue
    destiny = int(input("Digite o indice de destino: "))
    if destiny == '':
      print('Destino invalido!')
      continue
    routes = g.find_best_route(source, destiny)
    break
  for route in routes:
    print("\n")
    for i, country_index in enumerate(route):
        print(g.get_vertex_name(country_index), end='')
        if i < len(route) - 1:
            print(' => ', end='')
  print("\n")

def menu():

  print("Mapeamento das fronteiras de países da Europa e América")

  g = Graph()

  while True:
    
    print(
      "\n*** MENU DE OPCOES ***\n" +
      "[a] Ler dados do arquivo grafo.txt\n" + 
      "[b] Gravar dados no arquivo grafo.txt\n" +
      "[c] Inserir vértice\n" +
      "[d] Inserir aresta\n" +
      "[e] Remove vértice\n" + 
      "[f] Remove aresta\n" + 
      "[g] Mostrar conteúdo do arquivo\n" + 
      "[h] Mostrar grafo\n" + 
      "[i] Apresentar a conexidade\n" + 
      "[j] Obter número de países vizinhos\n" + 
      "[k] Alcançar país a partir de outro país\n" + 
      "[l] Obter mapas de registro de cores\n" + 
      "[m] Encerrar a aplicação\n"
    )

    try:
      option = input("Escolha uma opcao: ").lower()
      if option == "a":
        g.makeGraphFromFile('grafo.txt')
      elif option == "b":
        g.makeFileFromGraph('grafo.txt')
      elif option == "c":
        insert_vertex_aux(g)
      elif option == "d":
        insert_edge_aux(g)
      elif option == "e":
        remove_vertex_aux(g)
      elif option == "f":
        remove_edge_aux(g)
      elif option == "g":
        showFileContent('grafo.txt')
      elif option == "h":
        g.show_min()
      elif option == "i":
        get_connectivity_aux(g)
      elif option == "j":
        get_vertex_degree_aux(g)
      elif option == "k":
        find_paths_between_countries_aux(g)
      elif option == "l":
        g.show_class_colouring()
      elif option == "m":
        print("Aplicacao encerrada!")
        break
      else:
        print("Opcao invalida, escolha novamente!")
    except:
      print('Nao foi possivel executar esta opcao!')
menu()