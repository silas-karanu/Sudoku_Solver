# Sudoku_Solver
 Sudoku Solver project with use of classes and objects to build a Sudoku grid and to solve a Sudoku puzzle.

# Sudoku Solver in Python

This project is a simple Sudoku solver implemented in Python using a backtracking algorithm. It includes a `Board` class that represents the Sudoku puzzle and provides methods for solving and validating the board.

---

## 📂 Files
- `sudoku_solver.py`: Contains the Sudoku solving logic.

---

## 🧠 Features
- Validates rows, columns, and 3x3 squares.
- Uses backtracking to fill in empty cells.
- Prints both the initial and solved Sudoku boards.

---

## 🔧 How It Works

1. **Initialization**
   ```python
   gameboard = Board(puzzle)
   ```
   
2. **Solving**
   ```python
   gameboard.solver()
   ```
   This recursively tries values in empty cells using a backtracking algorithm.
  
3. **Validation**
   Each guess is checked to ensure it's:
   - Not in the same row
     
   - Not in the same column
     
   - Not in the same 3x3 square
     
4. **Display**
The board is printed before and after solving using `__str__ ` method.

---
## 📌 Example Puzzle
```python
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
```
---

## 🚀 How to Run
1. Save the code into a file (e.g., sudoku_solver.py)

2. Run it using:

```bash
python sudoku_solver.py
```
---

## 🔍 Areas for Improvement
- Add a graphical user interface (GUI)

- Include error handling for invalid puzzles

- Allow loading puzzles from files or user input

- Optimize performance for harder puzzles

---

## 📝 License
This project is open-source and free to use.


