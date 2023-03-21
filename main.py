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

    pdf.ln(270)
    pdf.set_font(family='Times', style="I", size=8)
    pdf.set_text_color(91, 77, 77)
    pdf.cell(w=0, h=8, txt=row['Topic'], align="R")

    pdf.image(x=10, y=281, w=5, h=5,
        name='kisspng-python-computer-icons-tutorial-computer-programmin-social-icons-5ad5ccbb30c4a8.2707803315239610191998.jpg',
              link='https://www.python.org/')
    for int in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.set_font(family='Times', style="B", size=30)
        pdf.set_text_color(62, 52, 206)
        pdf.cell(w=0, h=0, txt="  /  /  ", align="R")
        pdf.line(10, 20, 200, 20)
        pdf.image(x=10, y=281, w=5, h=5,
                  name='kisspng-python-computer-icons-tutorial-computer-programmin-social-icons-5ad5ccbb30c4a8.2707803315239610191998.jpg',
                  link='https://www.python.org/')

        pdf.ln(270)

        pdf.set_font(family='Times', style="I", size=8)
        pdf.set_text_color(91, 77, 77)
        pdf.cell(w=0, h=8, txt=row['Topic'], align="R")




pdf.output("output.pdf")
