from django.utils.tree import Node
from django import template


class MyNode(Node):
    def __init__(self, menu_item, *args, **kwargs):
        super().__init__(args, **kwargs)
        self.item = menu_item
        self.id = menu_item.pk
        self.name = menu_item.name
        self.slug = menu_item.slug
        self.parent = menu_item.parent

    def __str__(self):
        return self.name

    @property
    def url(self):
        table_name = self.item._meta.db_table.split('_')[1]
        item = self.item
        url = ''
        while item:
            url = f'{item.slug}/{url}'
            item = item.parent
        return f'{table_name}\{url}'


class MenuBuilder(template.Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name.strip('\'\"')

    def render(self, context):
        path = context.get('path')
        queryset = context.get(self.menu_name)
        forest = self.build_tree(queryset=queryset)
        return self.get_output(forest, path)

    def get_output(self, nodes, path):
        path: str = path or ''
        output = ''
        for node in nodes:
            if node.parent is None or path.startswith(self.menu_name) and \
                    (node.slug in path or node.parent.slug in path):
                output += f'\n<li>' \
                          f'<a href="/{node.url}">{node.name}'
                if path and path.startswith(self.menu_name) and path.endswith(f'{node.slug}/'):
                    output += ' >'
                output += '</a>'
                if node.children:
                    output += f'\n<ul>' \
                              f'{self.get_output(node.children, path)}' \
                              f'\n</ul>'
                output += '\n</li>'
        return output

    def build_tree(self, queryset, parent_id=None):
        nodes = []
        if queryset is not None:
            for item in queryset.filter(parent_id=parent_id):
                node = MyNode(item)
                node.children = self.build_tree(queryset=queryset, parent_id=item.pk)
                nodes.append(node)
        return nodes
