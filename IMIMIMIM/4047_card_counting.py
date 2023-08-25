'''
딕셔너리 참고
https://bigdaheta.tistory.com/9
https://gammistory.tistory.com/58
'''

T = int(input())

for tc in range(1, T + 1):
    arr = input()
    ans = ''
    card = {'S' : [], 'H' : [], 'D' : [], 'C' : [] }

    for i in range(0, len(arr), 3):
        if arr[i+1:i+3] in card[arr[i]]:
            ans = 'ERROR'
            break
        card[arr[i]].append(arr[i+1:i+3])

    if not ans:
        for j in 'SHDC':
            ans += (str(13 - len(card[j])) + ' ')

    print(f'#{tc} {ans}')


