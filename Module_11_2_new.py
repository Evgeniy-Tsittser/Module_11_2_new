import inspect


class Introspector:
    def __init__(self, name, school, age):
        self.name = name
        self.school = school
        self.age = age

    def write_file(self):
        atr_list = [self.name, self.school, self.age]
        with open('info.txt', 'w', encoding='utf-8') as file:
            for line in atr_list:
                file.write(str(line) + '\n')


def introspection_info(obj):
    dict_ = {'type': type(obj), 'attributes': obj.__dict__ if hasattr(obj, '__dict__') else 'Нет атрибутов',
             'metods': [func for func, _ in inspect.getmembers(obj, predicate=inspect.ismethod)],
             'module': inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else 'Нет модуля'}
    return dict_


number_info = Introspector('John', 'Urban', 43)
number_info.write_file()

print(introspection_info(number_info))
print(introspection_info(10))
print(introspection_info('Это строка'))