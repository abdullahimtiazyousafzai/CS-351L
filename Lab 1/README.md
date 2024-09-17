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
   - Implement the Number Guessing Game using an algorithm of your choice. The chosen algorithm in this solution is **Simulated Annealing**, a probabilistic technique for approximating the global optimum of a function. This algorithm introduces randomness in exploration and decreases this randomness over time, mimicking the cooling process of metal annealing.

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

#### 5. Custom Algorithm: Simulated Annealing
The custom algorithm implemented in this solution is **Simulated Annealing**. In this algorithm:
   - The AI begins with a random guess and uses a probabilistic approach to either stay with the current guess or explore a new guess.
   - As the "temperature" decreases, the AI becomes less likely to make large jumps, focusing on smaller adjustments as it converges on the correct number.
   - This mimics how metals cool and anneal, making this an interesting and effective algorithm for global search problems.

Each algorithm implementation prints the number of attempts it took to guess the correct number, providing an insight into the efficiency and effectiveness of each approach.
