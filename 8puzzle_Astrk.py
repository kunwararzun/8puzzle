# 8 puzzle solution using A* Algorithm
'''
@Author : Arjun Kunwar 
'''

from heapq import *  #define a priority queue 
import copy
import time
visited = 0
def main():
	global visited
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
	print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
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
	i = 0
	visited_nodes[i] = copy.deepcopy(initial)
	heap = []
	item = [count_manhatton(lists, final)+level,copy.deepcopy(lists),level,'x'] #+count_misplace(lists)
	heappush(heap,item)
	while heap:
		get_item = heappop(heap)
		getlist = copy.deepcopy(get_item[1])
		lists = copy.deepcopy(getlist)
		level = get_item[2]
		level = level + 1
		prev_pos = get_item[3]
		l = check_validity_operate(lists, "left", prev_pos )
		if l != 0:
			print "---------------"
			print "LEVEL ", level 
			print "---------------"	
			if check_visited(lists, visited_nodes) == 0:
				if count_misplace(lists) !=0 :	
					item = [count_manhatton(lists, final)+level,copy.deepcopy(lists),level,'l']#+count_misplace(lists)
					heappush(heap,item)
					i = i + 1
					visited_nodes[i] = copy.deepcopy(lists)
				else:
					print "Final state reached"
					print "Total no of nodes generated ", i
					print "Visited nodes found ", visited
					break

		lists = copy.deepcopy(getlist)
		r = check_validity_operate(lists, "right", prev_pos )
		if r != 0:
			print "---------------"
			print "LEVEL ", level 
			print "---------------"				
			if check_visited(lists, visited_nodes) == 0:
				if count_misplace(lists) !=0 :	
					item = [count_manhatton(lists, final)+level,copy.deepcopy(lists),level,'r'] #+count_misplace(lists)
					heappush(heap,item)
					i = i + 1
					visited_nodes[i] = copy.deepcopy(lists)
				else:
					print "Final state reached"
					print "Total no of nodes generated ", i
					print "Visited nodes found ", visited
					break		
	
	
		lists = copy.deepcopy(getlist)	
		d = check_validity_operate(lists, "down", prev_pos )
		if d != 0:
			print "---------------"
			print "LEVEL ", level 
			print "---------------"	
			if check_visited(lists, visited_nodes) == 0:
				if count_misplace(lists) !=0 :	
					item = [count_manhatton(lists, final)+level,copy.deepcopy(lists),level,'d'] #+count_misplace(lists)
					heappush(heap,item)
					i = i + 1
					visited_nodes[i] = copy.deepcopy(lists)
				else:
					print "Final state reached"
					print "Total no of nodes generated ", i
					print "Visited nodes found ", visited				
					break		
	
	
		lists = copy.deepcopy(getlist)
		u = check_validity_operate(lists, "up", prev_pos )
		if u != 0:
			print "---------------"
			print "LEVEL ", level 
			print "---------------"	
			if check_visited(lists, visited_nodes) == 0:
				if count_misplace(lists) !=0 :
					item = [count_manhatton(lists, final)+level,copy.deepcopy(lists),level,'u']#+count_misplace(lists)
					heappush(heap,item)
					i = i + 1
					visited_nodes[i] = copy.deepcopy(lists)
				else:
					print "Final state reached"
					print "Total no of nodes generated ", i
					print "Visited nodes found ", visited
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
	
def check_validity_operate(lists, position, prev_pos ):
	i , j = get_pos(lists, 0)
	if position == "up" and i > 0 and prev_pos != 'd':
		up(lists)
		return 1
	elif position == "down" and i < 2 and prev_pos != 'u':
		down(lists) 
		return 1
	elif position == "left" and j > 0 and prev_pos != 'r':
		left(lists) 
		return 1
	elif position == "right" and j < 2 and prev_pos != 'l':
		right(lists) 
		return 1
	else:
		return 0

def count_manhatton(lists, final):
	distance = 0
	for i in range(1,9):
		ra , ca = get_pos(lists,i)
		rb , cb = get_pos(final,i)
		if ra == rb and ca == cb:
			distance = distance + 0
		elif ra == rb and ca != cb:
			x = abs(ca-cb)
			distance = distance + x
		elif ra != rb and ca == cb:
			y = abs (ra-rb)
			distance = distance + y
		else:
			z = abs(ra-rb) + abs(ca-cb)
			distance = distance + z
	return distance
	
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
	
def check_visited(lists, visited_nodes):
	global visited	
	if lists in visited_nodes.itervalues():
		print " Visited "
		visited = visited + 1			
		return 1		
	else:
		return 0	
			
def get_pos(lists, value):
	for a in range(0,3):
		for b in range(0,3):
			if lists[a][b]==value:
				return (a,b)

				
	
def down(lists):
	i , j = get_pos(lists, 0)
	display(lists)
	print "down vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"		
	temp = lists[i+1][j]
	lists[i+1][j] = 0
	lists[i][j] = temp
	display(lists)
		
def up(lists):
	i , j = get_pos(lists,0)
	display(lists)
	print "up ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
	temp = lists[i-1][j]
	lists[i-1][j] = 0
	lists[i][j] = temp
	display(lists)
				
def right(lists):
	i , j = get_pos(lists,0)
	display(lists)
	print "right >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
	temp = lists[i][j+1]
	lists[i][j+1] = 0
	lists[i][j] = temp
	display(lists)
			
def left(lists):
	i , j = get_pos(lists,0)
	display(lists)
	print "left <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
	temp = lists[i][j-1]
	lists[i][j-1] = 0
	lists[i][j] = temp
	display(lists)
	
if __name__ == '__main__':
	start = time.time()
	main()
	end = time.time()
	print "Time elapsed in seconds : ", end - start
	
