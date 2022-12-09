import config
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

engine = create_async_engine(
    config.db,
)
