import os
from dotenv import load_dotenv
from langchain_classic import hub
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI

load_dotenv()
openaiApiKey = os.getenv("OPENAI_API_KEY")
serpApiKey = os.getenv("SERPAPI_API_KEY")

chat = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key = openaiApiKey)
tools = load_tools(
    ["serpapi"],
    tool_kwargs={
        "serpapi": {"serpapi_api_key": serpApiKey}
    }
)

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(chat, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# print(prompt.template)
result = agent_executor.invoke({"input": "2024 파리 올림픽 사격 여자 10m 공기권총에서 메달을 획득한 대한민국 선수는?"})
print(result)