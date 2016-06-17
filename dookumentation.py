#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Dookumentation."""


import atexit
import os
import pkgutil
import re
import sys

from argparse import ArgumentParser
from datetime import datetime
from hashlib import sha1
from json import loads
from multiprocessing import Pool, cpu_count
from platform import platform, python_version
from shutil import make_archive
from string import punctuation
from subprocess import getoutput
from time import sleep

from core.parser import PyParse
from templates.variables import HTML, RST, MD, ODT

from anglerfish import ( beep, check_encoding,  # fades.pypi  #FIXME
                        check_folder, get_free_port, html2ebook, json_pretty,
                        make_logger, make_post_exec_msg, set_process_name,
                        set_single_instance, set_terminal_title, walk2list)


try:
    from pylama.main import check_path, parse_options
except ImportError:
    check_path = parse_options = None
    print("WARNING: PyLama Not Found !!!, Run: \nsudo pip3 install pylama")

try:
    import pygments
except ImportError:
    pygments = None
    print("WARNING: Pygments Not Found !!!, Run: \nsudo pip3 install pygments")

try:  # https://github.com/lepture/python-livereload
    import livereload  # sudo pip3 install livereload
except ImportError:
    from webbrowser import open_new_tab
    import http.server as server
    from http.server import CGIHTTPRequestHandler
    livereload = None  # Still works Ok without LiveReload


__version__ = '2.0.0'
__license__ = 'GPLv3+ LGPLv3+ AGPLv3+ MIT'
__author__ = 'Juan Carlos'
__email__ = 'juancarlospaco@gmail.com'
__url__ = 'https://github.com/juancarlospaco/dookumentation'
__source__ = ('https://raw.githubusercontent.com/juancarlospaco/'
              'dookumentation/master/dookumentation.py')


start_time, IGNORE = datetime.now(), (".scss", ".coffee", ".less", ".sass")
vuiltins = tuple(set([_.lower() for _ in sorted(
    sys.builtin_module_names + tuple(dir(__builtins__)) +
    tuple(__builtins__.__dict__.keys()) + tuple(globals().keys()))]))
third_party_mods = tuple(set([_[1].lower() for _ in pkgutil.iter_modules()]))


##############################################################################
# Data handlers and miscellaneous


"""Templar is a tiny Template Engine that Render and Runs native Python."""
# Renamed from Templar to TemplatePython for easy of use.
# Was about to use TemplateString, but will confuse with string.Template

from urllib import parse
class TemplatePython(str):

    """Templar is a tiny Template Engine that Render and Runs native Python."""

    def __init__(self, template):
        """Init the Template class."""
        self.tokens = self.compile(template.strip())

    @classmethod
    def from_file(cls, fl):
        """Load template from file.A str/file-like object supporting read()."""
        return cls(str(open(fl).read() if isinstance(fl, str) else fl.read()))

    def compile(self, t):
        """Parse and Compile all Tokens found on the template string t."""
        tokens = []
        for i, p in enumerate(re.compile("\{\%(.*?)\%\}", re.DOTALL).split(t)):
            if not p or not p.strip():
                continue
            elif i % 2 == 0:
                tokens.append((False, p.replace("{\\%", "{%")))
            else:
                lines = tuple(p.replace("%\\}", "%}").replace(
                    "{{", "spit(").replace("}}", "); ") .splitlines())
                mar = min(len(_) - len(_.lstrip()) for _ in lines if _.strip())
                al = "\n".join(line_of_code[mar:] for line_of_code in lines)
                tokens.append((True, compile(al, "<t {}>".format(al), "exec")))
        return tokens

    def render(__self, __namespace={}, mini=False, **kw):
        """Render template from __namespace dict + **kw added to namespace."""
        html = []
        __namespace.update(kw, **globals())
        def spit(*args, **kwargs):
            for _ in args:
                html.append(str(_))
            if kwargs:
                for _ in tuple(kwargs.items()):
                    html.append(str(_))
        __namespace["spit"] = spit
        for is_code, value in __self.tokens:
            eval(value, __namespace) if is_code else html.append(value)
        return re.sub('>\s+<', '> <', "".join(html)) if mini else "".join(html)

    __call__ = render  # shorthand


