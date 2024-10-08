# FSM-on-dynamodb

<a href="https://opensource.org/license/MIT"><img src="https://img.shields.io/badge/license-MIT-green.svg?logo=mit&logoColor=f5f5f5" alt="MIT-license"></a>
<a href="https://github.com/general-soldatov/FSM-on-dynamodb/"><img src="https://img.shields.io/badge/dynamo-fsm-blue.svg?logo=telegram&logoColor=f5f5f5" alt="dynamo-fsm"></a>
<img src="https://img.shields.io/badge/python-3.9%7C3.10%7C3.11-blue?logo=python&logoColor=f5f5f5" alt="Python" />
<a href="https://github.com/aiogram/aiogram/blob/dev-3.x/"><img src="https://img.shields.io/badge/aiogram-3.10-blue.svg?logo=telegram&logoColor=blue" alt="dynamo-fsm"></a>
<img src="https://img.shields.io/badge/boto3-dynamodb-green.svg?logo=" alt="dynamodb-boto3">

Надстройка над `aiogram` для организации FSM (finite-state-machine) на базе базы данных dynamodb с использованием библиотеки boto3 &amp; botocore. Может быть использована на serverless-решениях AWS и YandexCloud. Установить библиотеку можно с помощью команды:
```bash
pip install dynamodb-fsm
```
В GUI облачной панели управления или с помощью CLI создайте динамическую serverless базу данных и сервисный аккаунт с ключом. Для пользователей YandexCloud можете воспользоваться [документацией](https://yandex.cloud/ru/docs/ydb/quickstart).
Для корректной работы библиотеки `boto3` используется dataclass c переменными окружения, поэтому не забудьте внести следующую информацию в файл `.env`
```BASH
ENDPOINT='url_endpoint'
REGION_NAME='ru-central1'
AWS_ACCESS_KEY_ID='key_id'
AWS_SECRET_ACCESS_KEY='access_key_db'
```
В случае использования собственной конфигурации рекомендуется реализовать следующий код:

```python
from dynamodb_fsm import FSMDynamodb

...

@dataclass
class DatabaseConfig:
    endpoint_url: str = 'ENDPOINT'
    region_name: str = 'REGION_NAME'
    aws_access_key_id: str = 'AWS_ACCESS_KEY_ID'
    aws_secret_access_key: str = 'AWS_SECRET_ACCESS_KEY'


config = DatabaseConfig().__dict__
storage = FSMDynamodb(config=config)
```
Для подключения хранилища состояний к диспетчеру `aiogram` используйте следующий пример кода:

```python
from dynamodb_fsm import FSMDynamodb

...

storage = FSMDynamodb()
dp = Dispatcher(storage=storage)
```

Если вы планируете использование aiogram-dialog, то рекомендуется использование следующих надстроек:
```python
storage = FSMDynamodb(with_destiny=True)
```
Поскольку в хранилище из коробки используется строитель ключей, рекомендуемый aiogram, то при использовании меняйте параметр `with_destiny=True`, по умолчанию равен `False`.
Актуальная информация о функциях надстройки есть в репозитории [dynamodb-fsm](https://github.com/general-soldatov/FSM-on-dynamodb/tree/main)
