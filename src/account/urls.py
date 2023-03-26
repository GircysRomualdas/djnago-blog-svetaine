from django.urls import path

from account.views import(

    getAccounts,
    getAccount,
    addAccount,
    updateAccount,
    deleteAccount,
)

app_name = 'account'

urlpatterns = [
    path('accounts/', getAccounts, name='accounts'),
    path('accounts/<slug>/', getAccount, name='accountsid'),
    path('accounts/post', addAccount, name='accountspost'),
    path('accounts/<slug>/put', updateAccount, name='accountsput'),
    path('accounts/<slug>/delete', deleteAccount, name='accountsdelete'),
]