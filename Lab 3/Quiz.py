import random

#################
### FUNCTIONS ###
#################

# Ask user multiple choice question
# INPUTS
#   - Question (string)
#   - Answer (string)
#   - False Answers (list)
# OUTPUT
#   - Result (boolean)
def ask_multi_choice(_question, _answer, _fake_answers):
    print(_question)

    _answers = _answer.split("\\") + _fake_answers
    random.shuffle(_answers)
    for num in range(len(_answers)):
        print(str(num) + ") ", _answers[num])

    if _answers[int(input("What is the answer: "))] == _answer:
        print("Correct!")
        return True

    print("Incorrect!")
    return False


# Ask user text question
# INPUTS
#   - Question (string)
#   - Answer (string)
# OUTPUT
#   - Result (boolean)
def ask_text(_question, _answer):
    print(_question)

    if input("What is the answer: ").lower() == _answer.lower():
        print("Correct!")
        return True

    print("Incorrect!")
    return False


############
### MAIN ###
############

# Define how many answers the user got correct
correct_answers = 0

print("~~~~~ MULTIPLE CHOICE AND TEXT QUIZ ~~~~~\n - Make sure your answer is spelt correct!")

# Ask questions
print("\n~ QUESTION ONE ~")
correct_answers += ask_multi_choice("What is 2 to the power of 5?", "32", ["25", "10", "7"])

print("\n~ QUESTION TWO ~")
correct_answers += ask_multi_choice("What does W.I.N.E stand for?", "Wine Is Not an Emulator", ["Wiring is not Enumerated", "Wage Intergration and Node Emulation"])

print("\n~ QUESTION THREE ~")
correct_answers += ask_text("How many devices run java (x billions)?", "3 billion")

print("\n~ QUESTION FOUR ~")
correct_answers += ask_text("What was the result of 11001 xor 01101?", "10100")

print("\n~ QUESTION FIVE ~")
correct_answers += ask_text("What is 32 in HEX?", "20")

# Out answer as persentage
print("\n~ RESULTS ~")
print("You got " + str(correct_answers) + " (" + str((correct_answers/5)*100) + "%) correct!")