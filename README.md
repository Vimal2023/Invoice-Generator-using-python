Objective:
Develop a programmatic way of generating an invoice for orders placed on an e-commerce platform. The
invoice format and structure should match the invoice in this  (to the extent possible).
Requirements:
● There needs to be a placeholder for the company logo.
● Assume that the below can be taken as input parameters:
○ Seller Details: Name, Address, (City, State, Pincode), PAN No., GST Registration No.
○ Place of Supply
○ Billing Details: Name, Address, (City, State, Pincode), State/UT Code
○ Shipping Details: Name, Address, (City, State, Pincode), State/UT Code
○ Place of Delivery
○ Order Details: Order No., Order Date
○ Invoice Details: Invoice No., Invoice Details, Invoice Date
○ Reverse Charge: Yes/No
○ Item Details - List of items in the order with each item in the below format (see table in
the invoice):
■ Description
■ Unit Price
■ Quantity
■ Discount
■ Net Amount (to be derived as Unit Price * Quantity - Discount)
■ Tax Rate: (18% in the example below)
○ Signature image
● You will need to compute/derive the below parameters:
○ Item Details:
■ Net Amount: Unit Price * Quantity - Discount
■ Tax Type: If Place of Supply = Place of Delivery, then Tax Type should be broken
down as CGST & SGST at 9% each (18% / 2). Else Tax Type should be a single
component as IGST at 18%.
■ Tax Amount: Net Amount * Tax Rate (2 separate components in case of
CGST/SGST; a single component in case of IGST).
■ Total Amount: Net Amount + Tax Amount
○ Total row
○ Amount in words
● The signature image needs to be inserted as shown in the invoice image:
○ For <Seller Name>:
<Insert Signature>
Authorised Signatory
Suggested implementation approaches:
● Most preferred: You can use Zoho's API for creating the invoice in the required format. Ensure
that we are able to generate the invoice in PDF format as well.
● Open-source: Similarly, you can also use Invoice Ninja API, an open-source invoicing software.
● Custom approach: You can also construct an HTML file that will match the required invoice
format, which can accommodate the inputs and the derived parameters.
Deliverables:
● Program of generating invoices as described above in a language of your choice.
● Clear and concise documentation explaining the program's implementation and usage.
Optional notes to consider:
● Handle situations where discount is not provided for an item.
● Validate all input parameters and handle potential errors gracefully.
● Designed for performance and scalability to handle a large volume of orders.
● The program should be platform-agnostic and readily deployable.
