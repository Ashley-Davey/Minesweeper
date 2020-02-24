from argparse import ArgumentParser
from random import choice


if __name__ == '__main__':
    #Handle command lone arguments
    parser = ArgumentParser(description="Minesweeper")
    parser.add_argument("--mines", "-m", type=int, default = 8, help = 'Number of mines in grid')
    parser.add_argument("--size", "-s", type=int, default = 8, help = 'Width and height of (square) grid')
    arguments = parser.parse_args()
    size = arguments.size
    mines = arguments.mines
    
    #initialise 2d grid, add mines one by one
    grid = [['' for _ in range(size)] for _ in range(size)]
    spots = range(size**2)
    mine_locations = []
    for _ in range(mines):
        location = choice([i for i in spots if i not in mine_locations])
        i,j = (location // mines, location % mines) #converting to 2d
        grid[i][j] = 'X'
        mine_locations.append(location)
            
    #find adjacent mines to set each grid space
    for i in range(size):
        for j in range(size):
            if grid[i][j] != 'X':
                counter = 0
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        if i + k > -1 and i + k < size and j + l > -1 and j + l < size:
                            counter += grid[i+k][j+l]=='X'
                grid[i][j] = str(counter) 
    
    #output grid using discord 'spoiler' markdown, and code blocks to make the grid look even
    print('Minesweeper! X = mine, number is how many mines are adjacent to the square. Have fun!')             
    for line in grid:
    
        for element in line:
            print('||`' + element + '`||', end = ' ')
        print('')
