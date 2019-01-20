from flask import Flask
from flask_table import Table, Col, LinkCol
from csh_client import CshClient

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class ItemTable(Table):
    name = Col(
        'Name',
        # Apply this class to both the th and all tds in this column
        column_html_attrs={'class': 'my-name-class'},
    )
    description = Col(
        'Description',
        # Apply these to both
        column_html_attrs={
            'data-something': 'my-data',
            'class': 'my-description-class'},
        # Apply this to just the th
        th_html_attrs={'data-something-else': 'my-description-th-class'},
        # Apply this to just the td - note that this will things from
        # overwrite column_html_attrs.
        td_html_attrs={'data-something': 'my-td-only-data'},
    )


def table_main():
    items = []
    items.append(Item('Name1', 'Description1'))
    items.append(Item('Name2', 'Description2'))
    items.append(Item('Name3', 'Description3'))

    table = ItemTable(items)

    # or {{ table }} in jinja
    return table.__html__()

app=Flask(__name__)

@app.route('/')
def index():
    csh_client = CshClient()

    req = {"path": "stadb.s", "arguments": ""}
    data = csh_client.req(req)
    print(data)
    del csh_client

    return data

if __name__=="__main__":

    app.run()