# Graph Traversal Algorithms (BFS & DFS)

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Computer Science](https://img.shields.io/badge/CS-Data_Structures_%26_Algorithms-red?style=for-the-badge)](https://en.wikipedia.org/wiki/Graph_traversal)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

**[Visit Project Repository / Proje Deposu](https://github.com/ietkose/bfs-dfs-representations)**

.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖

## 🇬🇧 ENGLISH

A Python implementation of two fundamental graph traversal algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. The project models a non-linear network using an **Adjacency List** representation and allows dynamic user-input for custom node values.

---

### 🕸️ Graph Topology
The algorithms operate on the following interconnected network topology:

```text
         0
       /   \
      1 --- 2
     / \   /  
    4 - 3 - 5
    | \ | /
    7   6
```

### 🕸️ Key Features
* **Breadth-First Search (BFS):** Level-order traversal implemented iteratively using a FIFO Queue (collections.deque).
* **Depth-First Search (DFS):** Deep-path traversal implemented recursively leveraging the call stack.
* **Adjacency List Representation:** Memory-efficient graph modeling using dictionary-based adjacency lists.
* **Interactive Node Labeling:** Allows users to dynamically map custom strings or integer values to nodes 0 through 7.
* **Path Visualization:** Outputs clear step-by-step traversal results (e.g., A -> B -> C).

### 🕸️ Tech Stack & Concepts
* **Language:** Python 3.x
* **Core Concepts:** Graph Theory, Data Structures, Queue (FIFO), Recursion, Adjacency List

### 🕸️ Installation & Usage
1. Clone the Repository
```bash
git clone [https://github.com/ietkose/bfs-dfs-representations.git](https://github.com/ietkose/bfs-dfs-representations.git)
cd bfs-dfs-representations
```

2. Run the Script
```bash
python bfs_dfs.py
```

### 🕸️ Example Output
```text
Plaintext
Enter value for node 0: A
Enter value for node 1: B
... (Input for 8 nodes) ...
```
```text
Start Node: A
-------------------------------------
Breadth-First Search (BFS) Result:
A -> B -> C -> E -> D -> F -> H -> G
-------------------------------------
Depth-First Search (DFS) Result:
A -> B -> E -> D -> C -> F -> G -> H
*************************************
```

### 🕸️ License 
This project is licensed under the MIT License.

.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖.✦ ݁˖

## 🇹🇷 TÜRKÇE
Temel grafik tarama algoritmaları olan Genişlik Öncelikli Arama (BFS) ve Derinlik Öncelikli Arama (DFS) yöntemlerinin Python ile yazılmış uygulaması. Proje, doğrusal olmayan grafik yapısını Komşuluk Listesi (Adjacency List) verimliğiyle modeller ve kullanıcının düğümlere dinamik değer atamasına olanak tanır.

### 🕸️ Grafik Topolojisi
Algoritmalar aşağıdaki bağlı grafik topolojisi üzerinde çalışmaktadır:

```text
Plaintext
         0
       /   \
      1 --- 2
     / \   /  
    4 - 3 - 5
    | \ | /
    7   6
```

### 🕸️ Öne Çıkan Özellikler
* **Genişlik Öncelikli Arama (BFS):** Kuyruk (Queue - FIFO) veri yapısı kullanılarak yinelemeli (iterative) mantıkla yazılmıştır.
* **Derinlik Öncelikli Arama (DFS):** Özyinelemeli (recursive) yapı kullanılarak derinlemesine tarama gerçekleştirir.
* **Komşuluk Listesi Mimarisi:** Bellek verimliliği sağlayan sözlük tabanlı grafik modellemesi.
* **Dinamik Düğüm Etiketleme:** Kullanıcının 0 ile 7 arasındaki düğümlere özel metin veya sayı değerleri atamasına imkan tanır.
* **Adım Adım Yol Görselleştirme:** Tarama sırasını net bir şekilde ekrana basar (Örn: A -> B -> C).

### 🕸️ Kullanılan Teknolojiler ve Kavramlar
* **Dil:** Python 3.x
* **Temel Kavramlar:** Grafik Teorisi (Graph Theory), Veri Yapıları, Kuyruk (Queue), Özyineleme (Recursion), Komşuluk Listesi

### 🕸️ Kurulum ve Çalıştırma
1. Depoyu Klonlayın
```bash
git clone [https://github.com/ietkose/bfs-dfs-representations.git](https://github.com/ietkose/bfs-dfs-representations.git)
cd bfs-dfs-representations
```

3. Programı Çalıştırın
```bash
python bfs_dfs.py
```

### 🕸️ Örnek Çıktı
```text
Plaintext
0. Düğüm için değer giriniz: A
1. Düğüm için değer giriniz: B
... (8 düğüm için de değer girilir) ...
```
```text
Başlangıç Düğümü: A
-------------------------------------
Breadth-First Search (BFS) Sonucu:
A -> B -> C -> E -> D -> F -> H -> G
-------------------------------------
Depth-First Search (DFS) Sonucu:
A -> B -> E -> D -> C -> F -> G -> H
*************************************
```

### 🕸️ Lisans
Bu proje MIT lisansı altında lisanslanmıştır.
