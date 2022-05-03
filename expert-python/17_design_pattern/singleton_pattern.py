class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ConcreateClass(Singleton):
    pass


class Borg(object):
       _state = {}
       def __new__(cls, *args, **kwargs):
           ob = super().__new__(cls, *args, **kwargs)
           ob.__dict__ = cls._state
           return ob


# インスタンスの生成順序に依存せず、Singletonにできる

if __name__ == '__main__':
    a = ConcreateClass()
    b = ConcreateClass()
    assert a == b
    c = Singleton()
    d = Singleton()
    assert c == d
