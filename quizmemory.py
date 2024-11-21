import random


users = {}
questions = {
    "DSA": [
        [1, "What is a binary tree?", "A graph", "A linear list", "A tree with two children max", "A sorting method", 3],
        [2, "What is a stack?", "FIFO", "LIFO", "Random Access", "None of these", 2],
        [3, "What is a queue?", "LIFO", "FIFO", "Tree", "Graph", 2]
    ],
    "DBMS": [
        [1, "What is SQL?", "Programming Language", "Query Language", "Markup Language", "Scripting Language", 2],
        [2, "What does ACID stand for?", "Automatic, Clean, Immediate, Data", "Atomicity, Consistency, Isolation, Durability", "Accuracy, Consistency, Immediate, Data", "None", 2]
    ],
    "Python": [
        [1, "What is Python?", "Programming Language", "Snake", "Database", "None", 1],
        [2, "What is PEP8?", "Python Style Guide", "Python Compiler", "Python IDE", "None", 1]
    ]
}

def banner():
    print("QUIZ APPLICATION")

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users:
        print("User already exists.")
    else:
        users[username] = password
        print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if users.get(username) == password:
        print("Login successful!")
        return username
    else:
        print("Invalid credentials.")
        return None

def attempt_quiz():
    print("Choose a subject: ")
    for subject in questions:
        print(f"- {subject}")
    choice = input("Enter subject: ").strip().capitalize()
    
    if choice in questions:
        score = 0
        random.shuffle(questions[choice])
        for q in questions[choice][:5]:
            print(f"\n{q[1]}")
            print(f"1. {q[2]}")
            print(f"2. {q[3]}")
            print(f"3. {q[4]}")
            print(f"4. {q[5]}")
            answer = int(input("Your answer: "))
            if answer == q[6]:
                score += 1
        print(f"\nYour score: {score}/{len(questions[choice])}")
    else:
        print("Invalid subject.")

def main():
    while True:
        banner()
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                attempt_quiz()
        elif choice == "3":
            print("Exiting application.")
            break
        else:
            print("Invalid choice.")

main()
