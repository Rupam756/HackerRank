from collections import deque

class Solution:
    def minPushBox(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Find the starting positions
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        # State = (box_row, box_col, player_row, player_col)
        # deque stores (pushes, box_position, player_position)
        dq = deque()
        dq.append((0, box, player))

        visited = set()
        visited.add((box, player))

        while dq:
            pushes, box, player = dq.popleft()

            # Box reached target
            if box == target:
                return pushes

            br, bc = box
            pr, pc = player

            for dr, dc in directions:

                # Position where the player needs to stand
                player_r = br - dr
                player_c = bc - dc

                # Position where the box will be pushed
                new_box_r = br + dr
                new_box_c = bc + dc

                # Check boundaries
                if not (0 <= player_r < m and 0 <= player_c < n):
                    continue

                if not (0 <= new_box_r < m and 0 <= new_box_c < n):
                    continue

                # Both cells must be free
                if grid[player_r][player_c] == '#':
                    continue

                if grid[new_box_r][new_box_c] == '#':
                    continue

                # Check whether player can reach the required position
                if not self.can_reach(
                    grid,
                    player,
                    (player_r, player_c),
                    box
                ):
                    continue

                new_box = (new_box_r, new_box_c)
                new_player = box

                state = (new_box, new_player)

                if state not in visited:
                    visited.add(state)

                    # This is a push, so cost = pushes + 1
                    dq.append((pushes + 1, new_box, new_player))

        return -1

    def can_reach(self, grid, start, target, box):
        """
        Check whether the player can walk from start to target
        without crossing the box.
        """

        m = len(grid)
        n = len(grid[0])

        queue = deque([start])
        visited = {start}

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while queue:
            r, c = queue.popleft()

            if (r, c) == target:
                return True

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if (nr, nc) in visited:
                    continue

                # Cannot walk through walls or the box
                if grid[nr][nc] == '#':
                    continue

                if (nr, nc) == box:
                    continue

                visited.add((nr, nc))
                queue.append((nr, nc))

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna