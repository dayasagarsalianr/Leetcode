from collections import defaultdict

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # Helper function to check if a given coloring pattern for a column is valid
        def is_valid_pattern(pattern: int) -> bool:
            last_color = -1
            for _ in range(m):
                current_color = pattern % 3
                if current_color == last_color:
                    return False
                last_color = current_color
                pattern //= 3
            return True

        # Helper function to check if two adjacent columns' coloring patterns are valid
        def are_adjacent_patterns_valid(first: int, second: int) -> bool:
            for _ in range(m):
                if first % 3 == second % 3:
                    return False
                first, second = first // 3, second // 3
            return True

        # Mod value for the final result to prevent integer overflow
        mod = 10**9 + 7
      
        # The maximum value for a coloring pattern
        max_pattern_value = 3**m
      
        # Set of all valid coloring patterns
        valid_patterns = {i for i in range(max_pattern_value) if is_valid_pattern(i)}
      
        # Dictionary that maps each valid pattern to other patterns which it can be adjacent to
        adjacent_patterns = defaultdict(list)
        for pattern in valid_patterns:
            for adjacent in valid_patterns:
                if are_adjacent_patterns_valid(pattern, adjacent):
                    adjacent_patterns[pattern].append(adjacent)
      
        # List storing the number of ways to color each pattern for a single column
        ways_to_color = [int(pattern in valid_patterns) for pattern in range(max_pattern_value)]
      
        # Iterate over all columns from the second to the last to calculate possible colorings
        for _ in range(n - 1):
            next_column_ways = [0] * max_pattern_value
            # Iterate over each valid pattern
            for pattern in valid_patterns:
                # Add up the ways to color this pattern based on its adjacent patterns from previous column
                for adjacent in adjacent_patterns[pattern]:
                    next_column_ways[pattern] = (next_column_ways[pattern] + ways_to_color[adjacent]) % mod
            ways_to_color = next_column_ways
      
        # Sum all the ways to color the final column
        return sum(ways_to_color) % mod

