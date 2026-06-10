def get_range_for_difficulty(difficulty):
    if difficulty == "Easy":   return 1, 20
    if difficulty == "Normal": return 1, 100
    if difficulty == "Hard":   return 1, 50
    return 1, 100

def parse_guess(raw):
    if not raw:
        return False, None, "Enter a guess."
    try:
        value = int(float(raw)) if "." in raw else int(raw)
        return True, value, None
    except Exception:
        return False, None, "That is not a number."

def check_guess(guess, secret):
    if guess == secret:
        return "Win", "Correct!"
    if guess > secret:
        return "Too High", "Go LOWER!"
    return "Too Low", "Go HIGHER!"