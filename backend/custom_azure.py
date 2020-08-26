from storages.backends.azure_storage import AzureStorage


class AzureStaticStorage(AzureStorage):
    account_name = 'hbtodostatic'
    account_key = 'eAHGnZdRbPwFw8E4kEGqhZYYwdYaaDtIbequ1Ss/lYts9h21bTbtabeYw57Fng20GyLHetFpDNksqyBnb0jnpg=='
    azure_container = 'static'
    expiration_secs = None

