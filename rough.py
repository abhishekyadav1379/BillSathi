import requests

def send_pdf_with_text_to_telegram(pdf_path, caption):
    api_token = '6536259159:AAGaU6QTIoiiSdpEawLb0MAvktwgdziXoUY'
    chat_id = '1010585302'
    api_url = f'https://api.telegram.org/bot{api_token}/sendDocument'

    try:
        with open(pdf_path, 'rb') as pdf_file:
            files = {'document': ("abhishek_yadav.pdf",pdf_file)}
            data = {'chat_id': chat_id, 'caption': caption}
            response = requests.post(api_url, data=data, files=files)
            print(response.text)
    except Exception as e:
        print(e)

# Usage:
send_pdf_with_text_to_telegram("./Main_Software/Image_pdf/customer_details.pdf", "This is an example PDF with a caption.")
