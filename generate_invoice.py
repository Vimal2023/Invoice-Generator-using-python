from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from num2words import num2words
import datetime

def generate_invoice(data):
    items = []
    total_amount = 0

    for item in data['items']:
        net_amount = item['unit_price'] * item['quantity'] - item.get('discount', 0)
        tax_type = 'IGST' if data['place_of_supply'] != data['place_of_delivery'] else 'CGST/SGST'
        tax_rate = item['tax_rate']
        tax_amount = net_amount * tax_rate / 100
        if tax_type == 'CGST/SGST':
            tax_amount /= 2  # Split between CGST and SGST
        total_amount += net_amount + tax_amount * (2 if tax_type == 'CGST/SGST' else 1)
        items.append({
            'description': item['description'],
            'unit_price': item['unit_price'],
            'quantity': item['quantity'],
            'discount': item.get('discount', 0),
            'net_amount': net_amount,
            'tax_rate': tax_rate,
            'tax_type': tax_type,
            'tax_amount': tax_amount,
            'total_amount': net_amount + tax_amount * (2 if tax_type == 'CGST/SGST' else 1)
        })

    data['items'] = items
    data['total_amount'] = total_amount
    data['amount_in_words'] = num2words(total_amount, to='currency', lang='en_IN')

    # Load HTML template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('invoice_template.html')
    html_out = template.render(data)

    # Convert HTML to PDF
    HTML(string=html_out).write_pdf(f"invoice_{data['invoice_no']}.pdf")

# Sample data
data = {
    'logo': '/img/logo.png',
    'seller_name': 'Varasiddhi Silk Exports',
    'seller_address': '75, 3rd Cross, Lalbagh Road',
    'seller_city_state_pincode': 'BENGALURU, KARNATAKA, 560027',
    'seller_country': 'IN',
    'seller_pan': 'AACFV3325K',
    'seller_gst': '29AACFV3325K1ZY',
    'place_of_supply': 'KARNATAKA',
    'billing_name': 'Madhu B',
    'billing_address': 'Eurofins IT Solutions India Pvt Ltd., 1st Floor, Maruti Platinum, Lakshminarayana Pura, AECS Layout',
    'billing_city_state_pincode': 'BENGALURU, KARNATAKA, 560037',
    'billing_country': 'IN',
    'billing_state_code': '29',
    'shipping_name': 'Madhu B',
    'shipping_address': 'Eurofins IT Solutions India Pvt Ltd., 1st Floor, Maruti Platinum, Lakshminarayana Pura, AECS Layout',
    'shipping_city_state_pincode': 'BENGALURU, KARNATAKA, 560037',
    'shipping_country': 'IN',
    'shipping_state_code': '29',
    'place_of_delivery': 'KARNATAKA',
    'order_no': '403-3225714-7676307',
    'order_date': '2019-10-28',
    'invoice_no': 'KA-310565025-1920',
    'invoice_date': '2019-10-28',
    'reverse_charge': 'No',
    'items': [
        {
            'description': 'Varasiddhi Silks Men\'s Formal Shirt (SH-05-42, Navy Blue, 42) B07KGF3KW8 ( SH-05--42 )\nShipping Charges',
            'unit_price': 338.10,
            'quantity': 1,
            'discount': 0,
            'tax_rate': 2.5
        },
        {
            'description': 'Varasiddhi Silks Men\'s Formal Shirt (SH-05-40, Navy Blue, 40) B07KGCS2X7 ( SH-05--40 )\nShipping Charges',
            'unit_price': 338.10,
            'quantity': 1,
            'discount': 0,
            'tax_rate': 2.5
        }
    ],
    'signature': '/img/Vimal Anand signature.jpg'
}

generate_invoice(data)
