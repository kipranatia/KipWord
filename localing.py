from os import access,F_OK

def create_dictionary(config):

    if access(config, F_OK) != True:
        print("Cannot find dictionary file!")
        quit()
        
    locale_file = open(config,'r')
    print(locale_file.read())
    locale_file.close
    





def analyze():
    if access('config.txt',F_OK) != True:
        print("Cannot find config file!")
        quit()
    
    config_file = open('config.txt') #Открываем файл
    
    config = "" #Переменная имени файла с локалью
    
    for line in config_file:#проходимся по каждой линии конфига

        word_num = 1 #Переменные для разделения строки с параметрами
        word_num2 = 1
        first = 0 #Переменная для определения первого и второго символа "
    
        for word in line: #Проход по каждой букве строки
            if word != '"': 
                if first == 0: #Если символ не равен " и он еще не встречался, то переменная первого параметра разделения плюс 1
                    word_num += 1
                    continue
                else: #Если символ не равен " и он встречался, то переменная второго параметра разделения плюс 1
                    
                    word_num2 +=1
                    continue
        
            else: 
                if first == 0: #Иначе, если символ " встретился, то переменная определения первого и второго символа " плюс 1
                    first+=1
                    word_num2 = word_num
                
                else: #Иначе, если символ " встретился второй раз, то записываем имя файла локали в переменную config
                    config = line[word_num:word_num2]
                    break


    config_file.close() #Закрываем файл
    print(config)
    create_dictionary(config)








if __name__ == "__main__": #Если модуль выполняется как главный, то запустить функцию analyze
    analyze()
