from fpdf import FPDF
import pandas as pd

data = pd.read_csv('topics.csv')

pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style="I", size=30)
    pdf.set_text_color(62, 52, 206)
    pdf.cell(w=0, h=0, txt=row['Topic'], align="L", ln=1)
    pdf.cell(w=0, h=0, txt="  /  /  ", align="R")
    pdf.line(10,20, 200, 20)

pdf.output("output.pdf")
