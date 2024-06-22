class AIMessage:
    message = {}
    def __init__(self, content, role = "system"):
        self.message = {
            "role" : role,
            "content" : content
        }

