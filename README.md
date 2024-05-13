# TreeSitter

## Prepare Grammer Files

- Download language grammer, compile it, get the `so` library file
- For this library, simply

```shell
git submodule init
cd ./tree-sitter-lua
make
cp ./tree-sitter-lua/libtree-sitter-lua.so ./
```

## Import Language and Passes to Parser

1. create a Language instance, say `LUA`, with the library and langauge's name
2. create a Parser instance
3. pass lanauge to the Parser


## Parsing

1. Parsing: call `Parser.parse(src_code)` on the language src code, you get the `Tree`
2. Get root node from `Tree` using `Tree.root_node`
3. You can inspect `Node`'s property, like `text`, `range`

## Query

1. Create `Query` instance using `LUA.query(node)`
2. Query uses a lisp-like syntax. Not so hard, just read [official documentation](https://tree-sitter.github.io/tree-sitter/syntax-highlighting#queries)
3. Use `Query.capture(node)` or `Query.match(node)` to capture code block you want. Differences are subtle, inspect it with `icecream.ic` makes more sense, and don't forget to read the source code of the python bindings of treesitter. This is quite self-explainary.
