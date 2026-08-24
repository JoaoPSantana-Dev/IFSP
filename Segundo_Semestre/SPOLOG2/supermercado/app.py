import os

from datetime import datetime

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    send_file
)

from openpyxl import Workbook

from database import (
    get_connection,
    init_db
)


app = Flask(__name__)

app.secret_key = "supermercado-chave-aula"


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

EXPORT_DIR = os.path.join(
    BASE_DIR,
    "exports"
)

os.makedirs(
    EXPORT_DIR,
    exist_ok=True
)


# ---------------------------------------------------
# FUN��ES AUXILIARES
# ---------------------------------------------------

def converter_float(valor):
    """
    Permite:
    10.50
    ou
    10,50
    """

    if valor is None:
        return 0

    valor = valor.strip()

    valor = valor.replace(",", ".")

    return float(valor)


def carregar_itens_formulario(conn):
    """
    Recebe os produtos selecionados no formul�rio
    do caixa e transforma os dados em uma estrutura
    para processamento.
    """

    produtos_ids = request.form.getlist(
        "produto_id"
    )

    quantidades = request.form.getlist(
        "quantidade"
    )

    itens_agregados = {}

    for produto_id, quantidade in zip(
        produtos_ids,
        quantidades
    ):

        if not produto_id:
            continue

        try:
            quantidade = int(quantidade)
        except ValueError:
            continue

        if quantidade <= 0:
            continue

        produto_id = int(produto_id)

        if produto_id in itens_agregados:
            itens_agregados[produto_id] += quantidade
        else:
            itens_agregados[produto_id] = quantidade

    if not itens_agregados:
        raise ValueError(
            "Selecione pelo menos um produto."
        )

    itens = []

    for produto_id, quantidade in itens_agregados.items():

        produto = conn.execute(
            """
            SELECT *
            FROM produtos
            WHERE id = ?
            """,
            (produto_id,)
        ).fetchone()

        if produto is None:
            raise ValueError(
                "Produto n�o encontrado."
            )

        if quantidade > produto["estoque"]:
            raise ValueError(
                f'Estoque insuficiente para '
                f'{produto["nome"]}. '
                f'Dispon�vel: {produto["estoque"]}.'
            )

        subtotal = (
            quantidade *
            produto["preco"]
        )

        itens.append(
            {
                "produto_id": produto["id"],

                "produto_nome":
                    produto["nome"],

                "quantidade":
                    quantidade,

                "preco_unitario":
                    produto["preco"],

                "subtotal":
                    subtotal
            }
        )

    return itens


# ---------------------------------------------------
# IN�CIO
# ---------------------------------------------------

@app.route("/")
def index():

    conn = get_connection()

    quantidade_produtos = conn.execute(
        """
        SELECT COUNT(*) AS total
        FROM produtos
        """
    ).fetchone()["total"]

    quantidade_compras = conn.execute(
        """
        SELECT COUNT(*) AS total
        FROM compras
        """
    ).fetchone()["total"]

    faturamento = conn.execute(
        """
        SELECT COALESCE(
            SUM(total),
            0
        ) AS total
        FROM compras
        """
    ).fetchone()["total"]

    conn.close()

    return render_template(
        "index.html",
        quantidade_produtos=quantidade_produtos,
        quantidade_compras=quantidade_compras,
        faturamento=faturamento
    )


# ===================================================
# PRODUTOS
# ===================================================


# ---------------------------------------------------
# CONSULTAR PRODUTOS
# ---------------------------------------------------

@app.route("/produtos")
def listar_produtos():

    pesquisa = request.args.get(
        "q",
        ""
    ).strip()

    categoria = request.args.get(
        "categoria",
        ""
    ).strip()

    conn = get_connection()

    sql = """
        SELECT *
        FROM produtos
        WHERE 1 = 1
    """

    parametros = []

    if pesquisa:

        sql += """
            AND (
                nome LIKE ?
                OR fabricante LIKE ?
            )
        """

        termo = f"%{pesquisa}%"

        parametros.extend(
            [
                termo,
                termo
            ]
        )

    if categoria:

        sql += """
            AND categoria LIKE ?
        """

        parametros.append(
            f"%{categoria}%"
        )

    sql += """
        ORDER BY
            categoria,
            nome
    """

    produtos = conn.execute(
        sql,
        parametros
    ).fetchall()

    conn.close()

    return render_template(
        "produtos/listar.html",
        produtos=produtos,
        pesquisa=pesquisa,
        categoria=categoria
    )


# ---------------------------------------------------
# INCLUIR PRODUTO
# ---------------------------------------------------

