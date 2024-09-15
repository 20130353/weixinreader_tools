# -*-coding:utf-8 -*-
import io
import sys

import requests
from bs4 import BeautifulSoup


def get_have_book_name():
    filename = "have_book_names.txt"
    res = set()
    with open(filename, 'r') as f:
        for each in f.readlines():
            arr = each.strip().split()
            book = arr[1]
            res.add(book)
    return res


# 参考文档：https://blog.csdn.net/qq_45196785/article/details/124767864
def get_books_name():
    import re
    pattern = re.compile(r'(?<=\")\S+(?=\")')

    filename = "books_name.txt"
    res = []
    with open(filename, 'r') as f:
        for each in f.readlines():
            if "\"" not in each:
                continue

            arr = re.findall(pattern, each)
            res.append(arr[0])
            # print(arr[0])
    return res


def main():
    # 改变标准输出的默认编码
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

    # 爬取微信读书书架书籍字数
    shelf_arr = get_books_name()

    have_book_name = get_have_book_name()

    # 分组所有书籍
    # 将要输出保存的文件地址（自行更改），若文件不存在，则会自动创建
    fw = open("./文本.txt", 'w', encoding='utf-8')
    for link in shelf_arr:
        req = requests.get(url=link)
        req.encoding = "utf-8"
        soup = BeautifulSoup(req.text, features="html.parser")
        book_titles = soup.find_all("h2", class_="bookInfo_right_header_title_text")  # 书名
        book_authors = soup.find_all("a", class_="bookInfo_author")  # 作者
        book_nums = soup.find_all("div", "introDialog_content_pub_line")  # 字数
        # 书名
        book_name = ""
        for book_title in book_titles:
            book_title_handle = book_title.text.strip()
            book_name = book_title_handle

        # 作者
        author_name = ""
        for book_author in book_authors:
            book_author_handle = book_author.text.strip()
            author_name = book_author_handle

        # 分类
        tag_name = ""
        if len(book_nums) >= 1:
            tag_name = book_nums[-1].text.strip().replace("分类", "")

        if book_name not in have_book_name:
            fw.write(book_name + ";" + author_name + ";" + tag_name)
            fw.write("\n")


if __name__ == '__main__':
    get_books_name()
    main()
