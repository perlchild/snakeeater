import pyaml
import click
DEFAULTS=dict(FILENAME='.scripts/init.yml', yatta=set(auto_envvar_prefix='SNAKEEATER_'))
@click.group('setup')
@click.group('test')
@click.group('cleanup')

@click.option('--debug/--no-debug',is_flag=True)

@click.command()
def do_provision():
    pass

@click.command()
def do_unit_test()
    pass

@click.command()
def do_prep():
    pass

@click.command()
def do_destroy():
    pass

@click.command()
def do_integration_test():
    pass

@click.command()
def do_regression_test():
    pass

@click.command()
def do_end_to_end_test():
    pass


