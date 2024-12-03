# nedc_mladp_gui
GUI that allows users to view breast tissue slides that have gone through various Machine Learning models. The slides can be viewed in different stages (original annotations, RNF predicted, and CNN predicted). Text predictions included.

### some pre-steps
1. In your `.bashrc`, export this environment variable.
   ```
   MLADP_GUI=/data/isip/exp/pabcc/exp_0001
   export MLADP_GUI
   ```
2. Reload bash profile in the terminal.
   ```
   source ~/.bashrc
   ```
3. Compile everything.
   ```
   cd $MLADP_GUI/nedc_mladp_gui/src
   ./make.sh
   ```
Note:
    GUI might not work on VSCode. Use MobaXterm or any other terminal.
