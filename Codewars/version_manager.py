class VersionManager:
    def __init__(self, version=''):
        self.version = self.check(version)
        self.previous = []

    @staticmethod
    def check(vs):
        if not vs:
            return [0, 0, 1]

        vs = vs.split('.')
        if len(vs) > 3:
            vs = vs[0: 3]

        while len(vs) != 3:
            vs.append('0')

        for i in range(len(vs)):
            if vs[i].isdigit():
                vs[i] = int(vs[i])
            else:
                raise Exception("Error occured while parsing version!")
        return vs

    def major(self):
        self.previous.append(self.version.copy())
        self.version[0] += 1
        self.version[1] = 0
        self.version[2] = 0

        return self

    def minor(self):
        self.previous.append(self.version.copy())
        self.version[1] += 1
        self.version[2] = 0

        return self

    def patch(self):
        self.previous.append(self.version.copy())
        self.version[2] += 1

        return self

    def rollback(self):
        if len(self.previous):
            self.version = self.previous.pop()
        else:
            raise Exception("Cannot rollback!")

        return self

    def release(self):
        return '.'.join(map(str, self.version))


a = VersionManager("a")
