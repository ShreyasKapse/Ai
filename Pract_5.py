def get_response(input_text):
    if input_text.lower() == "what is ai?":
        return "Artificial intelligence is the simulation of human intelligence processes by machines!"
    elif input_text.lower() == "why is ai important?":
        return "AI is important for its potential to change how we live, work and play. !"
    elif input_text.lower() == "what are the advantages of ai?":
        return "Good at detail-oriented jobs,Reduced time for data-heavy tasks,Saves labor and increases productivity."
    if input_text.lower() == "what are the disadvantages of ai?":
        return "Expensive,Requires deep technical expertise,Reflects the biases of its training data"
    else:
        return "I'm sorry, I don't understand that."
# Main function to run the chatbot
def main():
    print( "Welcome to the chatbot!" )
    while True:
        user_input = input( "You: " )
        if user_input.lower() == "bye":
             print( "Chat: Goodbye!" )
             break
        response = get_response( user_input )
        print( "Chat:", response )
if __name__ == "__main__":
 main()
