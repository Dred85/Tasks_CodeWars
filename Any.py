import asyncio

async def func():
    print("A")
    await asyncio.sleep(5)  # Не блокирует, просто "ждёт"
    print("B")

async def main():
    print("Я тебя опередил!")

# asyncio.run(main())

async def plan():
    await asyncio.gather(func(), main())

asyncio.run(plan())
