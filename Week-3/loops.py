total_score = 0

# Define the test bank with quiz questions
test_bank = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin"],
        "answer": "B"
    },
    {
        "prompt": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5"],
        "answer": "B"
    }
]

# Iterating through the list of dictionaries
for q in test_bank:
    print("\n" + q["prompt"])
    for option in q["options"]:
        print(option)
        
    # user_answer = input("Enter your answer (A, B, or C): ")
    # For practice, let's hardcode an answer instead of using input()
    user_answer = "A" 
    
    if user_answer == q["answer"]:
        print("Correct!")
        total_score += 1
    else:
        print("Incorrect.")

# Do it now: Write a simple `while` loop that acts as a 10-second timer, printing the seconds counting down from 10 to 0.

