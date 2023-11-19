"""
Test for the Journal Table API
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from datetime import datetime, timedelta
from core.models import Journal, JournalTables

CREATE_JOURNAL_URL = reverse("journal:journal-list")
CREATE_JOURNAL_TABLE_URL = reverse("journal:journaltables-list")
TOKEN_URL = reverse("user:token")


def create_user(**params):
    """
    Create and return a user
    """
    return get_user_model().objects.create_user(**params)


def create_journal(
    user,
    journal_name="new journal",
    journal_description="kvldsjfksd sdjflsjd lfjsldjf jdlfjd sfsdff",
):
    """
    Create and return a journal
    """
    return Journal.objects.create(
        journal_name=journal_name, journal_description=journal_description, user=user
    )


def detail_url(journal_table_id):
    """
    Return the url for a journal table
    """
    return reverse("journal:journaltables-detail", args=[journal_table_id])


class PublicJournalTableApiTest(TestCase):
    """
    Test the public features for the journal table api
    """

    def setUp(self):
        self.client = APIClient()
        user_payload = {
            "first_name": "Test",
            "last_name": "User",
            "email": "user@example.com",
            "password": "Awesomeuser123",
        }
        self.user = create_user(**user_payload)
        self.journal = create_journal(self.user)

        # self.client.force_authenticate(self.user)

    def test_create_journal_table_for_unauthenticated_user(self):
        """
        Test creating journal table for unauthenticated users fails
        """
        payload = {
            "journal": self.journal.id,
            "table_name": "skdvn djfsldkjfsdf",
        }
        res = self.client.post(CREATE_JOURNAL_TABLE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_journal_table_for_unauthenticated_user(self):
        """
        Test retrieving journal table for unauthenticated users fails
        """
        res = self.client.get(CREATE_JOURNAL_TABLE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateJournalTableApiTests(TestCase):
    """
    Private tests for journal table api
    """

    def setUp(self) -> None:
        self.client = APIClient()
        user_payload = {
            "first_name": "Test",
            "last_name": "User",
            "email": "user@example.com",
            "password": "Awesomeuser123",
        }
        self.user = create_user(**user_payload)
        self.journal = create_journal(self.user)

        self.client.force_authenticate(self.user)

    def test_create_journal_table_succeeds(self):
        """
        Test create journal table succeeds for
        authenticated user
        """
        payload = {"journal": self.journal.id, "table_name": "kdljfaklsd jfsdf"}

        res = self.client.post(CREATE_JOURNAL_TABLE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_retrieve_journal_table_succeeds(self):
        """
        Test retrieve journal table succeeds for authenticated user
        """
        payload = {"journal": self.journal.id, "table_name": "kdljfaklsd jfsdf"}

        res = self.client.post(CREATE_JOURNAL_TABLE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        res2 = self.client.get(CREATE_JOURNAL_TABLE_URL)
        self.assertEqual(res2.status_code, status.HTTP_200_OK)

    def test_delete_journal_table_succeeds(self):
        """
        Test delete journal table succeeds for authenticated user
        """
        journal_table = JournalTables.objects.create(
            journal=self.journal, table_name="lsdfjsdf dskfjlsdfjdsff"
        )

        delete_url = detail_url(journal_table.id)

        res = self.client.delete(delete_url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_journal_for_other_user_by_authenticated_user_fails(self):
        """
        Test deleting journal for other user by the authenticated user fails
        """
        journal_table = JournalTables.objects.create(
            journal=self.journal, table_name="lsdfjsdf dskfjlsdfjdsff"
        )

        user_payload = {
            "first_name": "Test",
            "last_name": "User",
            "email": "user2@example.com",
            "password": "Awesomeuser123",
        }
        user = create_user(**user_payload)
        self.client.force_authenticate(user)
        delete_url = detail_url(journal_table.id)

        res = self.client.delete(delete_url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_full_update_of_journal_table(self):
        """
        Test full update of a journal table succeeds
        """
        journal_table = JournalTables.objects.create(
            journal=self.journal, table_name="lsdfjsdf dskfjlsdfjdsff"
        )

        update_url = detail_url(journal_table.id)
        payload = {"table_name": "full update"}

        res = self.client.put(update_url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        journal_table.refresh_from_db()
        self.assertEqual(res.data["table_name"], payload["table_name"])

    def test_partial_update_of_journal_table(self):
        """
        Test partial update of a journal table succeeds
        """
        journal_table = JournalTables.objects.create(
            journal=self.journal, table_name="lsdfjsdf dskfjlsdfjdsff"
        )

        update_url = detail_url(journal_table.id)
        payload = {"table_name": "dklkfsdf"}

        res = self.client.patch(update_url, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        journal_table.refresh_from_db()
        self.assertEqual(res.data["table_name"], payload["table_name"])