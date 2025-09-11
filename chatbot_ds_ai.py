#write a simple chatbot that uses while loop to answer questions about data science and AI
print('Hello! I am your Data Science & AI chatbot.')
print('You can ask me anthing about Data Science and AI')
print('Type "exit" to end the chat.')
 
while True:
    user_input = input('You:')
    if user_input.lower() == 'exit':
        print('Chatbot:Goodbye!Have a great day!')
        break
    elif 'Data Science' in user_input.lower():
        print('Chatbot: Data Science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data.')
    elif 'AI' in user_input.lower() or 'artificial intelligence' in user_input.lower():
        print('Chatbot: Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems. These processes include learning, reasoning and self-correction.')
    else:
        print('Chatbot: I am sorry, I can only answer questions about Data Science and AI. Please ask something related to these topics.')
        