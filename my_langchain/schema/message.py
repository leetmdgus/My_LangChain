class Message:
    def __init__(self, content, role):
        self.message = {
            "role" : role,
            "content" : content
        }
