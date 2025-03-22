from openai import OpenAI
import httpx

client = OpenAI(base_url="xxx", api_key="xxx")

def gpt_call(prompt, model_name='gpt-3.5-turbo'):
    while True:
        try:
            response = client.chat.completions.create(
                # model=model_name,
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            break
        except Exception as e:
            print(e)
            continue
    return response.choices[0].message.content