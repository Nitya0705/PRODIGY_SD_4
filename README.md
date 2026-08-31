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
Puzzle to solve:

. . . | 2 6 . | 7 . 1 
6 8 . | . 7 . | . 9 . 
1 9 . | . . 4 | 5 . . 
---------------------
8 2 . | 1 . . | . 4 . 
. . 4 | 6 . 2 | 9 . . 
. 5 . | . . 3 | . 2 8 
---------------------
. . 9 | 3 . . | . 7 4 
. 4 . | . 5 . | . 3 6 
7 . 3 | . 1 8 | . . . 

Solved Sudoku:

4 3 5 | 2 6 9 | 7 8 1 
6 8 2 | 5 7 1 | 4 9 3 
1 9 7 | 8 3 4 | 5 6 2 
---------------------
8 2 6 | 1 9 5 | 3 4 7 
3 7 4 | 6 8 2 | 9 1 5 
9 5 1 | 7 4 3 | 6 2 8 
---------------------
5 1 9 | 3 2 6 | 8 7 4 
2 4 8 | 9 5 7 | 1 3 6 
7 6 3 | 4 1 8 | 2 5 9
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
