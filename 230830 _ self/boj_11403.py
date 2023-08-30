import sys

N = int(input())
G = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# i -> j 간선 존재 # i,i 는 항상 0

visited = [[0] * N for _ in range(N)]


