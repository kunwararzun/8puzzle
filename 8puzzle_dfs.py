#8 puzzle solution using DFS
# Author : Arjun Kunwar 
# For infinite depth remove the level limitations in the code below and increase the stack size. 
#In linux terminal use the command: ulimit -s 131072 before running the code if the depth is made infinite.   
import copy
import sys
import time
sys.setrecursionlimit(10000000)
m = 0
def main():
	start = time.time()
	global m
	initial = []
	initial.append([])
	initial.append([])
	initial.append([])
	initial[0].append(2)
	initial[0].append(8)
	initial[0].append(3)
	initial[1].append(1)
	initial[1].append(6)
	initial[1].append(4)
	initial[2].append(7)
	initial[2].append(0)
	initial[2].append(5)
	lists = copy.deepcopy(initial)
	final = []
	final.append([])
	final.append([])
	final.append([])
	final[0].append(1)
	final[0].append(2)
	final[0].append(4)
	final[1].append(8)
	final[1].append(0)
	final[1].append(3)
	final[2].append(7)
	final[2].append(5)
	final[2].append(6)
	print "Initial State "
	display(initial)
	print "Goal State"
	display(final)
	print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	print "!!!!!             START             !!!!!"
	print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	level = 0
	display(initial)	
	print "---------------"
	print "LEVEL ", level 
	print "---------------"
	visited_nodes = {}
	visited_nodes[m] = copy.deepcopy(initial)		
	while(1):		
		getlist = copy.deepcopy(lists)			
		left(lists, level, visited_nodes,start)
		lists = copy.deepcopy(getlist)
		right(lists, level, visited_nodes,start)
		lists = copy.deepcopy(getlist)
		up(lists, level, visited_nodes,start)
		lists = copy.deepcopy(getlist)
		down(lists, level, visited_nodes,start)
		print "Increase the depth of the DFS"
		break
		

def display(lists):
	print " "
	print " ------------------- "
	print " | ",lists[0][0]," | ",lists[0][1] ," | ",lists[0][2] ," | "
	print " ------------------- "
	print " | ",lists[1][0]," | ",lists[1][1] ," | ",lists[1][2] ," | "
	print " ------------------- "
	print " | ",lists[2][0]," | ",lists[2][1] ," | ",lists[2][2] ," | "
	print " -------------------"
	print " "
	
def check_visited(lists, visited_nodes):
	if lists in visited_nodes.itervalues():		
		return 1		
	else:
		return 0
		
		
def check_list(list1 , list2 ):
	if list1[0][0] == list2[0][0] and list1[0][1] == list2[0][1] and list1[0][2] == list2[0][2] and list1[1][0] == list2[1][0] and list1[1][1] == list2[1][1] and list1[1][2] == list2[1][2] and list1[2][0] == list2[2][0] and list1[2][1] == list2[2][1] and list1[2][2] == list2[2][2]:
		return 1
	else:
		return 0 
		
def count_misplace(list1):
	a = 0
	if list1[0][0] != 1:
		a = a+1
	if list1[0][1] != 2:
		a = a+1 
	if list1[0][2] != 4:
		a = a+1
	if list1[1][0] != 8:
		a = a+1
	if list1[1][1] != 0:
		a = a+1
	if list1[1][2] != 3:
		a = a+1
	if list1[2][0] != 7:
		a = a+1
	if list1[2][1] != 5:
		a = a+1
	if list1[2][2] != 6:
		a = a+1
	return a
		
def get_pos(lists, value):
	for a in range(0,3):
		for b in range(0,3):
			if lists[a][b]==value:
			 	return (a,b)

			
def left(lists, level, visited_nodes,start):
	global m
	i , j = get_pos(lists,0)
	if j > 0:
		print "------------------"
		print "FROM LEVEL ", level 
		print "------------------"			
		display(lists)
		print "left <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
		temp = lists[i][j-1]
		lists[i][j-1] = 0
		lists[i][j] = temp
		display(lists)
		level = level + 1
		print "-----------------"
		print "TO LEVEL ", level 
		print "-----------------"		
		if check_visited(lists, visited_nodes) == 0 and level < 22: # remove the code level < 22 for making an infinite depth
			if count_misplace(lists) != 0 :
				m = m + 1
				visited_nodes[m] = copy.deepcopy(lists)
				getlist = copy.deepcopy(lists)
				lists = copy.deepcopy(getlist)
				left(lists, level, visited_nodes,start)
				lists = copy.deepcopy(getlist)				
				up(lists, level, visited_nodes,start)				
				lists = copy.deepcopy(getlist)
				down(lists, level, visited_nodes,start) 
			else:
				print "Final State reached"
				print "Total no of nodes generated", m
				end = time.time()
				print "Time elapsed in seconds : ", end - start
				sys.exit()
					
		else:
			print "BackTrack"
			
				
				
	
