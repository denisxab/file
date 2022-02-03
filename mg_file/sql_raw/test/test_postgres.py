import sql_raw.async_sql.async_postgres_sql
import sql_raw.async_sql.async_postgres_sql
import sql_raw.async_sql.async_postgres_sql
import sql_raw.async_sql.async_serializer
import sql_raw.sync_sql.sync_postgres_sql
import sql_raw.sync_sql.sync_serializer

NAME_DB = "fast_test"
NAME_TABEL = "test_tabel"

Refresh_TABLE = f"""
DROP TABLE IF EXISTS {NAME_TABEL};
CREATE TABLE {NAME_TABEL}
(
    id    serial PRIMARY KEY,
    email varchar(255),
    buy   money
);
"""


def refresh_db():
    """
     Если `FATAL: Peer authentication failed for user "postgres"`

     1. Установить или сменить пароль для пользователя `postgres`
         `sudo passwd postgres;`

     2. Изменить способ подключения е БД
         `sudo micro /etc/postgresql/12/main/pg_hba.conf`
         "
         local   all             postgres                                password
         "
     3. Перезагрузить БД
         `sudo systemctl restart  postgresql`
     """
    # Подключаемся к СУБД
    db = sql_raw.sync_sql.sync_postgres_sql.Config(user="postgres", password="root")
    # Удаляем БД
    db.wsql(f"DROP DATABASE IF EXISTS {NAME_DB};", autocommit=True)
    # Создаем БД
    db.wsql(f"CREATE DATABASE {NAME_DB};", autocommit=True)


class Test_Sync:

    def setup(self):
        refresh_db()
        # Подключаемся к БД
        self.db = sql_raw.sync_sql.sync_postgres_sql.Config(user="postgres", password="root", database=NAME_DB)
        # Создаем таблицу
        self.db.wsql(Refresh_TABLE)

    def test_write(self):
        self.db.wsql(f"""
        INSERT INTO {NAME_TABEL} (id, email, buy)
        VALUES (1, 'dcurrington0@umn.edu', 955),
               (2, 'rhartland1@blog.com', 430),
               (3, 'zkinton2@so-net.ne.jp', 817),
               (4, 'btuison6@themeforest.net', 281),
               (5, 'gczajka4@tinypic.com', 610),
               (6, 'btuison6@themeforest.net', 281),
               (7, 'btuison6@themeforest.net', 281),
               (8, 'aclancy7@tmall.com', 884),
               (9, 'zkinton2@so-net.ne.jp', 817),
               (10, 'ndelaperrelle9@smh.com.au', 523);
        """)
        assert self.db.Rsql(
            f"SELECT * FROM {NAME_TABEL}") == "[(1, 'dcurrington0@umn.edu', '955,00 ₽'),\n (2, 'rhartland1@blog.com', '430,00 ₽'),\n (3, 'zkinton2@so-net.ne.jp', '817,00 ₽'),\n (4, 'btuison6@themeforest.net', '281,00 ₽'),\n (5, 'gczajka4@tinypic.com', '610,00 ₽'),\n (6, 'btuison6@themeforest.net', '281,00 ₽'),\n (7, 'btuison6@themeforest.net', '281,00 ₽'),\n (8, 'aclancy7@tmall.com', '884,00 ₽'),\n (9, 'zkinton2@so-net.ne.jp', '817,00 ₽'),\n (10, 'ndelaperrelle9@smh.com.au', '523,00 ₽')]"

        assert self.db.rsql(f"SELECT * FROM {NAME_TABEL}") == [
            (1, 'dcurrington0@umn.edu', '955,00 ₽'),
            (2, 'rhartland1@blog.com', '430,00 ₽'),
            (3, 'zkinton2@so-net.ne.jp', '817,00 ₽'),
            (4, 'btuison6@themeforest.net', '281,00 ₽'),
            (5, 'gczajka4@tinypic.com', '610,00 ₽'),
            (6, 'btuison6@themeforest.net', '281,00 ₽'),
            (7, 'btuison6@themeforest.net', '281,00 ₽'),
            (8, 'aclancy7@tmall.com', '884,00 ₽'),
            (9, 'zkinton2@so-net.ne.jp', '817,00 ₽'),
            (10, 'ndelaperrelle9@smh.com.au', '523,00 ₽')]

        assert self.db.rsql(f"SELECT * FROM {NAME_TABEL}", tdata=sql_raw.sync_sql.sync_serializer.Efetch.dict_) == [
            {'id': 1, 'email': 'dcurrington0@umn.edu', 'buy': '955,00 ₽'},
            {'id': 2, 'email': 'rhartland1@blog.com', 'buy': '430,00 ₽'},
            {'id': 3, 'email': 'zkinton2@so-net.ne.jp', 'buy': '817,00 ₽'},
            {'id': 4, 'email': 'btuison6@themeforest.net', 'buy': '281,00 ₽'},
            {'id': 5, 'email': 'gczajka4@tinypic.com', 'buy': '610,00 ₽'},
            {'id': 6, 'email': 'btuison6@themeforest.net', 'buy': '281,00 ₽'},
            {'id': 7, 'email': 'btuison6@themeforest.net', 'buy': '281,00 ₽'},
            {'id': 8, 'email': 'aclancy7@tmall.com', 'buy': '884,00 ₽'},
            {'id': 9, 'email': 'zkinton2@so-net.ne.jp', 'buy': '817,00 ₽'},
            {'id': 10, 'email': 'ndelaperrelle9@smh.com.au', 'buy': '523,00 ₽'}]

        assert self.db.Rsql(f"SELECT * FROM {NAME_TABEL}",
                            tdata=sql_raw.sync_sql.sync_serializer.Efetch.namedtuple) == "[_(id=1, email='dcurrington0@umn.edu', buy='955,00 ₽'),\n _(id=2, email='rhartland1@blog.com', buy='430,00 ₽'),\n _(id=3, email='zkinton2@so-net.ne.jp', buy='817,00 ₽'),\n _(id=4, email='btuison6@themeforest.net', buy='281,00 ₽'),\n _(id=5, email='gczajka4@tinypic.com', buy='610,00 ₽'),\n _(id=6, email='btuison6@themeforest.net', buy='281,00 ₽'),\n _(id=7, email='btuison6@themeforest.net', buy='281,00 ₽'),\n _(id=8, email='aclancy7@tmall.com', buy='884,00 ₽'),\n _(id=9, email='zkinton2@so-net.ne.jp', buy='817,00 ₽'),\n _(id=10, email='ndelaperrelle9@smh.com.au', buy='523,00 ₽')]"

        assert self.db.rsql(f"SELECT * FROM {NAME_TABEL}",
                            tdata=sql_raw.sync_sql.sync_serializer.Efetch.one) == (
                   1, 'dcurrington0@umn.edu', '955,00 ₽')


