import json
from django.test import TestCase
from .models import Bills, Clients, Products
from rest_framework import status
import pandas as pd
from faker import Faker
import faker_commerce

# Create your tests here.


class ClientTestCase(TestCase):
    fake = Faker()
    _url_client = ""

    @property
    def url_client_all(self):
        return f"/api/clients/all/"

    @property
    def url_client(self):
        return self._url_client

    @url_client.setter
    def url_client(self, value):
        self._url_client = f"/api/client/{value}/"

    @classmethod
    def setUpTestData(self):
        list_client = []

        for i in range(1, 10):
            client = Clients.objects.create(document=self.fake.msisdn(), first_name=self.fake.first_name(),
                                            last_name=self.fake.last_name(), email=self.fake.safe_email())
            list_client.append(client)
        return list_client

    def setUp(self):
        pass

    def test_create_client(self):
        self.payload = {"document": self.fake.msisdn(), "first_name": self.fake.first_name(),
                        "last_name": self.fake.last_name(), "email": self.fake.safe_email()}

        print("Creating Client:")
        response = self.client.post(self.url_client_all, data=json.dumps(self.payload), content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("-"*50)

    def test_create_multiple_client(self):
        list_products = []
        for i in range(1, 100):
            clients = {"document": self.fake.msisdn(), "first_name": self.fake.first_name(),
                       "last_name": self.fake.last_name(), "email": self.fake.safe_email()}
            list_products.append(clients)

        df = pd.DataFrame(list_products)
        compression_opts = dict(method='zip', archive_name='MultipleClients.csv')
        df.to_csv('BulkClients.zip', index=False, compression=compression_opts)

    def test_get_single_client(self, pk=1):
        print(f"Get Client with id={pk}")
        self.url_client = pk
        url = self.url_client
        response = self.client.get(url, kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)
        return(response.json())

    def test_get_all_clients(self):
        print("Get all Clients")
        response = self.client.get(self.url_client_all,  content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)

    def test_update_client(self, pk=4):
        print(f"Updating Client pk= {pk}")
        self.payload_updated = {"id": pk, "document": self.fake.msisdn(), "first_name": "Client Edited",
                                "last_name": "LastName Edited", "email": "email@Edited.com"}

        self.url_client = pk
        url = self.url_client
        response = self.client.put(url, data=self.payload_updated, content_type='application/json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)

    def test_delete_client(self, pk=2):
        print(f"Deleting Client pk= {pk}")
        self.url_client = pk
        url = self.url_client
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("-"*50)


class ProductsTestCase(TestCase):
    fake = Faker()

    _url_product = ""

    @property
    def url_product_all(self):
        return f"/api/products/all/"

    @property
    def url_product(self):
        return self._url_product

    @url_product.setter
    def url_product(self, value):
        self._url_product = f"/api/product/{value}/"

    @classmethod
    def setUpTestData(self):
        list_products = []
        self.fake.add_provider(faker_commerce.Provider)
        for i in range(1, 5):
            description = self.fake.ecommerce_name()
            atribute = self.fake.ecommerce_price()
            name = self.fake.bothify(text='Product ????', letters='ABCDE')

            product = Products.objects.create(name=name, description=description,
                                              attribute=atribute)
            list_products.append(product)
        return list_products

    def setUp(self):
        pass

    def test_get_single_product(self, pk=2):
        print(f"Get Product with id={pk}")
        self.url_product = pk
        url = self.url_product
        response = self.client.get(url, kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)
        return(response.json())

    def test_get_all_products(self):
        print("Get all Products")
        response = self.client.get(self.url_product_all, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)

    def test_create_product(self):
        description = self.fake.ecommerce_name()
        atribute = self.fake.ecommerce_price()
        name = self.fake.bothify(text='Product ????', letters='ABCDE')

        self.payload = {"name": name, "description": description,
                        "attribute": atribute}
        print("Creating Product:")
        response = self.client.post(self.url_product_all, data=json.dumps(self.payload),
                                    content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("-"*50)

    def test_update_product(self, pk=2):
        print(f"Updating product pk= {pk}")

        self.payload_updated = {"id": pk, "name": "product Updated", "description": "description Updated",
                                "attribute": 78}
        self.url_product = pk
        url = self.url_product

        response = self.client.put(url, data=self.payload_updated, content_type='application/json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)

    def test_delete_client(self, pk=1):
        print(f"Deleting Product pk= {pk}")
        self.url_product = pk
        url = self.url_product
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("-"*50)


class BillTestCase(TestCase):
    clients = ClientTestCase()
    products = ProductsTestCase()
    fake = Faker()
    _url_bill = ""

    @property
    def url_bills_all(self):
        return f"/api/bills/all/"

    @property
    def url_bill(self):
        return self._url_bill

    @url_bill.setter
    def url_bill(self, value):
        self._url_bill = f"/api/bill/{value}/"

    @classmethod
    def setUpTestData(self):

        response_client = self.clients.setUpTestData()
        response_product = self.products.setUpTestData()
        Faker.seed(0)
        for client in response_client:
            random_code = self.fake.localized_ean13()
            nit = self.fake.localized_ean8()
            company_name = self.fake.company()

            bill = Bills.objects.create(client_id=client, company_name=company_name,
                                        nit=nit, code=random_code)
            bill.products.add(response_product[0], response_product[1])

    def setUp(self):
        pass

    def test_get_all_bills(self):
        print("Get all Bills")
        print(self.url_bills_all)
        response = self.client.get(self.url_bills_all, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)

    def test_get_single_bill(self, pk=3):
        print(f"Get Bill with id={pk}")
        self.url_bill = pk
        url = self.url_bill
        print(url)
        response = self.client.get(url, kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)
        return(response.json())

    def test_create_bill(self, pk=1):
        self.clients.url_client = pk
        url = self.clients.url_client
        response = self.client.get(url, kwargs={'pk': None}, content_type='application/json')
        client_response = response.json()

        url = self.products.url_product_all
        response = self.client.get(url, kwargs={'pk': None}, content_type='application/json')
        products_response = response.json()

        list_id_products = []
        for product in products_response:
            list_id_products.append(product["id"])

        random_code = self.fake.localized_ean13()
        nit = self.fake.localized_ean8()
        company_name = self.fake.company()

        self.payload = {"client_id": client_response["id"], "company_name": company_name, "nit": nit,
                        "code": random_code, "products": list_id_products}

        print("Creating Bill:")
        url = self.url_bills_all
        response = self.client.post(url, data=json.dumps(self.payload), content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("-"*50)
