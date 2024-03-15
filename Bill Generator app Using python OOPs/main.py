from fpdf import FPDF
from filestack import Client

from roomates import the_bill, roommate_1, roommate_2


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        roommate1_pays = str(round(roommate1.pays(bill, roommate2), 2))
        roommate2_pays = str(round(roommate2.pays(bill, roommate1), 2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert the title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Roommate Bill', border=1, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=40, txt='Period:', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)
        # Insert Roommate names and payments
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=40, txt=roommate1.name, border=1)
        pdf.cell(w=150, h=40, txt=roommate1_pays, border=1, ln=1)
        pdf.cell(w=100, h=40, txt=roommate2.name, border=1)
        pdf.cell(w=150, h=40, txt=roommate2_pays, border=1, ln=1)

        pdf.output(f"files/{self.filename}")
        return f"files/{self.filename}"  # Return the path to the generated PDF file

class FileShare:
    def __init__(self, filepath, api_key="Axz4DvYVbRByuUS0IElArz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        try:
            new_filelink = client.upload(filepath=self.filepath)
            print("File uploaded successfully. URL:", new_filelink.url)
        except Exception as e:
            print("An error occurred while uploading the file:", e)

# Usage example
if __name__ == "__main__":
    # Your existing code for bill generation and roommate details...
    # ...

    # Generate PDF report
    pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
    pdf_path = pdf_report.generate(roommate1=roommate_1, roommate2=roommate_2, bill=the_bill)

    # Share the generated PDF file
    file_sharer = FileShare(filepath=pdf_path)
    file_sharer.share()
