# coding=utf-8

import nester

movies = ["The Holy Grail", "The Life of Brain", "The Meaning of Life"]
print(movies[1])
print(movies)
print(len(movies))

movies.insert(1, 1975)
movies.insert(3, 1979)
movies.append(1983)
print(movies)

fav_movies = ["The Holy Grail", "The Meaning of Life"]
for each_flick in fav_movies:
    print(each_flick)

count = 0
while count < len(movies):
    print(movies[count])
    count += 1

movies.pop()
movies.pop()
movies.remove("The Life of Brain")
movies.remove(1979)
print(movies)

movies.extend(["Terry Jones & Terry Gilliam", 91])
"""extend在列表末尾添加一个数据项集合"""
print(movies)  # 打印列表

charpman = ["Graham chapman", ["Michael Plain", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]
movies.extend(charpman)
for each_item in movies:
    print(each_item)

nester.print_lol(movies, True, 8)  # 模块名.函数名
nester.print_lol(movies)
nester.print_lol(movies, True)
