from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, flowables

from write_number import monetario

from config import ISSUER, SESSION


def compose_texts(issuer: dict, session: dict) -> dict:
    written_cost = monetario(session["cost"])
    session["written_cost"] = written_cost

    texts = {
        "title_text": "<para align=center>RECIBO</para>",
        "summary_text": f"<para align=left>Valor total: R${str(session['cost'])},00 ({session['written_cost']})</para>",
        "main_text": f"<para align=left>Recebi de {session['name']} a importância de R${str(session['cost'])},00 ({session['written_cost']}) referente a uma sessão de psicoterapia, realizada no dia {session['date']}.</para>",
        "issuer_text": f"<para align=center> Emitente: {issuer['name']} <br /> CPF: {issuer['cpf']} </para>",
        "psychologist_text": f"<para align=center>{issuer['name']} <br /> Psicóloga <br /> CRP {issuer['crp']}</para>",
    }

    return texts


def format_paragraphs(texts: dict) -> list:
    styles = getSampleStyleSheet()

    flowables = []

    title = Paragraph(texts["title_text"], style=styles["Heading1"])
    flowables.append(title)

    spacer = Spacer(width=0, height=30)
    flowables.append(spacer)

    p = Paragraph(texts["summary_text"], style=styles["Normal"])
    flowables.append(p)

    spacer = Spacer(width=0, height=30)
    flowables.append(spacer)

    p = Paragraph(texts["main_text"], style=styles["Normal"])
    flowables.append(p)

    spacer = Spacer(width=0, height=30)
    flowables.append(spacer)

    p = Paragraph(texts["issuer_text"], style=styles["Normal"])
    flowables.append(p)

    spacer = Spacer(width=0, height=50)
    flowables.append(spacer)

    p = Paragraph(texts["psychologist_text"], style=styles["Normal"])
    flowables.append(p)

    return flowables


def build_doc(name: str, flowables: list) -> None:
    doc = SimpleDocTemplate(f"docs/{name}.pdf", pagesize=A4)

    doc.build(flowables)


def main() -> None:
    texts = compose_texts(issuer=ISSUER, session=SESSION)
    flowables = format_paragraphs(texts=texts)
    build_doc(name="recibo", flowables=flowables)


if __name__ == "__main__":
    main()
