# file: $MLADP_GUI/nedc_mladp_gui/src/functs/nedc_mladp_main_page/nedc_mladp_main_page.py
#

# define source and object files
#
SRC = $(wildcard *.py)

# define an installation target
#
install:
	cd $(MLADP_GUI)/nedc_mladp_gui/lib/
	cp -f $(SRC) $(MLADP_GUI)/nedc_mladp_gui/lib/
	cd $(MLADP_GUI)/nedc_mladp_gui/lib; chmod u+rw,g+rw,o+r $(SRC)

#
# end of file
