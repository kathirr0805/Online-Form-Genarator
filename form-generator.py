from fpdf import FPDF


def collect_user_data():
    user_data = {}
    user_data['Name'] = input("Enter your name: ")
    user_data['Date of Birth'] = input("Enter your date of birth (DD/MM/YYYY): ")
    user_data['Address'] = input("Enter your address: ")
    user_data['Phone Number'] = input("Enter your phone number: ")
    user_data['Email'] = input("Enter your email: ")
    return user_data

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

def save_form_as_pdf(form_content, filename="user_form.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, form_content)
    pdf.output(filename)
    print(f"Form saved as {filename}")

if __name__ == "__main__":
    user_data = collect_user_data()
    form_content = format_form(user_data)
    
    # Save the form as a PDF
    save_form_as_pdf(form_content)
