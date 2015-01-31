all: csvedit_mod/ui/mainwindow.py

csvedit_mod/ui/mainwindow.py: ui/mainwindow.ui
	pyside-uic ui/mainwindow.ui -o csvedit_mod/ui/mainwindow.py

clean:
	$(RM) csvedit_mod/ui/mainwindow.py
