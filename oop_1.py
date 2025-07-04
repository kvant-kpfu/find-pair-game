class Kvantovec:
    name = ''
    date_of_birt = 0
    napravlenie: str    # переменные внутри класса - поля
    phone_number: int
    mail: str
    test_score: int

    # методы класса - функции внутри класса
    def passed():
        if test_score >= 115:
            return True
        else:
            return False