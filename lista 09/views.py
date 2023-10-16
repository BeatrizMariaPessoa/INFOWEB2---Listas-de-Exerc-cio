from cliente import Cliente, NCliente

def cliente_inserir(nome, email, fone):
  cliente = Cliente(0, nome, email, fone)
  NCliente.inserir(cliente)
  
def cliente_atualizar(id, nome, email, fone):
  cliente = Cliente(id, nome, email, fone)
  NCliente.atualizar(cliente)