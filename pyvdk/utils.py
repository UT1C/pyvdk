from types import Any


class DictToObject:
  """ Transforms dict to object """

  _raw_dict: dict

  def __init__(self, dict_object: dict) -> None:
    self._raw_dict = dict_object
    for k, v in dict_object.items():
      selected = self.type_handle(v)
      self.__setattr__(k, selected)

  def __repr__(self) -> str:
    return f"<DictToObject: {self.__dict__}>"

  def get(self, attr: str) -> Any:
    """ Get attribute """

    return self._raw_dict.get(attr)

  @staticmethod
  def type_handle(x: Any) -> Any:
    """ Handle types """

    if isinstance(x, dict):
      return DictToObject(x)
    if isinstance(x, (list, tuple)):
      return [DictToObject.type_handle(i) for i in x]
    return x