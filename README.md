# dookumentation
![The Dark Side of Documentation](https://raw.githubusercontent.com/juancarlospaco/dookumentation/master/dookumentation.jpg "The Dark Side of Documentation !")

[![GPL License](http://img.shields.io/badge/license-GPL-blue.svg?style=plastic)](http://opensource.org/licenses/GPL-3.0) [![LGPL License](http://img.shields.io/badge/license-LGPL-blue.svg?style=plastic)](http://opensource.org/licenses/LGPL-3.0) [![Python Version](https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic)](http://python.org) 


### Screenshots

![Desktop](https://lh5.googleusercontent.com/-tORGiVrBQJ8/ViRI8yOURvI/AAAAAAAALKU/y7fklCK0FQg/s0/temp.jpg "HTML5 Material Design Desktop Responsive")

![Desktop](https://lh6.googleusercontent.com/-9FmGoCbMCNQ/Viqy8Y0a3tI/AAAAAAAALL8/GWn_Ax9msdM/s0/docs.jpg "HTML5 Material Design Desktop Responsive")

![Mobile](https://lh3.googleusercontent.com/-NY1dYAmLezk/Vhne9A8gQkI/AAAAAAAALFA/FAc5VNF2y5M/s0/15%2B-%2B1 "HTML5 Material Design Mobile Responsive")

![Source Code View with Python Syntax Highlighting](https://lh3.googleusercontent.com/-TG5gJ_-J_SM/VjHj_7nYh3I/AAAAAAAALOk/uO70RzZ_psQ/s0/dookumentation_code_view.jpg "Source Code View with Python Syntax Highlighting")

![eBook Documentation on Okular Viewer](https://lh6.googleusercontent.com/-aI9SIUzt23E/ViHcqejiISI/AAAAAAAALIg/kefIUyBNllY/s0/temp.jpg "eBook Documentation on Okular Viewer")

![Dookumentation Command Line Interface showing the Help](https://lh5.googleusercontent.com/-hNeMwFV_QBs/ViRgw6-HmnI/AAAAAAAALLI/ZxdWgFdet8Q/s0/temp.jpg "Dookumentation Command Line Interface showing the Help")


### Features

- **KISS**, Takes a full path to anything, a file or a folder, parse and generate multiple documentation formats.
- **Standalone**, uses ONLY Standard Libraries, built-in on Python 3.
- **Async**, does not Block or Slows down even with large amount of files and folders to process.
- **Watch**, Watch for changes on files re-process only the changes, you code and forget about Documentations.
- **Zero Config**, No configurations, No settings, No `*.yml` or `makefile` files required to work, ever.
- **Single-File**, everything is just 1 file, with PEP-8, Lint and other Python Best Practices, very readable.
- **Python3 ready**, it will only work with Python >= 3, instead of soon to be deprecated *(year 2020)* python2.
- **Unicode ready**, it should handle correctly any kind of character that `UTF-8` can support without escaping.
- **Plugins**, write your own plugins with native unrestricted Python 3, plugins are single file plain text.
- **Templates Custom**, Custom Templates ARE plugins, write one get two at the same price.
- **Export to Anything**, Templates are Plugins and are for Exporting to any kind of format you need.
- **Serve + Live-Reload**, HTTP Web Server from local computer to the network, with Live-Reload.
- **Minimalism**, do 1 thing do it awesome, is tiny and simple, K.I.S.S., its < 1.000 lines.
- **Scripting**, Execute custom Scripts *(eg. Bash *.sh)* After and Before the processing of files and folders.
- **Recursive**, it can work recursively processing whole project folders at once.
- **MetaData + Statistics**, Parse, Collect and Display nice MetaData and Statistics of your work.
- **Link-ability**, Automagically determines a word is referring to Python Library and Link to its Documentation.
- **Download/Export**, Get a JSON file or MarkDown file directly from the generated HTML documentation.
- **ProcessName**, Sets its own Process name and show up on Process lists, like `htop` and System Monitors.
- **Updates**, Can optionally check for updates for itself, from the Internet.
- **Smooth CPUs**, Sets Smooth CPU usage, good for portable devices on battery.
- **Colored Logging**, Colors on the logs, log file for troubleshooting, SysLog support.
- **Single Instance**, via Sockets.
- [*Your Feature or idea here...*](https://github.com/juancarlospaco/dookumentation/pulls "Send new Features")


### Input Formats

- `*.py` Python source code file, single file or whole folders recursively.
- `*.pyw` Python source code file for MS Windows, single file or whole folders recursively.
- ~~*.PYZ Python source code file ZIP Compressed, single file or whole folders recursively.~~ Planned for future, not supported yet.
- [*Your Input Format here...*](https://github.com/juancarlospaco/dookumentation/pulls "Send new Input Formats")


### Output Formats

- **HTML5**, [Material Design](http://www.getmdl.io "Material Design"), [Minified](https://github.com/juancarlospaco/css-html-js-minify#css-html-js-minify "Im Author of an HTML, CSS, JS minifier"), Download/Export **JSON** and **MarkDown** from the HTML Docs `*.html`
- **MarkDown**, [GitHub Compatible](https://help.github.com/articles/github-flavored-markdown "GitHub Flavored Markdown"), Pretty-Printed `*.md`
- **RST**, [ReSTructuredText](http://docutils.sourceforge.net/rst.html "ReSTructuredText Home Page"), Nikola Compatible, Pretty-Printed `*.rst`
- **JSON**, [Pretty-Printed](https://gist.github.com/juancarlospaco/358bcefc7df07bdc6b80#gistcomment-1573844 "Gist used to Pretty-Print the JSON"), JavaScript Compatible `*.json`
- **ODT**, [ODF ODT Document](https://en.wikipedia.org/wiki/OpenDocument "Open Standard Documentation ODF"), LibreOffice Compatible `*.odt`
- **eBook**, Compressed eBook with HTML5 Documentation, ePub3 compliant, optional via `--ebook` parameter `*.epub`
- **ZIP**, Compressed ZIP with HTML5 Documentation inside, optional via `--zip` parameter `*.zip`
- **SVG** for the Web, HTML5 `<svg>` standalone document, Pretty-Printed, [via single-file provided plugin](https://github.com/juancarlospaco/dookumentation/blob/master/plugins/template.svg "SVG Template-Plugin") `*.svg`
- **XML**, generic XML, Pretty-Printed, [via single-file provided plugin](https://github.com/juancarlospaco/dookumentation/blob/master/plugins/template.xml "XML Template-Plugin") `*.xml`
- **TXT**, Unformatted Plain Text, Pretty-Printed, easy to parse from scripts, [via single-file provided plugin](https://github.com/juancarlospaco/dookumentation/blob/master/plugins/template.txt "TXT Template-Plugin") `*.txt`
- **Infinite?**, via [third party Do-It-Yourself single-file plugin](https://gist.github.com/juancarlospaco/97a6a09d64b190a630ad#gistcomment-1576482 "Write 1 file, export 1 new format !")
- [*Your Output Format here...*](https://github.com/juancarlospaco/dookumentation/pulls "Send new Output Formats by sending your Plugins")


### Usage:

```bash
dookumentation.py file.py

dookumentation.py /path/to/folder/
```


### Plugins Usage:

- Download and save the plugins to `/doc/plugins/`, thats all.

**Example:** 
If your plugin is named `template.xml` then save it to `./doc/plugins/` being the actual relative path as `./doc/plugins/template.xml`, on the next run, your plugin will be used.


### Folders Hierarchy 

- This folder structure will be created automatically by Dookumentation if it does not exist.
- Relevant directories and files with Description:

```
/                   "This is the relative path to the project being Documented (eg. *.py)."
│
└── doc/
    ├── html/       "HTML Documentation files are saved here (eg. *.html)."
    ├── md/         "MarkDown Documentation files are saved here (eg. *.md)."
    ├── rst/        "ReSTructuredText Documentation files are saved here (eg. *.rst)."
    ├── odt/        "ODT ODF Documentation files are saved here (eg. *.fodt)."
    ├── json/       "JSON Documentation files are saved here (eg. *.json)."
    ├── txt/        "Unformatted Plain Text Documentation files are saved here (eg. *.txt)."
    ├── plugins/    "Template-Plugin files are read from here (eg. SVG, XML, etc)."
    ├── html.epub   "Compressed eBook Documentation from HTML5 (if --ebook is used)."
    └── html.zip    "HTML Documentation on Compressed ZIP file (if --zip is used)."
```


### Install
**PIP:** *(Recommended!)*
- TBD, comming soon...

**WGET:**
```
sudo wget -O /usr/bin/dookumentation.py https://raw.githubusercontent.com/juancarlospaco/dookumentation/master/dookumentation.py
sudo chmod +x /usr/bin/dookumentation.py
dookumentation.py
```

**MANUALLY:**

- Save [this file](https://raw.githubusercontent.com/juancarlospaco/dookumentation/master/dookumentation.py) and run it with Python3.


### Why?:

- **Pycco/Docco:** Abandonware since ~2012, Broken on Python3, Broken Unicode, very Limited and Uncomplete port of Docco, Docco may be Ok for CoffeeScript, but Pycco is too unfinished, is for single-files, no Watch, no LiveReload.
- **PyDoc/ePyDoc:** Ugly as hell, old html Markup, hard to style its CSS, html only output, is for single-files *(?)*, no Watch, no LiveReload.
- **MkDocs:** Dont generate Docs from Source, just build HTML from MD, lots of Dependencies, config files required, manual boilerplate required, html only output, no Watch, no LiveReload.
- **Sphinx:** Makefiles [*Ain't Nobody Got Time For That*](https://www.youtube.com/watch?v=8cT_Ulmcrys), Lots of Manual Configuration required, old html Markup, Ugly by default, Dont generate Docs from Source by default, lots of Dependencies, manual boilerplate required, you still need to mess around with PanDoc and Plugins for other outputs formats than HTML, no Watch, no LiveReload.


### Requisites:

- [Python 3.x](https://www.python.org "Python Homepage") *(or PyPy 3.x, or Python Nightly)*

**Optionals:**

- [PyLama](https://github.com/klen/pylama#-pylama)


### Coding Style Guide:

- Lint, [PEP-8](https://www.python.org/dev/peps/pep-0008), [PEP-257](https://www.python.org/dev/peps/pep-0257), [PyLama](https://github.com/klen/pylama#-pylama), [iSort](https://github.com/timothycrosley/isort) must Pass Ok. `pip install pep8 pep257 pylama isort`
- If theres any kind of Tests, they must Pass Ok, if theres no Tests, its ok, if Tests provided, is even better.
- [PEP-0257 Official Python Docstring Style Guide](https://www.python.org/dev/peps/pep-0257/)


### Contributors:

- **We need Designers, Web-UI, Front-End Dev for help making Templates look Awesome !!!.**
- **Please Star this Repo on Github !**, it helps to show up faster on searchs.
- **Ad-Hocracy Meritocracy**: 3 Pull Requests Merged on Master you become Repo Admin. *Join us!*
- [Help](https://help.github.com/articles/using-pull-requests) and more [Help](https://help.github.com/articles/fork-a-repo) and Interactive Quick [Git Tutorial](https://try.github.io).


### Ethics and Humanism Policy:
- May this FLOSS be always Pristine and Clean, No AdWare, No Spamm, No BundleWare, No Infomercial, No MalWare.
- This project is [LGBTQQIAAP friendly](http://www.urbandictionary.com/define.php?term=LGBTQQIAAP "Whats LGBTQQIAAP").


### Licence:

- GNU GPL Latest Version, GNU LGPL Latest Version, GNU AGPL Latest Version, MIT Latest Version, any Licence [YOU Request via Bug Report](https://github.com/juancarlospaco/dookumentation/issues/new).


### Donate, Charityware :

- [Charityware](https://en.wikipedia.org/wiki/Donationware) is a licensing model that supplies fully operational unrestricted software to the user and requests an optional donation be paid to a third-party beneficiary non-profit. The amount of donation may be left to the discretion of the user.
