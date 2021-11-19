import asyncio

print("Program asynchroniczny")


async def pozdrowienie(pierwszy, drugi):
    print(pierwszy)
    await asyncio.sleep(3)
    print(drugi)


# asyncio.run(pozdrowienie("Witaj", "Do widzenia"))
async def zadanie(i):
    print("Zadanie:",i)

async def main():

    for i in range(10):
        task = asyncio.create_task(zadanie(i))
        await task

asyncio.run(main())
