from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config import get_settings

async_engine = create_async_engine(
    url=get_settings().postgres.SQLALCHEMY_URL,
    echo=False,
    pool_size=5,
    max_overflow=10
)

async_session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(async_engine)
