from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="Compare the price of gpt-o1 and DeepSeek-R1",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
