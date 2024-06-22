class HumanMessage:
    message = {}
    def __init__(self, content, role = "user"):
        self.message = {
            "role" : role,
            "content" : content
        }

