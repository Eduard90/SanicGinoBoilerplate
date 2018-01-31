import click


@click.command(help="Show current revision")
def current():
    import os
    import settings
    from alembic.config import Config
    from alembic.command import current

    alembic_ini_path = os.path.join(settings.BASE_DIR, 'alembic.ini')
    alembic_cfg = Config(alembic_ini_path)
    current(alembic_cfg)
