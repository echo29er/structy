# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a data structures and algorithms practice repository containing Python implementations organized into progressive learning modules. The codebase follows the Structy.net curriculum structure.

## Project Structure

The repository is organized into 6 main modules in order of progression:
- **01_arrays_and_strings/**: Fundamental array and string manipulation problems
- **02_recursion/**: Recursive problem-solving techniques
- **03_linked_lists/**: Linked list data structure implementations
- **04_binary_trees/**: Binary tree algorithms and traversals
- **05_graphs/**: Graph algorithms including DFS, BFS, and shortest path
- **06_new_format/**: Latest problems with enhanced documentation format

## Development Commands

Individual Python files can be executed directly:
```bash
python 01_arrays_and_strings/20220511_uncompress.py
python 05_graphs/20220813_island_count.py
```

For the graphs module, there's a test runner utility:
```bash
python 05_graphs/utils/test_runner.py
```

## Code Architecture

### Problem File Structure
Each problem file follows this consistent pattern:
1. Comprehensive docstring with problem description, examples, and complexity analysis
2. Data structure definitions (e.g., Node classes) when needed
3. Main solution function with detailed comments
4. Alternative implementations (often both iterative and recursive)
5. Test cases at the bottom with `if __name__ == "__main__":` block

### Naming Convention
Files use date-based naming: `YYYYMMDD_problem_name.py`

### Code Style
- Type hints are used throughout
- Functions include detailed docstrings with time/space complexity
- Comments explain algorithmic reasoning
- ASCII art visualizations for complex data structures
- Multiple implementation approaches are provided

### Common Patterns
- Node classes are consistently defined across modules
- Graph problems use adjacency list representations
- Tree problems include both recursive and iterative solutions
- All solutions include comprehensive test cases

## Key Implementation Details

### Data Structure Definitions
Standard Node class used across modules:
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None  # for linked lists
        self.left = None  # for binary trees
        self.right = None # for binary trees
```

### Testing Approach
- Each file includes multiple test cases
- Edge cases are explicitly tested
- Expected outputs are clearly documented
- Test cases can be run by executing the file directly

### Algorithm Categories
The repository covers standard interview topics:
- Two-pointer techniques
- Sliding window
- Dynamic programming
- Tree traversals (DFS, BFS)
- Graph algorithms (connected components, shortest path)
- Recursion and backtracking