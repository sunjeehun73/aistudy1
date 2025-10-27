from openai import OpenAI

systemMessage1 =  """
일반적인 1차 방적식을 해결하려면 다음 단계를 따르세요 

1. **방적식 식별:** 해결하려는 방적식을 식별합니다. 
   방정식은 'ax + b = c' 형태여야 합니다. 
   여기서 'a'는 변수의 계수, 'x'는 변수, 'b'는 상수, 'c'는 또 다른 상수입니다. 
2. **변수 고립화:** 목표는 변수 'x'를 방정식 한쪽에 고립시키는 것입니다. 
   이를 위해 다음 단계를 수행합니다:
   a. **상수 추가 또는 빼기:** 상수를 한쪽으로 이동시키기 위해 양쪽에서 'b'를 더하거나 뺍니다. 
   b. **계수로 나누기:** 'x'를 고립시키기 위해 양쪽을 'a'로 나눕니다. 
   'a'가 0이면 방적시에는 고유한 해가 없을 수 있습니다. 
3. **단순화:** 방적식의 양쪽을 최대한 단순화 합니다. 
4. **'x'에 대해 해결:** 'x'를 한쪽에 고립시키면 해결책을 얻을 수 있습니다. 
   이는 'x = 값' 형태가 될 것입니다. 
5. **해 검토:** 찾은 'x' 값을 원래 방정식에 대입하여 방정식을 만족하는지 확인합니다. 
   만족한다면 올바른 해결책을 찾은 것입니다. 
6. **해 표현:** 해결책을 명확하고 간결한 형태로 작성합니다. 
7. **특수 경우 고려:** 'a'가 0일 때 해가 없거나 무한히 많은 해가 있을 수 있는 특수한 경우를 인지합니다.  

방정식 :  
"""

equation = "3x + 5 = 11"

def loadProperties(filepath):
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

config = loadProperties('config.properties')

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
            {"role": "system", "content": systemMessage1},
            {"role": "user", "content": equation}
        ]
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"오류 발생: {e}")
    print("\nAPI 키를 확인하세요: https://platform.openai.com/account/api-keys")