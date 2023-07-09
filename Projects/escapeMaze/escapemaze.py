# -*- coding: utf-8 -*-
"""EscapeMaze.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Nnq8UjJxM0BtAGnsRUlhoZQsIveQfp4
"""

import pprint

maze = [
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 오른쪽, 왼쪽, 위, 아래

def find_maze_path(maze, x, y):
    if x == 4 and y == 4:  # 목적지에 도달한 경우
        maze[x][y] = 2
        return True

    if maze[x][y] == 1 or maze[x][y] == 2:  # 벽이거나 이미 지나간 길인 경우
        return False

    maze[x][y] = 2  # 이미 지나간 길을 표시

    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < 5 and 0 <= new_y < 5:
            if find_maze_path(maze, new_x, new_y):  # 재귀적으로 다음 위치를 탐색
                maze[new_x][new_y] = 2  # 가능한 모든 경로를 2로 표시

    return False  # 미로를 찾을 수 없는 경우

start_x, start_y = 0, 0

if find_maze_path(maze, start_x, start_y):
    print("미로를 찾았습니다.")
else:
    print("미로를 찾을 수 없습니다.")

pprint.pprint(maze)