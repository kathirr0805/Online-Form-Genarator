from flask import Flask, render_template, request, jsonify, send_file
from fpdf import FPDF
import io

app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Collect form data
        user_data = {
            'Name': request.form.get('name'),
            'Date of Birth': request.form.get('dob'),
            'Address': request.form.get('address'),
            'Phone Number': request.form.get('phone'),
            'Email': request.form.get('email')
        }

        # Check for missing fields
        if any(value is None for value in user_data.values()):
            return jsonify({"error": "All fields are required."}), 400

        # Format the form content
        form_content = format_form(user_data)

        # Create a PDF and return it as a response
        pdf_output = create_pdf(form_content)
        return send_file(pdf_output, attachment_filename="user_form.pdf", as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def format_form(user_data):
    form_template = f"""
    -----------------------------
             User Form
    -----------------------------
    Name: {user_data['Name']}
    Date of Birth: {user_data['Date of Birth']}
    Address: {user_data['Address']}
    Phone Number: {user_data['Phone Number']}
    Email: {user_data['Email']}
    -----------------------------
    """
    return form_template

def create_pdf(form_content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, form_content)

    # Save the PDF to a BytesIO object and return it
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    return pdf_output

if __name__ == '__main__':
    app.run(debug=True, port=8080)
