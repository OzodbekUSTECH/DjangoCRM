# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from website.views import  home, logout, register_user, customer_record, add_record, delete_record, update_record

# class TestUrls(SimpleTestCase):

#     def  test_home_url(self):
#         url = reverse('home')
#         self.assertEquals(resolve(url).func, home)

#     def  test_reg_url(self):
#         url = reverse('register')
#         self.assertEquals(resolve(url).func, register_user)

#     def  test_record_url(self):
#         url = reverse('record', args=['3'])
#         self.assertEquals(resolve(url).func, customer_record)

#     def  test_add_record_url(self):
#         url = reverse('add_record')
#         self.assertEquals(resolve(url).func, add_record)

#     def  test_delete_record_url(self):
#         url = reverse('delete_record', args=['2'])
#         self.assertEquals(resolve(url).func, delete_record)

#     def  test_update_record_url(self):
#         url = reverse('update_record', args=['2'])
#         self.assertEquals(resolve(url).func, update_record)