def down(lists, level, visited_nodes,start):
	global m
	i , j = get_pos(lists, 0)
	if i < 2:
		print "------------------"
		print "FROM LEVEL ", level 
		print "------------------"
		display(lists)
		print "down vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"		
		temp = lists[i+1][j]
		lists[i+1][j] = 0
		lists[i][j] = temp
		display(lists)
		level = level + 1	
		print "-----------------"
		print "TO LEVEL ", level 
		print "-----------------"
		if check_visited(lists, visited_nodes) == 0 and level < 22: # remove the code level < 22 for making an infinite depth
			if count_misplace(lists) !=0 :
				m = m + 1
				visited_nodes[m] = copy.deepcopy(lists)
				getlist = copy.deepcopy(lists)
				lists = copy.deepcopy(getlist)
				down(lists, level, visited_nodes,start)
				lists = copy.deepcopy(getlist)
				left(lists, level, visited_nodes,start)
				lists = copy.deepcopy(getlist)
				right(lists, level, visited_nodes,start)
			else:
				print "Final State reached"
				print "Total no of nodes generated", m
				end = time.time()
				print "Time elapsed in seconds : ", end - start
				sys.exit()
		else:
			print "BackTrack"
		
def up(lists, level, visited_nodes,start):
	global m
	i , j = get_pos(lists,0)
	if i > 0:
		print "------------------"
		print "FROM LEVEL ", level 
		print "------------------"
		display(lists)
		print "up ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
		temp = lists[i-1][j]
		lists[i-1][j] = 0
		lists[i][j] = temp
		display(lists)
		level = level + 1
		print "-----------------"
		print "TO LEVEL ", level 
		print "-----------------"
		if check_visited(lists, visited_nodes) == 0 and level < 22: # remove the code level < 22 for making an infinite depth
			if count_misplace(lists) !=0 :
				'''q.put(copy.deepcopy(lists))
				q.put(level)
				q.put('u')'''
				m = m + 1
				visited_nodes[m] = copy.deepcopy(lists)
				getlist = copy.deepcopy(lists)
				lists = copy.deepcopy(getlist)
				up(lists, level, visited_nodes,start)
				lists = copy.deepcopy(getlist)
				left(lists, level, visited_nodes,start)
				lists = copy.deepcopy(getlist)
				right(lists, level, visited_nodes,start)

			else:
				print "Final State reached"
				print "Total no of nodes generated", m
				end = time.time()
				print "Time elapsed in seconds : ", end - start
				sys.exit()
		else:
			print "BackTrack"
				
def right(lists, level, visited_nodes,start):
	global m
	i , j = get_pos(lists, 0)
	if j < 2:
		print "------------------"
		print "FROM LEVEL ", level 
		print "------------------"
		display(lists)
		print "right >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
		temp = lists[i][j+1]
		lists[i][j+1] = 0
		lists[i][j] = temp
		display(lists)
		level = level + 1
		print "-----------------"
		print "TO LEVEL ", level 
		print "-----------------"			
		if check_visited(lists, visited_nodes) == 0 and level < 22: # remove the code level < 22 for making an infinite depth
			if count_misplace(lists) !=0 :
				m = m + 1
				visited_nodes[m] = copy.deepcopy(lists)
				getlist = copy.deepcopy(lists)
				lists = copy.deepcopy(getlist)
				right(lists, level, visited_nodes,start)
				lists = copy.deepcopy(getlist)				
				up(lists, level, visited_nodes,start)	
				lists = copy.deepcopy(getlist)
				down(lists, level, visited_nodes,start) 			

			else:
				print "Final State reached"
				print "Total no of nodes generated", m
				end = time.time()
				print "Time elapsed in seconds : ", end - start
				sys.exit()
		else:
			print "BackTrack"

		 
	
if __name__ == '__main__':
	main()

