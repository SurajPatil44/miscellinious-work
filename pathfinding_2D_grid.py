import copy
import random

INF = 0xFFFF

def fun(num):
	if num > INF:
		return '0'
	else:
		return str(num)
		
def print_list(_l):
	_l2 = copy.deepcopy(_l)
	_st = ''
	for _ll in _l2:
		_ll = list(map(lambda x : fun(x),_ll))
		_st += '\t'.join(_ll)
		_st += '\n\n'
		
	print(_st)
	
GRID_WIDTH = 5
GRID_HEIGHT = 5
#GRID = [[1,4,INF,1,1],[1,INF,1,INF,1],[1,1,INF,1,1],[INF,1,INF,1,1],[1,1,1,1,1]]
GRID = [[random.randint(1,9) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
#GRID = [[r for _ in range(GRID_LEN)] for _ in range(GRID_LEN)]
weights = copy.deepcopy(GRID)
path_see = [[0 for _ in range(GRID_WIDTH)]for _ in range(GRID_HEIGHT)]
weights_see = [[0 for _ in range(GRID_WIDTH)]for _ in range(GRID_HEIGHT)]
path = []
start = (0,0)
destination = (GRID_HEIGHT-1,GRID_WIDTH-1,)

################################################
#  WEIGHTS TABLE CALCULATE BY BELOW SUROUTINT  #
#                                              #
#    2       4       7       13      20        #
#                                              #
#    9       12      16      15      19        #
#                                              #
#    11      13      19      17      24        # 
#                                              #
#    19      20      21      21      29        #
#                                              #
#    24      23      22      30      38        #
################################################



for i in range(start[0],destination[0]+1):
	for j in range(start[1],destination[1]+1):
		upper,side = None,None
		if i > 0:
			upper = weights[i-1][j]
			#print("i {0} and u is {1}".format(i,upper))
		if j > 0:
			side = weights[i][j-1]
			#print("j {0} and s is {1}".format(i,side))
		if upper and side:
			ans = min(upper,side)
			weights[i][j] += ans
		else:
			if upper and not side:
				weights[i][j] += weights[i-1][j]
			elif side and not upper:
				weights[i][j] += weights[i][j-1]
			else:
				weights[i][j] += 0
				
#path.append([start,destination])

pos = (destination[0],destination[1])
path.append(pos)

step = 0
		
while True:
	if pos[0] > start[0] and pos[1] > start[1]:
		#print(f"POSITION IS {pos[0]},{pos[1]}")
		step += 1
		side = weights[pos[0]][pos[1]-1]
		upper = weights[pos[0]-1][pos[1]]
		#print(f"{side},{upper}")
		if side < upper:
			new = pos[0],pos[1]-1
			pos = new
		elif upper < side:
			new = pos[0]-1,pos[1]
			pos = new
		else:
			new1 = pos[0]-1,pos[1]
			new2 = pos[0],pos[1]-1
			new = random.choice((new1,new2))
			pos = new	
		path.append(pos)
		
	elif pos[0] == start[0] and pos[1] > start[1]:
		step += 1
		#print(f"POSITION IS {pos[0]},{pos[1]}") 
		#print(f"{weights[pos[0]][pos[1]]}")
		new = pos[0],pos[1]-1
		pos = new
		path.append(pos)

	elif pos[1] == start[1] and pos[0] > start[0]:
		step += 1
		#print(f"POSITION IS {pos[0]},{pos[1]}")
		#print(f"{weights[pos[0]][pos[1]]}")
		new = pos[0]-1,pos[1]
		pos = new
		path.append(pos)
	
	else:
		#print(f"POSITION IS {pos[0]},{pos[1]}")
		break
	
	if pos[0] == start[0] and pos[1] == start[1]:
		#print(f"POSITION IS {pos[0]},{pos[1]}")
		#print(f"{weights[pos[0]][pos[1]]}")
		break

for co in path:
	#print(co)
	path_see[co[0]][co[1]] = 1
	weights_see[co[0]][co[1]] = GRID[co[0]][co[1]]
	
print(f"STEPS {step}")

print_list(path_see)

#########################################################
#    '1' is shortest path from start to destination     #
#                                                       #
#        1       1       1       1       0              #
#                                                       #
#        0       0       0       1       0              #
#                                                       #
#        0       0       0       1       0              #
#                                                       #
#        0       0       0       1       1              #
#                                                       #
#        0       0       0       0       1              #
#                                                       #
#########################################################

#print_list(weights_see)	
print_list(weights)
'''						
print_list(GRID)

print_list(weights_see)
print_list(weights)
'''