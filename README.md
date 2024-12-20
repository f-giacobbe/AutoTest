# AutoTest
A simple Python tool that will help you keep track of your progress studying with a flashcard-like model.


To start create a file (for example a .csv file) for each subject that you want to study inside the "questions"
folder. The user is able to choose the separator between the question and the answer, both of which share one
line. Afterward, the user is able to edit the "autotest.py" file and create a new Subject object using its
constructor which takes in two strings as parameters: the subject name and its file path.
The separator is contained inside the "split_symbol" variable inside the "autotest.py" file.


Once the user runs the autotest.py file, a prompt appears where the choice of the subject is made.
After the choice is made the game starts: the questions inside the subject's questions file are shuffled and are
asked randomly. To each question, the user can input "Y" if the answer is known, "N" otherwise. The program keeps
track of the unknown answers and will only ask those during the next round.
At the end of each round, a percentage of the unknown answers out of the total is shown and the flashcards are shuffled
once again, and after the user responds "Y" to each question, the program terminates.