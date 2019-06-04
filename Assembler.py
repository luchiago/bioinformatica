def read_kdmer(file, D, G):
  lineList = ''
  with open(file) as f:
    for line in f:
      lineList += line
  lineList = lineList.strip('][').split(',')

  kdmer = [i.split('|') for i in lineList]
  print(kdmer)

  k = len(kdmer[0][0])
  for l in kdmer:
    G.append_node((l[0])[0:k - 1] + (l[1])[0:k - 1])
    G.append_node((l[0])[1:k] + (l[1])[1:k])
    D.append_node((l[0])[0:k - 1] + (l[1])[0:k - 1])
    D.append_node((l[0])[1:k] + (l[1])[1:k])
    G.append_edge((l[0])[0:k - 1] + (l[1])[0:k - 1], (l[0])[1:k] + (l[1])[1:k])
    D.append_edge_digraph((l[0])[0:k - 1] + (l[1])[0:k - 1], (l[0])[1:k] + (l[1])[1:k])
  f.close()
  return kdmer

def deBruijin(path, k, list):
  edges = []
  sequence = ''
  for i in range(len(path) - 1):
    edges.append([(path[i])[:k] + path[i + 1][k - 1], (path[i])[k:] + path[i + 1][k + k - 1]])
    sequence += path[i] + '\n'
    sequence += path[i + 1] + '\n'
    sequence += (path[i])[:k] + path[i + 1][k - 1] + '_' + (path[i])[k:] + path[i + 1][k + k - 1] + '\n'
  return edges

def assemble_sequence(edges, d, k):
  sequence = edges[0][0]
  for i in range(1, len(edges)):
    sequence += edges[i][0][k - 1]
  sequence += (edges[len(edges) - 1 - d][1])[:d] # O correto é d apenas e não (d-1) - corrigido
  sequence += edges[len(edges) - 1][1]
  return sequence


class Graph:
  def __init__(self):
    self.edges = {}
    self.nodes = {}

  def see_nodes(self):
    return self.nodes.keys()

  def append_node(self, node):
    self.nodes[node] = True

  def append_edge(self, node, neighbour):
    if not node in self.edges:
      self.edges[node] = []
    self.edges[node].append(neighbour)
    if not neighbour in self.edges:
      self.edges[neighbour] = []
    self.edges[neighbour].append(node)

  def append_edge_digraph(self, node, neighbour):
    if not node in self.edges:
      self.edges[node] = []
    self.edges[node].append(neighbour)
    if not neighbour in self.edges:
      self.edges[neighbour] = []

  def neighbors(self, node):
    if node in self.edges:
      return self.edges[node]
    else:
      return []

  def select_start_and_end(self, list):
    array = []
    for i in list.keys():
      if list[i][0] % 2 != 0:
        array.append(i)
    return array

def degree(Graph):
  count = -1
  list_count = {}
  list_aux = []
  for i in Graph.nodes.keys():
    list_count[i] = []
    list_count[i].append(count)
    list_aux.append(i)
    for j in Graph.edges[i]:
      list_aux.append(j)
  for l in list_aux:
    list_count[l][0] += 1
  return list_count

def eulerian_graph(Graph, l):
  heap = []
  path = []
  while len(heap) > 0 or len(Graph[l]) > 0:
    if len(Graph[l]) > 0:
      heap.append(l)
      l = Graph[l].pop(0)
    elif len(heap) > 0:
      path.append(l)
      l = heap.pop()
  path.append(l)
  return path

def eulerian_graph_path(circuit, reverse_list):
  k = len(circuit) - 1
  path = []
  for i in circuit:
    path.append(reverse_list[circuit[k]])
    k -= 1
  return path

def fill(Graph, normal_list, reverse_list):
  Graph = []
  Graph.append([])
  list = []
  count = 1
  for i in D.nodes.keys():
    normal_list[i] = count
    reverse_list[count] = i
    count += 1
  for j in D.nodes.keys():
    for l in D.edges[j]:
      list.append(normal_list[l])
    Graph.append(list)
    list = []

  return (normal_list, Graph, reverse_list)

def get_kd():
  

if __name__ == '__main__':
  file = input('Input file name of generated kdmer:')
  list = {}
  reverse_list = {}
  array = []
  G = Graph()
  D = Graph()
  kdmer = read_kdmer(file, D, G)
  (list, graph, reverse_list) = fill(D, list, reverse_list)
  degree = degree(G)
  array = G.select_start_and_end(degree)
  size_graph = len(G.see_nodes())
  circuit = eulerian_graph(graph, list[array[0]])
  if len(circuit) < size_graph:
    circuit = eulerian_graph(graph, list[array[1]])
  path = eulerian_graph_path(circuit, reverse_list)
  edges = deBruijin(path, len(kdmer[0][0]) - 1, list)
  d = 2 # tem que pegar direto do arquivo ainda
  sequence = assemble_sequence(edges, d, len(kdmer[0][0]))
  f = open('output.fasta', 'w')
  f.write(sequence)
  f.close()
  print('Assembled sequence!')
