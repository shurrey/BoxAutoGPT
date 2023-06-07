import json

from . import BoxPlugin

plugin = BoxPlugin()

"""
who_am_i(query)
list_box_files(),
get_content(file_id),
post_metadata(metadata, file_id)
"""


def who_am_i(query: str) -> str | list[str]:
    res = ""

    try:
        me = plugin.client.user().get()
        print(f'My user ID is {me.id}')
        res=me
    except Exception as e:
        return f"'who_am_i' on query: '{query}' raised exception: '{e}'"
    return res

def list_box_files():
    res = ""

    try:
        items = plugin.client.folder(folder_id='0').get_items()
        for item in items:
            print(f'{item.type.capitalize()} {item.id} is named "{item.name}"')
        res=items
    except Exception as e:
        return f"'list_box_files' raised exception: '{e}'"
    return res

def get_content(file_id: str) -> str | list[str]:
    res = ""

    try:
        file_content = plugin.client.file(file_id).content()
        print(f'file content: {file_content}"')
        res=file_content
    except Exception as e:
        return f"'get_content' on query: '{file_id}' raised exception: '{e}'"
    return res

def post_metadata(value: str, file_id: str):
    res = ""

    metadata = {
        "summary" : value
    }

    try:
        applied_metadata = plugin.client.file(file_id=file_id).metadata(scope='enterprise', template='AutoGPT-Template').set(metadata)
        print(f'Set metadata in instance ID {applied_metadata["$id"]}')
        res=applied_metadata
    except Exception as e:
        return f"'post_metadata' on query: '{metadata}' and '{file_id}' raised exception: '{e}'"
    return res