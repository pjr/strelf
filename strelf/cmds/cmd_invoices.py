import os
import click
from strelf.helper.invoice import InvoiceHelper


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.option(
    '--output-dir',
    required=True,
    help="Directory to output invoices to. Defaults to invoices/"
)
@click.option(
    '--yes',
    is_flag=True
)
@click.pass_context
def download(ctx, output_dir, yes):
    """ Download all invoices from stripe and output to a directory """
    # Don't allow outputting to a directory that isn't empty
    # unless there's an explicit yes. Stops overwriting.
    if not yes and os.listdir(output_dir):
        print("Dir '%s' not empty. Pass --yes to ignore" % output_dir)
        return

    # Get all customer and invoice objects
    for cust, inv in InvoiceHelper.get_all(ctx.obj.cfg['src.live']):
        # Make sure customer object has an email or use id
        # Replace any @ symbols in the email as it's
        # being used for directory name
        sub = cust['id'] if len(cust['email']) == 0 \
                else cust['email'].replace('@', '__')
        path = f"{output_dir}/{sub}/{inv['id']}.pdf"
        InvoiceHelper.download_pdf(ctx.obj.cfg['src.live'],
                                   inv['invoice_pdf'], path)
