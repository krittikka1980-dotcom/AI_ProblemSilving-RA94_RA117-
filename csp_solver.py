def is_valid(region, color, assignment, neighbors):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def backtrack(assignment, regions, neighbors, colors):
    if len(assignment) == len(regions):
        return assignment

    # Select unassigned region
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(region, color, assignment, neighbors):
            assignment[region] = color

            result = backtrack(assignment, regions, neighbors, colors)
            if result:
                return result

            # Backtrack
            del assignment[region]

    return None


def solve_map_coloring(regions, neighbors, colors):
    return backtrack({}, regions, neighbors, colors)