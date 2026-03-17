import sys
import subprocess
try:
    import PyPDF2
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    import PyPDF2

def extract_pdf(pdf_path):
    reader = PyPDF2.PdfReader(pdf_path)
    text = []
    for page in reader.pages:
        text.append(page.extract_text())
    return "\n".join(text)

if __name__ == "__main__":
    text = extract_pdf("SwaraliShirke_Resume.pdf")
    with open("extracted_resume.txt", "w") as f:
        f.write(text)
    print("Extracted to extracted_resume.txt")
