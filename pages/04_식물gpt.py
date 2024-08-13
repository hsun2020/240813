import openai

openai.api_key = 'YOUR_API_KEY'

def ask_ai(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# 예시 질문
question = "초등학교 3학년 수학 문제를 도와줘."
answer = ask_ai(question)
print(answer)
