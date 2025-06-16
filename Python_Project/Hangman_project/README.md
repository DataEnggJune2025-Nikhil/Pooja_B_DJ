# 🎮 Hangman Game - Python Console Edition

Welcome to **Hangman**, the classic word-guessing game implemented in Python!  
This is a console-based interactive game with single-player and multiplayer modes, difficulty levels, and optional hints.

---

## 📝 Features

- ✅ Single-player mode with difficulty selection (`easy`, `medium`, `hard`)
- 👥 Multiplayer mode (Player 1 sets the word, Player 2 guesses)
- 💡 Optional hints (first letter reveal)
- 🔤 Dynamic word categorization from external `words.txt` file
- ➕ Ability to add custom words to the word list
- 🎨 ASCII art hangman graphics (from `hangman_Art.py`)
- 📊 Score tracking (wins/losses)

---

## 📁 File Structure

```
Python_Project/Hangman_project
│
├── hangman_game.py         # Main game script
├── hangman_Art.py          # Contains HANGMAN_PICS list (ASCII graphics)
├── words.txt               # Word bank file used in the game
├── README.md               # Project overview and usage guide
├── Screenshots             # Contains screenshots of the game
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/DataEnggJune2025-Nikhil/Pooja_B_DJ.git
cd hangman-game
```

### 2. Prepare the Word List

Make sure you have a `words.txt` file in the same directory with a list of words (one word per line):

```
banana
computer
umbrella
python
```

### 3. Add Hangman Art

Create a `hangman_Art.py` file with ASCII stages of the hangman. Example:

```python
HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''',
    '''
     +---+
     O   |
         |
         |
        ===''',
    ...
]
```

### 4. Run the Game

```bash
python hangman_game.py
```

---

## 🧠 How to Play

- **Single Player Mode**: Choose a difficulty and guess the word one letter at a time.
- **Multiplayer Mode**: One player enters a secret word, the other player guesses.
- **Hint Option**: Reveals the first letter of the word at the beginning.
- **Win Condition**: Guess all letters before the hangman drawing is complete.
- **Lose Condition**: Run out of 6 attempts.

---

## 🛠 Requirements

- Python 3.x

---

## 📌 Example Gameplay

```
Choose mode: single or multiplayer? single
Choose difficulty (easy/medium/hard): easy
Do you want a hint for this round? (y/n): y

💡 Hint: The word starts with 'C'
Word: C _ _ _ _
Wrong letters:
Attempts remaining: 6
Enter a letter: o
...
🎉 Congratulations! You guessed the word: CLOUD
🏁 Score → Wins: 1 | Losses: 0
```

---

## 👥 Author

- **Pooja Bavisetti** – https://github.com/poojab2813

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
