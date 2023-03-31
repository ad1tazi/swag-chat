import openai
import json

openai.api_key = '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'

def generate(input_text, conversation):
    input_text = input_text.lower()

    # Load conversation history
    conversation_history = [{
        "role": "system", 
        "content": "You are a helpful assistant."
    }]
    conversation_history += json.loads(conversation)
    conversation_history.append({"role": "user", "content": input_text})

    # Add the conversation history to the API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )
    generated_text = 'Swag. ' + response['choices'][0]['message']['content']

    # Update the conversation history
    conversation_history.append({"role": "assistant", "content": generated_text})

    print(conversation_history)

    return generated_text, conversation_history
