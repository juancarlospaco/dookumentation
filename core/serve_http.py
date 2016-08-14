#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Dookumentation."""


import os

from anglerfish import get_free_port  # fades.pypi

try:  # https://github.com/lepture/python-livereload
    import livereload  # sudo pip3 install livereload
except ImportError:
    from webbrowser import open_new_tab
    import http.server as server
    from http.server import CGIHTTPRequestHandler
    livereload = None  # Still works Ok without LiveReload


__all__ = ["serve_http"]


def serve_http(where=os.getcwd()):
    """Serve HTTP files and HTML on the where folder,with LiveReload if any."""
    prt = get_free_port()
    if livereload:  # with LiveReload
        livereload.Server().serve(port=prt, host="0.0.0.0",
                                  open_url_delay=1, root=where)
    else:  # without LiveReload
        print("Run:pip install livereload\nServer running on localhost...")
        httpd = server.HTTPServer(('', prt), CGIHTTPRequestHandler)
        open_new_tab("http://localhost:{0}/doc/html/index.html".format(prt))
        httpd.serve_forever()
