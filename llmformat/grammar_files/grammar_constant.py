import codecs
from os import path

from llmformat.constant import _SPECIAL_TOKENS
from llmformat.lex_helper import symbol_character_parse


def parse_lex_definition(grammar):
    lex_definition = grammar
    symbol2def = {}
    char2symbol = {}
    def add_char_symbol(symbol, char):
        nonlocal char2symbol
        char2symbol[char] = symbol

    for line in lex_definition.split("\n"):
        line = line.strip()
        if line.startswith("#") or line.startswith("\\") or line.startswith("//"):
            continue
        pos = line.find(":")
        if pos == -1:
            continue
        symbol = line[:pos].strip()
        definition = line[pos+1:].strip()
        # Capitalized symbol is token in grammar
        if symbol == symbol.upper() and symbol not in _SPECIAL_TOKENS:
            symbol2def[symbol] = definition
            symbol_character_parse(symbol, definition, add_char_symbol)
    return symbol2def, char2symbol

if __name__ == "__main__":
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "base.bnf"))
    print(parse_lex_definition())