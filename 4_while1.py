"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
      
    while True:
          # я использовал lower(), т.к. многие вводят ответ не с большой буквы
          user_answer = input("How are you?: ").lower()
          if user_answer == "good":
                print("Nice!")
                break

    
if __name__ == "__main__":
    ask_user()
