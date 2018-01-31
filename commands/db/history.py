import click


@click.command(help="Apply migrations")
def history():
    import os
    import settings
    from alembic.config import Config
    from alembic.command import history

    alembic_ini_path = os.path.join(settings.BASE_DIR, 'alembic.ini')
    alembic_cfg = Config(alembic_ini_path)
    history(alembic_cfg)

