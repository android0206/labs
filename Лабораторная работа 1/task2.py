# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44  # Mb
volumeinb = volume * 1024 * 1024  # b

symb = 4
str_ = symb * 25
page_ = str_ * 50
book = page_ * 100

books_in_disk = int(volumeinb) // book
# print(volumeinb, book)
print("Количество книг, помещающихся на дискету:", books_in_disk)
