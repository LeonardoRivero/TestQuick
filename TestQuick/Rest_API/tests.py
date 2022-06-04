import email
import json
from pydoc import Helper
from xmlrpc import client
from django.test import TestCase
from .models import Bills, Clients, Products
from rest_framework import status
import random
import string
# Create your tests here.


class Helpers():
    def random_email(self):
        letters = string.ascii_lowercase
        email = ''.join(random.choice(letters) for i in range(10))
        email += '@gmail.com'
        return email

    def random_document(self):
        document_random = random.randrange(1, 9999999999, 10)
        return document_random

    def random_code(self):
        length_strings = 5
        random_code = ''.join(random.choices(string.digits, k=length_strings))
        return random_code


class ClientTestCase(TestCase):
    helper = Helpers()

    @classmethod
    def setUpTestData(self):
        list_client = []

        for i in range(1, 10):
            document = self.helper.random_document()
            email_random = self.helper.random_email()
            client = Clients.objects.create(document=document, first_name=f"Name {i}",
                                            last_name=f"LastName {i}", email=email_random)
            list_client.append(client)
        return list_client

    def setUp(self):
        pass

    def test_create_client(self):
        document = self.helper.random_document()
        email_random = self.helper.random_email()
        self.payload = {"document": document, "first_name": "New Client",
                        "last_name": "LastName NewClient", "email": email_random}

        print("Creating Client:")
        response = self.client.post("/api/clients/all/", data=json.dumps(self.payload), content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("-"*50)

    def test_get_single_client(self, pk=1):
        print(f"Get Client with id={pk}")
        response = self.client.get(f"/api/client/{pk}/", kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)
        return(response.json())

    def test_get_all_clients(self):
        print("Get all Clients")
        response = self.client.get("/api/clients/all/",  content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)

    def test_update_client(self, pk=4):
        print(f"Updating Client pk= {pk}")
        document = self.helper.random_document()
        email_random = self.helper.random_email()
        self.payload_updated = {"id": pk, "document": document, "first_name": "Client Edited",
                                "last_name": "LastName Edited", "email": email_random}

        response = self.client.put(f"/api/client/{pk}/", data=self.payload_updated, content_type='application/json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)

    def test_delete_client(self, pk=2):
        print(f"Deleting Client pk= {pk}")
        response = self.client.delete(f"/api/client/{pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("-"*50)


class ProductsTestCase(TestCase):
    helper = Helpers()

    @classmethod
    def setUpTestData(self):
        PRODUCTS = ({"telephone": "device for call"},
                    {"car": "is a vehicule"}, {"card": "plastic money"}, {"lamp": "provide light"},
                    {"pencil": "for drawing"}, {"sunglasses": "to wear on beach"})
        list_products = []
        for i in range(1, 5):
            product = random.choice(PRODUCTS)
            description, name = self.get_value_key(self, product)
            product = Products.objects.create(name=name, description=description,
                                              attribute=i)
            list_products.append(product)
        return list_products

    def setUp(self):
        pass

    def get_value_key(self, dictionary):
        for key in dictionary:
            value = dictionary[key]
        return value, key

    def test_get_single_product(self, pk=2):
        print(f"Get Product with id={pk}")
        response = self.client.get(f"/api/product/{pk}/", kwargs={'pk': None}, content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)
        return(response.json())

    def test_get_all_products(self):
        print("Get all Products")
        response = self.client.get("/api/products/all/",  content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)

    def test_create_product(self):
        self.payload = {"name": "new product", "description": "to do something",
                        "attribute": 78}
        print("Creating Product:")
        response = self.client.post("/api/products/all/", data=json.dumps(self.payload),
                                    content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("-"*50)

    def test_update_product(self, pk=2):
        print(f"Updating product pk= {pk}")

        self.payload_updated = {"id": pk, "name": "new product Updated", "description": "to do something Updated",
                                "attribute": 78}
        response = self.client.put(f"/api/product/{pk}/", data=self.payload_updated, content_type='application/json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)

    def test_delete_client(self, pk=1):
        print(f"Deleting Product pk= {pk}")
        response = self.client.delete(f"/api/product/{pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("-"*50)


class BillTestCase(TestCase):
    helper = Helpers()

    @classmethod
    def setUpTestData(self):
        clients = ClientTestCase()
        response_client = clients.setUpTestData()
        products = ProductsTestCase()
        response_product = products.setUpTestData()

        for client in response_client:
            random_code = self.helper.random_code()
            nit = self.helper.random_document()
            bill = Bills(client_id=client, company_name=f"Company {client.id}",
                         nit=nit, code=random_code)
            bill.save()
            bill.products.add(response_product[0], response_product[1])

    def setUp(self):
        pass

    def test_get_all_bills(self):
        print("Get all Bills")
        response = self.client.get("/api/bills/all/",  content_type='application/json')
        print("Response as Json", response.json())
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        print("-"*50)
#     def test_Exampl(self):
#         print("sdfdsfsdfsdfds")
