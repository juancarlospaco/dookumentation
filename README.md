# dookumentation


*W.I.P.  More Documentation soon...*


![Mobile](https://lh3.googleusercontent.com/-NY1dYAmLezk/Vhne9A8gQkI/AAAAAAAALFA/FAc5VNF2y5M/s0/15%2B-%2B1 "HTML5 Material Design Mobile Responsive")


### Features

- **Standalone**, uses ONLY Standard Libraries, built-in on Python 3.
- **Async**, does not Block or Slows down even with large amount of files and folders to process.
- **Watch**, Watch for changes on files re-process only the changes, you code and forget about Documentations.
- **Zero Config**, No configurations, No settings, No `*.yml` files required to work, ever.
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
- **ZIP**, Compressed ZIP with HTML5 Documentation inside, optional via `--zip` parameter `*.zip`
- **SVG** for the Web, HTML5 `<svg>` standalone document, Pretty-Printed, [via single-file provided plugin](https://github.com/juancarlospaco/dookumentation/blob/master/plugins/template.svg "SVG Template-Plugin") `*.svg`
- **XML**, generic XML, Pretty-Printed, [via single-file provided plugin](https://github.com/juancarlospaco/dookumentation/blob/master/plugins/template.xml "XML Template-Plugin") `*.xml`
- **Infinite?**, via [third party Do-It-Yourself single-file plugin](https://gist.github.com/juancarlospaco/97a6a09d64b190a630ad#gistcomment-1576482 "Write 1 file, export 1 new format !")
- [*Your Output Format here...*](https://github.com/juancarlospaco/dookumentation/pulls "Send new Output Formats by sending your Plugins")


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
    ├── json/       "JSON Documentation files are saved here (eg. *.json)."
    ├── plugins/    "Template-Plugin files are read from here (eg. SVG, XML, etc)."
    └── html.zip    "HTML Documentation on Compressed ZIP file (if --zip is used)."
```


### Why?:

- TBD.


### Requisites:

- [Python 3.x](https://www.python.org "Python Homepage") *(or PyPy 3.x, or Python Nightly)*


### Coding Style Guide:

- Lint, [PEP-8](https://www.python.org/dev/peps/pep-0008), [PEP-257](https://www.python.org/dev/peps/pep-0257), [PyLama](https://github.com/klen/pylama#-pylama), [iSort](https://github.com/timothycrosley/isort) must Pass Ok. `pip install pep8 pep257 pylama isort`
- If theres any kind of Tests, they must Pass Ok, if theres no Tests, its ok, if Tests provided, is even better.
- [PEP-0257 Official Python Docstring Style Guide](https://www.python.org/dev/peps/pep-0257/)


### Licence:

- GNU GPL Latest Version, GNU LGPL Latest Version, GNU AGPL Latest Version, MIT Latest Version, any Licence [YOU Request via Bug Report](https://github.com/juancarlospaco/dookumentation/issues/new).
