# from django.test import TestCase, Client
# from django.urls import reverse
# from website.models import Record
# import json
# class TestViews(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.record_url = reverse('home')
#         self.add_record_url = reverse('add_record')
#         # self.detail_url = reverse('record', args=[11])
#         # self.record1 = Record.objects.create(
#         #     first_name = 'john',
#         #     last_name = 'doe',
#         #     email = 'john.doe@example.com',
#         #     phone = '5555555',
#         #     address = 'dojwakdwa',
#         #     city = 'San Francisco',
#         #     state = 'CA',
#         #     zipcode = '94'
#         # )



#     def test_record_list_GET(self):

#         response = self.client.get(self.record_url)

#         self.assertEquals(response.status_code, 200)

#         self.assertTemplateUsed(response, 'home.html')
    
#     # ERROR 302
#     # def test_record_detail_GET(self):
#     #     response = self.client.get(self.detail_url)

#     #     self.assertEquals(response.status_code, 200)

#     #     self.assertTemplateUsed(response, 'record.html')

#     def test_record_detail_POST(self):
       

#         response = self.client.post(self.add_record_url, {     
#             'first_name': 'john',
#             'last_name': 'doe',
#             'email': 'john.doe@example.com',
#             'phone': '5555555', 
#             'address': 'dojwakdwa',
#             'city': 'San Francisco',
#             'state': 'CA',
#             'zipcode': '94' 
#         })

#         self.assertEquals(response.status_code, 302)
#         # self.assertEquals()