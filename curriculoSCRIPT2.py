from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# ══════════════════════════════════════════════════════════════
#  ARQUIVO DE SAÍDA
# ══════════════════════════════════════════════════════════════
OUTPUT = "curriculoTESTE.pdf"  # [alterar aqui] nome do arquivo gerado


# ══════════════════════════════════════════════════════════════
#  DADOS PESSOAIS
# ══════════════════════════════════════════════════════════════
NOME            = "NOME DE EXEMPLO"                        # [alterar aqui]
TITULO          = "PROFISSÃO E OBJETIVO"        # [alterar aqui]
ENDERECO        = "ENDEREÇO"  # [alterar aqui]
TELEFONE        = "TELEFONE"                              # [alterar aqui]
EMAIL           = "EMAIL"                      # [alterar aqui]
NASCIMENTO      = "DATA"                                   # [alterar aqui]
CNH             = "CARTEIRA DE HABILITAÇÃO"  # [alterar aqui] ou deixe "" para omitir
#CASO QUEIRA ADICIONAR ALGO MAIS

# ══════════════════════════════════════════════════════════════
#  OBJETIVO
# ══════════════════════════════════════════════════════════════
OBJETIVO = (
    "OBJETIVO"
    "OBJETIVO"
    "OBJJETIVO"
)  # [alterar aqui]


# ══════════════════════════════════════════════════════════════
#  EXPERIÊNCIA PROFISSIONAL
#  Formato: ("Nome da Empresa", "Cargo", "Período")
#  Adicione ou remova linhas conforme necessário
# ══════════════════════════════════════════════════════════════
EXPERIENCIAS = [
    ("EMPRESA LTDA",                                                                        "FUNÇÃO",       "DATAINICIO – DATA FINAL"),  # [alterar aqui]
    ("EMPRESA LTDA",                                                                        "FUNÇÃO",       "DATAINICIO – DATA FINAL"),  # [alterar aqui]
    ("EMPRESA LTDA",                                                                        "FUNÇÃO",       "DATAINICIO – DATA FINAL"),  # [alterar aqui]
    ("EMPRESA LTDA",                                                                        "FUNÇÃO",       "DATAINICIO – DATA FINAL"),  # [alterar aqui]
    ("EMPRESA LTDA",                                                                        "FUNÇÃO",       "DATAINICIO – DATA FINAL"),  # [alterar aqui]
    ("EMPRESA LTDA",                                                                        "FUNÇÃO",       "DATAINICIO – DATA FINAL"),  # [alterar aqui]
]


# ══════════════════════════════════════════════════════════════
#  ESCOLARIDADE
#  Formato: ("Nível / Curso", "Instituição", "Período")
#  Deixe Instituição e Período como "" se não quiser exibir
# ══════════════════════════════════════════════════════════════
ESCOLARIDADE = [
    ("UNIVERSIDADE", "DATAINICIO – DATAFINAL", "NOME INSTITUIÇÃO"),  # [alterar aqui]
    ("ESCOLARIDADE",       "",               ""),                     # [alterar aqui]
]


# ══════════════════════════════════════════════════════════════
#  CURSOS E CERTIFICAÇÕES
#  Adicione ou remova itens conforme necessário
# ══════════════════════════════════════════════════════════════
CURSOS = [
    "CURSOS",  # [alterar aqui]
    "CURSOS",                    # [alterar aqui]
    "CURSOS",                                      # [alterar aqui]
    "CURSOS",                                   # [alterar aqui]
]


# ══════════════════════════════════════════════════════════════
#  CORES  (códigos hex — não precisa alterar se gostar do visual)
# ══════════════════════════════════════════════════════════════
AZUL_ESCURO = colors.HexColor("#1B3A6B")   # [alterar aqui caso queria mudar a cor] cabeçalho
AZUL_MED    = colors.HexColor("#2E5FA3")   # [alterar aqui caso queria mudar a cor] subtítulo e destaques
AZUL_CLARO  = colors.HexColor("#D6E4F7")   # [alterar aqui caso queria mudar a cor] texto do subtítulo
CINZA_TEXTO = colors.HexColor("#333333")   # [alterar aqui caso queria mudar a cor] texto geral
BRANCO      = colors.white


# ══════════════════════════════════════════════════════════════
#  MARGEM (igual nos 4 lados = margem "quadrada")
# ══════════════════════════════════════════════════════════════
MARGEM = 1.9 * cm   # [alterar aqui caso queira alterar a margem] ex: 2.0*cm, 1.5*cm


# ════════════════════════════════════════════════════════════════════
#  NÃO PRECISA ALTERAR ABAIXO DESTA LINHA CASO QUEIRA O LAYOUT PADRÃO
# ════════════════════════════════════════════════════════════════════

