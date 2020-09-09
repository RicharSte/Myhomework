"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    
    def ask_user_dict():
            
            answers_dict =  {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Ты голоден?": "Пока что нет", 
                           "Может сыграем в радугу?": "Давай, хорошая идея", "Ты давно тут сидишь?": "А какой сейчас год?"}
            
            while True:
                  
                  try:
                    users_input = input('Задай вопрос. Напиши \"Стоп\" чтобы остановить программу: ')
                  except KeyboardInterrupt:
                    print("Bye!")
                    break
                  
                  if users_input == 'Стоп': 
                      break
                  elif users_input in answers_dict:
                      print(answers_dict.get(users_input))
                  else:
                      print("Я не знаю что на это ответить...")
        
    
if __name__ == "__main__":
    ask_user()
