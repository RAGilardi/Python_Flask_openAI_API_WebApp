# Python_Flask_openAI_API_WebApp
This small code was thought as a self-assignment aimed to help me understand better how to build a WebApp using Flask, connecting it to an API through Python and also play a bit with AI chatBots.

Being this project connected to an OpenAI chatbot I used their Python Library **"openai"** (https://github.com/openai/openai-python) instead of the generical purpose **"requests"** (https://pypi.org/project/requests/). 

The jupyter-notebook "manual" describe and explain all the code in its parts.

Contact me through the issue tab of this github page or via pm if you find any issue with the code.

#### Simple overview

The project works as this:

- calling the **app.py** file will create a **Flask web server**, using the html (and corresponding css) file as a template. This file will also execute an **API call** to openAI services (keeping it on as long as the server runs)

- on this server's **webpage**, there is a text box with a submit button. Writing a message and submitting it (**javascript interaction**) will trigger the **Flask server's routes**

- these **routes** will format the message from the user input and send it to a **python function** called get_bot_response (contained in the app.py file too)

- the **get_bot_response** will interact with the **chatbot** and return a response, which will take into considerations the conversation history

- the chatbot route of the flask server will take this response and return it to the javascript function, which will show it on the page

#### Directory structure
The project, exluding the documentation, is formed by the following:

    1) the python project, ./app.py
    2) the html file, ./template/index.py
    3) the javascript file, ./static/scripts.js
    4) the css file, ./static/style.css
    
The directory structure, as commented later, depends on how flask webapps works, but could be changed manually.

Also, I'm not adding to the gitHub repository my personal API key, which in my case was stored in the file named **./hidden.txt**.