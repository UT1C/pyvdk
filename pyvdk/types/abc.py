

class Model:
    def __init__(self, **kw):
        for k in kw:
            if k in self.__annotations__:
                # TODO: type check?
                self.__setattr__(k, kw[k])
            else:
                raise ValueError(f"{self.__class__}.{repr(k)} not annotated")
