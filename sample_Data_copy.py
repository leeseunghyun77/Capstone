import json

# 1. 파일 불러오기 (파일명은 실제 경로에 맞게 수정하세요)
file_path = file_path = "C://Users/LSH/Desktop/Capstone/Sample_Data/furniture_train_dials.json"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. 데이터 추출 시작
print(f"{'No':<5} | {'User Utterance':<40} | {'AI Intent'}")
print("-" * 80)

count = 0
# dialogue_data 내부를 순회합니다.
for dial_entry in data['dialogue_data']:
    # 각 대화(dialogue) 안의 턴(turn)들을 확인합니다.
    for turn in dial_entry['dialogue']:
        user_text = turn.get('transcript', '')

        # transcript_annotated는 문자열 형태의 리스트이므로 변환이 필요할 수 있습니다.
        # 여기서는 가장 명확한 turn_label의 act를 가져옵니다.
        if turn.get('turn_label'):
            ai_intent = turn['turn_label'][0].get('act', 'N/A')
        else:
            ai_intent = "None"

        # 화면에 출력
        print(f"{count:<5} | {user_text[:38]:<40} | {ai_intent}")
        count += 1

        # 너무 많으면 복잡하니 일단 20개만 출력해봅니다.
        if count >= 20:
            break
    if count >= 20:
        break

print("-" * 80)
print(f"총 {count}개의 데이터 샘플을 확인했습니다.")
