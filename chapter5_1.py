import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
openaiApiKey = os.getenv("OPENAI_API_KEY")
template = """문장 : {sentence}
{language}로 번역: """
prompt = PromptTemplate(template=template, input_variables=["sentence", "language"])

print(prompt.format(sentence = "탁자위에 고양이가 있다.", language = "영어"))