def set_folder_structure(folder4docs):
    """Recreate the required folder structure for documentation files."""
    folder4docs = os.path.join(os.path.abspath(folder4docs), "doc")
    log.debug("Recreating required folder structure: {0}".format(folder4docs))
    if not os.path.isdir(folder4docs):  # What if folder is not a folder.
        log.warning("Creating Required Folder: {0}/".format(folder4docs))
        os.makedirs(folder4docs, exist_ok=True)
    basic_folders = ("json", "html", "md", "rst", "odt", "plugins",
                     os.path.join("html", "css"), os.path.join("html", "js"))
    for subfolder in [os.path.join(folder4docs, _) for _ in basic_folders]:
        if not os.path.isdir(subfolder):
            log.warning("Creating Required Sub-Folder: {0}/".format(subfolder))
            os.makedirs(subfolder, exist_ok=True)


def process_multiple_files(file_path):
    """Process multiple Python files with multiprocessing."""
    log.debug("Process {0} is Processing {1}.".format(os.getpid(), file_path))
    if args.watch:
        previous = int(os.stat(file_path).st_mtime)
        log.info("Process {0} is Watching {1}.".format(os.getpid(), file_path))
        while True:
            actual = int(os.stat(file_path).st_mtime)
            if previous == actual:
                sleep(60)
            else:
                previous = actual
                log.debug("Modification detected on '{0}'.".format(file_path))
                process_single_python_file(file_path)
    else:
        process_single_python_file(file_path)


def python_file_to_json_meta(python_file_path):
    """Take python source code string and extract meta-data as json file."""
    log.debug("INPUT: Reading Python file {0}.".format(python_file_path))
    with open(python_file_path, encoding="utf-8-sig") as python_file:
        python_code, json_meta = python_file.read(), {}
    json_meta["generator"] = __doc__.splitlines()[0] + " " + __version__
    json_meta["relpath"] = os.path.relpath(python_file_path)  # Paths
    json_meta["basename"] = os.path.basename(python_file_path)
    json_meta["dirname"], all_fades = os.path.dirname(python_file_path), []
    json_meta["fullpath"], json_meta["is_index"] = python_file_path, False
    json_meta["lines_total"] = len(python_code.splitlines())  # Statistics
    json_meta["characters"] = len(python_code.replace("\n", ""))
    json_meta["kilobytes"] = int(os.path.getsize(python_file_path) / 1024)
    json_meta["lines_code"] = len([_ for _ in python_code.splitlines() if len(
        _.strip()) and not _.strip().startswith("#")])
    json_meta["words"] = len([_ for _ in re.sub(
        "[^a-zA-Z0-9 ]", "", python_code).split(" ") if _ != ""])
    json_meta["punctuations"] = len(
        [_ for _ in python_code if _ in punctuation])
    json_meta["permissions"] = int(oct(os.stat(python_file_path).st_mode)[-3:])
    json_meta["writable"] = os.access(python_file_path, os.W_OK)
    json_meta["executable"] = os.access(python_file_path, os.X_OK)
    json_meta["readable"] = os.access(python_file_path, os.R_OK)
    json_meta["symlink"] = os.path.islink(python_file_path)
    json_meta["sha1"] = sha1(python_code.encode("utf-8")).hexdigest()
    json_meta["import_procedural"] = "__import__(" in python_code
    json_meta["has_set_trace"] = ".set_trace()" in python_code
    json_meta["has_print"] = "print(" in python_code
    json_meta["has_tab"] = "\t" in python_code
    json_meta["has_shebang"] = re.findall('^#!/.*python', python_code)
    json_meta["accessed"] = datetime.utcfromtimestamp(os.path.getatime(
        python_file_path)).isoformat(" ").split(".")[0]
    json_meta["modified"] = datetime.utcfromtimestamp(os.path.getmtime(
        python_file_path)).isoformat(" ").split(".")[0]
    json_meta["pylama"] = [  # Bugs
        pylama_error.__dict__["_info"]  # dict with PyLama Errors from linters
        for pylama_error in check_path(parse_options((python_file_path, )))
        ] if check_path and parse_options else []  # if no PyLama empty list
    if len(json_meta["pylama"]) and json_meta["lines_total"]:
        json_meta["lines_per_bug"] = int(
            json_meta["lines_total"] / len(json_meta["pylama"]))
    regex_for_todo, all_todo = r"(  # TODO|  # FIXME|  # OPTIMIZE|  # BUG)", []
    for index, line in enumerate(python_code.splitlines()):
        if re.findall(regex_for_todo, line):
            all_todo.append({  # Using same keywords as PyLama array.
                "lnum": index + 1, "text": line.strip(),
                "type": re.findall(regex_for_todo, line)[0].replace(
                    "#", "").strip().lower()})
    if len(all_todo):
        json_meta["todo"] = all_todo  # this is all todo, fixme,etc on the code
    for index, line in enumerate(python_code.splitlines()):
        if re.findall(r"(  # fades)", line):
            all_fades.append({"lnum": index + 1, "text": line.strip(),
                              "type": line.split("#")[1].strip()})
    if len(all_fades):  # Fades: https://github.com/PyAr/fades
        json_meta["fades"] = all_fades  # this is all todo,fixme,etc on code
    json_meta["links"] = re.findall(r"(?P<url>https?://[^\s]+)", python_code)
    for key, value in PyParse().parse_file(python_file_path).items():
        json_meta[key] = value  # "some_code_entity": "value_of_that_entity",
    return json_meta  # return the Big Ol' JSON


