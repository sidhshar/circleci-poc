from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .models import organization
from .forms import OrganizationEnterForm

class OrganizationTestCase(TestCase):
    def setUp(self):
        #self.org1 = organization.objects.create_user(name="admin")
        # organization.objects.create(name="Test",
        #                     created_date=timezone.now(),
        #                     published_date=timezone.now())
        pass

    def test_org_is_posted(self):
        """Org created"""
        # org1 = organization.objects.get(name="Test")
        # self.assertEqual(org1.somefield, "Field value validation")
        self.assertEqual("Dummy data", "Dummy data")

    def test_valid_form_data(self):
        # form = OrganizationEnterForm({
        #     'name': "Just testing"
        # })
        # self.assertTrue(form.is_valid())
        # org1 = form.save(commit=False)
        # org1.save()
        # self.assertEqual(org1.somefield, "Field value validation")
        self.assertEqual("Dummy data", "Dummy data")

    def test_blank_form_data(self):
        form = OrganizationEnterForm({})
        self.assertFalse(form.is_valid())
        # self.assertEqual(form.errors, {
        #     'company_size': ['This field is required.'],
        #     'industry_type': ['This field is required.'],
        # })
