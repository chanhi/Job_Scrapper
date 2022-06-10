# Job_Scrapper
### with nomad coder '파이썬으로 웹 스크래퍼 만들기'

## Data Types
- string: a="text" or a='text' *not a="text'
- number: a=2
- float: a=1.2
- boolean: a=True, b=False
- none: a=None

## List, Tuple, Dicts
#### List
```python
  a=[1,2,3,4,5]
  b=["a","b","c","d"]
  
  print("a" in b)
  print(a[2])
  print(len(a))
  a.append(6)
  print(a)
```
True    
3    
5    
[1,2,3,4,5,6]    
- list is mutable(수정가능한)
#### Tuple
```python
  a=(1,2,3,4,5)
  b=("a","b","c","d")
  
  print("a" in b)
  print(a[2])
  print(len(a))
```
True    
3    
5    
- tuple is immutable
#### Dicts
```python
  dict_name = {
    "name": "chanhuy",
    "age": 22,
    "Man": True,
    "skill": ["hellFire", iceAge]
  }
  dict_name["height"]=188
```
- 없는 key와 value를 쓰면 해당 dict에 추가됨

## Function
built in funtion
- print()
- len()
- int()
- type()

create funtion
```python
  def say_hello(name):
    print("hello" + name)
    print(f"nice to meet you {name}")
    
  def plus(a, b):
    return a+b
    
  say_hello("chanhuy")
  result = plus(3, 2)
  print(result + 3)
```
hello chanhuy   
nice to meet you chanhuy    
8    
- 단 한개의 값만 return 할 수 있다.
- 함수에 필요한 argument를 입력하지 않으면 오류가 난다.





