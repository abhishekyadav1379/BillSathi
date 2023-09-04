from fpdf import FPDF
from All_function import all_function
class InvoicePdf:
    @staticmethod
    def generate_invoice(id, name, address, phone, product, date, time, method, give, subtotal, remaining):
        w = 76
        h = 70 + int(len(product) * (100 / 14)) + 22
        pdf = FPDF(orientation='P', unit='mm', format=(w, h))
        pdf.set_margin(0)
        pdf.add_page()

        # Use default font, size 12 for header
        pdf.image("./Main_Software/Image_pdf/mahendra_logo.png", x=8, y=0, w=60, h=27,keep_aspect_ratio = True)
        pdf.ln(27)
        pdf.set_font("Arial", size=14)
        # pdf.cell(w, txt="New Mahendra Traders", ln=1, align="C")
        pdf.set_font("Arial", size=10)
        pdf.cell(w, txt="Ahrauli shekh, Pukhrayan - 209111", ln=1, align="C")
        pdf.cell(w, txt="9450728660, 9936103300", ln=1, align="C")
        # pdf.set_font("Arial", size=12)
        pdf.cell(w, txt="ESTIMATE", ln=1, align="C")
        pdf.cell(w, txt=" ", ln=1, align="L")

        # pdf.set_font("Arial", size=12)
        # pdf.text(54, 23, date)
        # pdf.text(59, 27, time[:6])
        # pdf.dashed_line(0,38,w,38)
        pdf.dashed_line(19,41,19,59)
        # pdf.dashed_line(0,59,w,60)
        pdf.set_font("Arial", size=10)
        customer = [("ID               ", id), ("Name         ", name), ("Address     ", address), ("Phone No. ", phone)]
        for det in customer:
            pdf.cell(txt=det[0], ln=0)
            pdf.cell(txt=det[1], ln=1)
        pdf.cell(txt=f"Date            {date} {time}", ln=1)
        pdf.ln()

        # Write table code below
        pdf.set_font("Arial", size=9)
        with pdf.table(width=74, col_widths=(30, 14, 14, 18)) as table:
            for data_row in product:
                row = table.row()
                for datum in data_row:
                    row.cell(datum)

        pdf.ln()
        pdf.set_font("Arial", size=10)
        payment = [("Method:", method), ("Paid:", "Rs " + give), ("Total:", "Rs " + subtotal), ("Remaining:", "Rs " + remaining)]
        for det in payment:
            pdf.cell(txt=det[0], ln=0)
            pdf.cell(txt=det[1], ln=1)

        pdf.ln()
        pdf.set_font("Arial", size=8)
        pdf.cell(w, txt="Thank you, Please visit again", ln=1, align="C")
        pdf.cell(w, txt="Mahendratraders786@gmail.com", ln=1, align="C")
        pdf.output("invoice.pdf")

    @staticmethod
    def generate_customer_details(id):
        w = 210
        h = 297
        pdf = FPDF(orientation='P', unit='mm', format=(w, h))
        pdf.add_page()
        fn = all_function()

        # Use default font, size 16 for header
        pdf.image("./Main_Software/Image_pdf/mahendra_logo.png", x=84, y=0, w=60, h=27,keep_aspect_ratio = True)
        pdf.ln(18)
        # pdf.set_font("Arial", size=16)
        # pdf.cell(w, txt="New Mahendra Traders", ln=1, align="C")
        pdf.set_font("Arial", size=12)
        pdf.cell(w, txt="Ahrauli shekh, Pukhrayan -209111", ln=1, align="C")
        pdf.cell(w, txt="945072866, 9936103300", ln=1, align="C")
        pdf.cell(w, txt=" ", ln=1, align="L")

        def convert_matrix_to_strings(matrix):
            string_matrix = [[str(element) for element in row] for row in matrix]
            return string_matrix
        
        id,name,phone,address = fn.select_db(f"select id,name,phone,address from customer where id = '{id}'")[0]
        product =  fn.select_db(f"select date,prod,quantity,rate,value,method from product where id = '{id}'")
        money =  fn.select_db(f"select date,give,total,method from money where id = '{id}'")
        total = fn.select_db(f"select sum(total) from money where id = '{id}'")[0][0]
        remaining = fn.select_db(f"select sum(total - give) from money where id = '{id}'")[0][0]
        product = convert_matrix_to_strings(product)
        money = convert_matrix_to_strings(money)
        product.insert(0,["Date", "Product", "Quantity","Rate","Value","method"])
        money.insert(0,["Date","Paid","Total","Method"])
        # money = product
        if phone == "":
            phone = " "
        if address == "":
            address = " "
        if name == "": 
            name = " "
        pdf.set_font("Arial", size=16)
        customer = [("ID:", id), ("Name:", name), ("Address:", address), ("Phone No.:", phone)]
        for det in customer:
            pdf.cell(txt=det[0], ln=0)
            pdf.cell(txt=det[1], ln=1)
        pdf.ln()
        pdf.cell(txt=f"Overall Total: Rs {total}", ln=1)
        pdf.cell(txt=f"Remaining: Rs {remaining}", ln=1)
        pdf.ln()
        
        pdf.set_font("Arial", size=16)
        pdf.cell(txt="Product Details:", ln=1)

        # Write table code below
        pdf.set_font("Arial", size=12)
        with pdf.table() as table:
            for data_row in product:
                row = table.row()
                for datum in data_row:
                    row.cell(datum)

        pdf.ln()
        pdf.set_font("Arial", size=16)
        pdf.cell(txt="Cash Flow Details:", ln=1)

        pdf.set_font("Arial", size=12)
        with pdf.table() as table:
            for data_row in money:
                row = table.row()
                for datum in data_row:
                    row.cell(datum)

        pdf.ln()
        pdf.set_font("Arial", size=10)
        pdf.cell(w, txt="*All units in kg, foot and standard unit", ln=1)

        pdf.set_font("Arial", size=8)
        pdf.cell(w, txt="Thank you, Please visit again", ln=1, align="C")
        pdf.cell(w, txt="Mahendratraders786@gmail.com", ln=1, align="C")
        pdf.output("customer_details.pdf")

id = "20345678"
name = "Pbhishek Yadav"
address = "Pukhrayan"
phone = "78546212312"
remaining = "20000"
product = [
    ("Product", "Qty", "Rate", "Total"),
    ("Cement ultratech ", "1000.5", "100", "456000.0"),
    ("Sand", "10", "100", "1000"),
    ("Bricks", "10", "100", "1000"),
    ("Bricks", "10", "100", "1000"),
    ("", "", "Total", "458000.0")
]
date = "15-08-2023"
time = "12:12 PM"
method = "Cash"
give = "500000"
subtotal = "458000.0"
# InvoicePdf.generate_invoice(id, name, address, phone, product, date, time, method, give, subtotal,remaining)

# InvoicePdf.generate_customer_details(id, name, address, phone, product, product)  # Note: You have a typo here, you might want to pass the `money` list instead of `product`.
