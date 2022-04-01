from os import environ

try:
    from sqlalchemy import text
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
except ImportError:
    pass

engine = create_async_engine(
    # "postgresql+asyncpg://ИмяПользователя:Пароль@Домен/БД"
    f"postgresql+asyncpg://{environ['POSTGRES_USER']}:{environ['POSTGRES_PASSWORD']}@{environ['POSTGRES_IP']}/{environ['POSTGRES_DB']}"
)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# Для ORM моделей
Base = declarative_base()


# Получить сессию
async def get_session() -> AsyncSession:
    # Получить сессию await get_session().__anext__()
    async with async_session() as session:
        yield session


# Получить сессию в транзакции
async def get_session_transaction() -> AsyncSession:
    # Получить сессию await get_session_transaction().__anext__()
    async with async_session() as session:
        async with session.begin():
            yield session


def get_session_decor(fun):
    """
    @get_session_dec
    async def NameFun(..., session: AsyncSession):
        await session.execute(text('''sql'''))
        # await session.commit()
    """

    async def wrapper(*arg, **kwargs):
        async with async_session() as session:
            res = await fun(*arg, **kwargs, _session=session)
        return res

    return wrapper


async def execute_raw_sql(raw_sql: str):
    """
    Создать таблицу из raw sql

    .. code-block:: python

        import asyncio

        schema = '''
        CREATE TABLE IF NOT EXISTS subscribe
        (
            id      serial PRIMARY KEY,
            user_id bigint unique,
            user_name VARCHAR (255)
        );
        '''

        if __name__ == '__main__':
            asyncio.run(execute_raw_sql(schema))
    """

    # AsyncConnection
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.execute(text(raw_sql))
        await conn.commit()
