from .objects import MessagesMessage


class Message(MessagesMessage):
    def __init__(self, api, **kwargs):
        self.api = api
        super().__init__(**kwargs)

    def __call__(self, **kwargs):
        return self.api.messages.send(**kwargs)
