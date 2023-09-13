# Guidelines on use of style library

## CSS files
 - Due to issues with css updating without versioning we decided so that the designs do not break on prod we download the Berlin css files. We update them before each release and img paths in them must be updated so remove https://www.berlin.de/... path and include the local path.

## JS files
 - Loaded via script tag in base.html

## Header
 - 2 headers, one simple structure for LS German and one more complex structure for EN and DE, editor is responsible for ensuring simple structure of LS
 - Template copied from style library and filled with links added in wagtail via Snippets > Navigation menus > header / header_ls
 - If statement in header.html checks and loads correct links for each header

## Upper footer
 - 2 footers, one simple structure for LS German and one more complex structure for EN and DE, editor is responsible for ensuring simple structure of LS
- Template copied from style library and filled with links added in wagtail via Snippets > Navigation menus > footer / footer_ls
- If statement in upper_footer.html checks and loads correct links for each footer

## Lower footer
 - Loads from external site in upper_footer.html via `get_external_footer` template tag.
 - Template tag defined in contrib_tags, ensures site still loads even if footer not available from external source (was issue during a DOS attck)

## Fonts
- Arial is used for header and footer
- BerlinType is for content of main
