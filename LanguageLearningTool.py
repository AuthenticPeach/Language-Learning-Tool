import random

vocabulary = {
    "apple": "manzana",
    "house": "casa",
    "dog": "perro",
    "cat": "gato",
    # Add more vocabulary words and translations here
}

def vocabulary_quiz():
    score = 0
    questions = list(vocabulary.keys())
    random.shuffle(questions)

    for question in questions:
        answer = input(f"What is the translation of '{question}'? ")
        if answer.lower() == vocabulary[question].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct translation is '{vocabulary[question]}'.")

    print(f"\nQuiz completed! You scored {score}/{len(vocabulary)}.\n")

vocabulary_quiz()

grammar_exercises = [
    {
        "question": "Choose the correct form of the verb 'to be' in the present tense: I ___ a student.",
        "options": ["am", "is", "are"],
        "answer": "am"
    },
    {
        "question": "Which pronoun should be used to refer to a group of people?",
        "options": ["he", "she", "they"],
        "answer": "they"
    },
    # Add more grammar exercises here
]

def grammar_quiz():
    score = 0

    for exercise in grammar_exercises:
        print(exercise["question"])
        for index, option in enumerate(exercise["options"]):
            print(f"{index + 1}. {option}")
        answer = input("Enter your answer (number): ")
        if answer == str(exercise["options"].index(exercise["answer"]) + 1):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{exercise['answer']}'.")

    print(f"\nQuiz completed! You scored {score}/{len(grammar_exercises)}.\n")

grammar_quiz()

flashcards = {
    "Hello": "Hola",
    "Goodbye": "Adiós",
    "Thank you": "Gracias",
    "Yes": "Sí",
    # Add more flashcards here
}

def flashcard_system():
    print("Welcome to the Flashcard System!\n")
    print("Press 'q' to quit.\n")

    while True:
        word = random.choice(list(flashcards.keys()))
        print(f"Word: {word}")
        input("Press Enter to see the translation. ")
        print(f"Translation: {flashcards[word]}\n")
        choice = input("Enter your choice (q to quit): ")
        if choice.lower() == 'q':
            break

    print("\nFlashcard session ended.\n")

flashcard_system()
