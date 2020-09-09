"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    Data = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},   #You may add more, if you wish
       {'school_class': '10b', 'scores': [2, 1, 5, 3, 4]}]
    
    def all_school_score(): 
          
          empty_list = []
          
          for notes in Data:
                emtpy_list += notes
          
          return sum(list) / len(list)
        
    
    def for_one_class(your_class):  #write here the class, which mean notes you want to know
          your_class = str(your_class)
          list_of_classes = []
          
          for school_class in Data:
                list_of_classes.append(school_class.get('school_class'))
          
          index_of_class = list_of_classes.index(your_class)
          
          return sum(Data[index_of_class]['scores']) / len(Data[index_of_class]['scores'])
          
    
    
    
    
if __name__ == "__main__":
    main()
