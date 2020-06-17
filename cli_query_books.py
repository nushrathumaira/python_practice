import click
import requests

"""
As you can see, the group() decorator works like the command() decorator, but creates a Group object instead which can be given multiple subcommands that can be attached with Group.add_command().
For simple scripts, it’s also possible to automatically attach and create a command by using the Group.command() decorator instead. .
You would then invoke the Group in your setuptools entry points or other invocations.
"""
__author__ = "Diana Gabaldon"

@click.group()
def main():
    """ Simple CLI"""
    pass

@main.command()
@click.argument('query')
def search(query):
    " This search and return results corresponding to the given query from google books"
    url_format = 'https://www.googleapis.com/books/v1/volumes'
    query = "+".join(query.split())
    
    query_params = {
        'q': query
    }
    
    response = requests.get(url_format, params = query_params)
    click.echo(response.json()['items'])
    
@main.command()
@click.argument('id')
def get(id):
    """This return a particular book from the given id on Google Books"""

    url_format = 'https://www.googleapis.com/books/v1/volumes/{}'
    click.echo(id)
    
    response = requests.get(url_format.format(id))
    click.echo(response.json())
    
    
if __name__ == "__main__":
    main()
    


    
    