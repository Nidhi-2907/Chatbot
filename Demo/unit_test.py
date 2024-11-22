import logging
from LLMHandler import LLMHandler

# Set up logging to suppress debug messages
logging.basicConfig(level=logging.WARNING)  # Only show warnings and errors
if __name__ == "__main__":
    llm_handler = LLMHandler()
    tweets = ["What is the status of my flight booked in name of Samantha Guerra and booking id is 41486539?", "what is my booking id"]

    for tweet in tweets:
        print(f"\nInput: {tweet}")
        result = llm_handler.handle_conversation(tweet)
        print("Output:", result)