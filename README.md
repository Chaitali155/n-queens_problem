# **Solving the N-Queens Problem with Exhaustive Search and Genetic Algorithms**

## **Overview**
This project implements two approaches to solve the N-Queens problem: 
1. **Exhaustive Search** using Depth-First Search (DFS) with backtracking.
2. **Genetic Algorithm (GA)** based on evolutionary principles.

The implementations are tested for \( N = 10, 50, 100 \) to compare their computational efficiency, scalability, and performance.

---

## **Features**
- **Exhaustive Search**:
  - Employs DFS with backtracking to explore all possible solutions.
  - Supports timeout handling for large \( N \) values.
- **Genetic Algorithm**:
  - Generates solutions using selection, crossover, and mutation operations.
  - Adjustable parameters for population size, mutation rate, and generations.
  - Includes timeout handling for performance management.
- Performance comparison and results analysis.

---

## **File Structure**
- `n-queens.py`  
  Implements the DFS-based exhaustive search for solving the N-Queens problem.

- `n-queens2.py`  
  Implements the Genetic Algorithm approach for solving the N-Queens problem.

- `README.md`  
  This documentation file.

- `mqueens_problem.pdf`  
  Detailed project report created using Overleaf, covering the design, implementation, results, and analysis.

---

## **How to Run**
### **Requirements**
- Python 3.7 or higher
- Required libraries (install via `pip`):
  ```bash
  pip install numpy
