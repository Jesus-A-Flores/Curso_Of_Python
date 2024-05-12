class Spam:
    __egg = 7
    def print(self):
        print(self.__egg)

s = Spam()
s.print()
print(s.__egg)