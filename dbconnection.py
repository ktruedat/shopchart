from sqlalchemy import create_engine


def create_connection():
    uri = "mysql://root:admin@127.0.0.1/shopchart"
    engine = create_engine(uri)
    return engine
