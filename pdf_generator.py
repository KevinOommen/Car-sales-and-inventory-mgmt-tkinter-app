#module for creating a PDF of the invoice
#this module is to be imported into Main_menu.py
def create_pdf(textlines,invno):
    from reportlab.pdfgen import canvas
    from tkinter import filedialog as fdialog
    try:
        fileName=fdialog.asksaveasfilename(initialdir=r"C:\Python\Scripts\MY_Project\Generated_PDFs",defaultextension='.pdf',filetypes=[('PDF','.pdf')])
    except FileNotFoundError:
        pass
    #fileName = r"C:\Python\Scripts\MY_Project\Generated_PDFs".format(invno)
    documentTitle = f'Sales_Invoice_no:{invno}'

    image = 'header2.png'
    
    pdf = canvas.Canvas(fileName)
    pdf.setPageSize((1310, 800))
    
    pdf.setTitle(documentTitle)
    pdf.drawImage(image ,0,700)
    
    #Inserting text from the Text widget
    text = pdf.beginText(40,650)
    text.setFont("Times-Roman",16)
    for line in textlines:
        text.textLine(line)
    pdf.drawText(text)
    pdf.save()
