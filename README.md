#  Maze Solver using AI Search Algorithms

##  Project Overview

This project is a Python-based Maze Solver that demonstrates core concepts of Artificial Intelligence using search algorithms. The system generates a random maze based on selected difficulty and solves it using different AI techniques.
It also compares the performance of each algorithm based on execution time and number of steps taken to reach the goal.

---

##  Features

*  Multiple AI Algorithms:

   * Breadth First Search (BFS)
   * Depth First Search (DFS)
   * Best First Search (Greedy)
   * A* Algorithm

*  Random Maze Generation

*  Difficulty Levels (Easy / Medium / Hard)

*  Colored Maze Output (Different color per algorithm)

*  Performance Comparison Chart

* User-based Algorithm Selection

*  Guaranteed Solvable Maze


##  Algorithms Explanation

###  BFS (Breadth First Search)

* Explores level by level
* Guarantees shortest path

###  DFS (Depth First Search)

* Explores deeply first
* Does not guarantee shortest path

###  Best First Search

* Uses heuristic (distance to goal)
* Faster but not always optimal

###  A* Algorithm

* Combines path cost and heuristic
* Most efficient and optimal in most cases

##  Project Structure

maze_solverusing ai search algorithms/
│── main.py
│── maze.py
│── bfs.py
│── dfs.py
│── best_first.py
│── astar.py
│── utils.py
│── README.md


##  How to Run

1. Open terminal in project folder
2. Run:
     python main.py
3. Select difficulty:
    - Easy
    - Medium
    - Hard
4. Select algorithm:
    - BFS
    - DFS
    - Best First Search
    - A*
    - All
    

##  How It Works

1. User selects difficulty level
2. Random maze is generated
3. System ensures maze is solvable
4. User selects algorithm(s)
5. Selected algorithms solve the maze
6. Colored paths are displayed
7. Comparison chart is generated



##  Color Legend

| Element     | Color      |
| ----------- | ---------- |
| Start (S)   | 🟢 Green   |
| End (E)     | 🔴 Red     |
| BFS Path    | 🟡 Yellow  |
| DFS Path    | 🔵 Blue    |
| BestFS Path | 🔷 Cyan    |
| A* Path     | 🟣 Magenta |
| Walls (#)   | ⚫ Grey     |
| Empty Cells | ⚪ White    |



##  Key Highlights

* BFS guarantees shortest path
* A* provides optimal and efficient solution
* DFS may explore unnecessary paths
* Best First is faster but not always accurate
* Visual comparison using colored outputs


##  Learning Outcomes

* Understanding AI search algorithms
* Difference between informed and uninformed search
* Performance comparison techniques
* Problem-solving using Python


##  Future Improvements

*  Step-by-step maze solving animation
*  Graphical performance charts
*  GUI using Tkinter


##  Author

NAME: Anshika Agnihotri
COURSE: BTECH (First Year)
PROGARM: CSE(AI/ML)
SUBJECT: Fundamentals of AI/ML


##  Acknowledgment

This project demonstrates how search algorithms can be applied to solve real world problems such as Pathfinding, while also providing an interactive and visual learning experience.
This project is developed for academic learning in Artificial Intelligence and Python programming.
