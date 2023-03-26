from django.test import TestCase

from account.views import(

    getAccounts,
    getAccount,
    addAccount,
    updateAccount,
    deleteAccount,
)

class AccountTest(TestCase):

    # Accounts tests
    def test_getAccounts_code(self):
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, 200)