def json_to_json(json_meta, json_new):
    """Take multiple json str and append meta-data to existing single json."""
    json_meta["permissions"] = json_meta["sha1"] = " ? ? ? "
    json_meta["modified"] = json_meta["accessed"] = " ? ? ? "
    json_meta["relpath"] = json_meta["basename"] = " ? ? ? "
    json_meta["fullpath"] = json_meta["dirname"] = " ? ? ? "
    json_meta["lines_total"] += int(json_new["lines_total"])
    json_meta["characters"] += int(json_new["characters"])
    json_meta["kilobytes"] += int(json_new["kilobytes"])
    json_meta["lines_code"] += int(json_new["lines_code"])
    json_meta["words"] += int(json_new["words"])
    json_meta["punctuations"] += int(json_new["punctuations"])
    json_meta["has_shebang"] += list(json_new["has_shebang"])
    json_meta["has_shebang"] = sorted(set(json_meta["has_shebang"]))
    json_meta["writable"] += int(json_new["writable"])
    json_meta["executable"] += int(json_new["executable"])
    json_meta["readable"] += int(json_new["readable"])
    json_meta["symlink"] += int(json_new["symlink"])
    json_meta["import_procedural"] += int(json_new["import_procedural"])
    json_meta["has_set_trace"] += int(json_new["has_set_trace"])
    json_meta["has_print"] += int(json_new["has_print"])
    json_meta["has_tab"] += int(json_new["has_tab"])
    for key, value in json_new.items():  # "code_entity": "value_of_entity",
        if json_new["relpath"] not in json_meta["files"].keys():
            json_meta["files"][json_new["relpath"]] = {}
        json_meta["files"][json_new["relpath"]].update({key: value})
    return json_meta  # return the Big Ol' JSON


def json_meta_to_template(json_meta, template, mini=False):
    """Take json_meta string, convert it to Template file, optional minify."""
    html = TemplatePython(template)  # give template string,render.
    return html(data=json_meta, mini=mini)  # mini is Minification.


def json_meta_to_plugins(plugin_folder, python_file_path, json_meta):
    """Load and Run Plugins from Plugins folder."""
    plgns = [os.path.join(plugin_folder, _) for _ in os.listdir(plugin_folder)
             if "template" == os.path.splitext(_)[0] and not _.startswith(".")]
    for template_to_render in tuple(sorted(plgns)):
        subdir = os.path.splitext(template_to_render)[-1].replace(".", "")
        plugin_dr = os.path.join(os.path.dirname(args.fullpath), "doc", subdir)
        if not os.path.isdir(plugin_dr):  # Create Sub-Folder for nre Plugin
            log.warning("Creating Required Sub-Folder: {0}/".format(plugin_dr))
            os.makedirs(plugin_dr, exist_ok=True)
        log.debug("INPUT: Reading Template {0}.".format(template_to_render))
        with open(template_to_render, "r", encoding="utf-8") as template_file:
            template_plugin = template_file.read().strip()
        custom = TemplatePython(template_plugin)  # give it template
        custom_rendered = custom(data=json_meta, mini=False)
        new_file = os.path.join(plugin_dr, os.path.basename(python_file_path) +
                                os.path.splitext(template_to_render)[-1])
        log.debug("OUTPUT: Writing Plugin Documentation {0}.".format(new_file))
        with open(new_file, "w", encoding="utf-8") as new_file_from_plugin:
            new_file_from_plugin.write(custom_rendered)
    return plgns


