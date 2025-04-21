from users import User

class VotingSystem:
	parties = {"A":0, "B":0, "C":0}
	def vote(self):
		username = input("Enter your username to vote: ")
		password = input("Enter your password to vote: ")
		user = User.authenticate(username, password)
		if user:
			if user.has_voted:
				print("You have already voted.")
				return
			print("Parties: A, B, C")
			choice = input("Enter the Party name you want to vote for: ").upper()
			if choice in self.parties:
				self.parties[choice]+=1
				user.has_voted = True
				print("Vote cast successfully.")
			else:
				print("Invalid party choice.")
		else:
			print("Invalid username or password")
	def view_results(self):
		print("\n Voting Results: ")
		for party, votes in self.parties.items():
			print(f"Party {party}: {votes} Votes.")