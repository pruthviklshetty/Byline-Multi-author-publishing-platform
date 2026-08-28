import os

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool

from config import settings

# On serverless (Vercel) every invocation may run in its own process, so a
# per-process connection pool would multiply against Neon's connection limit.
# NullPool opens/closes a connection per request and lets Neon's pooler manage
# concurrency. Long-lived hosts (Render) keep SQLAlchemy's default pool.
_engine_kwargs = {"poolclass": NullPool} if os.environ.get("VERCEL") else {}

engine = create_async_engine(settings.database_url, **_engine_kwargs)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session