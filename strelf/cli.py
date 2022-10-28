import os
import click
from strelf.config import ConfigStripe


class StrelfCmd(click.MultiCommand):
    cmd_folder = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "cmds")
    )

    def list_commands(self, ctx):
        rv = []
        for file in os.listdir(self.cmd_folder):
            if file.endswith(".py") and file.startswith("cmd_"):
                rv.append(file[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        mod = __import__(f"strelf.cmds.cmd_{name}", None, None, ["cli"])
        return mod.cli


class Strelf:
    def __init__(self):
        self.cfg = ConfigStripe()


@click.command(cls=StrelfCmd)
@click.option(
    '--dry-run',
    is_flag=True
)
@click.pass_context
def cli(ctx, dry_run):
    """ CLI for Strelf, a stripe elf migration helper tool"""
    ctx.obj = Strelf()


cli()
