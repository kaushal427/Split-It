# from veryfi import Client

# client_id = 'vrfRl22mUGLU5CxXWGGKwUxGb9aRpGtVaGNWTM3'
# client_secret = 'VBxKGjuEbamppe1HK5S89Y7UJO9UiEp44Bhong2v0A1pxau51C8CvUGLNxWGTYmO5gJXKDFY5rIWHiykijvsXRMus0kM0duNJNS1JXnm1zuLSPLhOJ1I9nJc53JFauwl'
# username = 'kaushal7343'
# api_key = 'af6d1ce0ee2ea2c3f1a61171f7e51ebe'

# veryfi_client = Client(client_id, client_secret, username, api_key)

# categories = ['Grocery', 'Utilities', 'Travel']
# file_path = 'receipt.jpg'
# # This submits document for processing (takes 3-5 seconds to get response)
# document_json = veryfi_client.process_document(file_path, categories=categories)
# print (document_json)
import json

x = {'account_number': None, 
      'bill_to': {
        'address': None, 
        'name': None, 
        'parsed_address': None, 
        'vat_number': None
        }, 
      'cashback': None, 
      'category': 'Grocery', 
      'created_date': '2022-10-15 18:24:52', 
      'currency_code': 'SGD', 
      'date': '2016-01-13 15:49:52', 
      'delivery_date': None, 
      'discount': None, 
      'document_reference_number': None, 
      'document_title': 'TAX INVOICE', 
      'document_type': 'receipt', 
      'due_date': None, 
      'duplicate_of': 96864864, 
      'external_id': None, 
      'id': 96868307, 
      'img_file_name': '96868307.png', 
      'img_thumbnail_url': 'https://scdn.veryfi.com/receipts/4c076508-ab50-4113-971d-937cb3abeb27/thumbnail.png?Expires=1665859193&Signature=EOfi6kH9pl-aHAPJrQr-xNcvWfhQHuwIbs8CymsiOLvCvPxum-GIvDnkouXxXwI5oZaCAlQ5AuPoqR5vdRHJyKjoI8LU1yJ56Un3g4~p1eFzs7B6E9ITDSfSxzm8O8gaJ3HVfkkFLwFcdQ-708woRkzsPKde5Kzij47X07ZZ1jchKjzCwLWKZxtTvs1wecNeBbFSs0Uze49vjGFyR9BpOEQLHyqGl6vx9GFNnTqOLZ9Cekzl1iYQm5z8hcQNtkfalNH2zUwKqC07YN7v8basgJNMdUMNLUGPKnM~NpRFqxEcr08lAghfUZi7fIYjJoKEkf9rJEud~SsujG7xZdJVVA__&Key-Pair-Id=APKAJCILBXEJFZF4DCHQ', 'img_url': 'https://scdn.veryfi.com/receipts/4c076508-ab50-4113-971d-937cb3abeb27/9a1f1daa-7917-47fe-b658-dd1cbe26315a.png?Expires=1665859193&Signature=W8cAB8HDsB6uPOZurGYESKr9CdFxiBi-tGQH-TqY3GfYtMqcBoSZkuT9nfPlEwqdFBFxqPYKoVN6p2tJPVyCmNZEx7mHQDBYOgdSPExszWdvLuZOMV4JrN7zNwrVzVw5xMZakeKhpb876s2muDC~NgmMfHki5sycWxjKUtNW4pkclyTT0HzvyEaxzRLGpKl3-XSLyRbmHVPAker2RXN7DaAolhBJ26JiMc3kgbO8c8TGKODcnAmtWNBgJ~dK2mMLyhH96HRHJKtRlZKxHhGJvg4rf0dphYfLzHH6KvQpInqcie0ZGr7Zj7bECcfkjXNXnHVlaS6Cbeq1Kme64t0L8A__&Key-Pair-Id=APKAJCILBXEJFZF4DCHQ', 
      'insurance': None, 
      'invoice_number': '002201330026', 
      'is_duplicate': True, 
      'is_money_in': False, 
      'line_items': [{
        'date': None, 
        'description': 'Med Ice Lemon Tea', 
        'discount': None, 
        'discount_rate': None, 
        'id': 358195807, 
        'order': 0, 
        'price': None, 
        'quantity': 1.0, 
        'reference': None, 
        'section': None, 
        'sku': None, 
        'tax': None, 
        'tax_rate': None, 
        'text': '1 Med Ice Lemon Tea\t2.95', 
        'total': 2.95, 
        'type': 'food', 
        'unit_of_measure': None, 
        'upc': None
        }, 
        {'date': None, 
        'description': 'Coffee with Milk', 
        'discount': None, 
        'discount_rate': None, 
        'id': 358195808, 
        'order': 1, 
        'price': None, 
        'quantity': 1.0, 
        'reference': None, 
        'section': None, 
        'sku': None, 
        'tax': None, 
        'tax_rate': None, 
        'text': '1 Coffee with Milk\t2.40', 
        'total': 2.4, 
        'type': 'food', 
        'unit_of_measure': None, 
        'upc': None}], 
        'meta': {
          'owner': 'kaushal7343'}, 
          'notes': None, 
          'ocr_text': "McDonald's Toa Payoh Central\n¹600 @ Toa Payoh #01-02,\nSingapore 319515\nTel: 62596362\nMcDonald's Restaurants Pte Ltd\nGST REGN NO: M2-0023981-4\nTAX INVOICE\nINV# 002201330026\nORD #57 -REG #1- 13/01/2016 15:49:52\nQTY ITEM\t\t\tTOTAL\n1 Med Ice Lemon Tea\t2.95\n1 Coffee with Milk\t2.40\nEat-In Total (incl GST)\t5.35\nCash Tendered\t\t10.00\nChange\t\t\t4.65\nTOTAL INCLUDES GST OF\t0.35\nThank You and Have A Nice Day", 
          'order_date': None, 
          'payment': {
            'card_number': None, 
            'display_name': 'Cash', 
            'terms': None, 
            'type': 'cash'
          }, 
          'pdf_url': 'https://scdn.veryfi.com/receipts/4c076508-ab50-4113-971d-937cb3abeb27/b990b744-8b6b-4934-88e0-5696b96d178f.pdf?Expires=1665859193&Signature=NyBO3OMvJRU84JUxql-tyDM7kdRcK6yt6lspza3RxiNkZf29KiWjVL8keOi~OhQJKyR-OyoHi0Vd1jMtZrFx55k58Oe~agDpLeZaqtVuhk5trNwU8R4xo58gL4L-UPClu-glxc0zZ6qsUdq5k4w391HttLG~-iTNNvSySOzLPjur7DJxOQdXNIgBn5r3BdsEoDMMB6PCdS8RSTxWHeK~knOdpHM0f0bYy4ZwOygxWPyUpuk2TBMewBuuCjQIwDfvZBxgyZRxzFKb8eQjjKKOQfm6~E36EVaNxfLsmDi2DqXBBpGi2sZ5gb3EbdTttRvCrzlVxeLN0xZUwITNS87K9A__&Key-Pair-Id=APKAJCILBXEJFZF4DCHQ', 
          'purchase_order_number': None, 
          'reference_number': 'VHIIG-8307', 
          'rounding': None, 
          'service_end_date': None, 
          'service_start_date': None, 
          'ship_date': None, 
          'ship_to': {
            'address': None, 
            'name': None, 
            'parsed_address': None
          }, 
          'shipping': None, 
          'store_number': None, 
          'subtotal': 5.0, 
          'tax': 0.35, 
          'tax_lines': [], 
          'tip': None, 
          'total': 5.35, 
          'total_weight': None, 
          'tracking_number': None, 
          'updated_date': '2022-10-15 18:24:53', 
          'vendor': {
            'abn_number': None, 
            'account_number': None, 
            'address': '600 Lorong 4 Toa Payoh, #01-02, 600@Toa Payoh, Singapore 319515', 
            'bank_name': None, 
            'bank_number': None, 
            'bank_swift': None, 
            'category': 'restaurant, food, point_of_interest, establishment', 
            'email': None, 
            'fax_number': None, 
            'iban': None, 
            'lat': None, 
            'lng': None, 
            'logo': 'https://cdn.veryfi.com/logos/us/218019458.jpeg', 
            'name': "McDonald's", 
            'phone_number': '62596362', 
            'raw_address': '¹600 @ Toa Payoh #01-02,\nSingapore 319515', 
            'raw_name': "McDonald's", 
            'reg_number': None, 
            'type': 'restaurant, food, point_of_interest, establishment', 
            'vat_number': 'M2-0023981-4', 
            'web': None
          }
    }
#print(x['line_items'])
items = x['line_items']

for i in items:
  print(i['description'] + "\t\t" + str(i['total']))

print("Subtotal:\t\t\t" + str(x['subtotal']))
print("Tax:\t\t\t\t" + str(x['tax']))
print("Total:\t\t\t\t" + str(x['total']))

