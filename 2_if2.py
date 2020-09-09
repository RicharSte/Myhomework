"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    
    str1 = #write something here
    str2 = #write something here

    def about_strings(str1, str2,):
          if str(str1) != str1 or str(str2) != str2:
                return 0
          elif str1 == str2:
                return 1
          elif str1 != str2 and len(str1) > len(str2):
                return 2
          elif str1 != str2 and str2 == 'learn':
                return 3
          else:
                return "Something wrong..."

    print(about_strings(str1, str2))
    
if __name__ == "__main__":
    main()