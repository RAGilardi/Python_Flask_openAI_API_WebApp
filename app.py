from flask import Flask, render_template, request

app = Flask(__name__)

import openai

# save directly you api key in a string variable or create the file as I did. There two are not the most secure way to protect a private API key
with open('../hidden.txt') as file:
    openai.api_key = file.read()

conversation_history = []

# Define a function to get the bot's response
def get_bot_response(prompt: str) -> str | None:
    text: str | None = None
    
    try:
        conversation = "\n".join([f"{msg['sender']}: {msg['message']}" for msg in conversation_history])
        prompt_with_history = f"{conversation}\nHuman: {prompt}\nAI:"

        # API call to OpenAI
        response: dict = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt_with_history,
            temperature=0.9,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[' Human:', ' AI:']
        )

        choices: dict =  response.get('choices')[0]
        text = choices.get('text')

    except Exception as e:
        print('ERROR:', e)
        text = f'Something went wrong: {e}'

    return text

# Define a route to handle requests to the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle requests to the chatbot endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.form['message']

    user_html = f'<p><strong>You:</strong> {message}</p>'

    prompt = f'\nHuman: {message}\nAI:'

    response = get_bot_response(prompt)

    bot_html = f'<p><strong>Bot:</strong> {response}</p>'

    conversation_history.append({'sender': 'user', 'message': message})
    
    #Don't add a response to the list if null
    if response:
        conversation_history.append({'sender': 'bot', 'message': response})

    # Return both messages as HTML strings
    return user_html + bot_html

if __name__ == '__main__':
    app.run(debug=True)