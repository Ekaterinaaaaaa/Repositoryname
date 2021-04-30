import igraph

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


