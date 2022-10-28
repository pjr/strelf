import os
import stripe
import requests


class InvoiceHelper:
    # TODO: Add logging & rate limiting
    @staticmethod
    def download_pdf(api_key, url_pdf, to_file):
        to_dir = os.path.dirname(to_file)
        if not os.path.exists(to_dir):
            os.makedirs(to_dir)

        response = requests.get(url_pdf)
        with open(to_file, 'wb') as f:
            f.write(response.content)
        f.close()

    @staticmethod
    def get_all(api_key):
        for cust in stripe.Customer.list(api_key=api_key):
            for inv in stripe.Invoice.list(api_key=api_key):
                yield [cust, inv]
