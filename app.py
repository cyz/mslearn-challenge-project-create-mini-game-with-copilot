# It seems there is a misplaced line in the provided code that could be causing an error.
# Let's correct the code and then try running it.

import random

def get_user_choice():
    """Get the user's choice from the console."""
    choice = input("Choose rock, paper or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        choice = input("Choose rock, paper or scissors: ").lower()
    return choice

def get_computer_choice():
    """Randomly select the computer's choice."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of a round."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def update_scores(winner, scores):
    """Update the scores based on the winner of the round."""
    if winner == 'user':
        scores['user'] += 1
    elif winner == 'computer':
        scores['computer'] += 1
    return scores

def show_results(scores):
    """Show the game results and the final scores."""
    print("Game over!")
    print(f"Your score: {scores['user']}")
    print(f"Computer's score: {scores['computer']}")
    if scores['user'] > scores['computer']:
        print("Congratulations, you won!")
    elif scores['user'] < scores['computer']:
        print("Sorry, the computer won this time.")
    else:
        print("It's a tie!")
        
# Example of using these functions in a simple game loop

def play_game():
    scores = {'user': 0, 'computer': 0}
    play_again = 'yes'
    
    while play_again.lower() == 'yes':
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}. Computer chose {computer_choice}.")
        
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win this round!")
        else:
            print("Computer wins this round!")
        
        scores = update_scores(winner, scores)
        play_again = input("Do you want to play again? (yes/no): ")
    
    show_results(scores)

# Uncomment the line below to play the game
play_game()

# Since we cannot run interactive input in this notebook, we will comment out the actual play_game() call.
# To run the game, you would uncomment the play_game() call in your local environment and run the Python script.
