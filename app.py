import streamlit as st

def get_response(message):
   
    if 'hello' in message.lower():
        return "Hi there! How can I help you today?"
    elif 'help' in message.lower():
        return "Sure, I'm here to help. What do you need assistance with?"
    elif 'bye' in message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you try asking something else?"


def main():
    st.title("Simple Chatbot")

    user_input = st.text_input("Type your message here:")

    if user_input:
        response = get_response(user_input)
        st.text_area("Chatbot says:", value=response, height=100, max_chars=None, key=None)

if __name__ == "__main__":
    main()
