import random

# List of questions, each question is a dictionary with 'question', 'options', 'answer' keys
questions = [
    {
        "question": "Who was the first Prime Minister of independent India?",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel", "Subhash Chandra Bose"],
        "answer": "Jawaharlal Nehru"
    },
    {
        "question": "When did India gain independence?",
        "options": ["26th January 1950", "15th August 1947", "2nd October 1947", "15th August 1950"],
        "answer": "15th August 1947"
    },
    {
        "question": "What is the national animal of India?",
        "options": ["Elephant", "Lion", "Tiger", "Peacock"],
        "answer": "Tiger"
    },
    {
        "question": "Which Indian city is known as the 'City of Joy'?",
        "options": ["Mumbai", "Kolkata", "Chennai", "Delhi"],
        "answer": "Kolkata"
    },
    {
        "question": "Who wrote the Indian National Anthem?",
        "options": ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Mahatma Gandhi"],
        "answer": "Rabindranath Tagore"
    },
    {
        "question": "Which movement was launched by Mahatma Gandhi in 1942?",
        "options": ["Non-Cooperation Movement", "Dandi March", "Quit India Movement", "Civil Disobedience Movement"],
        "answer": "Quit India Movement"
    },
    {
        "question": "What is the national sport of India?",
        "options": ["Cricket", "Hockey", "Football", "Kabaddi"],
        "answer": "Hockey"
    },
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Chennai", "Kolkata", "New Delhi"],
        "answer": "New Delhi"
    },
    {
        "question": "Who was the leader of the 1857 revolt?",
        "options": ["Rani Lakshmibai", "Mangal Pandey", "Bahadur Shah Zafar", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Who gave the slogan 'Inquilab Zindabad'?",
        "options": ["Bhagat Singh", "Mahatma Gandhi", "Jawaharlal Nehru", "Lal Bahadur Shastri"],
        "answer": "Bhagat Singh"
    }
]

def play_quiz():
    print("Welcome to the Patriotic Quiz Game!")
    print("Test your knowledge about India!")
    print("Let's get started...\n")

    score = 0

    # Shuffle questions to randomize quiz each time
    random.shuffle(questions)

    for i, question in enumerate(questions):
        print(f"Q{i+1}: {question['question']}")
        for idx, option in enumerate(question['options']):
            print(f"  {idx + 1}. {option}")

        # Get user's answer
        try:
            answer_idx = int(input("Enter the option number: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        # Check if the answer is correct
        if question['options'][answer_idx] == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}\n")

    print(f"Quiz Over! Your final score is: {score}/{len(questions)}")
    if score > len(questions) // 2:
        print("Great job! You know your country well!")
    else:
        print("Keep learning more about India's rich history and culture!")

if __name__ == "__main__":
    play_quiz()
