from openai import OpenAI
systemMessage1 =  """
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

systemMessage2 = """
당신은 수수께끼를 푸는 데 특화된 AI어시스턴트입니다. 
주어진 수수께끼를 최선을 다해 풀어주세요 
답변에 대한 명확한 정당화와 그 뒤의 추론 과정을 제공해 주세요 

수수께끼 :
"""

riddle = """
얼굴과 두 손은 있지만, 팔과 다리는 없는 것은 무엇일까요?
"""

systemMessage3 = """
당신은 파이썬 전문가로서 사용자의 요구에 따라 파이썬 코드를 생성합니다. 

===>예제시작 

---사용자 질문---
문자열을 출력하는 함수를 만들어 주세요.

---사용자 출력---
문자열을 출력하는 함수는 아래와 같습니다.
```def myPring(str):
       return print(str)
```

<===예제 끝 
"""

query = "n번째 피보나치 수를 계산하는 파이썬 함수를 생성하세요"

def load_properties(filepath):
  """프로퍼티 파일에서 설정을 읽어오는 함수"""
  props = {}
  try:
    with open(filepath, 'r', encoding='utf-8') as f:
      for line in f:
        line = line.strip()
        # 빈 줄이나 주석은 무시
        if line and not line.startswith('#') and not line.startswith('!'):
          if '=' in line:
            key, value = line.split('=', 1)
            props[key.strip()] = value.strip()
  except FileNotFoundError:
    print(f"오류: {filepath} 파일을 찾을 수 없습니다.")
    return None
  return props

config = load_properties('config.properties')

if config is None or 'OPENAI_API_KEY' not in config:
    print("오류: config.properties 파일에 OPENAI_API_KEY가 설정되지 않았습니다.")
    print("config.properties 파일을 생성하고 다음 형식으로 작성하세요:")
    print("OPENAI_API_KEY=your-api-key-here")
    exit(1)

apiKey = config['OPENAI_API_KEY']

if not apiKey or apiKey == 'your-api-key-here':
    print("오류: 유효한 API 키를 config.properties 파일에 설정하세요.")
    exit(1)

try:
    client = OpenAI(api_key = apiKey)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": systemMessage3},
            {"role": "user", "content": query}
        ]
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"오류 발생: {e}")
    print("\nAPI 키를 확인하세요: https://platform.openai.com/account/api-keys")
