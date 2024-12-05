# file: $MLADP_GUI/nedc_mladp_gui/src/utils/nedc_mladp_gui_run/nedc_mladp_gui_run.py
#

# define source and object files
#
SRC = $(wildcard *.py)

# define an installation target
#
install:
	cp -f $(SRC) $(MLADP_GUI)/nedc_mladp_gui/bin/$(SRC)
	cd $(MLADP)/nedc_mladp/bin; chmod u+rwx,g+rwx,o+rw $(SRC)

#
# end of file
