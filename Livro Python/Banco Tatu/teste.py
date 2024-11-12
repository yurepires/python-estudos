from clientes import Cliente
from contas import Conta, ContaEspecial
from bancos import Banco
yure = Cliente('Yure Pires', '777-1234')
maria = Cliente('Maria da Silva', '555-4321')
jose = Cliente('Jóse Maria', '333-2134')
contaJM = Conta([jose, maria], 100, 1000)
contay = Conta([yure], 10)
conta2 = ContaEspecial([maria, yure], 2, 500, 1000)
tatu = Banco('Tatú')
conta2.saque(1500)
conta2.extrato()
