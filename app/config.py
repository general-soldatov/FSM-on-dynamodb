import boto3
from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv

@dataclass
class DatabaseConfig:
    endpoint_url: str = getenv('ENDPOINT')
    region_name: str = getenv('REGION_NAME')
    aws_access_key_id: str = getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key: str = getenv('AWS_SECRET_ACCESS_KEY')


load_dotenv()
# database_config = DatabaseConfig(endpoint_url=getenv('ENDPOINT'),
#                                  region_name=getenv('REGION_NAME'),
#                                  aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'),
#                                  aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY'))

# kwargs_config = {
#     'endpoint_url': database_config.endpoint_url,
#     'region_name': database_config.region_name,
#     'aws_access_key_id': database_config.aws_access_key_id,
#     'aws_secret_access_key': database_config.aws_secret_access_key
# }

dynamodb_config = boto3.resource('dynamodb', **DatabaseConfig().__dict__)
dynamodb_client = boto3.client('dynamodb', **DatabaseConfig().__dict__)