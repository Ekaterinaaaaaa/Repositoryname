import igraph
import sys
import time

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


listok = [] #Список смежности
array = [] #Список массива записей
name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Now', 'Dec']

def zapol_listok():
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if matrix[i][j] != 0:
				listok.append([i, j, matrix[i][j]])  


#Создание графа
def graph():
	g = igraph.Graph(directed = True)
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


#Массив записей
def zapol_array():
	for i in range(len(matrix)):
		array.append([i, name[i], [], [], [] ])
		for j in range(len(matrix)):
			if matrix[i][j] != 0:
				array[i][2].append(j)
				array[i][4].append(matrix[i][j])
			if matrix[j][i] != 0:
				array[i][3].append(j)


#Cоседи для матрицы смежности
def sosedi_matr(x, flag_test=0):
	for j in range(len(matrix)):
		if matrix[x][j] !=0:
			if flag_test == 0:
				print(name[j])
		if matrix[j][x] !=0:
			if flag_test == 0:
				print(name[j])


#Соседи для списка
def sosedi_spisok(x, flag_test=0):
	for i in listok:
		if i[0] == x:
			if flag_test == 0:
				print(i[1])
		if i[1] == x:
			if flag_test == 0:
				print(i[0])


#Соседи для массива
def sosedi_array(x, flag_test=0):
	if flag_test == 0:
		print(array[x][2])
		print(array[x][3])


#Цепь для матрицы
def zep_matr(x, flag_test=0):
	for i in range(len(x)-1):
		a = x[i]
		j = x[i+1]
		if matrix[a][j] == 0:
			if flag_test == 0:
				print("Не цепь")
			return
	if flag_test == 0: 
		print("Цепь")

#Цепь для списка
def zep_spis(x, flag_test=0):
	for i in range(len(x)-1):
		a = x[i]
		j = x[i+1]
		f = False
		for z in listok:
			if z[0] == a and z[1]==j:
				f = True
				break
		if not f:
			if flag_test == 0:
				print("не цепь")			
			return
	if flag_test == 0:		
		print("цепь")


#Цепь для массива
def zep_array(x, flag_test=0):
	for i in range(len(x)-1):
		a = x[i]
		j = x[i+1]
		if j not in array[a][2]:
			if flag_test == 0:
				print("Не цепь")
			return
	if flag_test == 0:
		print("цепь")


#Инцидентные ребра
# В матрице смежности
def reb_matr(x, flag_test=0):
    incidence_list = []
    for i in range(len(name)):
        counter = 0
        for j in range(len(name)):
            if matrix[i][j] != 0:
                counter += 1
            if matrix[j][i] != 0:
                counter += 1
        if counter > x:
            incidence_list.append(name[i])
    if flag_test == 0:
        print("Search matrix:")
        print("List from vertex, whose sum of incident edges is greater than", x, ":", incidence_list)



# В списке смежности
def reb_spis(x, flag_test=0):
	incidence_list = []
	for i in range(len(name)):
		counter = 0
		for j in listok:
			if j[0] == i or j[1] == i:
				counter += 1
		if counter > x:
			incidence_list.append(name[i])
	if flag_test == 0:
		print("Search list:")
		print("List from vertex, whose sum of incident edges is greater than", x, ":", incidence_list)


# В массиве записей
def reb_array(x, flag_test=0):
    incidence_list = []
    for i in array:
        if len(i[2]) + len(i[3]) > x:
            incidence_list.append(i[1])
    if flag_test == 0:
    	print("Search list:")
    	print("List from vertex, whose sum of incident edges is greater than", x, ":", incidence_list)


# Количество ребер в графе
# Из матрицы смежности
def kol_matr(flag_test=0):
    counter = 0
    for i in matrix:
        for j in i:
            if j != 0:
                counter += 1
    if flag_test == 0:            
    	print("Search matrix:")
    	print("The number of edges in the graph is equal to", counter)


# Из списка смежности
def kol_list(flag_test=0):
    counter = len(listok)
    if flag_test == 0:
    	print("Search list:")
    	print("The number of edges in the graph is equal to", counter)


# Из массива записей
def kol_array(flag_test=0):
    counter = 0
    for i in array:
        counter += len(i[2])
    if flag_test == 0:    
    	print("Search array:")
    	print("The number of edges in the graph is equal to", counter)