def process_single_python_file(python_filepath: str):
    """Process a single Python file."""
    log.info("Processing Python file: {0}".format(python_filepath))
    global args
    if os.path.isfile(python_filepath) and os.access(python_filepath, os.R_OK):
        json_meta = python_file_to_json_meta(python_filepath)
    new_json_file = os.path.join(os.path.dirname(args.fullpath), "doc", "json",
                                 os.path.basename(python_filepath) + ".json")
    log.debug("OUTPUT: Writing MetaData JSON file {0}.".format(new_json_file))
    with open(new_json_file, "w", encoding="utf-8") as json_file:
            json_file.write(json_pretty(json_meta))
    html = json_meta_to_template(json_meta, HTML, bool(not pygments))
    new_html_file = os.path.join(os.path.dirname(args.fullpath), "doc", "html",
                                 os.path.basename(python_filepath) + ".html")
    log.debug("OUTPUT: Writing HTML5 Documentation {0}.".format(new_html_file))
    with open(new_html_file, "w", encoding="utf-8") as html_file:
            html_file.write(html)
    md = rst = json_meta_to_template(json_meta, MD, False)
    new_md_file = os.path.join(os.path.dirname(args.fullpath), "doc", "md",
                               os.path.basename(python_filepath) + ".md")
    log.debug("OUTPUT: Writing MD Documentation {0}.".format(new_md_file))
    with open(new_md_file, "w", encoding="utf-8") as md_file:
            md_file.write(md)
    new_rst_file = os.path.join(os.path.dirname(args.fullpath), "doc", "rst",
                                os.path.basename(python_filepath) + ".rst")
    log.debug("OUTPUT: Writing RST Documentation {0}.".format(new_rst_file))
    with open(new_rst_file, "w", encoding="utf-8") as md_file:
            md_file.write(rst)
    fodt = json_meta_to_template(json_meta, ODT, False)
    new_fodt_file = os.path.join(os.path.dirname(args.fullpath), "doc", "odt",
                                 os.path.basename(python_filepath) + ".fodt")
    log.debug("OUTPUT: Writing ODT Documentation {0}.".format(new_fodt_file))
    with open(new_fodt_file, "w", encoding="utf-8") as fodt_file:
            fodt_file.write(fodt)
    plugin_dir = os.path.join(os.path.dirname(args.fullpath), "doc", "plugins")
    log.debug("Checking for Plugins and Running from {0}.".format(plugin_dir))
    json_meta_to_plugins(plugin_dir, python_filepath, json_meta)


def serve_http(where=os.getcwd()):
    """Serve HTTP files and HTML on the where folder,with LiveReload if any."""
    prt = get_free_port()
    if livereload:  # with LiveReload
        livereload.Server().serve(port=prt, host="0.0.0.0",
                                  open_url_delay=1, root=where)
    else:  # without LiveReload
        log.info("Run:pip install livereload\nServer running on localhost...")
        httpd = server.HTTPServer(('', prt), CGIHTTPRequestHandler)
        open_new_tab("http://localhost:{0}/".format(prt))
        httpd.serve_forever()


def make_arguments_parser():
    """Build and return a command line agument parser,parse CLI arguments."""
    parser = ArgumentParser(description=__doc__, epilog="""    Dookumentation:
    Takes file or folder full path string and Documents all Python code found.
    Watch works for whole folders, with minimum of ~60 Secs between runs.""")
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('fullpath', metavar='fullpath', type=str,
                        help='Full path to local file or folder.')
    parser.add_argument('--quiet', action='store_true', help="Quiet, Silent.")
    parser.add_argument('--after', type=str,
                        help="Command to execute after run (Experimental).")
    parser.add_argument('--before', type=str,
                        help="Command to execute before run (Experimental).")
    parser.add_argument('--watch', action='store_true', help="Watch changes.")
    parser.add_argument('--zip', action='store_true', help="HTML as ZIP file")
    parser.add_argument('--ebook', action='store_true', help="HTML as eBook")
    parser.add_argument('--serve', action='store_true', help="HTTP Serve HTML")
    parser.add_argument('--beep', action='store_true',
                        help="Beep sound will be played when it ends at exit.")
    global args
    args = parser.parse_args()


