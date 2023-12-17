# importing modules 
import json 
from difflib import get_close_matches   #this import module from difflib is gonna allow us to match the best reponse for the input
#loading knowledge_base from json file
def load_knowledge_base(filepath : str) -> dict:     #this function will load our knowledge_base into data 
    
    """ Reads the knowledge base from a json file.
    file_path: the path to the json file containing the knowledge base. """

    with open (filepath,"r") as file:
        data: dict = json.load(file)
    return data 

def save_knowledge_base(filepath : str, data: dict):  #this function helps in saving old responses
    with open(filepath,"w") as file:
        json.dump(data, file , indent = 2)             # it dumps the data back in the file 

def find_best_match(user_question: str, questions : list[str]) -> str | None:  # this function will find the best match from the dictionary; it will return a string or none.
    matches: list = get_close_matches(user_question, questions, n = 1, cutoff = 0.6)     #here n = 1 will give the top 1 similar repsonse and 0.6 means 60% similar response 
    return matches[0] if matches else None                                              #will return the first match i.e closest match .

def get_answer_for_question(question: str, knowledge_base : dict) -> str | None:                #this function is designed to retrieve an asnwer to a specified question from knowledge_base
    for q in knowledge_base["questions"]:
        if q["question"] == question: 
            return q["answer"]

def chat_bot():                                                                                 #this function we define our chatbot 
    knowledge_base: dict = load_knowledge_base("/Users/abdulbasith/knowledge_base.json")
    while True:     #creating an infinite loop to chat 
        user_input : str = input("You: ")

        if user_input == "quit":
            break

        best_match : str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer : str = get_answer_for_question(best_match, knowledge_base) 
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't know the answer. Can you teach me ? ")
            new_answer : str = input("Type the answer or 'skip' to skip: ")

            if new_answer.lower() != "skip":
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print("Bot: Thank you! I learned a new response!")


chat_bot()






