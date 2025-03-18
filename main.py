import asyncio
import telebot.async_telebot
from settings import TOKEN, CHAT_ID, r

# Инициализация бота
bot = telebot.async_telebot.AsyncTeleBot(TOKEN)

# Функция подписки на канал Redis
async def redis_listener():
    pubsub = r.pubsub()
    await pubsub.subscribe("bot_channel")  # Замените на нужный канал

    async for message in pubsub.listen():
        if message["type"] == "message":
            text = message["data"]
            await bot.send_message(CHAT_ID, text)

# Обработчик входящих сообщений в группе
@bot.message_handler(func=lambda message: True)
async def handle_group_message(message):
    text = message.text
    await r.publish("notifications", text)  # Отправляем сообщение в Redis канал "notifications"
    print("Сообщение отправлено")

# Запуск бота и подписки на Redis
async def main():
    asyncio.create_task(redis_listener())  # Запускаем подписку в фоне
    await bot.polling(non_stop=True)

if __name__ == "__main__":
    asyncio.run(main())