def main():
    """Main Loop."""
    make_arguments_parser()
    global log
    log = make_logger("dookumentation")
    check_encoding()  # AutoMagically Check Encodings/root
    set_process_name("dookumentation")  # set Name
    set_single_instance("dookumentation")  # Auto set Single Instance
    set_terminal_title("dookumentation")
    log.disable(log.CRITICAL) if args.quiet else log.debug("Max Logging ON")
    atexit.register(beep) if args.beep else log.debug("Beep sound at exit OFF")
    log.info(" ".join((__doc__, __version__, __url__, "by " + __author__)))
    log.debug((platform(), python_version(), str(os.environ), str(args)))
    check_folder(os.path.dirname(args.fullpath))
    set_folder_structure(os.path.dirname(args.fullpath))
    if args.before and getoutput:
        log.info(getoutput(str(args.before)))
    files_exts, list_of_files = (".py", ".pyw"), str(args.fullpath)
    if os.path.isfile(args.fullpath) and args.fullpath.endswith(files_exts):
        log.info("Target is single a *.PY or *.PYW Python Source Code File.")
        process_single_python_file(args.fullpath)
    elif os.path.isdir(args.fullpath):
        log.info("Target is Folder with *.PY & *.PYW Python Source Code Files")
        log.warning("Processing a whole Folder may take some time...")
        list_of_files = walk2list(args.fullpath, files_exts, tuple())
        pool = Pool(cpu_count())  # Multiprocessing Async
        pool.map_async(process_multiple_files, list_of_files)
        pool.close()
        pool.join()
    else:
        sys.exit("File or folder not found, or cant be read, or I/O Error !.")
    html_folder = os.path.join(os.path.dirname(args.fullpath), "doc", "html")
    if args.zip and make_archive and os.path.isdir(html_folder):  # HTML to ZIP
        log.debug("OUTPUT: Writing ZIP Documentation {0}.".format(html_folder))
        make_archive(html_folder, 'zip', html_folder, logger=log)
    if args.ebook and os.path.isdir(html_folder):  # HTML to eBook
        log.debug("OUTPUT: Writing EPUB Documentation {0}".format(html_folder))
        html2ebook(walk2list(html_folder, ("", ), IGNORE),
                   html_folder + ".epub", {"des": __doc__ + __url__.upper()})
    json_meta = {  # Some placeholders and initialization is needed.
        "lines_total": 0, "characters": 0, "kilobytes": 0, "lines_code": 0,
        "words": 0, "punctuations": 0, "has_shebang": [], "writable": 0,
        "executable": 0, "readable": 0, "symlink": 0, "has_tab": 0,
        "import_procedural": 0, "has_set_trace": 0, "has_print": 0,
        "is_index": True, "files": {}, "generator": __doc__ + __version__,
        "html_files": walk2list(html_folder, (".html", ), tuple())}
    json_folder = os.path.join(os.path.dirname(args.fullpath), "doc", "json")
    for jotason in walk2list(json_folder, (".json", ), tuple()):
        log.debug("INPUT: Reading JSON file {0}.".format(jotason))
        with open(jotason, "r", encoding="utf-8") as jaison_file:
            json_meta = json_to_json(json_meta, loads(jaison_file.read()))
    new_json_file = os.path.join(json_folder, "index.json")
    log.debug("OUTPUT: Writing JSON Index file {0}.".format(new_json_file))
    with open(new_json_file, "w", encoding="utf-8") as json_file:
            json_file.write(json_pretty(json_meta))
    html_index = json_meta_to_template(json_meta, HTML, bool(not pygments))
    new_html_file = os.path.join(html_folder, "index.html")
    log.debug("OUTPUT: Writing HTML5 Docs Index {0}.".format(new_html_file))
    with open(new_html_file, "w", encoding="utf-8") as html_file:
            html_file.write(html_index)
    if args.after and getoutput:
        log.info(getoutput(str(args.after)))
    if args.serve and os.path.isdir(html_folder):  # HTML to HTTP LiveReload
        serve_http(html_folder)
    log.info('\n {0} \n Files Processed: {1}.'.format('-' * 80, list_of_files))
    log.info('Number of Files Processed: ~{0}.'.format(
        len(list_of_files) if isinstance(list_of_files, tuple) else 1))
    set_terminal_title()
    make_post_exec_msg(start_time, "dookumentation")


if __name__ in '__main__':
    main()
