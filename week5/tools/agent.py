from dotenv import load_dotenv
import requests
 
load_dotenv()
 
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
 
 
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)
 
 
 
search_tool = DuckDuckGoSearchRun()
 
@tool
def get_weather_data(city: str) -> str:
    """
    Fetch current weather data for a given city.
    """
    url = (
        f"https://api.weatherstack.com/current"
        f"?access_key=c05d4e9df26c50a992e63a1eeb3c8072&query={city}"
    )
 
    response = requests.get(url)
    return str(response.json())
 
 
 
agent = create_agent(
    model=llm,
    tools=[search_tool, get_weather_data],
    system_prompt="You are a helpful assistant."
)
 
 
response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Find the capital of Madhya Pradesh and tell me its current weather."
            }
        ]
    }
)
 
