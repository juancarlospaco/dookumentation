# dookumentation

![The Dark Side of Documentation](https://raw.githubusercontent.com/juancarlospaco/dookumentation/master/dookumentation.jpg "The Dark Side of Documentation !")

[![GPL License](http://img.shields.io/badge/license-GPL-blue.svg?style=plastic)](http://opensource.org/licenses/GPL-3.0) [![LGPL License](http://img.shields.io/badge/license-LGPL-blue.svg?style=plastic)](http://opensource.org/licenses/LGPL-3.0) [![Python Version](https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic)](http://python.org) 

[![Donate BitCoins](https://www.coinbase.com/assets/buttons/donation_large-5cf4f17cc2d2ae2f45b6b021ee498297409c94dcf0ba1bbf76fd5668e80b0d02.png)](https://www.coinbase.com/checkouts/c3538d335faee0c30c81672ea0223877 "Donate Bitcoins") [![Subscribe with BitCoins](https://www.coinbase.com/assets/buttons/subscription_large-11d991f628216af05156fae88a48ce25c0cb36447a265421a43a62e572af3853.png)](https://www.coinbase.com/checkouts/c3538d335faee0c30c81672ea0223877 "Subscribe with BitCoins") [![Pay with BitCoins](https://www.coinbase.com/assets/buttons/buy_now_large-6f15fa5979d25404827a7329e8a5ec332a42cf4fd73e27a2c3ccda017034e1b0.png)](https://www.coinbase.com/checkouts/c3538d335faee0c30c81672ea0223877 "Pay with BitCoins") [![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif "Donate with or without Credit Card")](http://goo.gl/cB7PR)


https://pypi.python.org/pypi/dookumentation


### Screenshots

![Desktop](https://lh5.googleusercontent.com/-OAqQ7mi5yeg/V7CRAx0mK6I/AAAAAAAAMsQ/YLqKBy-RIrkAo-GjGRRt8jaRc-fmyKTDwCL0B/w954-h629-no/dookumentation0.jpg "HTML5 Material Design Polymer WebComponents Desktop Responsive")

![Desktop](https://lh4.googleusercontent.com/-C-2hjmYQnB8/V7CRFpfjq5I/AAAAAAAAMsw/8DMDPlvKCiM42PDTuuekbZCvUCne_KobACL0B/w801-h717-no/dookumentation2.jpg "HTML5 Material Design Polymer WebComponents Desktop Responsive")

![Desktop](https://lh4.googleusercontent.com/-7RJm0XXDu6Q/V7CRI4nhhyI/AAAAAAAAMtQ/KiwRVRVXZGAeabRpx5OU198CwZusytxjQCLcB/w924-h760-no/dookumentation3.jpg "HTML5 Material Design Polymer WebComponents Desktop Responsive")

![Mobile](https://lh3.googleusercontent.com/-NY1dYAmLezk/Vhne9A8gQkI/AAAAAAAALFA/FAc5VNF2y5M/s0/15%2B-%2B1 "HTML5 Material Design Mobile Responsive")

![Source Code View with Python Syntax Highlighting](https://lh3.googleusercontent.com/-TG5gJ_-J_SM/VjHj_7nYh3I/AAAAAAAALOk/uO70RzZ_psQ/s0/dookumentation_code_view.jpg "Source Code View with Python Syntax Highlighting")

![eBook Documentation on Okular Viewer](https://lh6.googleusercontent.com/-aI9SIUzt23E/ViHcqejiISI/AAAAAAAALIg/kefIUyBNllY/s0/temp.jpg "eBook Documentation on Okular Viewer")

![Dookumentation Command Line Interface showing the Help](https://lh5.googleusercontent.com/-hNeMwFV_QBs/ViRgw6-HmnI/AAAAAAAALLI/ZxdWgFdet8Q/s0/temp.jpg "Dookumentation Command Line Interface showing the Help")


### Features

- **KISS**, Takes a full path to anything, a file or a folder, parse and generate multiple documentation formats.
- **Async**, does not Block or Slows down even with large amount of files and folders to process.
- **Watch**, Watch for changes on files re-process only the changes, you code and forget about Documentations.
- **Zero Config**, No configurations, No settings, No `*.yml` or `makefile` files required to work, ever.
- **Python3 ready**, it will only work with Python >= 3, instead of soon to be deprecated *(year 2020)* python2.
- **Unicode ready**, it should handle correctly any kind of character that `UTF-8` can support without escaping.
- **Plugins**, write your own plugins with native unrestricted Python 3, plugins are single file plain text.
- **Templates Custom**, Custom Templates ARE plugins, write one get two at the same price.
- **Export to Anything**, Templates are Plugins and are for Exporting to any kind of format you need.
- **Serve + Live-Reload**, HTTP Web Server from local computer to the network, with Live-Reload.
- **Fades**, Built-in [Fades](https://github.com/PyAr/fades) support by default.
- **YouTube**, Built-in [Youtube](https://www.youtube.com) support, Youtube links on DocStrings get Automagically Embedded.
- **Minimalism**, do 1 thing do it awesome, is tiny and simple, K.I.S.S., its < 1.000 lines.
- **Scripting**, Execute custom Scripts *(eg. Bash *.sh)* After and Before the processing of files and folders.
- **Recursive**, it can work recursively processing whole project folders at once.
- **MetaData + Statistics**, Parse, Collect and Display nice MetaData and Statistics of your work.
- **Cross-reference Links**, Automagically determines a word is referring to Python Library and Link to its Documentation.
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
    ├── html/            "HTML Documentation files are saved here (eg. *.html)."
    │    ├── css/        "Custom CSS StyleSheets files are read from here (eg. *.css)."
    │    ├── js/         "Custom JavaScript files are read from here (eg. *.js)."
    │    ├── favicon.ico "Custom FavIcon.ico file are read from here (eg. favicon.ico)."
    │    └── index.html  "Index main page are saved here (eg. index.html)."
    ├── md/              "MarkDown Documentation files are saved here (eg. *.md)."
    ├── rst/             "ReSTructuredText Documentation files are saved here (eg. *.rst)."
    ├── odt/             "ODT ODF Documentation files are saved here (eg. *.fodt)."
    ├── xml/             "XML Documentation files are saved here (eg. *.xml)."
    ├── json/            "JSON Documentation files are saved here (eg. *.json)."
    ├── plugins/         "Template-Plugin files are read from here (eg. SVG, XML, etc)."
    ├── html.epub        "Compressed eBook Documentation from HTML5 (if --ebook is used)."
    └── html.zip         "HTML Documentation on Compressed ZIP file (if --zip is used)."
```


### Install
**PIP:** *(Recommended!)*
```
pip3 install dookumentation
```
- Use `sudo pip3 install dookumentation` for System-wide installation.


### Why?:

- **Pycco/Docco:** Abandonware since ~2012, Broken on Python3, Broken Unicode, very Limited and Uncomplete port of Docco, Docco may be Ok for CoffeeScript, but Pycco is too unfinished, is for single-files, no Watch, no LiveReload.
- **PyDoc/ePyDoc:** Ugly as hell, old html Markup, hard to style its CSS, html only output, is for single-files *(?)*, no Watch, no LiveReload.
- **MkDocs:** Dont generate Docs from Source, just build HTML from MD, lots of Dependencies, config files required, manual boilerplate required, html only output.
- **Sphinx:** Makefiles [*Ain't Nobody Got Time For That*](https://www.youtube.com/watch?v=8cT_Ulmcrys), **imports all the modules** to be documented, Lots of Manual Configuration required, old html Markup, Ugly by default, Dont generate Docs from Source by default, lots of Dependencies, manual boilerplate required, you still need to mess around with PanDoc and Plugins for other outputs formats than HTML, no Watch, no LiveReload.


### Requisites:

- [Python 3.x](https://www.python.org "Python Homepage")
- Anglerfish

**Optionals:**

- [PyLama](https://github.com/klen/pylama#-pylama)
- Pygments
- [LiveReload](https://github.com/lepture/python-livereload)


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
