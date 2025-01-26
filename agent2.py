from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="""Price comparison and purchase:
        1. Navigate to Apple Store
           - Search "iPhone 16 Pro 256GB Space Black"
           - Extract price (Price_Apple)
           - Screenshot Apple Store price
        
        2. Navigate to Amazon
           - Search "iPhone 16 Pro 256GB Space Black"
           - Filter for Prime/Sold-by-Amazon
           - Extract price (Price_Amazon)
           - Screenshot Amazon price
        
        3. Compare Price_Apple vs Price_Amazon
           - If Price_Amazon < Price_Apple: 
             * Add to Amazon cart
             * Proceed to checkout page
           - Else:
             * Add to Apple Store cart
             * Proceed to checkout
        
        4. Capture final evidence:
           - Screenshot cart page
           - Save HTML of price details
        
        5. Report both prices:
           "Apple: {Price_Apple} | Amazon: {Price_Amazon}
            Buying from: {Cheaper_Store}" """,
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())