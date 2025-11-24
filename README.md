**ROCK PAPER SCISSORS**

**Overview of the project:**
The classic game of Rock-Paper-Scissors (RPS) is a simple yet engaging hand game, often used as a fair method of decision-making between two people. This project aims to translate this universally recognized game into a robust, interactive, and modular Python application. The choice of RPS serves as an excellent foundation to implement and demonstrate core programming concepts such as modular design, object-oriented programming (OOP), input/output validation, and algorithmic logic for an AI opponent.  


The project utilizes Python, known for its simplicity and extensive libraries, making it ideal for rapid prototyping and clear, readable code. The primary goal is not just to build a working game, but to focus on the technical expectations laid out in the project guidelines, particularly proper architectural design, modular implementation, and robust error handling. This report details the design process, implementation, testing, and evaluation of the final product.

 
**Features:**
Core Game Features
Randomized Computer Choice: This is the central feature enabled by the random module, specifically using the random.choice() function.

The computer selects its move (Rock, Paper, or Scissors) randomly from a predefined list of options, ensuring the opponent's choice is unpredictable.

User Input: The game uses the input() function to allow the player to enter their choice (e.g., "rock", "paper", or "scissors").

Game Rules Implementation: A series of conditional statements (if, elif, else) are used to compare the user's choice against the computer's random choice to determine the outcome (Win, Lose, or Tie) based on the classic rules:

Rock beats Scissors.

Scissors beats Paper.

Paper beats Rock.

Output and Feedback: The game prints the choices made by both the player and the computer, along with the result of the round (e.g., "You win!", "It's a tie!").

✨ Additional/Common Features
Continuous Play Loop: Many implementations use a while True loop to allow the user to play multiple rounds until they explicitly choose to exit (often by typing a specific word like "quit" or "exit", or selecting an exit option from a menu).

Score Keeping: Variables are often used to track and display the number of wins for the player and the computer, providing a running score.

Input Handling: Basic games often convert the user's input to lowercase (.lower()) to ensure the input is not case-sensitive, making the game more forgiving to play.

Simple Command Line Interface (CLI): The entire game typically runs in the terminal or command prompt, utilizing basic print() and input() functions for all interaction.


**Technolgies/Tools Used:**
Programming language - Python 3.14
User Interface - Command Line Interface(CLI)


**Steps to Install and Run the Project:**
