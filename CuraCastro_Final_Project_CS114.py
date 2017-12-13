import random

chapter_0 = [
    [ "What is programming?", 2, "A schedule of shows for a TV chanel", "Entering instructions for the computer to perform", "A list of items, pieces, performers, etc., in a musical, theatrical, or other entertainment" ],
    [ "What is debugging?", 3, "The process of removing bugs from your yard", "The software that runs your Python programs", "Finding and fixing errors" ],
    [ "What is IDLE?", 2, "The software that runs your Python programs", "The software is where you’ll enter your programs", "A word processor" ],
    [ "What is source code?", 1, "Programming instructions", "Where the code comes from", "The Matrix" ]
]
chapter_1 = [
    [ "What is an expression?", 1, "Consists of values and operators, and they can always evaluate down to a single value", "The order math operators are calculated in Python", "The grammar rules of Python" ],
    [ "What is a data type?", 1, "A category for values, and every value belongs to exactly one data type", "Numbers with decimal points", "A character in Star Trek" ],
    [ "What is a floating-point number?", 3, "A string with no characters in it", "Data type that indicates values that are whole numbers", "Numbers with a decimal point" ],
    [ "What is an argument?", 2, "A discussion when the parties do not agree", "A value that is passed to a funtion called", "Temporarily removing code while testing a programs" ]
]
chapter_2 = [
    [ "What is a condition?", 1, "A more specific name in the context of a flow control statement", "A value that is passed to a funtion called", "Numbers with a decimal point" ],
    [ "What are blocks?", 2, "Pieces like in Lego", "Lines of Python code grouped together", "Like an appartment block" ],
    [ "What is an infinite loop?", 3, "A term for the current instruction being executed", "A shortcut to getting the program execution to break out of a whole loops clause early", "A while loop whose condition is always true" ],
    [ "What are built-in functions?", 2, "Functions that need to be imported from a module", "Basic set of functions any program can call", "Functions from github"]
]
chapter_3 = [
    [ "Why are functions used?", 1, "To group code that gets executed multiple times", "To make the code work", "To make the code faster" ],
    [ "What is a return value?", 3, "A data type for returning things", "The keyword that defines a function", "The value returned by a function" ],
    [ "What kind of scope can variables have?", 3, "Local", "Global", "Both" ]
]
chapter_4 = [
    [ "What is a list?", 2, "A list of many different data types", "A value that contains multiple values in an ordered sequence", "All the data types in Python" ],
    [ "What is a list value?", 1, "The list itself", "A single value in a list", "Both" ],
    [ "What is slice?", 3, "Like a slice of pizza", "A copy of a list", "A way to get several values from a list as a new list"],
    [ "What is multiple assignment?", 1, "A shortcut that lets you assign multiple variables with the values in a list in one line of code", "Assigning variables in multiple lines of code", "When you have more than one homework to turn in" ]
]
chapter_5 = [
    [ "What is a dictionary?", 1, "Like a list but indexes can be many different data types", "A book that lists words in a language", "An ordered list of values" ],
    [ "What is a key-value pair?", 2, "How much space a key takes up in memory", "A dictionary key and its associated value", "The number of entries in a list" ]
]

def get_random_question(data):
    question = random.choice(data)
    return question

def ask_question(question_data):
    print()
    print(question_data[0])

    print("  1) " + question_data[2])
    print("  2) " + question_data[3])
    print("  3) " + question_data[4])

    answer = input(" Your choice (1-3): ")
    answer_number = int(answer)

    if (answer_number == question_data[1]):
        print(" -> You got it!")
        return True
    else:
        print(" -> Wrong answer")
        return False

def chapter_main(data, chapter_name):
    score = 0
    print()
    print("* Chapter " + chapter_name)
    while len(data) > 0:
        left = len(data)

        print()
        print("You have answered " + str(score) + " questions correctly." )
        print("You have " + str(left) + " questions to answer.")

        question = get_random_question(data)
        correct = ask_question(question)

        if (correct):
            data.remove(question)
            score += 1

    print()

def main():
    print()
    print(" Welcome to the quiz game for CS114!")
    print()
    print("For each chapter, you'll be asked questions until you get all of them correctly.")
    print("Once you get all the answers for a chapter correct, you can move on to the next one.")

    chapter_main(chapter_0, 'Introduction')
    chapter_main(chapter_1, 'Chapter 1')
    chapter_main(chapter_2, 'Chapter 2')
    chapter_main(chapter_3, 'Chapter 3')
    chapter_main(chapter_4, 'Chapter 4')
    chapter_main(chapter_5, 'Chapter 5')


main()
