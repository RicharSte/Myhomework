"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def main():
    
    try:
      user_age = int(input('Please write here, how old are you: '))
    except ValueError:
      print('Please use numbers')

    try:    
      def what_are_you_doing(age):
          if age < 0:
                return "You are too young, pleas write your real age "
          elif 0 <= age <= 7:
                return "You are in kindegarten"
          elif 8 <= age <= 18:
                return "You are in school"
          elif 19 <= age <= 25:
                return "You are at university"
          elif 26 <= age <= 120:
                return "You are working"
          else:
                return "You are too old, please write your real age"
    except UnboundLocalError:
      print("")     
         
    try:   
      all_info = user_age, what_are_you_doing(user_age)
      print(all_info)
    except NameError:
      print("")
          
          


if __name__ == "__main__":
    main()
