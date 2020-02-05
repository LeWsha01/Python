import inspect
from inspect import isfunction


class Corrective:
    def __new__(cls, *args, **kwargs):
        name, parents, attrs = args
        new_attr = {}
        new_name = 'Decorated' + name.title()
        for at, value in attrs.items():
            if name in at:
                new_attr[at] = value
            elif at[0] == '_' and str(at[1]).isalpha():
                continue
            elif isfunction(value):
                lst = list(inspect.signature(value).parameters.keys())
                if 'self' in lst and len(lst) == 1:
                    if 'get_' in at:
                        at = str(at).replace('get_', '')
                    new_attr[at] = property(value)
                elif 'cls' in lst:
                    new_attr[at] = classmethod(value)
                elif 'cls' and 'self' not in lst:
                    new_attr[at] = staticmethod(value)
                else:
                    new_attr[at] = value
            else:
                new_attr[at] = value
        return type(new_name, parents, new_attr)


class MyClass(metaclass=Corrective):
    name = 'Yura'
    _age = 27
    _town = 'Minsk'
    __work = 'Developer'

    def get_work(self):
        return self.__work

    def into_name(self):
        return self.name

    def name_plus_town(self, spc):
        result = self.name + spc + self._town
        return result

    def hello(cls):
        pass

    def st_met():
        pass

    def __str__(self):
        return 'hello'


if __name__ == '__main__':
    obj = MyClass
    print(obj.__name__)
    data = obj.into_name
    print(data)

