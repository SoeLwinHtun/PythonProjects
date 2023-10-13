import random

#a simple text based rock paper scissor program that will also remember the scores.

choices = ["rock","paper","scissor"]

cpu_score = 0
player_score = 0

while True:
	
	player = input("Enter rock, paper or scissor: ").lower()

	computer = random.choice(choices)

	if player==computer:
		print("Computer chose " + computer + " It's a tie!!")

	elif player=="rock":
		if computer == "scissor":
			print("Computer chose scissor, You win!!!")
			player_score += 1
		else:
			print("Computer chose paper, You lose!!!")
			cpu_score += 1

	elif player == "paper":
		if computer == "rock":
			print("Computer chose rock, You win!!!")
			player_score += 1
		else:
			print("Computr chose scissor, You lose!!!")
			cpu_score += 1

	elif player == "scissor":
		if computer == "paper":
			print("Computer chose paper, You win!!!")
			player_score += 1
		else:
			print("Computer chose rock, You lose!!!")
			cpu_score += 1

	flag = input("Enter 0 to exit or any others to keep playing!")

	if flag == "0":
		print("Total score is, player = " + str(player_score) + " and computer = " + str(cpu_score))
		break