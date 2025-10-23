from openai import OpenAI
systemMessage =  """
당신은 주어진 텍스트를 바탕으로 튜토리얼을 생성하는 AI 어시스턴트 입니다. 
텍스트에 어떤 절차를 진행하는 방법에 대한 지침이 포함되어 있다면, 
번호 목록 형식으로 튜토리얼을 생성하십시오. 
그렇지 않다면 텍스트에 지침이 포함되어 있지 않음을 사용자에게 알리십시오. 

텍스트 : 
"""

instructions = """
이탈리아 제노바에서 유명한 소스를 준비하려면, 먼저 잣을 구워
바질과 마늘과 함께 부엌 절구에 넣어 굵게 다집니다. 
그런 다음 절구에 오일의 절반을 넣고 소금과 후추로 간을 합니다. 
마지막으로 페스토를 그릇에 옮기고 파르메산 치즈 간 것을 넣고 저어줍니다. 
"""

client = OpenAI(api_key="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")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": systemMessage},
      {"role": "user", "content": "탸양이 빛나고 강아지가 뛰놀고 있습니다."}
    ]
)
print(response.choices[0].message.content)
