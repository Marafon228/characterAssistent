from characterai import aiocai
import asyncio


async def main():
    char = "AKAW5M09-IU9XBHNvQI0ReXSJHXpj3psKghEY9GHblg"
    chat_id = "7520546b-50ae-495d-98ad-733a7e367b98"
    token_denisof_2016 = "ab498e3c8c83178ae412f3a1ba8138163beeaf84"
    token_nas = "65bb4959cbacae7908d9675845f21f59ea707a80"
    client = aiocai.Client(token_nas)
    test = await client.get_chat(char)
    history = await client.get_history(chat_id)
    me = await client.get_me()
    await client.get_history(chat_id)

    async with await client.connect() as chat:

        new, answer = await chat.new_chat(
            char, me.id
        )

        print(f'{answer.name}: {answer.text}')

        while True:
            text = input('YOU: ')

            message = await chat.send_message(
                char, new.chat_id, text
            )
            print(f'history: {history}')
            print(f'test: {test}')
            print(f'message: {message}')
            print(f'{message.name}: {message.text}')


asyncio.run(main())