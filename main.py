import random
from replit import clear
from art import logo

class black_Jack():

  def __init__(self):
    self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # return None

  def deal_card(self):
    card = random.choice(self.cards)
    return card

  def calculate_score(self, cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)

  def compare(self, user_score, computer_score):
    if user_score == computer_score:
      return "Draw :)"
    elif computer_score == 0:
      return "Lose, opponent has Blackjack"
    elif user_score == 0:
      return "Win with a Blackjack  😎"
    elif user_score > 21:
      return "You went over. You lose T^T"
    elif computer_score > 21:
      return "Opponent went over. You win  😎"
    elif user_score > computer_score:
      return "You Win  😎"
    else:
      return "You lose T^T"


def play_game():

  print(logo)
  
  game_bj = black_Jack()
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(game_bj.deal_card())
    computer_cards.append(game_bj.deal_card())
  
  user_score = game_bj.calculate_score(user_cards)
  computer_score = game_bj.calculate_score(computer_cards)
  
  print(f"   Your cards: {user_cards}, current score: {user_score}")
  print(f"   Computer's first card: {computer_cards[0]}")
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(game_bj.deal_card())
    computer_score = game_bj.calculate_score(computer_cards)
    if computer_score >= 21:
      is_game_over = True
  
  while not is_game_over:
    if user_score == 0 or computer_score == 0 or user_score >= 21:
      is_game_over = True
    else:
      user_should_deal = input("Type y or n to deal card or type n to pass: ")
      if user_should_deal == "y":
        user_cards.append(game_bj.deal_card())
        user_score = game_bj.calculate_score(user_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
      else:
        is_game_over = True

  print(game_bj.compare(user_score,computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()