from conta import Conta
from data import Data

d = Data(18,4,2023)
conta = Conta(123,"rafael",1000,2345)
conta2 = Conta(123,"rafael",1000,2345)

d.formatada()
conta.extrato()
conta.deposito(1200)
conta.extrato()
