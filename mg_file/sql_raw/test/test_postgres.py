# from sql_raw.base_deco import wsql
import time

import sql_raw.async_sql.async_postgres_sql
import sql_raw.sync_sql.postgres_sql


def test_asyncread():
    db = sql_raw.async_postgres_sql.Config(user="postgres", password="root", database="fast_api")

    async def main():
        st = time.process_time()
        await db.Rsql("SELECT * FROM пользователь;")
        await db.Rsql("SELECT id FROM пользователь;")
        await db.Rsql("SELECT * FROM пользователь;")
        await db.Rsql("SELECT * FROM пользователь;")
        await db.Rsql("SELECT * FROM пользователь;")
        await db.Rsql("SELECT id FROM пользователь;")
        await db.Rsql("SELECT * FROM пользователь;")
        await db.Rsql("SELECT * FROM пользователь;")
        await db.Rsql("SELECT * FROM пользователь;")
        await db.Rsql("SELECT id FROM пользователь;")
        await db.Rsql("SELECT * FROM пользователь;")
        await db.Rsql("SELECT * FROM пользователь;")
        print("async_sql", time.process_time() - st)

    def te():
        st = time.process_time()
        db.extendTask([
            db.Rsql("SELECT * FROM пользователь;"),
            db.Rsql("SELECT id FROM пользователь;"),
            db.Rsql("SELECT * FROM пользователь;"),
        ])
        db.appendTask(db.Rsql("SELECT * FROM пользователь;"))
        print(db.executeTasks())
        print("async_sql", time.process_time() - st)

    te()

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())


def test_sync_read():
    db = sql_raw.postgres_sql.Config(user="postgres", password="root", database="fast_api")
    st = time.process_time()
    db.Rsql("SELECT * FROM пользователь;")
    db.Rsql("SELECT id FROM пользователь;")
    db.Rsql("SELECT * FROM пользователь;")
    db.Rsql("SELECT * FROM пользователь;")
    db.Rsql("SELECT * FROM пользователь;")
    db.Rsql("SELECT id FROM пользователь;")
    db.Rsql("SELECT * FROM пользователь;")
    db.Rsql("SELECT * FROM пользователь;")
    db.Rsql("SELECT * FROM пользователь;")
    db.Rsql("SELECT id FROM пользователь;")
    db.Rsql("SELECT * FROM пользователь;")
    db.Rsql("SELECT * FROM пользователь;")
    print("sync_sql", time.process_time() - st)


def test_main_test():
    test_asyncread()
    # test_sync_read()

# async_sql def go():
#     async_sql with aiopg.create_pool() as pool:
#         async_sql with pool.acquire() as conn:
#             async_sql with conn.cursor() as cur:
#                 await cur.execute("SELECT * FROM пользователь;")
#                 ret = await cur.fetchall()
#                 print(ret)
#
# async_sql def go_2():
#     async_sql with aiopg.connect('dbname=fast_api user=postgres password=root host=127.0.0.1') as _conn:
#         async_sql with _conn.cursor() as _cur:
#             await _cur.execute("SELECT * FROM пользователь")
#             ret = await _cur.fetchall()
#             print(ret)


# print(db.Rsql("SELECT * FROM пользователь;", tdata=Efetch.a))

# def test_write():
#     wsql("INSERT INTO пользователь (id,f_name, l_name) VALUES (16,'t', 'd');")
#
#
# def test_init():
#     wsql("""
#     CREATE TABLE пользователь
#     (
#         id     serial PRIMARY KEY,
#         f_name varchar(255) NOT NULL,
#         l_name varchar(255) NOT NULL
#     );
#     INSERT INTO пользователь (id, f_name, l_name)
#     VALUES (1, 'Carola', 'Yandle'),
#            (2, 'Risa', 'Follet'),
#            (3, 'Cele', 'Caslin'),
#            (4, 'Osgood', 'Demead'),
#            (5, 'Roldan', 'Malby'),
#            (6, 'Reynard', 'Garlee'),
#            (7, 'Erna', 'Vigurs'),
#            (8, 'Stewart', 'Naismith'),
#            (9, 'Poppy', 'Watling'),
#            (10, 'Sybila', 'Teliga');
#     CREATE TABLE фотографии
#     (
#         id         serial PRIMARY KEY,
#         id_user    integer REFERENCES пользователь (id) ON DELETE CASCADE ON UPDATE CASCADE,
#         path_image varchar(600)
#     );
#     INSERT INTO фотографии (id, id_user, path_image)
#     VALUES (1, 1, 'http://dummyimage.com/212x100.png/dddddd/000000'),
#            (2, 4, 'http://dummyimage.com/170x100.png/cc0000/ffffff'),
#            (3, 5, 'http://dummyimage.com/147x100.png/dddddd/000000'),
#            (4, 6, 'http://dummyimage.com/122x100.png/5fa2dd/ffffff'),
#            (5, 2, 'http://dummyimage.com/222x100.png/dddddd/000000'),
#            (6, 4, 'http://dummyimage.com/217x100.png/dddddd/000000'),
#            (7, 1, 'http://dummyimage.com/192x100.png/cc0000/ffffff'),
#            (8, 9, 'http://dummyimage.com/118x100.png/5fa2dd/ffffff'),
#            (9, 6, 'http://dummyimage.com/215x100.png/cc0000/ffffff'),
#            (10, 4, 'http://dummyimage.com/235x100.png/ff4444/ffffff');
#     """)
