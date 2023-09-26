import pdfkit
from jinja2 import Template
from All_function import all_function


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
        products, hei = convert_to_products_list(products)
        print(products)
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


    @staticmethod
    def Customer_details_pdf_create(id):
        html_template = ""
        first_html_content = """
        <!DOCTYPE html>
<html>
<head>
    <title>Customer Purchase Details</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 16px;
        }
        .container {
            margin: 20px;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        .company-details {
            font-weight: bold;
            font-size: 24px;
            margin-bottom: 10px;
        }
        .address {
            font-size: 18px;
            text-align: center;
        }
        .customer-details {
            margin-top: 20px;
            font-size: 18px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 2px solid #000;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        .payment-details {
            margin-top: 20px;
            font-weight: bold;
        }
        .tagline {
            margin-top: 20px;
            text-align: center;
        }
        .table_header{
            font-weight: bold;
            font-size: 20px;
            margin-top: 10px;
            text-align: center;
        }
        table tr:first-child {
            border-top: 2px solid black; /* You can change the color and style as needed */
          }
        .horizontal-line {
            border: none; /* Remove the default border */
            height: 2px; /* Set the height of the horizontal line */
            background-color: red; /* Set the background color (you can change it) */
        }
         .box {
            border: 4px solid black; 
            width: auto; 
            height: auto;
            padding: 25px;
        }
        .date-time{
            font-size: 22px;
        }
        .payment-details{
            font-size: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src = "data:image/png;base64, {{base64_image}} alt="Company Logo" height="150px" width="300px">
            <!-- <img src="../images/logo.png" alt="Company Logo" height="100px" width="200px"> Add your image here -->
            <!-- <div class="company-name">New Mahendra Traders</div> -->
            <div class="address">Ahrauli Shekh, Pukhrayan - 209111<br>9450728660, 9936103300<br><strong>Sales Report</strong></div>
        </div>
        
        <div class="customer-details">
            <div><strong>ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: </strong>{{ customer_id }}</div>
            <div><strong>Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: </strong>{{ customer_name }} <span style="float:right; margin-right: 10px;"><strong style = "color: red;"> Total:</strong> ₹ {{customer_total}}</span></div>
            <div><strong>Address&nbsp;&nbsp;: </strong>{{ customer_address }}<span style="float:right; margin-right: 10px;"><strong style = "color: red;">Remaining:</strong> ₹ {{customer_remaining}}</span></div>
            <div><strong>Phone&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: </strong>{{ customer_phone }}</div>
        </div>
        <div class = "table_header"><strong>Product Details </strong></div>
        
        """

        date_time = """
        <br>
        <div class=box>
        <div class = "date-time" ><strong style="color: red;">Date:</strong> {{date}} 
        <strong >&nbsp;&nbsp;&nbsp;Time:</strong> {{time}}</div>
        """

        product_table_heading = """
        <table>
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Quantity</th>
                    <th>Rate</th>
                    <th>Amount</th>
                </tr>
            </thead>
        """

        table_details = """
            <tbody>
                {% for product in products %}
                <tr>
                    <td> {{product[0] }}</td>
                    <td>{{ product[1] }}</td>
                    <td>{{ product[2] }}</td>
                    <td>{{ product[3] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        """

        payement_details = """
        <br>
        <div class= "payment-details"><strong>Method:</strong> {{payment_method}} 
        <strong style = "color: red;">&nbsp;&nbsp;&nbsp;Paid:</strong> ₹ {{paid_amount}}
        <div style="float: right;"><strong style = "color: red;">&nbsp;&nbsp;&nbsp;Total:</strong> ₹ {{total_price}}</div></div>
        </div>
        <br>
        """
        end_lines = """
                <div class="tagline">
                    <p>Thank you, Please visit again</p>
                </div>
            </div>
            
        </body>
        </html>
        """
        line = """
        <hr class="horizontal-line">
        """

        fn = all_function()
        customer_id, customer_name, customer_address, customer_phone = fn.select_db(
            f"Select id,name,address,phone from customer where id = '{id}'")[0]
        customer_total = fn.select_db(
            f"select sum(total) from money where id = '{id}'")[0][0]
        customer_remaining = fn.select_db(
            f"select sum(total - give) from money where id = '{id}'")[0][0]

        html_file = r"Main_Software\Customer_details.html"
        template = Template(first_html_content)
        # rendered_html = template.render()
        rendered_html = template.render(
            base64_image=InvoiceGenerator.read_text_file(
                r"Main_Software\logo_base64.txt"),
            customer_id=customer_id,
            customer_address=customer_address,
            customer_name=customer_name,
            customer_phone=customer_phone,
            customer_total=customer_total,
            customer_remaining=customer_remaining
        )
        with open(html_file, "w", encoding='utf-8') as existing_html_file:
            existing_html_file.write(rendered_html)
        products = fn.select_db(f'''select strftime('%d-%m-%Y', Date),CASE
        WHEN CAST(strftime('%H', time) AS INTEGER) >= 12 THEN
            CASE
                WHEN CAST(strftime('%H', time) AS INTEGER) > 12 THEN
                    printf('%02d', CAST(strftime('%H', time) AS INTEGER) - 12)
                ELSE
                    '12'
            END || ':' || 
            strftime('%M:%S', time) || ' PM'
        ELSE
            time || ' AM'
    END AS time,prod,quantity,rate,value,method from product where id = '{id}' order by date,time''')
        money = fn.select_db(f'''select strftime('%d-%m-%Y', Date),CASE
        WHEN CAST(strftime('%H', time) AS INTEGER) >= 12 THEN
            CASE
                WHEN CAST(strftime('%H', time) AS INTEGER) > 12 THEN
                    printf('%02d', CAST(strftime('%H', time) AS INTEGER) - 12)
                ELSE
                    '12'
            END || ':' || 
            strftime('%M:%S', time) || ' PM'
        ELSE
            time || ' AM'
    END AS time,give,total,method from money where id = '{id}' order by date,time''')

        pro_len = len(products)
        mon_len = len(money)

        p, m = 0, 0
        while p != pro_len and m != mon_len:
            if pro_len == 0:
                break
            if (products[p][0] + products[p][1]) != (money[m][0] + money[m][1]):
                date, time = money[m][0], money[m][1]
                method, paid, total = money[m][4], money[m][2], money[m][3]
                template = Template(date_time + payement_details)
                rendered_html = template.render(
                    date=date,
                    time=time,
                    payment_method=method,
                    total_price=total,
                    paid_amount=paid
                )

                with open(html_file, "a", encoding='utf-8') as existing_html_file:
                    existing_html_file.write(rendered_html)
                # print(money[m])
                m += 1
            else:
                product_list = []
                while (p != pro_len and m != mon_len) and ((products[p][0] + products[p][1]) == (money[m][0] + money[m][1])):
                    product_list.append(
                        [products[p][2], products[p][3], products[p][4], products[p][5]])

                    # print(products[p])
                    p += 1
                date, time = money[m][0], money[m][1]
                method, paid, total = money[m][4], money[m][2], money[m][3]
                template = Template(
                    date_time + product_table_heading + table_details + payement_details)
                rendered_html = template.render(
                    date=date,
                    time=time,
                    products=product_list,
                    payment_method=method,
                    total_price=total,
                    paid_amount=paid
                )
                with open(html_file, "a", encoding='utf-8') as existing_html_file:
                    existing_html_file.write(rendered_html)
                # print(money[m])
                m += 1

        while m != mon_len:
            date, time = money[m][0], money[m][1]
            method, paid, total = money[m][4], money[m][2], money[m][3]
            template = Template(date_time + payement_details)
            rendered_html = template.render(
                date=date,
                time=time,
                payment_method=method,
                total_price=total,
                paid_amount=paid
            )
            with open(html_file, "a", encoding='utf-8') as existing_html_file:
                existing_html_file.write(rendered_html)
            # print(money[m])
            m += 1

        template = Template(end_lines)
        rendered_html = template.render()
        with open(html_file, "a", encoding='utf-8') as existing_html_file:
            existing_html_file.write(rendered_html)

        with open(r'Main_Software\Customer_details.html', 'r', encoding='utf-8') as template_file:
            template_content = template_file.read()
        template = Template(template_content)
        rendered_html = template.render(
            base64_image=InvoiceGenerator.read_text_file(
                r"Main_Software\logo_base64.txt"),
            customer_id=customer_id,
            customer_address=customer_address,
            customer_name=customer_name,
            customer_phone=customer_phone
        )
        options = {
            'encoding': 'UTF-8',
            'enable-local-file-access': None
        }
        # Generate the PDF
        path_to_wkhtmltopdf = r"Main_Software\wkhtmltopdf\bin\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
        pdfkit.from_string(rendered_html, './Main_Software/Image_pdf/Customer_details.pdf',
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

    def customer(id):
        InvoiceGenerator.Customer_details_pdf_create(id)

    def new_customer(id):
        InvoiceGenerator.Customer_details_pdf_create(id)


# Call the static function to generate the PDF
# InvoiceGenerator.custom_test_case()
# InvoiceGenerator.customer('23080410')
# InvoiceGenerator.new_customer('23080408')
