from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'SharedgeKnowledge.apps.Accounts'
    def ready(self):
        import SharedgeKnowledge.apps.Accounts.signals
