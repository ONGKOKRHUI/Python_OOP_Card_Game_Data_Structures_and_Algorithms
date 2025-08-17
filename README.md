----

# **Python-Based Card Game Engine: An Algorithmic Implementation with Custom Data Structures**

## **Project Overview** 🃏

This project is a complete, from-scratch implementation of the classic card game **UNO** in Python. The primary focus was not just on creating a playable game, but on building the entire engine using custom-built **Abstract Data Types (ADTs)**. Every aspect of the game, from managing player turns to handling the card deck, was designed to utilize the most appropriate data structures for maximum efficiency.

This endeavor demonstrates a strong practical understanding of object-oriented programming, data structure design, and algorithmic complexity analysis.

-----

## **Key Features**

  * **Full Game Logic:** Implements all the standard rules of UNO, including special cards like Skip, Reverse, Draw Two, Wild, and Wild Draw Four.
  * **Object-Oriented Design:** The game is logically structured into distinct classes (`Game`, `Player`, `GameBoard`, `Card`), making the code modular, readable, and scalable.
  * **Custom Data Structures:** The core of the project is built upon custom ADTs like `CircularQueue`, `ArrayStack`, and `ArrayList`, rather than relying on Python's built-in data types.
  * **Complexity Analysis:** Every method includes detailed **Big O notation** for best and worst-case time complexity, showcasing a deep understanding of algorithm efficiency.

-----

## **Skills & Concepts Demonstrated**

This project was a deep dive into the practical application of computer science fundamentals.

### **1. Abstract Data Types (ADTs) & Data Structure Design**

I implemented and utilized several key data structures, choosing each one for its specific advantages in the context of the game's logic:

  * **CircularQueue:** Used to manage the sequence of player turns. This was the ideal choice as it naturally handles the round-robin nature of the game, efficiently serving the current player and appending them to the back of the queue for their next turn.
  * **ArrayStack (LIFO):**
      * Implemented for the **draw pile**, perfectly modeling the "Last-In, First-Out" behavior of drawing the top card from a deck.
      * Cleverly used within the `reverse_players` method. By popping all players from the `CircularQueue` onto the `ArrayStack` and then pushing them back, the player order is efficiently reversed.
  * **ArrayList:** Served as the foundation for a player's **hand** and the **discard pile**. Its dynamic resizing capability and direct index access were essential for adding, removing, and iterating through cards.

### **2. Algorithmic Thinking & Problem Solving**

Beyond data structures, this project showcases the ability to design and implement algorithms for complex game logic:

  * **Game Flow Management:** The main `play_game` loop is the heart of the engine, controlling the state of the game, handling player inputs, validating moves, and checking for a win condition.
  * **Card-Specific Logic:** I designed specific methods to handle the unique behavior of each action card:
      * `reverse_players()`: Reverses the game's turn order.
      * `skip_next_player()`: Manipulates the player queue to skip the next person.
      * `play_draw_two()` & `play_black()`: Manages card drawing penalties and updates game state accordingly.
  * **Deck Management:** The `reshuffle` algorithm in the `GameBoard` class efficiently handles the scenario where the draw pile is empty by shuffling the discard pile and using it to repopulate the draw pile.

### **3. Object-Oriented Programming (OOP)**

The project is built on solid OOP principles:

  * **Encapsulation:** Each class (`Game`, `Player`, `GameBoard`) encapsulates its own data and logic. For example, the `Player` class manages its own hand of cards, and the `Game` class does not need to know the internal details of how the hand is stored.
  * **Abstraction:** The classes provide a clear and simple interface to interact with complex underlying logic.
  * **Modularity:** The separation of concerns into different files and classes makes the code easy to maintain, debug, and extend.

### **4. Code Quality and Professional Practices**

  * **Complexity Analysis:** As mentioned, one of the key skills learned and demonstrated was the ability to analyze the time complexity of my own code. This is documented for every method, showing a commitment to writing efficient and performant software.
  * **Testing:** The inclusion of a `run_tests.py` file shows experience with creating and running a test suite to ensure the code is robust and functions as expected.

-----

## **How to Run the Project**

1.  Clone the repository to your local machine.
2.  Navigate to the project directory.
3.  Execute the main game file from your terminal:
    ```bash
    python game.py
    ```
    *(Note: You may need to create a main execution block in `game.py` to initialize and start the game if one does not already exist.)*