# Подсчет времени выполнения
def timee():
    t = 10**6
    x = 1
    print(f"Test data to find neighbors: {x}")
    start_time = time.monotonic()
    for i in range(t):
        sosedi_matr(x, flag_test=1)
    print(f"Search neighbors in matrix: {time.monotonic() - start_time} s")

    x = 1
    start_time = time.monotonic()
    for i in range(t):
        sosedi_spisok(x, flag_test=1)
    print(f"Search neighbors in list: {time.monotonic() - start_time} s")

    x = 1
    start_time = time.monotonic()
    for i in range(t):
        sosedi_array(x, flag_test=1)
    print(f"Search neighbors in array: {time.monotonic() - start_time} s")

    print()

    x = [8, 5, 6]
    print(f"Test data to find chain: {x}")
    start_time = time.monotonic()
    for i in range(t):
        zep_matr(x, flag_test=1)
    print(f"Search chain in matrix: {time.monotonic() - start_time} s")

    x = [8, 5, 6]
    start_time = time.monotonic()
    for i in range(t):
        zep_spis(x, flag_test=1)
    print(f"Search chain in list: {time.monotonic() - start_time} s")

    x = [8, 5, 6]
    start_time = time.monotonic()
    for i in range(t):
        zep_array(x, flag_test=1)
    print(f"Search chain in array: {time.monotonic() - start_time} s")

    print()

    x = 3
    print(f"Test data to find sum incidence: {x}")
    start_time = time.monotonic()
    for i in range(t):
        reb_matr(x, flag_test=1)
    print(f"Search incidence in matrix: {time.monotonic() - start_time} s")

    x = 3
    start_time = time.monotonic()
    for i in range(t):
        reb_spis(x, flag_test=1)
    print(f"Search incidence in list: {time.monotonic() - start_time} s")

    x = 3
    start_time = time.monotonic()
    for i in range(t):
        reb_array(x, flag_test=1)
    print(f"Search incidence in array: {time.monotonic() - start_time} s")

    print()

    start_time = time.monotonic()
    for i in range(t):
        kol_matr(flag_test=1)
    print(f"Search quantity in matrix: {time.monotonic() - start_time} s")

    start_time = time.monotonic()
    for i in range(t):
        kol_list(flag_test=1)
    print(f"Search quantity in list: {time.monotonic() - start_time} s")

    start_time = time.monotonic()
    for i in range(t):
        kol_array(flag_test=1)
    print(f"Search quantity in array: {time.monotonic() - start_time} s")


zapol_listok()
zapol_array()
timee()


if __name__ == "__main__":
    compile_adjacency_list()
    compile_record_array()

    while 1:
        print("Select action:")
        print("1 - Search menu\n"
              "2 - Sizes of structures\n"
              "3 - Print menu\n"
              "4 - Work time test\n"
              "5 - Test\n"
              "6 - Exit")
        select = input("Enter your select: ")
        if select == "1":
            while 1:
                print("Select search:")
                print("1 - Search of neighbors\n"
                      "2 - Search of chain\n"
                      "3 - Search of incidence\n"
                      "4 - Search of the number of edges in a graph\n"
                      "Any enter - Back")
                select = input("Enter your select: ")
                if select == "1":
                    request = input("Enter vertex: ")
                    if request not in name_array:
                        print(f"Vertex {request} does not exist in graph!\n")
                        continue
                    search_neighbors_matrix(request)
                    search_neighbors_list(request)
                    search_neighbors_array(request)
                    print()
                elif select == "2":
                    request = []
                    n = int(input("Enter the number of vertices: "))
                    # if n > len(name_array) or n <= 0:
                    #     print("The number of entered vertices must be greater than 0 "
                    #           "and less than or equal to their number in the graph!")
                    #     continue
                    if n <= 0:
                        print("The number of entered vertices must be greater than 0!")
                        continue
                    print("Enter the vertices via enter")
                    while n > 0:
                        vertex = input()
                        if vertex not in name_array:
                            print(f"Vertex {request} does not exist in graph!\nTry again!")
                            continue
                        request.append(vertex)
                        n -= 1
                    search_chain_matrix(request)
                    search_chain_list(request)
                    search_chain_array(request)
                    print()
                elif select == "3":
                    x = int(input("Enter the number greater than which the sum of the incident edges must be:\n"))
                    search_incidence_matrix(x)
                    search_incidence_list(x)
                    search_incidence_array(x)
                    print()
                elif select == "4":
                    search_quantity_matrix()
                    search_quantity_list()
                    search_quantity_array()
                else:
                    break
        elif select == "2":
            print("Size of matrix:", sys.getsizeof(adjacency_matrix), "byte")
            print("Size of list:", sys.getsizeof(adjacency_list), "byte")
            print("Size of array:", sys.getsizeof(record_array), "byte")
        elif select == "3":
            while 1:
                print("Select print:")
                print("1 - Print graph\n"
                      "2 - Print adjacency matrix\n"
                      "3 - Print adjacency list\n"
                      "4 - Print record array\n"
                      "Any enter - Back")
                select = input("Enter your select: ")
                if select == "1":
                    print_graph()
                elif select == "2":
                    out_adjacency_matrix()
                    print()
                elif select == "3":
                    out_adjacency_list()
                    print()
                elif select == "4":
                    out_record_array()
                    print()
                else:
                    break
        elif select == "4":
            time_counter()
        elif select == "5":
            min_w = 3
            max_w = 6
            for i in record_array:
                for j in i[3]:  # i[3] - Список детей
                    for z in range(len(i[7])):  # i[7] -  список соседей
                        if i[7][z] == j:
                            if min_w <= i[8][z] <= max_w:  # i[8] - веса соседей
                                print(f"{i[1]} - {j}: {i[8][z]}")
        elif select == "6":
            break
        else:
            print("Wrong select!")
