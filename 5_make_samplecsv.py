import csv

# Sample data
data = [
    ['이름', '나이', '도시'],
    ['존', 25, '뉴욕'],
    ['에밀리', 28, '로스엔젤레스'],
    ['미카엘', 22, '시카고']
]

# File name
file_name = 'sample.csv'

# 데이터를 CSV 파일에 기록
with open(file_name, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)

print(f'예제 CSV 파일 "{file_name}"를 만들었습니다.')