# csvedit

A work-in-progress attempt at writing a simple GUI CSV editor that exposes
the raw string data.

It's not useful at the moment.  I'm learning my way around pyside
(this is as much a learning exercise as a project to produce a useful
tool), so I'll be picking away at it gradually.

## Why

Usually I'd use Emacs with its csv-mode to edit CSV files, but the
align command can be quite slow on large files.  I aim to make this
work faster, but I'm not holding my breath.

Spreadsheets, including LibreOffice/OpenOffice Calc, Gnumeric and
(gritting teeth as I type this) MS Excel, are sometimes too clever
inferring numeric types for stuff that wasn't intended to be numeric
so ids, codes and phone numbers are mangled.

Also as a pyside learning exercise.
