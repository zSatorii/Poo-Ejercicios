class MayorTupla:
    def __init__(self, tupla):
        self.tupla = tupla

    def mayor(self):
        return max(self.tupla)

mt = MayorTupla((5, 8, 2, 9, 3))
print(mt.mayor())
