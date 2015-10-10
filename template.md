# Dookumentation


### [Imports](#imports "Imports")

{%
if data.get('imports'):
    for _ in data['imports'].items():
        {{ _[0], _[1] }}
else:
    {{ '- No Imports!, Parser can not find any Imports!.' }}
%}


### [Classes](#classes "Classes")

{%
if data.get('classes'):
    for _ in data['classes'].items():
        {{ _[0], _[1] }}
else:
    {{ '- No Classes!, Parser can not find any Classes!.' }}
%}


### [Functions](#functions "Functions")

{%
if data.get('functions'):
    for _ in data['functions'].items():
        {{ _[0], _[1] }}
else:
    {{ '- No Functions!, Parser can not find any Functions!.' }}
%}


### [Attributes](#attributes "Attributes")

{%
if data.get('attributes'):
    for _ in data['attributes'].items():
        {{ _[0], _[1] }}
else:
    {{ '- No Attributes!, Parser can not find any Attributes!.' }}
%}


### [&hercon; Bugs](#bugs "Bugs")

{%
if data.get('pylama'):
    {{ '- &star; You wrote 1 Bug every {0} Lines of Code!.{1}'.format(data['lines_per_bug'], os.linesep * 2) }}
    for _ in data['pylama']:
        {{ '- Line {0} Column {1} found by {2}: &raquo; {3}.{4}'.format(_['lnum'], _['col'], _['linter'].upper(), _['text'], os.linesep) }}
else:
    if check_path and parse_options:  # Theres PyLama but theres no Errors.
        {{ '<p style="color:green">No Bugs !, PyLama cant find any Errors.' }}
    else:  # Theres NO PyLama, but may or may not be no Errors ?.
        {{ '<p style="color:red">No PyLama!, Install PyLama using PIP !.' }}
%}


### [&check; Things To Do](#todo "To Do")

{%
if data.get('todo'):
    for _ in data['todo']:
        {{ '- {0} on Line {1} &raquo;&nbsp;&nbsp;&nbsp;{2}.{3}'.format(_['type'].upper(), _['lnum'], str(_['text'])[:99], os.linesep) }}
else:
    {{ '<p style="color:green">No Things To Do!.' }}
%}


### [&ccupssm; Statistics](#statistics "Statistics")

|  Lines Total  | Lines of Code  |  Size (KiloBytes)  |  Characters  |
| ------------- | -------------- | ------------------ | ------------ |
{%{{'|  {}  |  {}  |  {}  |  {}  |'.format(data['lines_total'], data['lines_code'], data['kilobytes'], data['characters'])}}%}


|  Words  |  Punctuations  |  Permissions  |  Bugs ?  |
| ------- | -------------- | ------------- | -------- |
{%{{'|  {}  |  {}  |  {}  |  {}  |'.format(data['words'], data['punctuations'], data['permissions'], bool(len(data['pylama'])))}}%}


|  SymLink ?  |  Writable ?  |  Executable ?  |  Readable ?  |
| ----------- | ------------ | -------------- | ------------ |
{%{{'|  {}  |  {}  |  {}  |  {}  |'.format(data['symlink'],data['writable'], data['executable'], data['readable'])}}%}


|  Has Print()?  |  Has import()?  |  Has BreakPoints ?  |  SheBang ?  |
| -------------- | --------------- | ------------------- | ----------- |
{%{{'|  {}  |  {}  |  {}  |  {}  |'.format(data['has_print'], data['import_procedural'],data['has_set_trace'],data['has_shebang'])}}%}


|  SHA-1 CheckSum Hash of the file (UTF-8)  |
| ----------------------------------------- |
|          {%{{ data['sha1'] }}%}           |


| Date of last Modification (ISO Format) | Date of last Accessed (ISO Format) |
| -------------------------------------- | ---------------------------------- |
|  {%{{ data['modified'] + "             |      " + data['accessed']          }}%}


<hr>

<details title="About Dookumentation">
    <summary>
        <i>Dookumentation !</i>
    </summary>
    <br>
    <sub>
        Made with Python StdLibs by Juan!.
        Tested on Chromium, Chrome, Android, Qupzilla.
        Share Dookumentation with friends and coworkers:
        {%{{
        '[Twitter](https://twitter.com/home?status=I%20Like%20{n}!:%20{u} "{n}"), [GooglePlus](https://plus.google.com/share?url={u} "{n}"), [Facebook](http://www.facebook.com/share.php?u={u}&t=I%20Like%20{n} "{n}")'.format(u=__url__, n="Dookumentation")
        }}%}
    </sub>
</details>


<!-- Dookumentation


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


-->
