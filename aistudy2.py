# 퓨샷 학습
from openai import OpenAI

systemMessage1 =  """
당신은 AI 마케팅 도우미입니다. 사용자가 새로운 제품 이름에 대한 캐치프레이즈를 만들 수 있도록 도와줍니다. 
주어진 제품명에 대해 다음 예시와 비슷한 홍보 문구를 만들어 주세요.

디오스 냉장고 - 여자라서 행복해요 
롯데리아 크랩버거 - 니들이 게 맛을 알아?
SK텔레콤 - 또 다른 세상을 만날 땐 잠시 꺼두셔도 좋습니다. 

제품명 :  
"""

productName = "첵스 파맛"

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
            {"role": "user", "content": productName}
        ]
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"오류 발생: {e}")
    print("\nAPI 키를 확인하세요: https://platform.openai.com/account/api-keys")