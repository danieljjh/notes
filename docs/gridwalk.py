# code utf8


import numpy as np

def initGrid():
    state = np.zeros((3,5,5))
    stats = []
    for i in range(3):
        for j in range(5):
            s1 = [1]*5
    #place red
    r = 8
    b = 8
    while r >0:
        s = randPair(0,5)
        if state[0][s] == 0:
            state[0][s] = 1
            r = r -1            
    #place blue 
    while b >0:
        s1 = randPair(0,5)
        if state[1][s1] == 0:
            state[1][s1] = -1
            b = b -1
#             print b, s1, state[0][s1], state[1][s1]
    state[2][0,0] = 9
    return state
    

def randPair(s,e):
    return np.random.randint(s,e), np.random.randint(s,e)

def dispGrid(state):
    '''
        print grid together
    '''
    grid = np.zeros((5,5), dtype='<U2')
    for i in range(0,5):
        for j in range(0,5):
            if state[2][i,j] ==9:
                grid[i,j] = 'V'
            elif state[2][i,j] == 4:
                 grid[i,j] = 'X'                
            elif state[0][i,j] == 1 and state[1][i,j] ==0:
                grid[i,j] = 'R'
            elif state[1][i,j] == -1 and state[2][i,j] ==0:
                 grid[i,j] = 'B'
            else:
                 grid[i,j] = ''
    return grid

def findLoc(state, obj):
    for i in range(0,5):
        for j in range(0,5):
            if (state[i,j] == obj):
                return [i,j]
            
def findAllLoc(state, obj):
    res = []
    for i in range(0,5):
        for j in range(0,5):
            if (state[i,j] == obj).all():
                res.append([i,j]) 
    return res
            

def makeMove(state, action):
    #need to locate player in grid
    #need to determine what object (if any) is in the new grid spot the player is moving to
    player_loc = findLoc(state[2], 9)
    print 'makeMove ..action', action, 'player_loc', player_loc
    goal = findLoc(state[0], 1)
    
#     actions = [[-1,0],[1,0],[0,-1],[0,1]]
    #e.g. up => (player row - 1, player column + 0)
    new_loc = (player_loc[0] + action[0], player_loc[1] + action[1])
    if ((np.array(new_loc) <= (4,4)).all() and (np.array(new_loc) >= (0,0)).all()):
            state[2][player_loc] = 4
            state[2][new_loc] = 9
    new_player_loc = findLoc(state[2], 9)
    state[0][new_loc] = 0
    print 'new_player_loc', new_player_loc
    return state, new_player_loc



def go_through(state):
    step = 0
    while np.sum(state[0]):
        print 'step: ', step+1

        print state[0]
        print '-'*10
#         #: V goes to [0, 0]
        obj = 9
        current_v = np.array(findLoc(state[2], 9))
        print 'current status'
        print state[2]
        
        print 'vcurrent position..', current_v
        print '*'*15
        R = np.array(findAllLoc(state[0], 1))
        #: next point
#         print 'Red..'
#         print R
        closest = closest_node(current_v, R)
        next_point = R[closest]
        next_direction = next_point - current_v
        print 'Closest Red', next_point,'target:', next_direction
        
        acts = go_to_nxt(next_direction)
        for s in acts:
            print 'action', s
            state, v_loc = makeMove(state, s) 
        step = step + 1
        print '-'*20
#     if np.sum(state[0]) == 0:
    print '.....Done, total: ', step
    print state[2]
    print 'Final Vehicle: ', v_loc
    ff = np.array(v_loc)
    print 'go out path', np.abs(ff-3)
    

    
    
def closest_node(node, nodes):
    print 'V', node
#     for x in range(len(nodes)):
#         print x, 'R.. ', nodes[x], 'node ', node, 'dist  ',  np.abs(nodes[x] - node)
    dist_2 = np.sum(np.abs(nodes - node), axis=1)
#     print 'dist_2', dist_2
    return np.argmin(dist_2)

def go_to_nxt(target):
    t = list(target)
    dd = []
    if t == [0, 0]:
        dd.append([0, 0])
    if t[0] > 0:
        for x in range(t[0]):
            dd.append([1, 0])
    else:
        for x in range(-t[0]):
            dd.append([-1, 0])
    if t[1] > 0:
        for x in range(t[1]):
            dd.append([0, 1])
    else:
        for x in range(-t[1]):
            dd.append([0, -1])
    return dd

if __name__ == '__main__':
    
    init_state =  initGrid()
    go_through(init_state)
        
