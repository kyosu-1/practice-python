from typing import Any

class Singleton(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ConcreateClass(Singleton):
    pass


# インスタンスの生成順序に依存せず、Singletonにできる

if __name__ == '__main__':
    a = ConcreateClass()
    b = ConcreateClass()
    assert a == b
    c = Singleton()
    d = Singleton()
    assert a == c
