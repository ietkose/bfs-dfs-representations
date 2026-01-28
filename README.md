# Graph Traversal Algorithms (BFS & DFS)

This project implements two fundamental graph traversal algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** in Python. 

The program utilizes an **Adjacency List** to represent the graph and allows users to input custom values for each node dynamically.

## Graph Topology

The algorithms run on the following hardcoded graph structure:

```text
         0.
       /    \
      1.  —  2.
     /  \   /  
    4. —  3. — 5.
    |  \  |  /
    7.    6.
    
## Features 

* **Breadth-First Search (BFS)**: Implemented iteratively using a Queue data structure.

* **Depth-First Search (DFS)**: Implemented recursively.

* **Interactive Input**: Users can assign integer values or names to the 8 nodes defined in the topology.

Visualization: Displays the traversal path clearly (e.g., A -> B -> C).

## Installation & Usage

Clone the repository:

```Bash
git clone https://github.com/ietkose/bfs-dfs-representations.git
```

Run the script:

```Bash
python bfs_dfs.py
Input Data: The program will ask you to enter 8 integers (or strings) to label the nodes from 0 to 7.
```

## Example Output

Enter an integer number: A
... (input for 8 nodes) ...

Start Node: A
-------------------------------------
Breadth-First Search (BFS) Result:
A -> B -> C -> E -> D -> F -> H -> G
-------------------------------------
Depth-First Search (DFS) Result:
A -> B -> E -> D -> C -> F -> G -> H
*************************************

## Tech Stack

Language: Python 3.x
Concepts: Graph Theory, Recursion, Queue, Adjacency List.