from csp_solver import solve_map_coloring

regions = ['A', 'B', 'C', 'D']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

solution = solve_map_coloring(regions, neighbors, colors)

print("\nColor Assignment:")
for region, color in solution.items():
    print(f"{region} → {color}")