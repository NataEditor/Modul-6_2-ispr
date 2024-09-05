class Vehicle:
    """любой транспорт"""

    new_color = str
    __COLOR_VARIANTS = ['red', 'blue', 'green', 'black', 'white', 'greyt']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner  # владелец
        self.__model =__model  # модель(марка) транспорта
        self.__engine_power =__engine_power  # мощность двигателя
        self.__color =__color  # название цвета

    def get_model(self):
        print(f'Модель, {self.__model}, транспорта')

    def get_horsepower(self):
        print(f'Мощность двигателя {self.__engine_power}')

    def get_color(self):
        print(f'Цвет транспорта {self.__color}')

    def print_info(self):
        print(
            f'Модель, {self.__model}\nМощность двигателя, {self.__engine_power} \nЦвет транспорта , {self.__color} '
            f'\nВладелец , {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    """седны"""
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark ||', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasya'
vehicle1.print_info()