# CS 351L - Artificial Intelligence Lab

## Lab 1: Introduction to Python and AI Development Environment

**Course**: CS 351L - Artificial Intelligence Lab  
**Instructor**: Mr. Usama Arshad, PhD CS  
**Program**: BS Cybersecurity  
**Semester**: 5th  
**Assigned Date**: 4th September 2024  
**Submission Deadline**: 10th September 2024

---

## Lab Overview

In this lab, we explore different algorithms by implementing a Number Guessing Game using both non-AI and AI-based approaches. Below are the key tasks and objectives for this lab:

### Task Breakdown:

1. **Non-AI Version**:
   - Implement a Number Guessing Game where the player guesses a randomly generated number. This serves as a baseline for further comparisons.
   
2. **AI Version with Binary Search**:
   - Implement a version where the computer guesses the player's number using the Binary Search algorithm, showcasing an efficient guessing strategy.

3. **Breadth-First Search (BFS) Version**:
   - Implement a version of the game where the computer guesses the number using the BFS algorithm, systematically exploring the range of numbers.

4. **Depth-First Search (DFS) Version**:
   - Implement a version where the computer guesses the number using the DFS algorithm, focusing on a more aggressive approach in terms of depth-first exploration.

5. **Custom Algorithm**:
   - Implement the Number Guessing Game using an algorithm of your choice. The chosen algorithm in this solution is **Ternary Search**, which is an extension of Binary Search that divides the search space into three parts instead of two.

### Code Structure and Implementation:

The `.ipynb` file contains modular code, with each algorithm implemented as a function to ensure clean separation of logic. Below is an explanation of the approach for each task:

#### 1. Non-AI Version: Player vs Computer
In the non-AI version, the game generates a random number, and the player tries to guess it. For each guess, the program gives feedback whether the guess was too high, too low, or correct.

#### 2. AI Version: Binary Search (Computer vs Player)
In this version, the computer employs the **Binary Search** algorithm to guess the number. The search space is repeatedly halved based on whether the number is too high or too low, making this approach efficient with a logarithmic time complexity \( O(\log n) \).

#### 3. Breadth-First Search (BFS) Version
In the BFS-based version, the game explores all possible numbers level by level. Although BFS ensures completeness, it is less efficient than Binary Search because it exhaustively checks every number in sequence, resulting in a linear time complexity \( O(n) \).

#### 4. Depth-First Search (DFS) Version
For the DFS-based version, the game explores numbers more aggressively by following a depth-based approach. However, this can lead to inefficient guessing patterns, with higher chances of overshooting the correct number, though it can be beneficial for certain search spaces.

#### 5. Custom Algorithm: Ternary Search
The custom algorithm implemented in this solution is **Ternary Search**. In this algorithm:
   - The AI divides the search range into three parts by selecting two midpoints: one at one-third of the range and the other at two-thirds.
   - Based on whether the target number is smaller, larger, or between these midpoints, the algorithm eliminates two-thirds of the search space in each step.
   - This leads to a faster narrowing of the possible numbers compared to linear or binary search approaches.
   - Ternary Search improves efficiency by reducing the search space more quickly, making it especially useful in situations where the range is large and multiple comparisons are beneficial.

Each algorithm implementation prints the number of attempts it took to guess the correct number, providing an insight into the efficiency and effectiveness of each approach.
