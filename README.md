**ROCK PAPER SCISSORS**

**OVERVIEW OF THE PROJECT:**
The classic game of Rock-Paper-Scissors (RPS) is a simple yet engaging hand game, often used as a fair method of decision-making between two people. This project aims to translate this universally recognized game into a robust, interactive, and modular Python application. The choice of RPS serves as an excellent foundation to implement and demonstrate core programming concepts such as modular design, object-oriented programming (OOP), input/output validation, and algorithmic logic for an AI opponent.  


The project utilizes Python, known for its simplicity and extensive libraries, making it ideal for rapid prototyping and clear, readable code. The primary goal is not just to build a working game, but to focus on the technical expectations laid out in the project guidelines, particularly proper architectural design, modular implementation, and robust error handling. This report details the design process, implementation, testing, and evaluation of the final product.

**FEATURES:**
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


**TECHNOLOGIES/TOOLS USED:**
Programming language - Python 3.14
User Interface - Command Line Interface(CLI)


**STEPS TO INSTALL AND RUN THE PROJECT:**


1. Install Python

Make sure you have **Python 3.x** installed.

Check your Python version:

```sh
python --version
```

or

```sh
python3 --version
```

If Python is not installed, download it from:
**python.org/downloads**

2. Download or clone the project

Place the project folder anywhere on your computer.

If your project is on GitHub, clone it using:

```sh
git clone <your-repository-url>
```

Or simply download the ZIP file and extract it.

3. Open a terminal or command prompt

Navigate to the folder containing your Python file, for example:

```sh
cd path/to/your/rock-paper-scissors-project
```
4. (Optional) Create a virtual environment

If your project includes dependencies, create and activate a virtual environment:

#Windows:

```sh
python -m venv venv
venv\Scripts\activate
```

#macOS / Linux:

```sh
python3 -m venv venv
source venv/bin/activate
```

If your project has a `requirements.txt` file, install dependencies with:

```sh
pip install -r requirements.txt
```

*(Most simple Rock–Paper–Scissors games don't require extra packages, so you may skip this.)*
5. Run the program

Run the game using:

```sh
python rock_paper_scissors.py
```

or on some systems:

```sh
python3 rock_paper_scissors.py
```

Make sure the filename matches your actual script name.

6. Play the game

Follow the prompts in the terminal.

Typical inputs might be:

```
rock
paper
scissors
```

or whatever options your program lists.

7. (Optional) Exit the virtual environment

If you used a virtual environment:

```sh
deactivate
```


**INSTRUCTIONS FOR TESTING:**

1. Make sure you have Python installed

Your system must have **Python 3.x**.
To check, open a terminal/command prompt and run:

```sh
python --version
```

or

```sh
python3 --version
```

If Python is not installed, download it from python.org.

2. Save your game file

Make sure your Rock–Paper–Scissors code is saved as something like:

```
rock_paper_scissors.py
```

3. Open a terminal or command prompt

Navigate to the folder where your Python file is saved.

Example:

```sh
cd path/to/your/project
```


4. Run the game

Use one of the commands below depending on your system:

```sh
python rock_paper_scissors.py
```

or

```sh
python3 rock_paper_scissors.py
```

5. Follow the on-screen instructions

You’ll typically be asked to enter something like:

```
rock
paper
scissors
```

or abbreviations like:

```
r
p
s
```

(Depending on how your code is written.)

6. Test all possible outcomes

To ensure your code works correctly, test each case:

 ✔ Player wins cases:

* rock vs scissors
* paper vs rock
* scissors vs paper

✔ Computer wins cases:

* rock vs paper
* paper vs scissors
* scissors vs rock

 ✔ Tie cases:

* rock vs rock
* paper vs paper
* scissors vs scissors



7. Try invalid input

Enter things like:

```
hello
123
roc
```

Make sure your program handles errors gracefully.

8. (Optional) Test multiple rounds

If your program supports looping or score-keeping, verify that:

* Scores update correctly
* Game ends only when expected
* Inputs between rounds work properly

**SCREENSHOTS:**
![IMG-20251123-WA0435](https://github.com/user-attachments/assets/36ee2700-1aab-4058-bb58-87aeb7f55322)
![IMG-20251123-WA0433](https://github.com/user-attachments/assets/dfafa673-ac77-447e-afeb-f168122cf64f)


