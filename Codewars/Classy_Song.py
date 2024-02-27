class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self._seen = set()

    def how_many(self, people):
        tmp = set(map(str.lower, people))
        res = len(tmp - self._seen)
        self._seen.update(tmp)
        return res


mount_moose = Song('Mount Moose', 'The Snazzy Moose')

print(mount_moose.how_many(['John', 'Fred', 'BOb', 'carl', 'RyAn']))
print(mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']))
print(mount_moose.how_many(['Amanda', 'CalEb', 'CarL', 'Furgus']))
print(mount_moose.how_many(['JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE']))
print(mount_moose.how_many(['fred', 'AMaNda', 'AMAnDA', 'fReD', 'jesica']))
