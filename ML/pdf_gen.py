from fpdf import FPDF

def generate_pdf(summary, scientific_formulas, chemical_formula, one_word_ans, keywords):
    
    summary1 = summary.encode('latin-1', 'replace').decode('latin-1')
    pdf = FPDF()
  
    
    pdf.add_page()
    
    
    pdf.set_font("Arial", 'B', size = 18)
    #pdf.image('../static/img/logopdf.jpg',100,0,20,20)
    pdf.cell(200, 10, txt = "", 
            ln = 1, align = 'C')
    pdf.cell(200, 10, txt = "", 
            ln = 1, align = 'C')

    pdf.cell(200, 10, txt = "Rapid notes", 
            ln = 1, align = 'C')
    
    #summary
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt = "Quick summary", 
            ln = 2, align = 'L')
    pdf.set_font("Arial", size = 13)
    pdf.multi_cell(200, 10, txt = summary1, 
            align = 'L')
    pdf.ln(0.5)

    #keywords
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt = "Important keywords", 
            ln = 2, align = 'L')
    pdf.set_font("Arial", size = 13)
    for keyword in keywords:
        pdf.cell(200, 10, txt = keyword.encode('latin-1', 'replace').decode('latin-1'), 
            ln = 2, align = 'L')


    #scientific formula
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt = "Scientific formula", 
            ln = 2, align = 'L')
    pdf.set_font("Arial", size = 13)
    for keyword in scientific_formulas:
        pdf.cell(200, 10, txt = keyword.encode('latin-1', 'replace').decode('latin-1'), 
            ln = 2, align = 'L')


    pdf.add_page()
    #chem data
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt = "Chemical formula", 
            ln = 2, align = 'L')
    pdf.set_font("Arial", size = 13)
    for keyword in chemical_formula:
        pdf.cell(200, 10, txt = keyword.encode('latin-1', 'replace').decode('latin-1'), 
            ln = 2, align = 'L')


    #QnA
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt = "Short questions", 
            ln = 2, align = 'L')
    pdf.set_font("Arial", size = 13)
    for keyword in one_word_ans:
        pdf.set_font('Arial', 'B', 13)
        pdf.cell(200, 10, txt = keyword[0].encode('latin-1', 'replace').decode('latin-1'), 
            ln = 2, align = 'L')
        pdf.set_font('Arial',size=13)
        pdf.cell(200, 10, txt = keyword[1].encode('latin-1', 'replace').decode('latin-1'), 
            ln = 2, align = 'L')

    
    
    pdf.output("test.pdf")
