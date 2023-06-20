# reproducibility_tests

Dependencies:
* PhysiCell source installation
* most likely a *nix platform
* imagemagick
* maybe later, if we render results other than .svg: matplotlib

Example usage:
```
# Sequentially build and run each sample project (or most of them, initially)
# This shell script uses "params_run.py" and a .txt file that's specific for each sample project

M1P~/dev/PhysiCell_v1.12.0$ sh reprod_test.sh

# Perform Unix "diff" on the (ascii) .svg files. Notify and pause if != 4:

M1P~/dev/PhysiCell_v1.12.0$ python diffs_svg.py ~/dev/PhysiCell_v1.12.0 ~/git/PhysiCell_rheiland_dev_v1_12

# Generate final .svg (.jpg) images of sample projects and displaying them side-by-side in .html
# (note we pipe the customized terminal output from the script into a .html file)

M1P~/dev/PhysiCell_v1.12.0$ python side_by_side.py ~/dev/PhysiCell_v1.12.0 ~/git/PhysiCell_rheiland_dev_v1_12
```

Finding `max_time` config files in v1.12.0
```
$ grep max_time */config/P*.xml
biorobots/config/PhysiCell_settings.xml:                <max_time units="min">2880</max_time>
cancer_biorobots/config/PhysiCell_settings.xml:        <max_time units="min">14400</max_time>
cancer_immune/config/PhysiCell_settings.xml:            <max_time units="min">30240</max_time> <!-- 21 days * 24 h * 60 min -->
celltypes3/config/PhysiCell_settings.xml:               <max_time units="min">7200</max_time> <!-- 5 days * 24 h * 60 min -->
heterogeneity/config/PhysiCell_settings.xml:            <max_time units="min">64800</max_time>
interactions/config/PhysiCell_settings.xml:             <max_time units="min">10080</max_time>
mechano/config/PhysiCell_settings.xml:        <max_time units="min">14400</max_time>
pred_prey_farmer/config/PhysiCell_settings.xml:         <max_time units="min">7200</max_time> <!-- 5 days * 24 h * 60 min -->
rules_sample/config/PhysiCell_settings-backup.xml:        <max_time units="min">14400</max_time>
rules_sample/config/PhysiCell_settings.xml:        <max_time units="min">7200</max_time>
template/config/PhysiCell_settings.xml:         <max_time units="min">7200</max_time> <!-- 5 days * 24 h * 60 min -->
virus_macrophage/config/PhysiCell_settings.xml:         <max_time units="min">2880</max_time>
worm/config/PhysiCell_settings.xml:             <max_time units="min">3000</max_time>
```

