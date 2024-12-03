#!/usr/bin/bash
mkdir "../bin" # create landing directory for driver programs
mkdir "../lib" # create landing directory for library

# compile the driver function
cd $MLADP_GUI/nedc_mladp_gui/src/utils/nedc_mladp_gui_run
make

# compile the main page
cd $MLADP_GUI/nedc_mladp_gui/src/functs/nedc_mladp_main_page
make

# compile the header block
cd ../nedc_mladp_header_block
make

# compile the display block
cd ../nedc_mladp_display_block
make

# compile the stats block
cd ../nedc_mladp_stats_block
make