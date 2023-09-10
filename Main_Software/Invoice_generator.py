import pdfkit
from jinja2 import Template


class InvoiceGenerator:
    @staticmethod
    def read_text_file(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents = file.read()
                return file_contents
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return f"An error occurred: {e}"

    @staticmethod
    def generate_invoice_pdf(id, name, address, phone, invoice_date, products, payment_method, total_price, paid_amount, remaining_amount):
        # Load the HTML template
        with open(r'Main_Software\invoice.html', 'r', encoding='utf-8') as template_file:
            template_content = template_file.read()

        # hei = 125
        # Define customer details and product details
        cust_id = id
        customer_name = name
        customer_address = address
        customer_phone = phone
        invoice_date = invoice_date
        translation_dict = {
            "Cement": "सीमेंट",
            "Cement JK Super": "सीमेंट JK Super",
            "Cement Ultratech": "सीमेंट Ultratech",
            "Cement Wonder": "सीमेंट Wonder",
            "Cement shree": "सीमेंट shree",
            "Gitti": "गिट्टी",
            "Gitti 10mm": "गिट्टी 10mm",
            "Gitti 20mm": "गिट्टी 20mm",
            "Maurang": "मौरंग",
            "Maurang moti": "मौरंग मोटी",
            "Maurang medium": "मौरंग मीडियम",
            "Maurang Plaster": "मौरंग प्लास्टर",
            "Sariya": "सरिया",
            "Sariya 6mm": "सरिया 6mm",
            "Sariya 8mm": "सरिया 8mm",
            "Sariya 10mm": "सरिया 10mm",
            "Sariya 12mm": "सरिया 12mm",
            "Sariya 16mm": "सरिया 16mm",
            "Sariya 20mm": "सरिया 20mm",
            "Fan Box": "फैन बॉक्स",
            "Tar": "टार",
            "Tar Tata": "टार टाटा",
            "Tractor Bhada": "ट्रैक्टर भाड़ा",
            "Pichla Baki": "पिछला बाकी",
            "Labour unloading": "लेबर अनलोडिंग",
            "Blade": "ब्लेड",
            "PVC Pipe": "PVC पाइप",
            "Band": "बैंड",
            "LED Box": "LED बॉक्स",
            "Water proofing": "वॉटर प्रूफिंग",
            "Cover Block": "कवर ब्लॉक",
            "Rings": "रिंग",
            "Rings 7*7": "रिंग 7*7",
            "Rings 7*3": "रिंग 7*3",
            "Rings 7*10": "रिंग 7*10",
            "Rings 7*12": "रिंग 7*12",
            "PVC Band": "पीवीसी बैंड",
        }

        def convert_to_products_list(list_of_lists):
            hei = 0
            products_list = []
            for sublist in list_of_lists:
                if len(sublist[0]) > 16:
                    hei += 5
                if sublist[0] in translation_dict:
                    sublist[0] = translation_dict[sublist[0]]
                product = {
                    'name': sublist[0],
                    'quantity': sublist[1],
                    'rate': sublist[2],
                    'value': sublist[3]
                }
                products_list.append(product)

            return [products_list, hei]

        # ... (your data setup)
        products,hei = convert_to_products_list(products)
        hei += 125
        method_dict = {
            "Cash": "नकद",
            "Udhar": "उधार",
            "Jma": "जमा",
            "UPI": "UPI",
            "Cheque": "चेक"
        }
        if payment_method in method_dict:
            payment_method = method_dict[payment_method]
        payment_method = payment_method
        total_price = total_price
        paid_amount = paid_amount
        remaining_amount = remaining_amount
        # Create a Jinja2 template
        template = Template(template_content)

        # Render the template with dynamic data
        rendered_html = template.render(
            base64_image=InvoiceGenerator.read_text_file(
                r"Main_Software\logo_base64.txt"),
            id=cust_id,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_phone=customer_phone,
            invoice_date=invoice_date,
            products=products,
            payment_method=payment_method,
            total_price=total_price,
            paid_amount=paid_amount,
            remaining_amount=remaining_amount
            # ... (other data)
        )
        hei = hei + len(products)*10
        # print(len(products))
        # Configure pdfkit options
        options = {
            'page-height': hei,
            'page-width': '78',
            'encoding': 'UTF-8',
            'margin-top': '0in',
            'margin-right': '0.0in',
            'margin-bottom': '0in',
            'margin-left': '0in',
            'enable-local-file-access': None
        }

        # Generate the PDF
        path_to_wkhtmltopdf = r"Main_Software\wkhtmltopdf\bin\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
        pdfkit.from_string(rendered_html, './Main_Software/Image_pdf/Invoice.pdf',
                           options=options, configuration=config)

    def custom_test_case():
        # Define your test data
        id = "12345"
        
        name = "John Doe"
        address = "123 Main St"
        phone = "555-1234"
        invoice_date = "2023-08-26 12:00:00 PM"
        products = [
            ["Cement JK Super", "1500", "100", "150000"],
            ["Maurang Plaster", "1", "100", "1000"],
            ["Cement Ultratech", "1", "100", "1000"],
            ["Tractor Bhada", "1", "100", "1000"],
            ["Gitti", "15", "100", "25000"],
            ["Water proofing", "1", "100", "1000"],
            ["Cover Block", "15", "100", "25000"],
            ["", "", "कुल", "250000"]

        ]
        payment_method = "Cash"
        total_price = 500
        paid_amount = 200
        remaining_amount = 300

        # Call the generate_invoice_pdf function with the test data
        InvoiceGenerator.generate_invoice_pdf(
            id, name, address, phone, invoice_date, products, payment_method, total_price, paid_amount, remaining_amount)


# Call the static function to generate the PDF
# InvoiceGenerator.custom_test_case()
