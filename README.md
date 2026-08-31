# 🧩 Sudoku Solver

![Prodigy InfoTech](https://img.shields.io/badge/Prodigy-InfoTech-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white)
![Task](https://img.shields.io/badge/Task-04-success?style=for-the-badge)

## 📋 Task Overview

> **PRODIGY_SD_4** — Software Development Internship

A program that solves Sudoku puzzles automatically. It takes an input grid representing an unsolved Sudoku puzzle and uses a backtracking algorithm to explore possible solutions and fill in the missing numbers, following standard Sudoku rules. Once solved, the program displays the completed Sudoku grid.

## ✨ Features

- 🧩 Solves any valid 9x9 Sudoku puzzle
- 🔁 Uses the backtracking algorithm to explore and find solutions
- ⌨️ Accepts custom puzzle input, or run with a built-in sample puzzle
- 🖨️ Displays both the unsolved and solved grids in a readable format
- ✅ Detects and reports if a puzzle has no valid solution

## 🛠️ Technologies Used

- **Python 3**

## 🚀 How to Run

```
python sudoku_solver.py
```

## 💡 Example

```
=== Sudoku Solver ===

Use sample puzzle? (y/n): y

Unsolved Sudoku:
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
---------------------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
---------------------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9

✅ Solved Sudoku:
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

## 📚 What I Learned

- Implementing the backtracking algorithm to solve constraint-based problems
- Validating rules across rows, columns, and 3x3 sub-grids
- Using recursion to explore and undo possible solutions
- Structuring and formatting grid-based console output

## 🎥 Demo


## 🏷️ Tags

`#ProdigyInfoTech` `#SoftwareDevelopment` `#Python` `#Internship`

---

<p align="center">Made with 💙 as part of the Prodigy InfoTech Internship Program</p>
