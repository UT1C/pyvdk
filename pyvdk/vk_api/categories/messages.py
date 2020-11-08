from ..category import Category


class Messages(Category):

    # FIXME:
    def send(
        self,
        message: str,
        peer_id: int,
    ):
        # FIXME:
        return self.__request__("send", locals())
