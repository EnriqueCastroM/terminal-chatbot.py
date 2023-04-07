import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

while True:

    engine_model_gpt3 = "text-davinci-003"

    prompt = input("Enter new prompt:")

    if prompt in ['exit','salir','terminar','quit']:
        break

    completion = openai.Completion.create(
        engine = engine_model_gpt3,
        prompt = prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    response = completion.choices[0].text

    print(response)