# -*- coding: utf-8 -*-

import re

from pygments.lexer import Lexer, RegexLexer, bygroups, do_insertions, \
    default, include
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Generic
from pygments import unistring as uni

__all__ = ['Smt2Lexer']


line_re = re.compile('.*?\n')

class CustomLexer(RegexLexer):
    """
    A SMT-Lib 2 parser
    """
    name = 'Smt2'
    aliases = ['smt2']
    filenames = ['*.smt2']
    mimetypes = ['text/x-smt2']

    # list of known keywords and builtins taken form vim 6.4 scheme.vim
    # syntax file.
    keywords = (
        'declare-const', 'declare-fun', 'declare-sort', 'define-fun', 'assert', 'check-sat',
        'get-model', 'get-proof', 'get-value', 'echo', 'exit', 'error',
        'sat', 'unsat', 'unknown', 'model', 'set-option', 'set-logic',
        'anchor', 'step', 'assume'
    )
    sorts = (
        'Int', 'Bool'
    )
    builtins = (
        '*', '+', '-', '/', '<', '<=', '=', '>', '>=', 'and', 'or', 'distinct',
        'not', ':=', 'forall', 'exists', 'cl'
    )

    # valid names for identifiers
    # well, names can only not consist fully of numbers
    # but this should be good enough for now
    valid_name = r'[\w\.!$%&*+,/:<=>?@^~|-]+'

    tokens = {
        'root': [
            # the comments
            # and going to the end of the line
            (r';.*$', Comment.Single),
            # multi-line comment
            (r'#\|', Comment.Multiline, 'multiline-comment'),
            # commented form (entire sexpr folliwng)
            (r'#;\s*\(', Comment, 'commented-form'),
            # signifies that the program text that follows is written with the
            # lexical and datum syntax described in r6rs
            (r'#!r6rs', Comment),

            # whitespaces - usually not relevant
            (r'\s+', Text),

            # numbers
            (r'-?\d+\.\d+', Number.Float),
            (r'-?\d+', Number.Integer),
            # support for uncommon kinds of numbers -
            # have to figure out what the characters mean
            # (r'(#e|#i|#b|#o|#d|#x)[\d.]+', Number),

            # strings, symbols and characters
            (r'"(\\\\|\\"|[^"])*"', String),
            (r"'" + valid_name, String.Symbol),
            (r"#\\([()/'\"._!§$%& ?=+-]|[a-zA-Z0-9]+)", String.Char),

            # constants
            (r'(true|false)', Name.Constant),

            # special operators
            (r"('|#|`|,@|,)", Operator),

            # highlight the keywords
            ('(%s)' % '|'.join(re.escape(entry) for entry in keywords),
             Keyword.Reserved),

            # highlight the sorts
            ('(%s)' % '|'.join(re.escape(entry) for entry in sorts),
             Keyword.Type),

            # first variable in a quoted string like
            # '(this is syntactic sugar)
            (r"(?<='\()" + valid_name, Name.Variable),
            (r"(?<=#\()" + valid_name, Name.Variable),

            # highlight the builtins
            ("(?<=\()(%s)" % '|'.join(re.escape(entry) + '\s+' for entry in builtins),
             Name.Builtin),

            (r':' + valid_name, Name.Function),

            # the remaining functions
            #(r'(?<=\()' + valid_name, Name.Function),
            # find the remaining variables
            (valid_name, Name.Variable),

            # the famous parentheses!
            (r'(\(|\))', Punctuation),
            (r'(\[|\])', Punctuation),
        ],
        'multiline-comment': [
            (r'#\|', Comment.Multiline, '#push'),
            (r'\|#', Comment.Multiline, '#pop'),
            (r'[^|#]+', Comment.Multiline),
            (r'[|#]', Comment.Multiline),
        ],
        'commented-form': [
            (r'\(', Comment, '#push'),
            (r'\)', Comment, '#pop'),
            (r'[^()]+', Comment),
        ],
    }
