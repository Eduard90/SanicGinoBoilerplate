async def connect_to_pg(host, port, user, password, database, loop):
    from models import db
    await db.create_pool(host=host, port=port, user=user, password=password, database=database, loop=loop)
