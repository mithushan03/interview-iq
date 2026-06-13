import re
from html import escape
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def _normalize_answer_text(text: str) -> list[tuple[str, str]]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = re.sub(r"(?<!\n)\s+(\d+\.\s+\*\*)", r"\n\1", normalized)
    normalized = normalized.replace(" * **", "\n- **")
    normalized = re.sub(r"(?<!\n)\s+(\*\*[A-Z][^*]+?\*\*:)", r"\n\1", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)

    blocks: list[tuple[str, str]] = []
    for raw_line in normalized.split("\n"):
        line = raw_line.strip()
        if not line:
            continue

        bullet_match = re.match(r"^[-*]\s+(.+)", line)
        if bullet_match:
            blocks.append(("bullet", bullet_match.group(1)))
            continue

        numbered_match = re.match(r"^(\d+\.)\s+(.+)", line)
        if numbered_match:
            blocks.append(("numbered", f"{numbered_match.group(1)} {numbered_match.group(2)}"))
            continue

        blocks.append(("paragraph", line))

    return blocks


def _format_inline(text: str) -> str:
    escaped = escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"`(.+?)`", r"<font face='Courier'>\1</font>", escaped)
    return escaped


def build_questions_pdf(title: str, questions: list[dict]) -> bytes:
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    question_style = ParagraphStyle(
        "QuestionTitle",
        parent=styles["Heading3"],
        fontSize=13,
        leading=17,
        spaceAfter=8,
        textColor=colors.HexColor("#111827"),
    )
    label_style = ParagraphStyle(
        "SectionLabel",
        parent=styles["BodyText"],
        fontSize=10,
        leading=12,
        spaceAfter=4,
        textColor=colors.HexColor("#374151"),
    )
    body_style = ParagraphStyle(
        "ExportBody",
        parent=styles["BodyText"],
        fontSize=10,
        leading=14,
        spaceAfter=6,
        textColor=colors.HexColor("#111827"),
    )
    meta_style = ParagraphStyle(
        "Meta",
        parent=styles["BodyText"],
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#4B5563"),
    )
    bullet_style = ParagraphStyle(
        "Bullet",
        parent=body_style,
        leftIndent=12,
        firstLineIndent=0,
    )
    numbered_style = ParagraphStyle(
        "Numbered",
        parent=body_style,
        leftIndent=12,
        firstLineIndent=0,
    )

    story = [Paragraph(escape(title), title_style), Spacer(1, 14)]

    for index, question in enumerate(questions, start=1):
        story.append(Paragraph(escape(f"{index}. {question['question']}"), question_style))

        story.append(Paragraph("<b>Expected Answer</b>", label_style))
        for block_type, block_text in _normalize_answer_text(question["expected_answer"]):
            formatted = _format_inline(block_text)
            if block_type == "bullet":
                story.append(Paragraph(f"• {formatted}", bullet_style))
            elif block_type == "numbered":
                story.append(Paragraph(formatted, numbered_style))
            else:
                story.append(Paragraph(formatted, body_style))

        story.append(Spacer(1, 2))
        story.append(Paragraph("<b>Key Points</b>", label_style))
        for point in question["key_points"]:
            story.append(Paragraph(f"• {_format_inline(point)}", bullet_style))

        story.append(
            Paragraph(
                escape(f"Category: {question['category']} | Difficulty: {question['difficulty']}"),
                meta_style,
            )
        )
        story.append(Spacer(1, 12))

    doc.build(story)
    return buffer.getvalue()
