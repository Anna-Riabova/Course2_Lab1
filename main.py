import doctest


class Human:
    def __init__(self, name: str, age: int, hight: int):
        """
        Создание и подготовка к работе объекта "Человек"

        :param name: имя
        :param age: возраст
        :param hight: рост

        Примеры:
        >>> Vasya = Human("Vasya",27, 180)  # инициализация экземпляра класса
        """
        if not isinstance(name, (str)):
            raise TypeError("У человека должно быть имя")
        self.name = name

        if not isinstance(age, (int)):
            raise TypeError("Возраст должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным числом")
        self.age = age

        if not isinstance(hight, (int)):
            raise TypeError("Рост должен быть целым числом")
        if hight < 0:
            raise ValueError("Рост не может быть отрицательным числом")
        self.hight = hight
    def is_teenager(self) -> bool:
        """
        Функция которая проверяет является ли человек подростком

        :return: Является ли человек подростком

        Примеры:
        >>> Vasya = Human("Vasya",27, 180)
        >>> Vasya.is_teenager()
        """
        ...

    def increase_hight(self, value: int) -> None:
        """
        Увеличивает рост человека.
        :param value: насколько вырос человек

        :raise ValueError: Если пытается применить не к подросткам

        Примеры:
        >>> Vasya = Human("Vasya",16, 165)
        >>> Vasya.increase_hight(7)
        """
        if not self.is_teenager():
            raise ValueError("Применимо только к подросткам")


    def change_name(self, new_name: "str") -> None:
        """
        Смена имени.

        :param new_name: новое имя
        :raise TypeError: Если имя введено не корректно.


        Примеры:
        >>> Vasya = Human("Vasya",16, 165)
        >>> Vasya.change_name("Moshe")
        """

class Book:
    def __init__(self, name: str, pages: int, genre: str):
        """
        Создание и подготовка к работе объекта "Книга"

        :param name: название книги
        :param pages: количество страниц
        :param genre: жанр

        Примеры:
        >>> Voina_i_Mir = Book("Voina_i_Mir", 1472, "classics")  # инициализация экземпляра класса
        """
        if not isinstance(name, (str)):
            raise TypeError("У книги должно быть название")
        self.name = name

        if not isinstance(pages, (int)):
            raise TypeError("Количество страниц должно быть определено целым числом")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным числом")
        self.pages = pages

        if not isinstance(genre, (str)):
            raise TypeError("Жанр должен быть обозначен текстом")
        self.genre = genre

    def is_classics(self) -> bool:
        """
        Функция которая проверяет является ли книга жанра классика

        :return: Является ли книга жанра классика

        Примеры:
        >>> Voina_i_Mir = Book("Voina_i_Mir", 1472, "classics")
        >>> Voina_i_Mir.is_classics()
        """
        ...

    def increase_genre(self, value: str) -> None:
        """
        Добавление нового жанра.

        :param value: новый жанр
        :raise ValueError: Если жанр уже присвоен книге.


        Примеры:
        >>> Voina_i_Mir = Book("Voina_i_Mir", 1472, "classics")
        >>> Voina_i_Mir.increase_genre("Epic novel")
        """

class Bag:
    def __init__(self, name: str, cost: int, color: str):
        """
        Создание и подготовка к работе объекта "Сумка"

        :param name: название бренда
        :param cost: цена
        :param color: цвет

        Примеры:
        >>> Birkin = Bag("Birkin", 2850000, "black")  # инициализация экземпляра класса
        """
        if not isinstance(name, (str)):
            raise TypeError("У сумки должно быть название")
        self.name = name

        if not isinstance(cost, (int)):
            raise TypeError("Цена должна быть определена целым числом")
        if cost < 0:
            raise ValueError("Цена не может быть отрицательным числом")
        self.cost = cost

        if not isinstance(color, (str)):
            raise TypeError("Цвет должен быть обозначен текстом")
        self.color = color

    def is_color(self) -> bool:
        """
        Функция которая проверяет является ли сумка нужного цвета

        :return: Является ли сумка нужного цвета

        Примеры:
        >>> Birkin = Bag("Birkin", 2850000, "black")
        >>> Birkin.is_color("black")
        """
        ...

    def decrease_cost(self, value: int) -> None:
        """
        Снижение цены (добавление скидок).

        :param value: стоимость, на которую надо уменьшить цену
        :raise ValueError: Если вводимое значение стоимости меньше цены сумки.


        Примеры:
        >>> Birkin = Bag("Birkin", 2850000, "black")
        >>> Birkin.decrease_cost(25000)
        """
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
