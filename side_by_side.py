# plot side-by-side .svg images from different runs

import os
import sys
from pathlib import Path
import glob

# print(len(sys.argv))
if (len(sys.argv) < 3):
  usage_str = "Usage: %s <dir1> <dir2>" % (sys.argv[0])
  print(usage_str)
  print("e.g.:  python diffs_svg.py ~/blah1 ~/blah2")
  exit(1)
else:
   dir1 = sys.argv[1]
   dir2 = sys.argv[2]


svg_files = Path(dir1).glob(f'{dir1}/out_heterog/snap*.svg')
#print("svg_files=",svg_files)


#for filename in glob.iglob(f'{dir1}/snap*.svg'):
#for d in ['out_template','out_biorobots','out_cancer_biorobots','out_heterog','out_mechano','out_predprey','out_virus_mac','out_worm','out_rules']
for out_dir in ['out_template','out_biorobots','out_cancer_biorobots','out_heterog','out_predprey','out_virus_mac','out_worm','out_rules']:
#for out_dir in ['out_template']:
    # print("----------  processing ",out_dir)
    svg_files = glob.glob(f'{dir1}/{out_dir}/snap*.svg')
    svg_files.sort()
    filename = svg_files[-1]
    # for filename in svg_files:
    if True:
        f = os.path.basename(filename)
        f1 = os.path.join(dir1,out_dir,f)
        f2 = os.path.join(dir2,out_dir,f)
        # print(f1,f2)
        # cmd =  f"diff {f1} {f2} | wc -l"

        # montage -geometry +0+0 -tile 2x1 out_template/snapshot00000010.svg ~/
# git/PhysiCell_rheiland_dev_v1_12/out_template/snapshot00000010.svg tmp.png
        cmd =  f"montage -geometry +0+0 -tile 2x1 {f1} {f2} tmp.png"
        # print(cmd)
        os.system(cmd)

        # cmd =  f"convert -resize 20% tmp.png {out_dir}.jpg"
        cmd =  f"convert -resize 800x tmp.png {out_dir}.jpg"
        # print(cmd)
        os.system(cmd)

        print(f"<img src={out_dir}.jpg><br>")
        print(f"                       ------- {out_dir} --------<br>")
        print(f"<hr>")
