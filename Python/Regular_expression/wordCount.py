# -*- coding: utf-8 -*-
"""quest3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N2tzzQoIuku5bex8llawsbNvD-uIptxo
"""

from google.colab import drive
drive.mount('/content/drive')

import re         # 정규표현식을 다루기 위한 파이썬 내장모듈 임포트
from collections import Counter          #collections 모듈에 포함된 Counter 클래스 (이터러블한 데이터를 받아 각 요소의 개수를 카운트하고 딕셔너리로 받는다.)

#hello
def find_2grams(words):
    return [(words[i], words[i+1]) for i in range(len(words)-1)]       #리스트 컴프리헨션을 사용해 2-gram을 찾는 함수를 정의한다.


with open('/06TheAvengers.txt', 'r') as file: # 파일을 읽기형식으로 연다
    script = file.read().lower()            # 읽기형식으로 불러낸 파일을 소문자로 다 바꾼다.
    words = re.findall(r'\b\w+\b', script)  # 단어만 추출하여 리스트로 만든다.
    two_grams = find_2grams(words)          #find_2grams 함수에 소문자로 된 단어만 추출하여 만든 리스트 words를 넣어 2-gram을 찾고 그 리스트를 two_grams라는 변수에 할당한다.


counter = Counter(two_grams)                # Counter 클래스 사용한 two_grams를 counter 라는 변수에 할당한다.(Counter 클래스는 딕셔너리 형태로 출력한다.)
max_2gram, max_count = counter.most_common(1)[0]   #max_2gram은 counter.most_common(1)을 할당하여 제일 많이 나온 2_gram을 할당하고, max_counter는 횟수를 할당한다.

# 결과 출력
print(max_2gram, max_count)
print(counter)