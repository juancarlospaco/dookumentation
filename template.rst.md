
.. ..

 **Dookumentation - {% {{ data['basename'][:99] }} %}**

 ---

 [Table of Contents](#toc "Table of Contents")

 - [**Statistics**](#statistics "Statistics about current source code"): Statistics about current source code.
 - [**Table of Contents**](#toc "Table of Contents"): This Table of Contents.
 - [**Build Logs**](#logs "Build Logs"): Build Logs for Developers and Debug.
 - [**Source Code View**](#sourcecode "Source Code View"): Source Code Raw View.
 - [**Imports**](#imports "Imports"): Information about all the Imports.
{%
toc_items = ""
if data.get('functions'):
    toc_items += ' - [**Functions**](#functions "Functions"): Functions (not Methods).\n'
if data.get('classes'):
    toc_items += ' - [**Classes**](#classes "Classes"):  Classes and Methods.\n'
if data.get('attributes'):
    toc_items += ' - [**Attributes**](#attributes "Attributes"): Attributes (probably Global).\n'
if data.get('pylama'):
    toc_items += ' - [**Bugs**](#bugs "Imperfections on the code"):  Imperfections on the code.\n'
if data.get('todo'):
    toc_items += ' - [**ToDo**](#todo "Auto-generated To-Do Lists"): Auto-generated To-Do Lists.\n'
if data.get('fades'):
    toc_items += ' - [**Fades**](#fades "Information about Fades"): Information about Fades.\n'
if data.get('links'):
    toc_items += ' - [**Links Farm**](#links "Links Farm"): All Links found on the code together.\n'
{{ toc_items }}
%}

 ---

 [Imports](#imports "Imports")
{%
if data.get('imports'):
    {{ ' **&check; {0} Imports!.**\n\n'.format(len(data['imports']['imports']) + len(data['imports']['from_imports'])) }}
    imports_content = ""
    for _ in data['imports']['imports'].items() :
        imports_content += ' - ` import {mod} {ass}` &raquo; Line {lin}\n\n'.format(mod=_[0], ass="as {}".format(_[1]['asname']) if _[1]['asname'] else "", lin=_[1]['lineno'])
    for _ in data['imports']['from_imports'].items():
        imports_content += ' - ` from {0} import {1} {2}` &raquo; Line {3}\n\n'.format(_[1]['module'], _[0], "as {}".format(_[1]['asname']) if _[1]['asname'] else "", _[1]['lineno'])
    {{ imports_content + ' [We recommend using iSort](https://github.com/timothycrosley/isort "We recommend using iSort")' }}
%}

 ---

 [Classes](#classes "Classes")
{%
if data.get('classes'):
    {{ ' **&check; {0} Classes!.**\n\n'.format(len(data.get('classes'))) }}
    for _ in data['classes'].items():
        decoradore = '\n\n'.join(_[1]['decorators']) + '\n\n' if _[1]['decorators'] != [] else ''
        attrivutes = ''
        if len(_[1]['attributes']):
            for atri in _[1]['attributes'].items():
                attrivutes += ' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{0} &raquo; Line {1}\n\n'.format(atri[0], atri[1])
        else:
            attrivutes = ' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; &bull; &bull;\n\n'
        {{ ' {deco} class **{name}:** &raquo; Line {lin}\n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<textarea readonly title=DocString style="width:350px">{docz}</textarea>\n\n {atri}\n\n'.format(name=_[0], deco=decoradore, docz=_[1]['docstring'], lin=_[1]['lineno'], atri=attrivutes) }}
        youtube_urls = re.findall(r'((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)', _[1]['docstring'])
        if len(youtube_urls):
            for y_tuple in youtube_urls:
                for y_id in y_tuple:
                    if len(y_id) > 10:
                        {{ ' <iframe class=youtube width=500 height=300 src="https://www.youtube-nocookie.com/embed/{0}" title="Youtube link found on DocString of {1} Class at Line {2}" alt="Youtube link found on DocString of {1} Class at Line {2}" frameborder=0 allowfullscreen ></iframe><br><i>Youtube link found on DocString of {1} Class at Line {2}.</i><br><br>'.format(y_id, _[0], _[1]['lineno']) }}
        if len(_[1]['functions']):
            for _ in _[1]['functions'].items():
                decoradore = '\n\n'.join(['&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + d for d in _[1]['decorators']]) + '\n\n' if _[1]['decorators'] != [] else ''
                attrivutes = ''
                if len(_[1]['attrs']):
                    for atri in _[1]['attrs'].items():
                        attrivutes += ' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{0} &raquo; Line {1}\n\n'.format(atri[0], atri[1])
                else:
                    attrivutes = ' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; &bull; &bull;\n\n'
                {{ ' {deco} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; def **{name}:** &raquo; Line {lin}\n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<textarea readonly title=DocString style="width:300px">{docz}</textarea>\n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{atri}'.format(name=_[0], deco=decoradore, docz=_[1]['docstring'], lin=_[1]['lineno'], atri=attrivutes) }}
                youtube_urls = re.findall(r'((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)', _[1]['docstring'])
                if len(youtube_urls):
                    for y_tuple in youtube_urls:
                        for y_id in y_tuple:
                            if len(y_id) > 10:
                                {{ ' <iframe class=youtube width=500 height=300 src="https://www.youtube-nocookie.com/embed/{0}" title="Youtube link found on DocString of {1} Function at Line {2}" alt="Youtube link found on DocString of {1} Function at Line {2}" frameborder=0 allowfullscreen ></iframe><br><i>Youtube link found on DocString of {1} Function at Line {2}.</i><br><br>'.format(y_id, _[0], _[1]['lineno']) }}
%}

 ---

 [Functions](#functions "Functions")
{%
if data.get('functions'):
    {{ ' **&boxbox; {0} Functions!.**\n'.format(len(data.get('functions'))) }}
    for _ in data['functions'].items():
        decoradore = '\n\n'.join(_[1]['decorators']) + '\n\n' if _[1]['decorators'] != [] else ''
        attrivutes = ''
        if len(_[1]['attrs']):
            for atri in _[1]['attrs'].items():
                attrivutes += ' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{0} &raquo; Line {1}\n\n'.format(atri[0], atri[1])
        else:
            attrivutes = ' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; &bull; &bull;\n\n'
        {{ ' {deco}\n\n def **{name}:** &raquo; Line {lin}\n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<textarea readonly title=DocString style="width:350px">{docz}</textarea>\n\n {atri}'.format(name=_[0], deco=decoradore, docz=_[1]['docstring'], lin=_[1]['lineno'], atri=attrivutes) }}
        youtube_urls = re.findall(r'((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)', _[1]['docstring'])
        if len(youtube_urls):
            for y_tuple in youtube_urls:
                for y_id in y_tuple:
                    if len(y_id) > 10:
                        {{ ' <iframe class=youtube width=500 height=300 src="https://www.youtube-nocookie.com/embed/{0}" title="Youtube link found on DocString of {1} Function at Line {2}" alt="Youtube link found on DocString of {1} Function at Line {2}" frameborder=0 allowfullscreen ></iframe><br><i>Youtube link found on DocString of {1} Function at Line {2}.</i><br><br>'.format(y_id, _[0], _[1]['lineno']) }}
%}

 ---

 [Attributes](#attributes "Attributes")
{%
if data.get('attributes'):
    attributes_content = ""
    for _ in sorted(data['attributes'].items()):
        attributes_content += ' - `{1}` &raquo; Line {0}\n\n'.format(_[1], _[0])
    {{ ' **&Diamond; {0} Attributes!.**\n\n'.format(len(data.get('attributes'))) + attributes_content }}
%}

 ---

 [&hercon; Bugs](#bugs "Bugs")
{%
if data.get('pylama'):
    bugs_content = ""
    if data.get('lines_per_bug'):
        {{ ' **&star; You wrote 1 Bug every {0} Lines of Code!.**\n\n'.format(data['lines_per_bug']) }}
    for _ in data['pylama']:
        bugs_content += ' - Line {0} Column {1} found by {2}: &raquo; `{3}`.\n\n'.format(_['lnum'], _['col'], _['linter'].upper(), _['text'])
    {{ bugs_content + ' [We recommend using PyLama](https://github.com/klen/pylama#-pylama "We recommend using PyLama")' }}
%}

 ---

 [&hercon; Fades](#fades "Fades")
{%
if data.get('fades'):
    fades_content = ""
    for _ in data['fades']:
        fades_content += ' - `{0}` on Line {1} &raquo; *{2}*\n\n'.format(_['type'].upper(), _['lnum'], _['text'][:99])
    {{ ' **&star; You use {0} Fades comments !.**\n\n'.format(len(data['fades'])) + fades_content + ' [We recommend Fades](https://github.com/PyAr/fades "We recommend using Fades")' }}
%}

 ---

 [&check; Things To Do](#todo "To Do")
{%
if data.get('todo'):
    todo_content = ""
    for _ in data['todo']:
        todo_content += ' - {0} on Line {1} &raquo;&nbsp;&nbsp;&nbsp;`{2}`.{3}'.format(_['type'].upper(), _['lnum'], str(_['text'])[:99], os.linesep)
    {{ ' &star; You have {0} Things to do!.\n\n'.format(len(data['todo'])) + todo_content }}
%}

 ---

 [&check; Link Farm](#links "All Links found on the code will be here")
{%
if data.get("links"):
    {{ ' **&diam; {0} Links found on the code.**\n\n ```\n\n {1}\n\n ```\n\n'.format(len(data.get("links")), data.get("links")) }}
%}

 ---

 [&check; Logs](#logs "Build Logs for Debugging and Developers")
{%
logs_content = ""
logs_content += ' **&ggg; Build Logs for Debugging and Developers**\n\n ```\n\n'
with open(log.getLogger().handlers[0].baseFilename, "r", encoding="utf-8") as __logs:
    for line in __logs.readlines():
        logs_content += ' ' + line
{{ logs_content + ' ```\n\n' }}
%}

 ---

 [&ccupssm; Statistics](#statistics "Statistics")

 <svg xmlns="http://www.w3.org/2000/svg" class="chart" width="99%" height="300px" role="img">
    <g class="bar">
        <rect x="9" y="10" height="30" fill="#8BC34A" width="99%" title="{% {{ data['characters'] }} %} Characters Total"></rect>
        <text x="9" y="30"> {% {{ data['characters'] }} %} Characters Total</text>
    </g>
    <g class="bar">
        <rect x="9" y="50" height="30" fill="#8BC34A" width="{%{{ int((data['punctuations'] / data['characters']) * 100) }}%}%" title="{% {{ data['punctuations'] }} %} Punctuations"></rect>
        <text x="9" y="70"> {% {{ data['punctuations'] }} %} Punctuations</text>
    </g>
    <g class="bar">
        <rect x="9" y="90" height="30" fill="#8BC34A" width="{%{{ int((data['words'] / data['characters']) * 100) }}%}%" title="{% {{ data['words'] }} %} Words"></rect>
        <text x="9" y="110" > {% {{ data['words'] }} %} Words</text>
    </g>
    <g class="bar">
        <rect x="9" y="150" height="30" fill="#8BC34A" width="99%" title="{% {{ data['lines_total'] }} %} Lines Total"></rect>
        <text x="9" y="170"> {% {{ data['lines_total'] }} %} Lines Total</text>
    </g>
    <g class="bar">
        <rect x="9" y="190" height="30" fill="#8BC34A" width="{%{{ int((data['lines_code'] / data['lines_total']) * 100) }}%}%" title="{% {{ data['lines_code'] }} %} Lines of Code"></rect>
        <text x="9" y="210"> {% {{ data['lines_code'] }} %} Lines of Code</text>
    </g>
    <g class="bar">
        <rect x="9" y="230" height="30" fill="#8BC34A" width="{%{{ int(((data['lines_total'] - data['lines_code']) / data['lines_total']) * 100) }}%}%" title="{% {{ data['lines_total'] - data['lines_code'] }} %} Lines of Comments and Blanks"></rect>
        <text x="9" y="250"> {% {{ data['lines_total'] - data['lines_code'] }} %} Lines of Comments and Blanks</text>
    </g>
 </svg>

 - **Lines Total**:      {% {{ data['lines_total']       }} %}
 - **Lines of Code**:    {% {{ data['lines_code']        }} %}
 - **Size (KiloBytes)**: {% {{ data['kilobytes']         }} %}
 - **Characters**:       {% {{ data['characters']        }} %}
 - **Words**:            {% {{ data['words']             }} %}
 - **Punctuations**:     {% {{ data['punctuations']      }} %}
 - **Permissions**:      {% {{ data['permissions']       }} %}
 - **Bugs ?**:           {% {{ bool(len(data['pylama'])) }} %}
 - **SymLink ?**:        {% {{ data['symlink']           }} %}
 - **Writable ?**:       {% {{ data['writable']          }} %}
 - **Executable ?**:     {% {{ data['executable']        }} %}
 - **Readable ?**:       {% {{ data['readable']          }} %}
 - **Has Print()?**:     {% {{ data['has_print']         }} %}
 - **Has import()?**:    {% {{ data['import_procedural'] }} %}
 - **Has BreakPoints ?**:{% {{ data['has_set_trace']     }} %}
 - **SheBang ?**:       `{% {{ data['has_shebang']       }} %}`
 - **Lines Total**:      {% {{ data['lines_total']       }} %}

 |  SHA-1 CheckSum Hash of the file (UTF-8)  |
 | ----------------------------------------- |
 |       ` {%{{ data['sha1'] }}%} `          |

 | Date of last Modification (ISO Format) | Date of last Accessed (ISO Format) |
 | -------------------------------------- | ---------------------------------- |
 |  {%{{ data['modified'] + "             |      " + data['accessed']       }}%}

 ---

 [&check; Source Code View](#sourcecode "Source Code Raw View")

 ```
{%
code_contents = ""
with open(data['fullpath'], 'r', encoding='utf-8') as __code:
    for line in __code.readlines():
        code_contents += ' ' + line
{{ code_contents + ' ```\n\n' }}
%}

 ---

 <details title="About Dookumentation">
    <summary><i>Dookumentation !</i></summary><br>
    <sub>
        Made with &hearts; and Python StdLibs by Juan!. Share Dookumentation with friends and coworkers:
        {%{{ '[Twitter](https://twitter.com/home?status=I%20Like%20{n}!:%20{u} "{n}"), [GooglePlus](https://plus.google.com/share?url={u} "{n}"), [Facebook](http://www.facebook.com/share.php?u={u}&t=I%20Like%20{n} "{n}")'.format(u=__url__, n="Dookumentation") }}%}
    </sub>
 </details>


 <!-- Dookumentation https://github.com/juancarlospaco/dookumentation#dookumentation -->










.. ..

<!--- **Dookumentation**

`Table of Contents <#toc>`_
---------------------------

- `Statistics <#statistics>`_: Statistics about current source code.
- `Table of Contents <#toc>`_: This Table of Contents.
- `Build Logs <#logs>`_: Build Logs for Developers and Debug.
- `Imports <#imports>`_: Information about all the Imports.
{%
toc_items = ""
if data.get('functions'):
    toc_items += '- `Functions <#functions>`_: Functions (not Methods).\n'
if data.get('classes'):
    toc_items += '- `Classes <#classes>`_:  Classes and Methods.\n'
if data.get('attributes'):
    toc_items += '- `Attributes <#attributes>`_: Attributes (probably Global).\n'
if data.get('pylama'):
    toc_items += '- `Bugs <#bugs>`_:  Imperfections on the code.\n'
if data.get('todo'):
    toc_items += '- `ToDo <#todo>`_: Auto-generated To-Do Lists.\n'
if data.get('fades'):
    toc_items += '- `Fades <#fades>`_: Information about Fades.\n'
if data.get('links'):
    toc_items += '- `Links Farm <#links>`_: All Links found on the code together.\n'
{{ toc_items }}
%}

-------------------------------------------------------------------------------

`Imports <#imports>`_
---------------------
{%
if data.get('imports'):
    imports_content = ""
    for _ in data['imports']['imports'].items() :
        imports_content += '- ``import {mod}{ass}`` Line {lin}\n\n'.format(mod=_[0], ass=" as {}".format(_[1]['asname']) if _[1]['asname'] else "", lin=_[1]['lineno'])
    for _ in data['imports']['from_imports'].items():
        imports_content += '- ``from {0} import {1}{2}`` Line {3}\n\n'.format(_[1]['module'], _[0], " as {}".format(_[1]['asname']) if _[1]['asname'] else "", _[1]['lineno'] )
    {{ '**{0} Imports!.**\n\n'.format(len(data['imports']['imports']) + len(data['imports']['from_imports'])) + imports_content + '`We recommend using iSort <https://github.com/timothycrosley/isort>`_' }}
%}

-------------------------------------------------------------------------------

`Classes <#classes>`_
---------------------

{%
if data.get('classes'):
    {{ '**{0} Classes!.**\n\n'.format(len(data.get('classes'))) }}
    for _ in data['classes'].items():
        decoradore = '\n\n'.join(_[1]['decorators']) + '\n\n' if _[1]['decorators'] != [] else ''
        attrivutes = ''
        if len(_[1]['attributes']):
            for atri in _[1]['attributes'].items():
                attrivutes += '    {0} Line {1}\n\n'.format(atri[0], atri[1])
        else:
            attrivutes = '    . . .\n\n'
        {{ '{deco}class **{name}:** Line {lin}\n\n    ``"""{docz}"""``\n\n{atri}\n\n'.format(name=_[0], deco=decoradore, docz=_[1]['docstring'], lin=_[1]['lineno'], atri=attrivutes) }}
        if len(_[1]['functions']):
            for _ in _[1]['functions'].items():
                decoradore = '\n\n'.join(['    ' + d for d in _[1]['decorators']]) + '\n\n' if _[1]['decorators'] != [] else ''
                attrivutes = ''
                if len(_[1]['attrs']):
                    for atri in _[1]['attrs'].items():
                        attrivutes += '        {0} Line {1}\n\n'.format(atri[0], atri[1])
                else:
                    attrivutes = '        . . .\n\n'
                {{ '{deco}    def **{name}:** Line {lin}\n\n        ``"""{docz}"""``\n\n{atri}'.format(name=_[0], deco=decoradore, docz=_[1]['docstring'], lin=_[1]['lineno'], atri=attrivutes) }}
        {{ '\n\n\n\n' }}
%}

-------------------------------------------------------------------------------

`Functions <#functions>`_
-------------------------

{%
if data.get('functions'):
    {{ '**{0} Functions!.**\n'.format(len(data.get('functions'))) }}
    for _ in data['functions'].items():
        decoradore = '\n\n'.join(_[1]['decorators']) + '\n\n' if _[1]['decorators'] != [] else ''
        attrivutes = ''
        if len(_[1]['attrs']):
            for atri in _[1]['attrs'].items():
                attrivutes += '    {0} Line {1}\n\n'.format(atri[0], atri[1])
        else:
            attrivutes = '    . . .\n\n'
        {{ '{deco}\n\ndef **{name}:** Line {lin}\n\n    ``"""{docz}"""``\n\n{atri}'.format(name=_[0], deco=decoradore, docz=_[1]['docstring'], lin=_[1]['lineno'], atri=attrivutes) }}
%}

-------------------------------------------------------------------------------

`Attributes <#attributes>`_
---------------------------

{%
if data.get('attributes'):
    attributes_content = ""
    for _ in sorted(data['attributes'].items()):
        attributes_content += '- ``{1}`` Line {0}\n\n'.format(_[1], _[0])
    {{ '**{0} Attributes!.**\n\n'.format(len(data.get('attributes'))) + attributes_content }}
%}

-------------------------------------------------------------------------------

`Bugs <#bugs>`_
---------------

{%
if data.get('pylama'):
    bugs_content = ""
    if data.get('lines_per_bug'):
        {{ '**You wrote 1 Bug every {0} Lines of Code!.**\n\n'.format(data['lines_per_bug']) }}
    for _ in data['pylama']:
        bugs_content += '- Line {0} Column {1} found by {2}: ``{3}``\n\n'.format(_['lnum'], _['col'], _['linter'].upper(), _['text'])
    {{ bugs_content + '`We recommend PyLama <https://github.com/klen/pylama#-pylama>`_' }}
%}

-------------------------------------------------------------------------------

`Fades <#fades>`_
-----------------

{%
if data.get('fades'):
    fades_content = ""
    for _ in data['fades']:
        fades_content += '- **{0}** on Line {1}: *{2}*\n\n'.format(_['type'].upper(), _['lnum'], _['text'][:99])
    {{  '**You use {0} Fades comments !.**\n\n'.format(len(data['fades'])) + fades_content + '`We recommend Fades <https://github.com/PyAr/fades>`_' }}
%}

-------------------------------------------------------------------------------

`Things To Do <#todo>`_
-----------------------

{%
if data.get('todo'):
    todo_content = ""
    for _ in data['todo']:
        todo_content += '- {0} on Line {1} ``{2}``.\n\n'.format(_['type'].upper(), _['lnum'], str(_['text'])[:99])
    {{ '**You have {0} Things to do!.**\n\n'.format(len(data['todo'])) + todo_content }}
%}

-------------------------------------------------------------------------------

`Link Farm <#links>`_
---------------------

{%
if data.get("links"):
    {{ '**{0} Links found on the code.**\n\n``{1}``\n\n'.format(len(data.get("links")), data.get("links")) }}
%}

-------------------------------------------------------------------------------

`Build Logs <#logs>`_
---------------------

{%
with open(log.getLogger().handlers[0].baseFilename, "r", encoding="utf-8") as __log:
    {{ '**Build Logs for Debugging and Developers**\n\n``{0}``\n\n'.format(__log.read().strip()) }}
%}

-------------------------------------------------------------------------------

`Statistics <#statistics>`_
---------------------------

- Lines Total:      {% {{ data['lines_total']       }} %}
- Lines of Code:    {% {{ data['lines_code']        }} %}
- Size (KiloBytes): {% {{ data['kilobytes']         }} %}
- Characters:       {% {{ data['characters']        }} %}
- Words:            {% {{ data['words']             }} %}
- Punctuations:     {% {{ data['punctuations']      }} %}
- Permissions:      {% {{ data['permissions']       }} %}
- Bugs ?:           {% {{ bool(len(data['pylama'])) }} %}
- SymLink ?:        {% {{ data['symlink']           }} %}
- Writable ?:       {% {{ data['writable']          }} %}
- Executable ?:     {% {{ data['executable']        }} %}
- Readable ?:       {% {{ data['readable']          }} %}
- Has print() ?:    {% {{ data['has_print']         }} %}
- Has __import__()?:{% {{ data['import_procedural'] }} %}
- Has BreakPoints ?:{% {{ data['has_set_trace']     }} %}
- SheBang ?:        {% {{ data['has_shebang']       }} %}

.. csv-table::
   :header: SHA-1 CheckSum Hash of the file (UTF-8)
   :widths: 80

   ``{% {{ data['sha1'] }} %}``

.. csv-table::
   :header: Date of last Modification (ISO Format), Date of last Accessed (ISO Format)
   :widths: 40, 40

    {%{{data['modified'] + ", " + data['accessed']}}%}

-------------------------------------------------------------------------------

**Dookumentation !**

*Made with Python StdLibs by Juan!. Share Dookumentation with friends and coworkers:*

{%{{ '`Twitter <https://twitter.com/home?status=I%20Like%20{n}!:%20{u}>`_ , `GooglePlus <https://plus.google.com/share?url={u}>`_ , `Facebook <http://www.facebook.com/share.php?u={u}&t=I%20Like%20{n}>`_'.format(u=__url__, n="Dookumentation") }}%}


.. comments

    Dookumentation https://github.com/juancarlospaco/dookumentation#dookumentation

..  --->
