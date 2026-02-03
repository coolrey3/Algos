# Algos 🧮

A collection of **algorithms and data structures** implemented in Python — built as a learning & reference repository.

## What's Inside

### Algorithm Exercises (`CE*.py`)
Practice problems covering core algorithm concepts:
| File | Topic |
|------|-------|
| `CE1.py` | Valid Anagram (frequency counting) |
| `CE2.py` | Count Unique Values (two pointers) |
| `CE10.py` | Power (recursion) |
| `CE11.py` | Factorial (recursion) |
| `CE12.py` | Product of Array (recursion) |
| `CE13.py` | Recursive Range (sum 0..n) |
| `CE24.py` | Linear Search |
| `CE25.py` | Binary Search |

### Sorting Algorithms (`sort_algorithms/`)
- **Bubble Sort** — ascending & descending with swap tracking
- **Selection Sort** — find minimum, place at front
- **Insertion Sort** — insert into sorted portion
- **Merge Sort** — divide & conquer with merge step

### Search Algorithms (`search_algorithms/`)
- **Linear Search** — O(n) sequential scan

### String Manipulation (`string_manipulation/`)
- **Count Vowels** — count vowels in a string
- **Reverse String** — reverse using stack-like pop

### Data Structures (`data_structures/`)

#### Hand-built from scratch (`handmade/`)
- **Array** — wrapper with insert, insertAt, removeAt
- **Linked List** — node-based with traversal
- **Binary Tree** — with left/right child traversal
- **Trie** — prefix tree with word marking

#### Full implementations (`*.py`)
- **Singly Linked List** — push, pop, shift, unshift, get, set, insert, remove, reverse
- **Doubly Linked List** — bidirectional linked list
- **Stack** — LIFO with push/pop
- **Queue** — FIFO with enqueue/dequeue
- **Binary Search Tree** — BST operations
- **Graph** — adjacency list with DFS (recursive + iterative) and BFS
- **Weighted Graph** — graph with edge weights
- **Heap / Priority Queue** — heap-based priority queue
- **HashMap** — hash map practice
- **Fibonacci** — memoized (top-down) and bottom-up dynamic programming

## Setup

```bash
# Clone
git clone https://github.com/coolrey3/Algos.git
cd Algos

# Install dev dependencies (for testing & linting)
pip install -r requirements-dev.txt
```

## Running Tests

```bash
# Run all tests
pytest -v

# Run specific test file
pytest tests/test_algorithms.py -v

# Run with short traceback
pytest -v --tb=short
```

## Linting & Formatting

```bash
# Check for issues
ruff check .

# Auto-fix what's possible
ruff check --fix .

# Format code
ruff format .
```

### Pre-commit Hooks (Optional)

Set up automatic linting on every commit:

```bash
# Install pre-commit
pip install pre-commit

# Install the git hooks
pre-commit install

# Now every commit will auto-lint!
```

## CI/CD

GitHub Actions runs automatically on push/PR to `main`:
- **Lint** — ruff check + format verification (Python 3.12)
- **Test** — pytest with coverage across Python 3.9, 3.10, 3.11, 3.12, 3.13

## Project Structure

```
Algos/
├── CE*.py                    # Algorithm exercises
├── main.py                   # Import playground
├── sort_algorithms/          # Sorting implementations
├── search_algorithms/        # Search implementations
├── string_manipulation/      # String utilities
├── data_structures/
│   ├── handmade/             # Built from scratch
│   ├── methods/              # Using Python libraries
│   ├── SLL_practice.py       # Singly Linked List
│   ├── Stack_practice.py     # Stack
│   ├── Queue_practice.py     # Queue
│   ├── Graph_practice.py     # Graph (DFS/BFS)
│   └── ...                   # BST, Heap, HashMap, etc.
├── tests/                    # Test suite
├── .github/workflows/ci.yml  # CI/CD pipeline
├── pyproject.toml            # Project config (pytest, ruff)
└── requirements-dev.txt      # Dev dependencies
```

## License

Personal learning repository.
