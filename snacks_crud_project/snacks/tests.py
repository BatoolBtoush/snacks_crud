from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class SnacksTestCase(TestCase):
    def test_snack_list_view(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Snack List")
        self.assertTemplateUsed(response, "snack_list.html")

    # def test_snack_detail_view(self):
    #     response = self.client.get(reverse('snack_detail', args=[1]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Snack Details')
    #     self.assertTemplateUsed(response, 'snack_detail.html')

    def test_snack_create_view(self):
        url = reverse("snack_create")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Create Snack")
        self.assertTemplateUsed(response, "snack_create.html")

    # def test_snack_update_view(self):
    #     url = reverse('snack_update', args=[1])
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertContains(response, 'Update Snack')
    # self.assertTemplateUsed(response, 'snack_update.html')

    # def test_snack_delete_view(self):
    #     response = self.client.get(reverse('snack_delete', args=[1]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Delete Snack')
    #     self.assertTemplateUsed(response, 'snack_delete.html')
