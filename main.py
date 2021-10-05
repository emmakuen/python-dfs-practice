def island_perimeter(grid):
    height = len(grid)
    width = len(grid[0])

    def dfs(row, column):
        if row < 0 or row >= height or column < 0 or column >= width or grid[row][column] == 0:
            return 1
        if grid[row][column] == 1:
            grid[row][column] = 2
            return dfs(row - 1, column) + dfs(row + 1, column) + dfs(row, column - 1) + dfs(row, column + 1)
        return 0

    perimeter_count = 0
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 1:
                perimeter_count += dfs(r, c)
    return perimeter_count
