import igraph
import sys
import time
import matplotlib.pyplot as plt

 
matrix = [
[0, 4, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0],
[0, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 7, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 7, 0, 3, 0, 0, 0, 0, 0],
[5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
]
 
name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Now', 'Dec']
#Создание списка смежности 
def compile_list(adjacency_matrix, name_array):
    adjacency_list = []
    for i in range(len(name_array)):
        for j in range(len(name_array)):
            if adjacency_matrix[i][j] != 0:
                adjacency_list.append([name_array[i], name_array[j], adjacency_matrix[i][j]])
    return adjacency_list
 
#Создание графа
def graph():
	listok = compile_list(matrix, name)
	g = igraph.Graph()
	g.add_vertices(12)
	g.vs["label"] = name
 
	ok = []
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if matrix[i][j] != 0:
				ok.append((i, j))
 
 
	g.add_edges(ok)
	g.es["weight"] = [i[2] for i in listok]
	g.es["label"] = [i[2] for i in listok]
	igraph.plot(g, bbox = (600,600), vertex_label_color = 'black',
vertex_label_size = 10, vertex_size = 20, vertex_color = 'white' )


def grid(m, flag = False):
	matrixa = []
	matrix = m**2

	for i in range(matrix):
		matrixa.append([])
		for j in range(matrix):
			matrixa[i].append(0)


	for i in range(m):
		for j in range(m):
			if i == m - 1 and j== m-1:
				pass
			elif i==m-1:
				matrixa[i*m + j][i*m + j+1] = 1
			elif j==m-1:
				matrixa[i*m +j][(i+1)*m +j] = 1
			else:
				matrixa[i*m + j][i*m + j+1] = 1
				matrixa[i*m +j][(i+1)*m +j] = 1

	if not flag:
		for i in matrixa:
			print(i)
	
	edges = []
	for i in range(len(matrixa)):
	    for j in range(len(matrixa)):
	    	if matrixa[i][j] != 0:
	            edges.append((i, j))

	g = igraph.Graph()
	g.add_vertices(len(matrixa))
	g.layout_grid_fruchterman_reingold()
	g.add_edges(edges)
	igraph.plot(g, bbox=(500, 500), vertex_label_color='black', vertex_size=2, vertex_color='white')

	return matrixa





def zav():
	arr_time = []  # Массив данных времени
	arr_mem = []  # Массив данных памяти
	arr_quant = []  # Массив количества узлов
	for j in range(2, 30):
	    matrix = grid(j, True)
	    name = [str(i) for i in range(len(matrix))]
	    start_time = time.monotonic()
	    ad_list = deikster(0, matrix, name, True)
	    arr_time.append(time.monotonic() - start_time)
	    arr_mem.append(sys.getsizeof(ad_list))
	    arr_quant.append(j**2)
	fig, ax = plt.subplots(figsize=(8, 6))
	ax.plot(arr_quant, arr_time)
	ax.grid()
	ax.set_title('Время выполнения от количество узлов')
	ax.set_xlabel('Количество узлов')
	ax.set_ylabel('Время (сек.)')
	plt.show()

	fig, ax = plt.subplots(figsize=(8, 6))
	ax.plot(arr_quant, arr_mem)
	ax.grid()
	ax.set_title('Занимаемая память от количество узлов')
	ax.set_xlabel('Количество узлов')
	ax.set_ylabel('Память (байт)')
	plt.show()




def deikster(k, matrix, name, flag = False):
	verticles_weight = [] #массив весов
	visited = []	#список посещенных вершин
	ver = [] #список вершин
	parents = [0 for i in range(len(name))] # массив предков
	 
	for i in range(len(matrix)):
		if i == k:
			verticles_weight.append(0)
		else:
			verticles_weight.append(float("inf"))
	 
	visited.append(k)
	 
	while len(visited) != len(verticles_weight):
		current_ver = visited[-1]
		for i in range(len(matrix)):
			if matrix[current_ver][i] != 0:
				if verticles_weight[current_ver] + matrix[current_ver][i] < verticles_weight[i]:
					verticles_weight[i] = verticles_weight[current_ver] + matrix[current_ver][i]
					parents[i] = current_ver
	 
			if matrix[i][current_ver] != 0:
				if verticles_weight[current_ver] + matrix[i][current_ver] < verticles_weight[i]:
					verticles_weight[i] = verticles_weight[current_ver] + matrix[i][current_ver]
					parents[i] = current_ver
	 
		min_weight = float("inf")
		ver = 0
	 
		for i in range(len(verticles_weight)):
			if i not in visited and verticles_weight[i] < min_weight:
				ver = i
				min_weight = verticles_weight[i]
	 
		visited.append(ver)
	 
	if not flag:
		print(verticles_weight)
		 
		for i in range(len(name)):
			tmp = []
			j = i
			if i != k:
				print(f"{name[k]} -> {name[i]}: {verticles_weight[i]}")
				while j != k:
					tmp.append(name[j])
					j = parents[j]
				tmp.append(name[k])
				tmp = tmp[::-1]
				for z in range(len(tmp)):
					if z != len(tmp)-1:
						print(f"{tmp[z]} -> ", end ="")
					else:
						print(tmp[z])
				print()
		graph()
	else:
		return verticles_weight


deikster(3, matrix, name)
