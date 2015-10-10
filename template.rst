

******************
**Dookumentation**
******************


`Imports <#imports>`_
---------------------

{%
if data.get('imports'):
    for _ in data['imports'].items():
        {{ _[0], _[1] }}
else:
    {{ '- No Imports!, Parser can not find any Imports!.' }}
%}


`Classes <#classes>`_
-------------------------

{%
if data.get('classes'):
    for _ in data['classes'].items():
        {{ _[0], _[1] }}
else:
    {{ '- No Classes!, Parser can not find any Classes!.' }}
%}


`Functions <#functions>`_
-------------------------

{%
if data.get('functions'):
    for _ in data['functions'].items():
        {{ _[0], _[1] }}
else:
    {{ '- No Functions!, Parser can not find any Functions!.' }}
%}


`Attributes <#attributes>`_
---------------------------

{%
if data.get('attributes'):
    for _ in data['attributes'].items():
        {{ _[0], _[1] }}
else:
    {{ '- No Attributes!, Parser can not find any Attributes!.' }}
%}


`Bugs <#bugs>`_
---------------

{%
if data.get('pylama'):
    {{ '- **You wrote 1 Bug every {0} Lines of Code!.**{1}'.format(data['lines_per_bug'], os.linesep * 2) }}
    for _ in data['pylama']:
        {{ '- Line {0} Column {1} found by {2}:    {3}.{4}'.format(_['lnum'], _['col'], _['linter'].upper(), _['text'], os.linesep) }}
else:
    if check_path and parse_options:  # Theres PyLama but theres no Errors.
        {{ '- No Bugs !, PyLama cant find any Errors.' }}
    else:  # Theres NO PyLama, but may or may not be no Errors ?.
        {{ '- No PyLama!, Install PyLama using PIP !.' }}
%}


`Things To Do <#todo>`_
-----------------------

{%
if data.get('todo'):
    for _ in data['todo']:
        {{ '- {0} on Line {1}    {2}.{3}'.format(_['type'].upper(), _['lnum'], str(_['text'])[:99], os.linesep) }}
else:
    {{ '- No Things To Do!.' }}
%}


`Statistics <#statistics>`_
---------------------------

.. csv-table::
   :header: Lines Total, Lines of Code, Size (KiloBytes), Characters
   :widths: 20, 20, 20, 20

{%{{'    {}, {}, {}, {}'.format(data['lines_total'], data['lines_code'], data['kilobytes'], data['characters'])}}%}


.. csv-table::
   :header: Words, Punctuations, Permissions, Bugs ?
   :widths: 20, 20, 20, 20

{%{{'    {}, {}, {}, {}'.format(data['words'], data['punctuations'], data['permissions'], bool(len(data['pylama'])))}}%}


.. csv-table::
   :header: SymLink ?, Writable ? , Executable ?, Readable ?
   :widths: 20, 20, 20, 20

{%{{'    {}, {}, {}, {}'.format(data['symlink'],data['writable'], data['executable'], data['readable'])}}%}


.. csv-table::
   :header: Has print() ? , Has __import__()? , Has BreakPoints ?, SheBang ?
   :widths: 20, 20, 20, 20

{%{{'    {}, {}, {}, {}'.format(data['has_print'], data['import_procedural'],data['has_set_trace'],data['has_shebang'])}}%}


.. csv-table::
   :header: SHA-1 CheckSum Hash of the file (UTF-8)
   :widths: 80

    {%{{data['sha1']}}%}


.. csv-table::
   :header: Date of last Modification (ISO Format), Date of last Accessed (ISO Format)
   :widths: 40, 40

    {%{{data['modified'] + ", " + data['accessed']}}%}


-------------------------------------------------------------------------------


**Dookumentation !**

*Made with Python StdLibs by Juan!. Tested on Chromium, Chrome, Android, Qupzilla.*

*Share Dookumentation with friends and coworkers:* {%{{ '`Twitter <https://twitter.com/home?status=I%20Like%20{n}!:%20{u}>`_ , `GooglePlus <https://plus.google.com/share?url={u}>`_ , `Facebook <http://www.facebook.com/share.php?u={u}&t=I%20Like%20{n}>`_'.format(u=__url__, n="Dookumentation") }}%}


.. comments

    Dookumentation


    Templates can execute unrestricted Python 3,
    it should Render something cute from a simple plain text JSON 'data' object,
    the plain text JSON 'data' is simply the *.json file from /doc/json/ folder,
    this Template-Plugin Renders JSON data to MD (MarkDown, GitHub Compatible).

    I/O, Reading and Writing, Folders, SubFolders is handled by Dookumentation.

    The Encoding is UTF-8 and Unicode ready.

    The Programming Code is normal Python 3.

    The Template Mini-Markup code is Templar (Django / Jinja alike):
    https://gist.github.com/juancarlospaco/97a6a09d64b190a630ad#gistcomment-1576482

    For more info about Dookumentation:
    https://github.com/juancarlospaco/dookumentation#dookumentation

