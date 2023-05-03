import openai

openai.api_key = "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"

conversation = "Operador es un chatbot que responde de manera psicópata,belicista y grosero"

while True:
    question = input("Tu: ")
    conversation += "\nTu: " + question + "\nOperador:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=2,
        max_tokens=200,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=[" Tu:"," Operador:"]
    )

    answer = response.choices[0].text.strip()
    conversation += answer
    print("Operador: \n" + answer + "\n")