def estilos():
    nome_s = ParagraphStyle("nome", fontName="Helvetica-Bold", fontSize=22,
        textColor=BRANCO, alignment=TA_CENTER, spaceAfter=2, leading=26)
    subtitulo_s = ParagraphStyle("subtitulo", fontName="Helvetica-Oblique", fontSize=10,
        textColor=AZUL_CLARO, alignment=TA_CENTER, spaceAfter=0, leading=14)
    contato_s = ParagraphStyle("contato", fontName="Helvetica", fontSize=8.5,
        textColor=CINZA_TEXTO, alignment=TA_CENTER, spaceAfter=0, leading=12)
    sec_s = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=9.5,
        textColor=AZUL_ESCURO, alignment=TA_LEFT, spaceBefore=14, spaceAfter=4,
        letterSpacing=1.2, leading=14)
    empresa_s = ParagraphStyle("empresa", fontName="Helvetica-Bold", fontSize=10,
        textColor=AZUL_ESCURO, alignment=TA_LEFT, spaceBefore=8, spaceAfter=1, leading=13)
    cargo_s = ParagraphStyle("cargo", fontName="Helvetica", fontSize=9,
        textColor=CINZA_TEXTO, alignment=TA_LEFT, spaceAfter=4, leading=12)
    label_s = ParagraphStyle("label", fontName="Helvetica", fontSize=9.5,
        textColor=CINZA_TEXTO, alignment=TA_LEFT, spaceBefore=3, spaceAfter=3, leading=14)
    normal_s = ParagraphStyle("normal", fontName="Helvetica", fontSize=9.5,
        textColor=CINZA_TEXTO, alignment=TA_LEFT, spaceBefore=3, spaceAfter=3, leading=14)
    bullet_s = ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.5,
        textColor=CINZA_TEXTO, alignment=TA_LEFT, leftIndent=14,
        spaceBefore=3, spaceAfter=3, leading=14)
    return dict(nome=nome_s, subtitulo=subtitulo_s, contato=contato_s, sec=sec_s,
                empresa=empresa_s, cargo=cargo_s, label=label_s, normal=normal_s, bullet=bullet_s)

E = estilos()
LARGURA = A4[0] - 2 * MARGEM

def divisor():
    return HRFlowable(width="100%", thickness=1.2, color=AZUL_MED, spaceAfter=6, spaceBefore=0)

def secao(titulo):
    return [Paragraph(titulo.upper(), E["sec"]), divisor()]

def bloco_emprego(empresa, cargo, periodo):
    linha = f'{cargo}'
    if periodo:
        linha += f' &nbsp;&nbsp;<font color="#AAAAAA">|</font>&nbsp;&nbsp; <font color="#2E5FA3"><i>{periodo}</i></font>'
    return [Paragraph(empresa, E["empresa"]), Paragraph(linha, E["cargo"]), Spacer(1, 3)]

def bloco_escolaridade(nivel, instituicao, periodo):
    txt = f'<b><font color="#2E5FA3">{nivel}</font></b>'
    if instituicao:
        txt += f'  {instituicao}'
    if periodo:
        txt += f' &nbsp;|&nbsp; <font color="#2E5FA3"><i>{periodo}</i></font>'
    return Paragraph(txt, E["label"])

# ── Montar story ───────────────────────────────────────────────
story = []

# Cabeçalho
header_table = Table([[Paragraph(NOME, E["nome"])]], colWidths=[LARGURA])
header_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), AZUL_ESCURO),
    ("TOPPADDING",    (0,0), (-1,-1), 14),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING",   (0,0), (-1,-1), 10),
    ("RIGHTPADDING",  (0,0), (-1,-1), 10),
]))
story.append(header_table)

sub_table = Table([[Paragraph(TITULO, E["subtitulo"])]], colWidths=[LARGURA])
sub_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), AZUL_MED),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("LEFTPADDING",   (0,0), (-1,-1), 10),
    ("RIGHTPADDING",  (0,0), (-1,-1), 10),
]))
story.append(sub_table)
story.append(Spacer(1, 8))

story.append(Paragraph(
    f"{ENDERECO} &nbsp;|&nbsp; {TELEFONE} &nbsp;|&nbsp; {EMAIL}", E["contato"]))
story.append(Spacer(1, 12))

# Dados pessoais
story += secao("Dados Pessoais")
story.append(Paragraph(f'<b><font color="#2E5FA3">Data de Nascimento:</font></b>  {NASCIMENTO}', E["label"]))
if CNH:
    story.append(Paragraph(f'<b><font color="#2E5FA3">CNH:</font></b>  {CNH}', E["label"]))
story.append(Spacer(1, 4))

# Objetivo
story += secao("Objetivo Profissional")
story.append(Paragraph(OBJETIVO, E["normal"]))
story.append(Spacer(1, 4))

# Experiência
story += secao("Experiência Profissional")
for emp, cargo, per in EXPERIENCIAS:
    story += bloco_emprego(emp, cargo, per)
story.append(Spacer(1, 4))

# Escolaridade
story += secao("Escolaridade")
for nivel, inst, per in ESCOLARIDADE:
    story.append(bloco_escolaridade(nivel, inst, per))
story.append(Spacer(1, 4))

# Cursos
story += secao("Cursos e Certificações")
for curso in CURSOS:
    story.append(Paragraph(f"&#9642; &nbsp; {curso}", E["bullet"]))

story.append(Spacer(1, 18))

# Gerar PDF
doc = SimpleDocTemplate(OUTPUT, pagesize=A4,
    leftMargin=MARGEM, rightMargin=MARGEM,
    topMargin=MARGEM, bottomMargin=MARGEM,
    title=f"Currículo — {NOME.title()}",
    author=NOME.title())
doc.build(story)
print(f"PDF gerado: {OUTPUT}")