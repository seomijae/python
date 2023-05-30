Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> heroes = []
>>> heroes.append("아이언맨")
>>> heroes.append("닥터 스트레인지")
>>> print(heroes)
['아이언맨', '닥터 스트레인지']
>>> letters = ['A', 'B', 'C', 'D', 'E', 'F']
>>> print(letter[0])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(letter[0])
NameError: name 'letter' is not defined. Did you mean: 'letters'?
>>> print(letters[0])
A
>>> print(letters[1])
B
>>> print(letters[2])
C
>>> letters = ['A', 'B', 'C', 'D', 'E', 'F']
>>> print(letters[:3])
['A', 'B', 'C']
>>> print(letters[0:3])
['A', 'B', 'C']
>>> print(letters[3:])
['D', 'E', 'F']
>>> print(letters[:])
['A', 'B', 'C', 'D', 'E', 'F']
>>> heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
>>> heroes[1] = "닥터 스트레인지"
>>> print(heroes)
['아이언맨', '닥터 스트레인지', '헐크', '스칼렛 위치']
>>> heroes.append("스파이더맨")
>>> print(heroes)
['아이언맨', '닥터 스트레인지', '헐크', '스칼렛 위치', '스파이더맨']
>>> heroes.insert(1, "배트맨")
>>> print(heroes)
['아이언맨', '배트맨', '닥터 스트레인지', '헐크', '스칼렛 위치', '스파이더맨']
