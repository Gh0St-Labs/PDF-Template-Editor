from fpdf import FPDF
import pandas as pd

data = pd.read_csv('topics.csv')

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
# What this above statement does is that when any kind of instance like an image, text, cell, etc is out of the
# page's orientation, it does not tend to move to the next page, rather it hides under the next page and is not
# shown outside.

for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style="B", size=30)
    pdf.set_text_color(62, 52, 206)
    pdf.cell(w=0, h=0, txt=row['Topic'], align="L", ln=1)
    pdf.cell(w=0, h=0, txt="  /  /  ", align="R")
    pdf.line(10,20, 200, 20)
    for i in range(20, 290, 10):
        pdf.line(10, i, 200, i)

    pdf.ln(270)
    pdf.set_font(family='Times', style="I", size=8)
    pdf.set_text_color(91, 77, 77)
    pdf.cell(w=0, h=8, txt=row['Topic'], align="R")
    for int in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.set_font(family='Times', style="B", size=30)
        pdf.set_text_color(62, 52, 206)
        pdf.cell(w=0, h=0, txt="  /  /  ", align="R")
        pdf.line(10, 20, 200, 20)

        pdf.ln(270)

        pdf.set_font(family='Times', style="I", size=8)
        pdf.set_text_color(91, 77, 77)
        pdf.cell(w=0, h=8, txt=row['Topic'], align="R")
        for i in range(20, 290, 10):
            pdf.line(10, i, 200, i)



pdf.output("output.pdf")
