from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from config import ISSUER, SESSIONS
from custom_types import Issuer, Sessions, Session
from write_number import monetario


def generate_for_all_dates(
    issuer: Issuer = ISSUER, sessions: Sessions = SESSIONS
) -> dict:
    all_texts: dict = {}

    for date in sessions["dates"]:
        session: Session = {}
        session["name"] = sessions["name"]
        session["cost"] = sessions["cost"]
        session["written_cost"] = monetario(session["cost"])
        session["date"] = date

        all_texts[date] = compose_texts(issuer=issuer, session=session)

    return all_texts


def compose_texts(issuer: Issuer, session: Session) -> dict:

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


def build_all_docs() -> None:
    all_texts = generate_for_all_dates()
    for date in all_texts:
        flowables = format_paragraphs(texts=all_texts[date])
        build_doc(name=f"recibo-{date.replace('/', '-')}", flowables=flowables)


def main() -> None:
    build_all_docs()


if __name__ == "__main__":
    main()
