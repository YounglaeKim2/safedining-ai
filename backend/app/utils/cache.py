import redis.asyncio as redis
from app.core.config import settings

_redis_client = None

async def get_redis_client():
    """
    Redis 클라이언트 반환 (싱글톤)
    """
    global _redis_client
    
    if _redis_client is None:
        _redis_client = redis.from_url(settings.redis_url)
    
    return _redis_client

async def close_redis_connection():
    """
    Redis 연결 종료
    """
    global _redis_client
    
    if _redis_client:
        await _redis_client.close()
        _redis_client = None
