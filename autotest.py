from subject import Subject
from flashcard import Flashcard
import random



# To be tuned by the user
split_symbol = ","
subjects_list = [
	Subject("Fondamenti di Elettromagnetismo - Definizioni e formule", "questions/elettromagnetismo_def.csv"),
	Subject("Fondamenti di Elettromagnetismo - Dimostrazioni", "questions/elettromagnetismo_dim.csv"),
	Subject("Analisi 2 - Definizioni", "questions/analisi2_def.csv")
]




print("\nWelcome to AutoTest. Choose a subject to continue.")
for i in range(len(subjects_list)):
	subject = subjects_list[i]
	print(f"{i}\t{subject.name}")
choice = int(input())

if choice < 0 or choice > len(subjects_list) - 1:
	raise RuntimeError("Invalid choice.")

subject = subjects_list[choice]


#loading flashcards
flashcards = []
with open(subject.questions_path, "r") as questions_file:
	for line in questions_file:
		split_line = line.split(split_symbol)

		#removing \n
		split_line[-1] = split_line[-1].rstrip('\n')

		question = split_line[0]
		answer = split_line[1]

		flashcard = Flashcard(question, answer)
		flashcards.append(flashcard)

#shuffle
random.shuffle(flashcards)



#testing until we run out of flashcards
total_questions = len(flashcards)
while len(flashcards) > 0:
	unknowns = 0

	print("\n\tLet's start...")

	flashcards_copy = flashcards[:]
	for q in flashcards_copy:
		print(f"\n{q.question}")
		user_input = input()

		if user_input.lower() == "y":
			flashcards.remove(q)
		elif user_input.lower() == "n":
			unknowns += 1
		else:
			print("\tInvalid input. Enter Y or N")
			unknowns += 1

		print(q.answer)

	print(f"{unknowns}/{total_questions} ({round(((unknowns/total_questions)*100), 2)}% of unknown answers)")
	input("Press enter to continue with the next round")