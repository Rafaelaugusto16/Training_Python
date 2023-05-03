class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes (self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

vingadores = Filme('vingadores - guerra infinita', 2018, 2)

vingadores.dar_likes()

print('Nome: {} - Ano: {} - Duração: {} horas - Likes: {}'.format(vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.likes))

atlanta = Serie('atlanta', 2018, 2)

atlanta.dar_likes()
atlanta.dar_likes()

print('Nome: {} - Ano: {} - Duração: {} horas - Likes: {}'.format(atlanta.nome, atlanta.ano, atlanta.temporadas, atlanta.likes))
