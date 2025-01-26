from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="""1. Navigate directly to YouTube.com/@OpenAI in the browser
        2. Wait for full page load and cookie consent handling
        3. Click the 'Videos' tab in the channel header
        4. Identify the most recent upload (top-left video in 'Latest' section)
        5. Verify upload date matches current date/week
        6. Click the video thumbnail to open player
        7. Wait for video preview to load
        8. Click the play button (center or bottom-left control)
        9. Confirm playback by checking: 
           - Time progress bar movement
           - Audio/video synchronization
           - No error messages displayed""",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())