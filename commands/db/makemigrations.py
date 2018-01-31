import click


@click.command(help="Auto make migrations")
@click.option("-m", help="Migration message")
def makemigrations(m):
    import os
    import settings
    from alembic.config import Config
    from alembic.command import revision

    alembic_ini_path = os.path.join(settings.BASE_DIR, 'alembic.ini')
    alembic_cfg = Config(alembic_ini_path)
    revision_kwargs = {'autogenerate': True}
    if m is not None:
        revision_kwargs['message'] = m
    revision(alembic_cfg, **revision_kwargs)
