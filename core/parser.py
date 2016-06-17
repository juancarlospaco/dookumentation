#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Python source code file path to JSON string meta-data Parser."""


import logging as log

import ast
import _ast


__all__ = ["PyParse"]


class PyParse(object):

    """Python source code file path to JSON string meta-data Parser."""

    def parse_file(self, filepath):
        """Parse file,create info Imports,Class,Function,Attr,Decorator,etc."""
        source = ""
        with open(filepath, 'r', encoding="utf-8") as python_file_to_read:
            source = python_file_to_read.read()
        if source:
            symbols = self.get_symbols(source, filepath)
            return symbols

    def get_symbols(self, source, filename=''):
        """Parse module code to get Classes, Functions and Assigns."""
        symbols, globalAttributes, globalFunctions, classes = {}, {}, {}, {}
        try:
            module = ast.parse(source)
        except:
            log.warning("Python file has syntax errors: {0}!".format(filename))
            return {}
        for symbol in module.body:
            if symbol.__class__ is ast.Assign:
                result = self.parse_assign(symbol)
                globalAttributes.update(result[0])
                globalAttributes.update(result[1])
            elif symbol.__class__ is ast.FunctionDef:
                result = self.parse_function(symbol)
                globalFunctions[result['name']] = result
            elif symbol.__class__ is ast.ClassDef:
                result = self.parse_class(symbol)
                classes[result['name']] = result
        if globalAttributes:
            symbols['attributes'] = globalAttributes
        if globalFunctions:
            symbols['functions'] = globalFunctions
        if classes:
            symbols['classes'] = classes
        symbols['imports'] = self.parse_import(module)
        symbols['docstring'] = ast.get_docstring(module, clean=True)
        return symbols

    def expand_attribute(self, attribute):
        """Expand attribute to get more info about itself."""
        parent_name = []
        while attribute.__class__ is ast.Attribute:
            parent_name.append(attribute.attr)
            attribute = attribute.value
        name, attr_id = '.'.join(reversed(parent_name)), ''
        if attribute.__class__ is ast.Name:
            attr_id = attribute.id
        elif attribute.__class__ is ast.Call:
            if attribute.func.__class__ is ast.Attribute:
                attr_id = "{0}.{1}()".format(
                    self.expand_attribute(attribute.func.value),
                    attribute.func.attr)
            else:
                attr_id = "{0}()".format(attribute.func.id)
        name = attr_id if name == "" else "{0}.{1}".format(attr_id, name)
        return name

    def parse_assign(self, symbol):
        """Parse assign and get info from itself."""
        assigns, attributes = {}, {}
        for var in symbol.targets:
            if var.__class__ == ast.Attribute:
                attributes[var.attr] = var.lineno
            elif var.__class__ == ast.Name:
                assigns[var.id] = var.lineno
        return (assigns, attributes)

    def parse_class(self, symbol):
        """Parse class and get info from itself."""
        docstring, attr, func, decora, name = "", {}, {}, [], symbol.name + '('
        name += ', '.join(self.expand_attribute(_) for _ in symbol.bases) + ')'
        for sym in symbol.body:
            if sym.__class__ is ast.Assign:
                result = self.parse_assign(sym)
                attr.update(result[0])
                attr.update(result[1])
            elif sym.__class__ is ast.FunctionDef:
                result = self.parse_function(sym)
                attr.update(result['attrs'])
                func[result['name']] = result
        docstring, lineno = ast.get_docstring(symbol, clean=1), symbol.lineno
        for decorator in symbol.decorator_list:
            decora.append("@" + self.expand_attribute(decorator))
        return {'name': name, 'attributes': attr, 'functions': func,
                'lineno': lineno, 'docstring': docstring, 'decorators': decora}

    def parse_function(self, symbol):
        """Parse function and get info from itself."""
        docstring, attrs, decorators, defaults, arguments = "", {}, [], [], []
        tipes = {_ast.Tuple: "tuple", _ast.List: "list", _ast.Str: "str",
                 _ast.Dict: "dict", _ast.Num: "int", _ast.Call: "function()"}
        func_name = symbol.name + '('
        for value in symbol.args.defaults:
            defaults.append(value)
        for arg in reversed(symbol.args.args):
            if arg.__class__ is not _ast.Name or arg.id == 'self':
                continue
            argument = arg.id
            if defaults:
                value = defaults.pop()
                arg_default = tipes.get(value.__class__, None)
                if arg_default is None:
                    if value.__class__ is _ast.Attribute:
                        arg_default = self.expand_attribute(value)
                    elif value.__class__ is _ast.Name:
                        arg_default = value.id
                    else:
                        arg_default = 'object'
                argument += '=' + arg_default
            arguments.append(argument)
        func_name += ', '.join(reversed(arguments))
        if symbol.args.vararg is not None:
            if not func_name.endswith('('):
                func_name += ', '
            func_name += '*' + symbol.args.vararg
        if symbol.args.kwarg is not None:
            if not func_name.endswith('('):
                func_name += ', '
            func_name += '**' + symbol.args.kwarg.arg
        func_name += ')'
        for sym in symbol.body:
            if sym.__class__ is ast.Assign:
                attrs.update(self.parse_assign(sym)[1])
        docstring, lineno = ast.get_docstring(symbol, clean=1), symbol.lineno
        for decorator in symbol.decorator_list:
            decorators.append("@" + self.expand_attribute(decorator))
        return {'name': func_name, 'lineno': lineno, 'attrs': attrs,
                'docstring': docstring, 'decorators': decorators}

    def parse_import(self, module):
        """Parse import, get info from itself."""
        imports, from_imports = {}, {}
        for simbolos in module.body:
            if type(simbolos) is ast.Import:
                for item in simbolos.names:
                    imports[item.name] = {"asname": item.asname,
                                          "lineno": simbolos.lineno}
            if type(simbolos) is ast.ImportFrom:
                for item in simbolos.names:
                    from_imports[item.name] = {
                        "module": simbolos.module, "lineno": simbolos.lineno,
                        "asname": item.asname}
        return {"imports": imports, "from_imports": from_imports}
