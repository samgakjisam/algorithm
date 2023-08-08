# 파이썬 내장함수, 라이브러리 사용 금지
def min_and_avg_score(scores):
    # 여기에 pass를 지우고 코드를 작성합니다.
    summation = 0
    cnt = 0
    min_num = scores[0]
    for i in scores: # scores 리스트 순회
        if i < min_num:
            min_num = i
        summation += i # sum에 요소 i 덧셈
        cnt += 1 # 1 증가
    avg_num = summation / cnt
    return min_num, avg_num



if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    answer = min_and_avg_score(scores)
    print(answer)
    print(type(answer))
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    
#### min, sum, avg, max 등 내장함수로 사용되는 것을 변수명으로 사용하지 말자