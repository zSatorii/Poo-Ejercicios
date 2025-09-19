class SumaTupla:
    def __init__(self, tupla):
        self.tupla = tupla

    def suma(self):
        total = 0
        for n in self.tupla:
            total += n
        return total

st = SumaTupla((1, 2, 3, 4))
print(st.suma())
