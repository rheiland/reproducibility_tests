# compare diffs between .svg files in different runs

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
for out_dir in ['out_template','out_biorobots','out_cancer_biorobots','out_heterog','out_predprey','out_virus_mac','out_worm','out_interact','out_rules']:
#for out_dir in ['out_template']:
    print("----------  processing ",out_dir)
    svg_files = glob.glob(f'{dir1}/{out_dir}/snap*.svg')
    svg_files.sort()
    for filename in svg_files:
        f = os.path.basename(filename)
        f1 = os.path.join(dir1,out_dir,f)
        f2 = os.path.join(dir2,out_dir,f)
        # print(f1,f2)
        # cmd =  f"diff {f1} {f2} | wc -l"
        cmd =  f"diff {f1} {f2} | wc -l > diff_result.txt"
        print(cmd)
        os.system(cmd)
        with open('diff_result.txt') as f:
            vstr = f.readline()
            print(vstr)
            # Note: a "diff" will almost certainly return 4 lines, showing different run times
            # 1340c1340
            # <    0 days, 0 hours, 1 minutes, and 12.1327 seconds
            # ---
            # >    0 days, 0 hours, 1 minutes, and 12.4215 seconds
            if (int(vstr) != 4):   # hard-coded "4"
                print("======---------------->  Warning: not a match!")
                userinput = input("\nPress Enter to skip remaining files for this sample:")
                # print("Username is: " + username)
                break
                # sys.exit(1)

# for fname in os.listdir(dir1):
#     fname1 = os.path.join(dir1, fname)
#     fname2 = os.path.join(dir2, fname)
#     # checking if it is a file
#     if os.path.isfile(f):
#         print(f)

#             cmd =  "diff " + dir1 + "out_heterog" + " > " + log_file + " " + background_str
#             print("----- cmd = ",cmd)
# #            os.system(cmd)   # <------ Execute the simulation
