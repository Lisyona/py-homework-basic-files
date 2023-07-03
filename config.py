access_token = 'https://oauth.vk.com/blank.html#access_token=vk1.a.wjefyk_law92tQthurDXFI2KVoA2eRpOu68jV6EJOI4jzBLfIs-IpR7JvLXPBqxbmquilTEcLERdfQuW4kAq8OCZftgfQ3_CYmucfWuL2pdcWQgdBNxZ1zG9IbiYebjZOMxKQMTlE9KAtXzsZTPx0ir8fCqxNn7WTa1IhmRyUgDM-yGIoFzAfkKn_kizopv2&expires_in=86400&user_id=15206350'
community_token = 5osBKv8CLGiNWkrLJqX2
DSN = 'postgresql://postgres:Lisyona@localhost:5432/books'
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()

create_tables(engine)