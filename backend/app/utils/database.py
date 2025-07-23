from azure.cosmos import CosmosClient
from app.core.config import settings

def get_cosmos_client():
    """
    Azure Cosmos DB 클라이언트 반환
    """
    if not settings.cosmos_db_uri or not settings.cosmos_db_key:
        raise ValueError("Cosmos DB 설정이 필요합니다")
    
    return CosmosClient(settings.cosmos_db_uri, settings.cosmos_db_key)

def get_cosmos_database():
    """
    Cosmos DB 데이터베이스 반환
    """
    client = get_cosmos_client()
    return client.get_database_client(settings.cosmos_db_name)

def get_cosmos_container(container_name: str):
    """
    Cosmos DB 컨테이너 반환
    """
    database = get_cosmos_database()
    return database.get_container_client(container_name)
