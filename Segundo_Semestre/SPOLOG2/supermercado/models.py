from dataclasses import dataclass, field


@dataclass
class Produto:
    id: int | None
    nome: str
    categoria: str
    fabricante: str
    unidade: str
    preco: float
    estoque: int


@dataclass
class ItemCompra:
    produto_id: int
    produto_nome: str
    quantidade: int
    preco_unitario: float

    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario


@dataclass
class Compra:
    id: int | None
    cliente: str
    data_hora: str
    itens: list[ItemCompra] = field(default_factory=list)

    @property
    def total(self):
        return sum(item.subtotal for item in self.itens)

