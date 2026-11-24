from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily = TavilyClient()


@tool
def search(query: str) -> dict:
    """
    Tool that searches over internet
    Args:
        query (str): They query to search for
    Returns:
        str: Search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-5")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello World")

    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo?")})
    print(result)

if __name__ == "__main__":
    main()