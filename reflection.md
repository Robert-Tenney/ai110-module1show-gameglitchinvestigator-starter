# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looked mostly normal except for the fact that it said to go higher when the guess was higher than the answer and to go lower when the guess was less than the answer. Additionally when I did get the correct answer and tried to click the button to start a new game it gave a new answer but didn't allow me to submit a new guess
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The hints were backwards and clicking new game did not reset the game only changed the secret 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
40|Too Low |Go Lower |N/A | |
60|Too High |Go Higher |N/A | |
New game|New secret and can resubmit new answer |was unable to |N/A | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
It told me to check the outputs for clicking new game to see if there
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided it was fixed when I saw that I was either given the correct hint when I entered an incorrect guess or I was able to properly start a new game by clicking the new game button instead of refreshing the page. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  Manual Test and it showed it worked after entering two incorrect answers(one higher and one lower) to ensure it properly displayed that the answer was lower or higher than the guess respectively 
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns are kinda like refreshing the page everytime you click a button, so when you try to submit an answer it causes the program to act like you refrehed the entier page. Session state is a fix that prevents certain inputs from being deleted when a page refreshes. An example of this would be a survey form that keeps your previous answers if you closed the page out and repopened it again.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I would use an AI program to help me double and triple check my work to see if it spotted an error I missed.
- What is one thing you would do differently next time you work with AI on a coding task?
I would ask AI for help on problems I ran into sooner. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
The project changed the way I viewed AI generate code as I now know I need to always be checking it incase it produces any errors. 