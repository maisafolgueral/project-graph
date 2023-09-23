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
      "[j] Encerrar a aplicação\n"
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
        print("Aplicacao encerrada!")
        break
      else:
        print("Opcao invalida, escolha novamente!")
    except:
      print('Nao foi possivel executar esta opcao!')
      
menu()