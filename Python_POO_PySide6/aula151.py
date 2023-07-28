# def meu_repr(self):
#     nome_classe = self.__class__.__name__
#     # class_dict = self.__dict__
#     classe_rapr = f"({nome_classe}) {self.nome}"
#     return classe_rapr


# def adc_repr(cls):
#     cls.__repr__ = meu_repr
#     return cls


def adc_repr(cls):
    def meu_repr(self):
        nome_classe = self.__class__.__name__
        # class_dict = self.__dict__
        classe_rapr = f"({nome_classe}) {self.nome}"
        return classe_rapr

    cls.__repr__ = meu_repr
    return cls


@adc_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


@adc_repr
class Time:
    def __init__(self, nome) -> None:
        self.nome = nome


terra = Planeta("Terra")
marte = Planeta("Marte")

brasil = Time("Brasil")
corinthians = Time("Corinthians")

print(brasil)
print(corinthians)
print(terra)
print(marte)
