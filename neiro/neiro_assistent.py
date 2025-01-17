import requests

async def get_response(message_text):
    prompt = {
        "modelUri": "gpt://b1gok529us99nbhikhqq/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.5,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты - нейронная сеть, которая может улучшить запрос от пользователя не превышая ограничение на 500 знаков, он передаёт тебе запрос, ты его улучшаешь в еденичном формате и передаёшь в неёроную сеть для генерации картинки "
            },
            {
                "role": "user",
                "text": message_text
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        'content-Type': 'application/json',
        'Authorization': 'Api-Key AQVN1R5hw1cVpAP8uXpSnOQLAI0IizmiZc2YqYfs'
    }

    response = requests.post(url=url , headers=headers, json=prompt)
    results = response.json()
    return results['result']['alternatives'][0]['message']['text']

# @dp.message_handler()
# async def analize_message(message:types.Message):
#     response_text = await get_response((message.text))
#     await message.answer(response_text)

