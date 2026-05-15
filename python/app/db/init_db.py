import pugsql

queries = pugsql.module("/queries")

def init_db(db_url: str = "sqlite:///links.db"):
    queries.connect(db_url)
    queries.create_links_table()