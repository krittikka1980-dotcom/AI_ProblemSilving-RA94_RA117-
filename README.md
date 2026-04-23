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

    # 🧩 Sudoku Solver using CSP

## 📌 Problem Description
This project solves a 9x9 Sudoku puzzle using Artificial Intelligence concepts.  
It uses the Constraint Satisfaction Problem (CSP) approach to fill missing values while satisfying all constraints.

---

## ⚙️ Algorithm Used
- Backtracking Algorithm
- Constraint Satisfaction Problem (CSP)

### Constraints:
- Each number must be unique in every row
- Each number must be unique in every column
- Each number must be unique in every 3x3 grid

---

## 🖥️ Features
- Simple Graphical User Interface (GUI)
- User can input Sudoku puzzle
- Automatically solves the puzzle
- Displays result instantly

---

## ▶️ How to Run

1. Install Python (3.x)
2. Run the file:
   ```bash
   python sudoku_solver.py
