import frappe
from frappe.utils.pdf import get_pdf

def setup():
    md_file = "/home/ameer/.gemini/antigravity-ide/brain/5243906a-7176-4927-ac82-eacee5617ef2/sr_continental_staff_training_guide.md"
    pdf_file = "/home/ameer/.gemini/antigravity-ide/brain/5243906a-7176-4927-ac82-eacee5617ef2/sr_continental_staff_training_guide.pdf"
    
    with open(md_file, "r") as f:
        md_content = f.read()
        
    html_content = frappe.utils.md_to_html(md_content)
    
    # Wrap in basic HTML structure for pdfkit
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: sans-serif; padding: 20px; }}
            h1, h2, h3 {{ color: #333; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    pdf = get_pdf(html)
    with open(pdf_file, "wb") as f:
        f.write(pdf)
        
    print("PDF generated successfully.")
