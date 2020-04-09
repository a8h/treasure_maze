def findTreasure(maze):
    # Use a BFS, that way we can also determine the minimum number of steps to find the treasure
    # DFS would probably be faster as far as determining whether the treasure can be gotten. Maybe?
    start = (0,0)
    if maze[0][0] == 9:
        return True, 0
    from collections import deque
    queue = deque()
    queue.append((start, 0))
    visited = set()
    while queue:
        start, curr_depth = queue.popleft() 
        curr_row, curr_col = start 
        visited.add(start)
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for direction in directions:
            nei_row = curr_row + direction[0]
            nei_col = curr_col + direction[1]
            if 0 <= nei_row < len(maze) and 0 <= nei_col < len(maze[0]):
                if (nei_row, nei_col) not in visited:
                    if maze[nei_row][nei_col] == 1:
                        queue.append(((nei_row, nei_col), curr_depth + 1))
                    elif maze[nei_row][nei_col] == 9:
                        return True, curr_depth + 1
    return False, 0

def generateMaze():
    from random import SystemRandom
    sr = SystemRandom()
    maze_size = 8
    maze = [[sr.randrange(0,2) for _ in range(maze_size)] for _ in range(maze_size)]
    maze[0][0] = 1
    maze[sr.randrange(0, maze_size)][sr.randrange(0, maze_size)] = 9
    return maze

count = 0
num_tries = 100000
total_depth = 0
for _ in range(num_tries):
    maze2 = generateMaze()
    found_treasure, depth = findTreasure(maze2)
    if found_treasure:
        count += 1
        total_depth += depth

print('A pirate tries to find the treasure in a 8 x 8 randomly generated maze')
print('The pirate starts at the top left')
print('After {} tries, the pirate found the treasure {} times (rate = {})'.format(num_tries, count, count / num_tries))
if count > 0:
    print('The average number of steps the pirate had to take to find the treasure was {}'.format(total_depth / count))
print((count / num_tries))
