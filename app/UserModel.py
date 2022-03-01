class User:
    def __init__(self, _id, username, avatar_url, _type, url):
        self._id = _id
        self.username = username
        self.avatar_url = avatar_url
        self.type = _type
        self.url = url

    def get_user_dict(self):
        return {
            'id': self._id,
            'username': self.username,
            'avatar_url': self.avatar_url,
            'type': self.type,
            'url': self.url
        }