class Test_Async:

    def setup(self):
        refresh_db()
        # Подключаемся к БД
        self.db = sql_raw.async_sql.async_postgres_sql.Config(user="postgres", password="root", database=NAME_DB)
        # Создаем таблицу
        self.db.appendTask(self.db.wsql(Refresh_TABLE))
        self.db.executeTasks()

    def test_write(self):
        ...

#
#
# def test_async_read():
#     db = sql_raw.async_postgres_sql.Config(user="postgres", password="root", database="fast_api")
#
#     st = time.process_time()
#     db.extendTask([
#         db.rsql("SELECT * FROM пользователь;", tdata=Efetch.dict_),
#         db.rsql("SELECT id FROM пользователь;"),
#         db.rsql("SELECT * FROM пользователь;"),
#     ])
#     db.appendTask(db.rsql("SELECT * FROM пользователь;"))
#     pprint(db.executeTasks())
#     print("async_sql", time.process_time() - st)
#
#
# def test_sync_read():
#     db = sql_raw.postgres_sql.Config(user="postgres", password="root", database="fast_api")
#     st = time.process_time()
#     db.Rsql("SELECT * FROM пользователь;")
#     db.Rsql("SELECT id FROM пользователь;")
#     db.Rsql("SELECT * FROM пользователь;")
#     db.Rsql("SELECT * FROM пользователь;")
#     db.Rsql("SELECT * FROM пользователь;")
#     db.Rsql("SELECT id FROM пользователь;")
#     db.Rsql("SELECT * FROM пользователь;")
#     db.Rsql("SELECT * FROM пользователь;")
#     db.Rsql("SELECT * FROM пользователь;")
#     db.Rsql("SELECT id FROM пользователь;")
#     db.Rsql("SELECT * FROM пользователь;")
#     db.Rsql("SELECT * FROM пользователь;")
#     print("sync_sql", time.process_time() - st)
#
#
# def test_main_test():
#     test_asyncread()
#     # test_sync_read()

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