@app.route(
    "/produtos/novo",
    methods=["GET", "POST"]
)
def novo_produto():

    if request.method == "POST":

        try:

            nome = request.form[
                "nome"
            ].strip()

            categoria = request.form[
                "categoria"
            ].strip()

            fabricante = request.form[
                "fabricante"
            ].strip()

            unidade = request.form[
                "unidade"
            ].strip()

            preco = converter_float(
                request.form["preco"]
            )

            estoque = int(
                request.form["estoque"]
            )

            if not nome:
                raise ValueError(
                    "Informe o nome."
                )

            if not categoria:
                raise ValueError(
                    "Informe a categoria."
                )

            if preco < 0:
                raise ValueError(
                    "Pre�o inv�lido."
                )

            if estoque < 0:
                raise ValueError(
                    "Estoque inv�lido."
                )

            conn = get_connection()

            conn.execute(
                """
                INSERT INTO produtos (
                    nome,
                    categoria,
                    fabricante,
                    unidade,
                    preco,
                    estoque
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    nome,
                    categoria,
                    fabricante,
                    unidade,
                    preco,
                    estoque
                )
            )

            conn.commit()

            conn.close()

            flash(
                "Produto cadastrado com sucesso."
            )

            return redirect(
                url_for(
                    "listar_produtos"
                )
            )

        except (
            ValueError,
            KeyError
        ) as erro:

            flash(
                f"Erro: {erro}"
            )

    return render_template(
        "produtos/form.html",
        produto=None
    )


# ---------------------------------------------------
# ALTERAR PRODUTO
# ---------------------------------------------------

@app.route(
    "/produtos/editar/<int:id>",
    methods=["GET", "POST"]
)
def editar_produto(id):

    conn = get_connection()

    produto = conn.execute(
        """
        SELECT *
        FROM produtos
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    if produto is None:

        conn.close()

        return "Produto n�o encontrado.", 404

    if request.method == "POST":

        try:

            nome = request.form[
                "nome"
            ].strip()

            categoria = request.form[
                "categoria"
            ].strip()

            fabricante = request.form[
                "fabricante"
            ].strip()

            unidade = request.form[
                "unidade"
            ].strip()

            preco = converter_float(
                request.form["preco"]
            )

            estoque = int(
                request.form["estoque"]
            )

            if not nome:
                raise ValueError(
                    "Nome obrigat�rio."
                )

            if not categoria:
                raise ValueError(
                    "Categoria obrigat�ria."
                )

            if preco < 0:
                raise ValueError(
                    "Pre�o inv�lido."
                )

            if estoque < 0:
                raise ValueError(
                    "Estoque inv�lido."
                )

            conn.execute(
                """
                UPDATE produtos

                SET
                    nome = ?,
                    categoria = ?,
                    fabricante = ?,
                    unidade = ?,
                    preco = ?,
                    estoque = ?

                WHERE id = ?
                """,
                (
                    nome,
                    categoria,
                    fabricante,
                    unidade,
                    preco,
                    estoque,
                    id
                )
            )

            conn.commit()

            conn.close()

            flash(
                "Produto alterado com sucesso."
            )

            return redirect(
                url_for(
                    "listar_produtos"
                )
            )

        except ValueError as erro:

            flash(
                f"Erro: {erro}"
            )

    conn.close()

    return render_template(
        "produtos/form.html",
        produto=produto
    )


# ---------------------------------------------------
# EXCLUIR PRODUTO
# ---------------------------------------------------

@app.post(
    "/produtos/excluir/<int:id>"
)
def excluir_produto(id):

    conn = get_connection()

    conn.execute(
        """
        DELETE FROM produtos
        WHERE id = ?
        """,
        (id,)
    )

    conn.commit()

    conn.close()

    flash(
        "Produto exclu�do."
    )

    return redirect(
        url_for(
            "listar_produtos"
        )
    )


# ---------------------------------------------------
# EXPORTAR PRODUTOS
# ---------------------------------------------------

@app.route(
    "/produtos/exportar"
)
def exportar_produtos():

    conn = get_connection()

    produtos = conn.execute(
        """
        SELECT *
        FROM produtos

        ORDER BY
            categoria,
            nome
        """
    ).fetchall()

    conn.close()

    workbook = Workbook()

    planilha = workbook.active

    planilha.title = "Produtos"

    planilha.append(
        [
            "ID",
            "Nome",
            "Categoria",
            "Fabricante",
            "Unidade",
            "Pre�o",
            "Estoque"
        ]
    )

    for produto in produtos:

        planilha.append(
            [
                produto["id"],
                produto["nome"],
                produto["categoria"],
                produto["fabricante"],
                produto["unidade"],
                produto["preco"],
                produto["estoque"]
            ]
        )

    arquivo = os.path.join(
        EXPORT_DIR,
        "produtos.xlsx"
    )

    workbook.save(
        arquivo
    )

    return send_file(
        arquivo,
        as_attachment=True,
        download_name="produtos.xlsx"
    )


# ===================================================
# COMPRAS / CAIXA
# ===================================================


# ---------------------------------------------------
# CONSULTAR COMPRAS
# ---------------------------------------------------

@app.route("/compras")
def listar_compras():

    pesquisa = request.args.get(
        "q",
        ""
    ).strip()

    conn = get_connection()

    if pesquisa:

        compras = conn.execute(
            """
            SELECT *
            FROM compras

            WHERE
                cliente LIKE ?
                OR data_hora LIKE ?

            ORDER BY
                data_hora DESC
            """,
            (
                f"%{pesquisa}%",
                f"%{pesquisa}%"
            )
        ).fetchall()

    else:

        compras = conn.execute(
            """
            SELECT *
            FROM compras

            ORDER BY
                data_hora DESC
            """
        ).fetchall()

    conn.close()

    return render_template(
        "compras/listar.html",
        compras=compras,
        pesquisa=pesquisa
    )


# ---------------------------------------------------
# NOVA COMPRA
# ---------------------------------------------------

@app.route(
    "/compras/nova",
    methods=["GET", "POST"]
)
def nova_compra():

    conn = get_connection()

    produtos = conn.execute(
        """
        SELECT *
        FROM produtos

        ORDER BY
            categoria,
            nome
        """
    ).fetchall()

    if request.method == "POST":

        try:

            cliente = request.form[
                "cliente"
            ].strip()

            if not cliente:
                raise ValueError(
                    "Informe o nome do cliente."
                )

            with conn:

                itens = carregar_itens_formulario(
                    conn
                )

                total = sum(
                    item["subtotal"]
                    for item in itens
                )

                data_hora = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                cursor = conn.execute(
                    """
                    INSERT INTO compras (
                        cliente,
                        data_hora,
                        total
                    )

                    VALUES (?, ?, ?)
                    """,
                    (
                        cliente,
                        data_hora,
                        total
                    )
                )

                compra_id = cursor.lastrowid

                for item in itens:

                    conn.execute(
                        """
                        INSERT INTO itens_compra (
                            compra_id,
                            produto_id,
                            produto_nome,
                            quantidade,
                            preco_unitario,
                            subtotal
                        )

                        VALUES (
                            ?, ?, ?, ?, ?, ?
                        )
                        """,
                        (
                            compra_id,
                            item["produto_id"],
                            item["produto_nome"],
                            item["quantidade"],
                            item["preco_unitario"],
                            item["subtotal"]
                        )
                    )

                    conn.execute(
                        """
                        UPDATE produtos

                        SET estoque =
                            estoque - ?

                        WHERE id = ?
                        """,
                        (
                            item["quantidade"],
                            item["produto_id"]
                        )
                    )

            conn.close()

            flash(
                "Compra registrada com sucesso."
            )

            return redirect(
                url_for(
                    "detalhe_compra",
                    id=compra_id
                )
            )

        except ValueError as erro:

            flash(
                f"Erro: {erro}"
            )

    conn.close()

    return render_template(
        "compras/form.html",
        compra=None,
        itens=[],
        produtos=produtos
    )


# ---------------------------------------------------
# DETALHE DA COMPRA
# ---------------------------------------------------

@app.route(
    "/compras/<int:id>"
)
def detalhe_compra(id):

    conn = get_connection()

    compra = conn.execute(
        """
        SELECT *
        FROM compras
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    if compra is None:

        conn.close()

        return "Compra n�o encontrada.", 404

    itens = conn.execute(
        """
        SELECT *
        FROM itens_compra

        WHERE compra_id = ?

        ORDER BY id
        """,
        (id,)
    ).fetchall()

    conn.close()

    return render_template(
        "compras/detalhe.html",
        compra=compra,
        itens=itens
    )


# ---------------------------------------------------
# ALTERAR COMPRA
# ---------------------------------------------------

@app.route(
    "/compras/editar/<int:id>",
    methods=["GET", "POST"]
)
def editar_compra(id):

    conn = get_connection()

    compra = conn.execute(
        """
        SELECT *
        FROM compras
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    if compra is None:

        conn.close()

        return "Compra n�o encontrada.", 404

    itens_antigos = conn.execute(
        """
        SELECT *
        FROM itens_compra

        WHERE compra_id = ?

        ORDER BY id
        """,
        (id,)
    ).fetchall()

    produtos = conn.execute(
        """
        SELECT *
        FROM produtos

        ORDER BY
            categoria,
            nome
        """
    ).fetchall()

    if request.method == "POST":

        try:

            cliente = request.form[
                "cliente"
            ].strip()

            if not cliente:
                raise ValueError(
                    "Informe o cliente."
                )

            with conn:

                # Devolve ao estoque os produtos
                # da compra antiga.

                for item in itens_antigos:

                    conn.execute(
                        """
                        UPDATE produtos

                        SET estoque =
                            estoque + ?

                        WHERE id = ?
                        """,
                        (
                            item["quantidade"],
                            item["produto_id"]
                        )
                    )

                # Agora processamos os novos itens.

                novos_itens = (
                    carregar_itens_formulario(
                        conn
                    )
                )

                novo_total = sum(
                    item["subtotal"]
                    for item in novos_itens
                )

                conn.execute(
                    """
                    UPDATE compras

                    SET
                        cliente = ?,
                        total = ?

                    WHERE id = ?
                    """,
                    (
                        cliente,
                        novo_total,
                        id
                    )
                )

                conn.execute(
                    """
                    DELETE FROM itens_compra
                    WHERE compra_id = ?
                    """,
                    (id,)
                )

                for item in novos_itens:

                    conn.execute(
                        """
                        INSERT INTO itens_compra (
                            compra_id,
                            produto_id,
                            produto_nome,
                            quantidade,
                            preco_unitario,
                            subtotal
                        )

                        VALUES (
                            ?, ?, ?, ?, ?, ?
                        )
                        """,
                        (
                            id,
                            item["produto_id"],
                            item["produto_nome"],
                            item["quantidade"],
                            item["preco_unitario"],
                            item["subtotal"]
                        )
                    )

                    conn.execute(
                        """
                        UPDATE produtos

                        SET estoque =
                            estoque - ?

                        WHERE id = ?
                        """,
                        (
                            item["quantidade"],
                            item["produto_id"]
                        )
                    )

            conn.close()

            flash(
                "Compra alterada com sucesso."
            )

            return redirect(
                url_for(
                    "detalhe_compra",
                    id=id
                )
            )

        except ValueError as erro:

            flash(
                f"Erro: {erro}"
            )

    conn.close()

    return render_template(
        "compras/form.html",
        compra=compra,
        itens=itens_antigos,
        produtos=produtos
    )


# ---------------------------------------------------
# EXCLUIR COMPRA
# ---------------------------------------------------

@app.post(
    "/compras/excluir/<int:id>"
)
def excluir_compra(id):

    conn = get_connection()

    itens = conn.execute(
        """
        SELECT *
        FROM itens_compra

        WHERE compra_id = ?
        """,
        (id,)
    ).fetchall()

    with conn:

        # Quando a compra � exclu�da,
        # as mercadorias voltam ao estoque.

        for item in itens:

            if item["produto_id"] is not None:

                conn.execute(
                    """
                    UPDATE produtos

                    SET estoque =
                        estoque + ?

                    WHERE id = ?
                    """,
                    (
                        item["quantidade"],
                        item["produto_id"]
                    )
                )

        conn.execute(
            """
            DELETE FROM compras
            WHERE id = ?
            """,
            (id,)
        )

    conn.close()

    flash(
        "Compra exclu�da e estoque restaurado."
    )

    return redirect(
        url_for(
            "listar_compras"
        )
    )


# ---------------------------------------------------
# EXPORTAR COMPRAS
# ---------------------------------------------------

@app.route(
    "/compras/exportar"
)
def exportar_compras():

    conn = get_connection()

    registros = conn.execute(
        """
        SELECT
            c.id AS compra_id,
            c.cliente,
            c.data_hora,
            i.produto_nome,
            i.quantidade,
            i.preco_unitario,
            i.subtotal,
            c.total

        FROM compras c

        JOIN itens_compra i
            ON i.compra_id = c.id

        ORDER BY
            c.data_hora,
            c.id,
            i.id
        """
    ).fetchall()

    conn.close()

    workbook = Workbook()

    planilha = workbook.active

    planilha.title = "Compras"

    planilha.append(
        [
            "Compra",
            "Cliente",
            "Data/Hora",
            "Produto",
            "Quantidade",
            "Pre�o Unit�rio",
            "Subtotal",
            "Total da Compra"
        ]
    )

    for registro in registros:

        planilha.append(
            [
                registro["compra_id"],
                registro["cliente"],
                registro["data_hora"],
                registro["produto_nome"],
                registro["quantidade"],
                registro["preco_unitario"],
                registro["subtotal"],
                registro["total"]
            ]
        )

    arquivo = os.path.join(
        EXPORT_DIR,
        "compras.xlsx"
    )

    workbook.save(
        arquivo
    )

    return send_file(
        arquivo,
        as_attachment=True,
        download_name="compras.xlsx"
    )


# ---------------------------------------------------
# EXECU��O
# ---------------------------------------------------

if __name__ == "__main__":

    init_db()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

