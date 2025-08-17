# Object-Oriented Card Game Engine: A Study in Data Structures and Algorithms

## Project Overview

This project is a command-line based card game to simulate UNO, **"Card-Clash-Color-Chaos,"** developed to apply and demonstrate core computer science principles. It's a turn-based strategy game where 2-4 players compete to be the first to empty their hands of cards. Players achieve this by matching the color or value of the card on top of the discard pile. The game is complicated by "Clash" cards, which introduce special actions like reversing the turn order, skipping a player, or forcing an opponent to draw additional cards.

The primary goal was not just to create a game, but to architect a robust and extensible software solution using **Object-Oriented Programming (OOP)** principles as well as applying **Abstract Data Structures and Algorithms**. The entire game logic, from shuffling the deck to validating player moves, is built upon a foundation of fundamental data structures and algorithms, showcasing the practical application of theoretical computer science concepts.


The application is architected around a clear separation of concerns, with distinct classes managing different aspects of the game:
* `Card`: A base class for all cards, with subclasses for `ValueCard` and `ActionCard`.
* `Deck`: Manages the collection of cards, including shuffling and dealing.
* `Player`: Encapsulates a player's state, including their hand and associated actions.
* `GameManager`: The central engine that controls the game flow, enforces rules, and manages the overall game state.

---

## Skills and Technologies Demonstrated

This project is a deep dive into the practical implementation of key software development concepts.

#### **Programming Language: Python**
The project is written entirely in **Python**. It leverages core language features such as f-strings for formatted output, list comprehensions for concise data manipulation, and the standard library (`random` for shuffling, `collections.deque` for efficient turn management).

#### **Object-Oriented Programming (OOP)**
A key focus of this project was a deep and practical application of OOP principles to create a modular and maintainable codebase.
* **Encapsulation:** Each class bundles its data (attributes) and the methods that operate on that data. For example, the `Player` class holds a list of `Card` objects for its hand, and only `Player` methods can directly add or remove cards from it, preventing illegal game moves.
* **Inheritance:** A `Card` base class defines common properties (e.g., color). `ValueCard` and `ActionCard` then inherit from `Card` and add their own specific attributes and behaviors. This reduces code duplication and creates a logical hierarchy.
* **Polymorphism:** The `GameManager` can treat all card types uniformly through the base `Card` interface. When a card is played, the manager calls a generic `play_effect()` method, which behaves differently depending on whether the object is a `ValueCard` (no effect) or a specific `ActionCard` (e.g., a "Reverse" card reverses the turn order queue).

#### **Data Structures**
The choice of data structure was critical for performance and logical correctness.
* **Lists/Arrays:** A player's hand is stored as a **List**, as it allows for efficient iteration and the easy removal/addition of cards from any position.
* **Stacks (LIFO):** The discard pile is implemented as a **Stack** (using a Python list's `append()` and `pop()` methods). This is a natural fit, as the most recently discarded card is the one that subsequent players need to match (Last-In, First-Out).
* **Queues (FIFO):** The order of player turns is managed with a **Queue**. This ensures that play proceeds in a fair, cyclical fashion (First-In, First-Out). When a "Reverse" card is played, the queue is efficiently reversed.

#### **Algorithms**
Core game mechanics are driven by classic algorithms.
* **Shuffling:** The main deck is randomized at the start of each game using the **Fisher-Yates shuffle** algorithm (as implemented in Python's `random.shuffle`) to ensure a fair and unpredictable card distribution.
* **Game State Machine:** The main game loop is designed as a **finite state machine**, transitioning between states like `START_GAME`, `PLAYER_TURN`, `EVALUATE_MOVE`, `CHECK_WIN_CONDITION`, and `END_GAME`. This creates a predictable and robust flow of control.

---

## Learning Outcomes

This project was a significant learning experience that bridged the gap between theory and practice.

* **Algorithmic Problem-Solving:** I encountered and solved non-trivial logical problems. For instance, implementing the logic for a "Wild Draw Four" card required checking the player's hand for valid alternative moves, a constraint that added significant algorithmic complexity. I solved this by creating a helper function that temporarily searched the player's hand before validating the move.

* **Abstract to Concrete Design:** I translated abstract requirements ("build a card game") into a concrete software design. This involved mapping game entities to classes, defining their relationships, and modeling the game's rules as methods and conditional logic. This process greatly improved my ability to architect software from the ground up.

* **The Importance of Code Quality:** To ensure the project was robust, I focused on writing high-quality code. I adhered to Python's **PEP 8 style guide**, wrote clear **docstrings** for every class and method, and manually created a suite of **unit tests** to verify the logic of individual components, such as ensuring the deck had the correct number of cards after dealing. This taught me that disciplined coding practices are essential for building reliable software.

---

## Game Overview
The card game involves multiple players and a deck of cards. The objective is to be the first player to get rid of all your cards. Each card has a color and a label, and there are special black cards with unique abilities.

## Important Restrictions and Assumptions
- You cannot use any built-in data structures (including tuples!) or algorithms from any libraries, except the ones we give you in the scaffold (and no, you cannot modify the code for these ones either). 
- This means that the use of Python in-built lists, dictionaries, tuples, and sets (among other built-in data structures) is forbidden. In addition to this, ArrayR is also prohibited.
- You cannot use any built-in sorting algorithms. You must use one of the sorting algorithms given to you in the scaffold OR use a data structure that facilitates sorting algorithms.
- You cannot change the import statements in the Python files. Please do not ask if you can use any external libraries on Ed, as the answer will always be no.
- You cannot use generative AI, machine learning, or any other form of AI software.
- You cannot use any hard-coded constant numbers. Please use the numbers provided in config.py.
- You cannot access the internals of ANY data structures or any classes except the custom classes that you edit in the tasks. You can only access the methods of the data structures that are provided to you in the scaffold. Each use of the internals of a data structure will count as a major mistake and will lose at least half of the marks for the task.
- The submitted program will be tested using Python version 3.10.0 or later.
