class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        island_count = 0

        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                    grid[r][c] == 'W' or (r, c) in visited):
                return
            visited.add((r, c))
            # Explore neighbors (up, down, left, right)
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and (r, c) not in visited:
                    island_count += 1
                    dfs(r, c)

        return island_count

# Example usage:
solution = Solution()

dispatch_1 = [
    ["L","L","L","L","W"],
    ["L","L","W","L","W"],
    ["L","L","W","W","W"],
    ["W","W","W","W","W"],
]

dispatch_2 = [
    ["L","L","W","W","W"],
    ["L","L","W","W","W"],
    ["W","W","L","W","W"],
    ["W","W","W","L","L"],
]

print(solution.getTotalIsles(dispatch_1))  # Output: 1
print(solution.getTotalIsles(dispatch_2))  # Output: 3
