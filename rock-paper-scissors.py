import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")

  options = ["rock", "paper", "scissors"]

  computer_choice = random.choice(options)

  choices = {"player": player_choice, "computer": computer_choice}
  
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  
  if player == computer:
    return "It's a tie!"

  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."

  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      return "Scissors cuts paper! You lose."

  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You win!"
    else:
      return "Rock smashes scissors! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

"""Zeile 1: Python Libraries sind eine Sammlung von nützlichen Funktionen und werden über - import - aufgerufen

Zeile 3-12: Durch das Aufrufen von choices = get_choices() kann def get_choices getestet werden.

choices = get_choices()
print(choices)

Zeile 15: print("You chose " + player + ", computer chose " + computer)

Das print-Statement von def check_win kann durch die Nutzung eines f-string lesbarer gemacht werden.

Zeile 17-36: Die beiden elif-Bedingungen können vereinfacht werden.
  
elif player == "rock" and computer == "scissors":
return "Rock smashes scissors! You win!"

elif player == "rock" and computer == "paper":
return "Paper covers rock! You lose.

Zeile 37: Mit check_win("rock", "paper") kann def check_win getestet werden.

Zeile 38-39: choices = get_choices() übermittelt das Dictionary {"player": player_choice, "computer": computer_choice}.
Bei der Konstruktion der Variable result wird die check_win-Funktion aufgerufen. Als Argumente der check_win-Funktion (player, computer) wird die Variable choices (choices = get_choices) in Kombination mit den Dictionary-Keys "player" und "computer" eingefügt. Dadurch werden aus dem Dictionary die Werte player_choice und computer_choice an def check_win übergeben.   
"""

"""Libraries are a set of useful functions and are usually imported at the top of a program, e.g. random-library.


Using f-strings allows to combine strings and variables (cf. Hamburg Coding School --> str.format() in Größter Kreis)

age = 36
print(f"Lucas ist {age} years old.")

If-, else- and elif-statements allow to check conditions

age = 36
if age >= 18:
  print("You are an adult.")
else:
  print("You are a child.")

age = 36
if age >= 18:
  print("You are an adult.")
elif age > 12:
  print("You are a teenager.")
elif age > 1:
  print("You are child.")
else:
  print("You are a baby.")


Refactoring is the process of restructuring code while keeping the original functionality."""