from collections import deque


def Breadth_First_Search(a, b, target):

	# dictionary for visited nodes
	visited_states = {}  
	isSolvable = False
	# list to track path
	path = []


	q = deque()
	# adding initial state to queue
	# both jugs are empty
	q.append((0, 0)) 
	# while queue has elements present
	while (len(q) > 0): 
		current_node = q.popleft()
		if ((current_node[0], current_node[1]) in visited_states):
			continue
		if ((current_node[0] > a or current_node[1] > b or
			current_node[0] < 0 or current_node[1] < 0)):
			continue

		
		path.append([current_node[0], current_node[1]])

		
		visited_states[(current_node[0], current_node[1])] = 1

		
		if (current_node[0] == target or current_node[1] == target):
			isSolvable = True

			if (current_node[0] == target):
				if (current_node[1] != 0):
					path.append([current_node[0], 0])		
			else:
				if (current_node[0] != 0):
					path.append([0, current_node[1]])

			
			single_path = len(path)
			for i in range(single_path):
				print("[", path[i][0], ",",
					path[i][1], "]")
			break

		
		q.append([current_node[0], b]) 
		q.append([a, current_node[1]]) 

		for ap in range(max(a, b) + 1):

			
			c = current_node[0] + ap
			d = current_node[1] - ap

			
			if (c == a or (d == 0 and d >= 0)):
				q.append([c, d])

			
			c = current_node[0] - ap
			d = current_node[1] + ap

			
			if ((c == 0 and c >= 0) or d == b):
				q.append([c, d])

		
		q.append([a, 0])

		
		q.append([0, b])

	
	if (not isSolvable):
		print("No solution exists for such combination")



if __name__ == '__main__':
		

	Jug1=int(input("Enter the capacity of Jug 1: "))
	Jug2=int(input("Enter the capacity of Jug 2: "))
	target=int(input("Enter the target amount of water that should be left in Jug 1:  "))
	print("Path from initial state to final state ")

	Breadth_First_Search(Jug1, Jug2, target)

