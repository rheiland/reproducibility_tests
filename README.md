# reproducibility_tests

in v1.12.0
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

