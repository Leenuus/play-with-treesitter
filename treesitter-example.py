#!/usr/bin/env python

from tree_sitter import Language, Parser
from tree_sitter_python import language
from icecream import ic

lua_src = b"""
nmap('ls', 'l', 'good')
"""

def main():

    lib = "./libtree-sitter-lua.so"
    LUA = Language(lib, "lua")
    parser = Parser()
    parser.set_language(LUA)

    tree = parser.parse(lua_src)
    root = tree.root_node
    ic(root)

    sexp = root.sexp()
    ic(sexp)

    query_src = """
        (function_call
        ) @f
"""
    q = LUA.query(query_src)
    # c = q.matches(root)
    cs = q.captures(root)
    ic(cs)

    for c in cs:
        c_name = c[1]
        node = c[0]
        if c_name == 'f':
            func_name = node.children_by_field_name('name')
            ic(func_name[0].text)


if __name__ == "__main__":
    main()
