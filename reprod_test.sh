# $ make list-projects
# Sample projects: template biorobots-sample cancer-biorobots-sample cancer-immune-sample
#                  celltypes3-sample heterogeneity-sample pred-prey-farmer virus-macrophage-sample
#                  worm-sample interaction-sample mechano-sample rules-sample

make reset
make
python params_run.py heterogeneity params_heterog.txt
make reset
make template
make
python params_run.py project params_template.txt
make reset
make biorobots-sample
make
python params_run.py biorobots params_biorobots.txt
make reset
make cancer-biorobots-sample
make
python params_run.py project params_cancer_biorobots.txt   # bug? exec is "project"
make reset
make celltypes3-sample
make
python params_run.py celltypes3 params_celltypes3.txt
make reset
make pred-prey-farmer
make
python params_run.py pred_prey params_predprey.txt
make reset
make virus-macrophage-sample
make
python params_run.py virus-sample params_virus_mac.txt
make reset
make worm-sample
make
python params_run.py worm params_worm.txt
make reset
make interaction-sample
make
python params_run.py interaction_demo params_worm.txt
make reset
make mechano-sample
make
python params_run.py project params_mechano.txt   # bug? "project"
make reset
make rules-sample
make
python params_run.py project params_rules.txt   # bug? "project"
