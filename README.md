# MDWiki - MarkDown Wiki

This project provide confluence liked wiki library based on markdown and file system.

It would be good choice using [SimpleMDE](https://github.com/sparksuite/simplemde-markdown-editor) with MDWiki.

## Features

### high-level

- Wiki Space
    - Authentication
- I18N for wiki content

### low-level

- File Base Database
    - CRUD
    - dump, migrate
    - history of wiki content
        - PyGit wrapper
        - history parser
    - page manager
        - markdown syntax checker
        - page is directory which includes meta.json, content-(locale).md and pages
    - token
        - authentication
        - authorization
- User Permission
    - provide middleware for FBD token
- i18n
