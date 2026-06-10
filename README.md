# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

<!--  -->
## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
You are supposed to guess a random number between 1 and 100.

- [x] Detail which bugs you found.
Bug 1 — State reset: clicking "New Game" (or any button) caused the
secret number to regenerate on every Streamlit rerun, making the game
impossible to win.
Bug 2 — Inverted hints: the Higher/Lower feedback was reversed — the
app said "Go Higher" when the guess was too high, and "Go Lower" when
the guess was too low.

- [x] Explain what fixes you applied.
Fix 1 — Used `st.session_state` to store the secret number so it
persists across reruns instead of being regenerated each time.
Fix 2 — Swapped the comparison branches so that a guess above the
secret number correctly shows "Go Lower" and a guess below correctly
shows "Go Higher".

## 📸 Demo Walkthrough

1. Open the application.
2. Click the options menu to bring up the difficulty select screen.
3. Choose your desired difficulty.
4. Enter a number between 1 and 100 and press Submit.
5. If correct, click "New Game" to start over.
   If incorrect, read the hint:
   - "Go Lower" → your guess is larger than the answer.
   - "Go Higher" → your guess is smaller than the answer.
**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
===================== test session starts ======================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\u\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\u\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 3 items

tests/test_game_logic.py::test_winning_guess PASSED       [ 33%]
tests/test_game_logic.py::test_guess_too_high PASSED      [ 66%]
tests/test_game_logic.py::test_guess_too_low PASSED       [100%]

====================== 3 passed in 0.04s =======================


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
