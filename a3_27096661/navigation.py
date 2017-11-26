# define a min-heap to guarantee the time complexity of finding the minimum element in O(log(n))
class MinHeap:
    # create the heap
    def __init__(self, length, start):
        self.heap = [None, start]
        self.count = 1
        self.distance = [0] * length

    # insert one element into the heap and rearrange according their distance
    def insert(self, num):
        self.heap.append(num)
        self.count += 1
        self.rearrange_btt(self.count)

    # get the minimum element from the heap and rearrange the heap according to their distance
    def get_min(self):
        minimum = self.heap[1]
        self.heap[1] = self.heap[self.count]
        del self.heap[-1]
        self.count -= 1
        self.rearrange_ttb()
        return minimum

    # rearrange the heap from top to the bottom
    def rearrange_ttb(self):
        i = 1
        while (i * 2) <= self.count:
            mc = self.minChild(i)
            if self.distance[self.heap[i]] > self.distance[self.heap[mc]]:
                self.heap[i], self.heap[mc] = self.heap[mc],self.heap[i]
            i = mc

    # return the smaller child
    def minChild(self, i):
        if i * 2 + 1 > self.count:
            return i * 2
        else:
            if self.distance[self.heap[i*2]] < self.distance[self.heap[i*2+1]]:
                return i * 2
            else:
                return i * 2 + 1

    # rearrange the heap from the given node to top
    def rearrange_btt(self, i):
        while i//2 > 0:
            if self.distance[self.heap[i]] < self.distance[self.heap[i//2]]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i //= 2


# the dijkstra algorithm implement
def dijkstra(start, graph):
    # define heap as discovered, distance list, finalized and previous
    heap = MinHeap(len(graph), start)
    previous = [0] * len(graph)
    # define 1 to be discovered, 0 to be non-discovered, -1 to be finalized
    state = [0]*len(graph)
    # while there is node not finalized
    while heap.heap != [None]:
        # get the minimum node from the discovered list
        current_node = heap.get_min()
        # for every node connected to the current node
        for neighbour_node in graph[current_node]:
            # if node is in finalized, do nothing, if not do following
            if state[neighbour_node[0]] != -1:
                # calculate the distance from the start node to this node
                dis = heap.distance[current_node] + neighbour_node[1]
                # if this node is not in the discovered
                if state[neighbour_node[0]] != 1:
                    # change the distance of this node in distance list to new distance
                    heap.distance[neighbour_node[0]] = dis
                    # add this node to discovered, after this function, heap is rearranged
                    heap.insert(neighbour_node[0])
                    # add current node as the previous node of this node
                    previous[neighbour_node[0]] = current_node
                    state[neighbour_node[0]] = 1
                # elif this node is in the discovered and distance can be smaller
                elif heap.distance[neighbour_node[0]] > dis:
                    # update the distance of this node
                    heap.distance[neighbour_node[0]] = dis
                    # as the distance of one node is changed, the heap may be no longer valid, since node must be
                    # smaller, rearrange from this node to the top
                    heap.rearrange_btt(heap.heap.index(neighbour_node[0]))
                    # update the previous node
                    previous[neighbour_node[0]] = current_node
        # after all of the nodes connected to current node is discovered, put current node into finalized
        state[current_node] = -1
    return heap.distance, previous


# create the graph
def create_graph():
    file = open("edges.txt", "r")
    contain = file.readlines()
    for i in range(len(contain)):
        contain[i] = contain[i].replace("\n", "")
        contain[i] = contain[i].split(" ")
    graph = [[] for h in range(6105)]
    for j in range(len(contain)):
        graph[int(contain[j][0])].append((int(contain[j][1]), int(contain[j][2])))
        graph[int(contain[j][1])].append((int(contain[j][0]), int(contain[j][2])))
    file.close()
    return graph


# return a list of nodes of customers
def find_customers():
    file = open("customers.txt", "r")
    contain = file.readlines()
    for i in range(len(contain)):
        contain[i] = contain[i].split(" ")
        contain[i] = int(contain[i][0])
    return contain


# main function
if __name__ == "__main__":
    graph = create_graph()
    customers = find_customers()
    start = int(input("Enter the start node: "))
    end = int(input("Enter the end node: "))
    # run the dijkstra fot the first time, get distance of every node from start
    diss, pres = dijkstra(start, graph)
    # print the distance from start to end
    print("The None detour distance is: ", diss[end])
    # get the path from start to end
    this = end
    path_ste = []
    while this != start:
        path_ste.append(str(this))
        path_ste.append("-->")
        this = pres[this]
    path_ste.append(str(start))
    # add symbol to customer node
    for i in range(len(path_ste)):
        if path_ste[i] != "-->":
            if int(path_ste[i]) in customers:
                path_ste[i] += " (c)"
    path_ste.reverse()
    # print the path without detour
    print("the None detour path is: " + " ".join(path_ste))
    # run dijkstra for the second time
    dise, pree = dijkstra(end, graph)
    i = 0
    # get the total distance of each customer
    disc = [0] * len(customers)
    while i < len(disc):
        disc[i] += diss[customers[i]]
        disc[i] += dise[customers[i]]
        i += 1
    # find the shortest distance and print
    print("The detour distance is: ",(min(disc)))
    # find the shortest distance customer
    shortestc = disc.index(min(disc))
    realc = customers[shortestc]
    # get path from the start to the customer
    this = realc
    pathdl = []
    while this != start:
        pathdl.append(str(this))
        pathdl.append("-->")
        this = pres[this]
    pathdl.append(str(start))
    for i in range(len(pathdl)):
        if pathdl[i] != "-->":
            if int(pathdl[i]) in customers:
                pathdl[i] += " (c)"
    pathdl.reverse()
    # get path from customer to the end
    this = realc
    pathdr = []
    while this != end:
        pathdr.append(str(this))
        pathdr.append("-->")
        this = pree[this]
    pathdr.append(str(end))
    for i in range(len(pathdr)):
        if pathdr[i] != "-->":
            if int(pathdr[i]) in customers:
                pathdr[i] += " (c)"
    del pathdr[0]
    # combine two path together
    for item in pathdr:
        pathdl.append(item)
    # print the detour path
    print("the detour path is: " + " ".join(pathdl))
