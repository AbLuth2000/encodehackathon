from chatbot_general import Chatbot

def enhance_output(question):
    sentences = [item['value'] for item in question['messages']]

    system_message = f"You are a sympathetic medical assistant. Take the input list of sentences and transform them with more comforting vocabulary."

    my_chatbot = Chatbot(system_message)
    enhanced_output = my_chatbot.get_response(f"{sentences}")

    return enhanced_output