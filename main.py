"""
Цель: парсировать комментарии из поста группы вк

Описание:
main.py - основной файл
config.py - храним служебную информацию ( token )
parsing.py - файл с парсингом и сохранением информации

Задачи:
A)
1 - Запрашивать у пользователя короткое  название группы, кол-во комментариев и номер нужного поста
2 - Узнать id группы и id поста
3 - Сохраняем в файлы информацию о постах и комментариях

"""

import json
import vk_api
from config import token
from parsing_comments.parsing import get_comments
from parsing_comments.analysis import work_to_words


def main():
    group_name = input("Введите название группы: ")
    count_comments = int(input("Введите кол-во комментариев (не более 100): "))
    number_post = int(input("Введите номер поста (не более 100): "))

    # работаем с файлом parsing.py
    comments_array = get_comments(group_name, count_comments, number_post)
    sentence, comments_array_2 = work_to_words(comments_array)
    print("comments_array", comments_array)
    #file = open("comments/comments_clear.txt", 'w', encoding="utf-8")
    #file_2 = open("comments/comments.txt", 'w', encoding="utf-8")

    #for i in sentence:
     #   file.write(i)

    #for j in comments_array:
     #   file_2.write(j)

    with open('comments/comments_clear.txt', 'w', encoding="utf-8") as filehandle:
        filehandle.writelines("%s\n" % i for i in sentence)

    with open('comments/comments.txt', 'w', encoding="utf-8") as filehandle:
        filehandle.writelines("%s\n" % i for i in comments_array_2)

    print(sentence)

if __name__ == '__main__':
    main()