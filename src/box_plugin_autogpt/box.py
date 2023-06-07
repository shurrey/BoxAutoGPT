from . import BoxPlugin

plugin = BoxPlugin()


def _box_folder_query(query: str) -> str | list[str]:
    res = ""

    try:
        me = plugin.client.user().get()
        print(f'My user ID is {me.id}')
        res=me
    except Exception as e:
        return f"'_box_folder_query' on query: '{query}' raised exception: '{e}'"
    return res