import os, re

main_dir = "E:/Videos/Videos/Anime/"
folders = [fld for fld in os.listdir(main_dir) if os.path.isdir(main_dir+fld)]

def num_from_str(string):
    return int(re.findall(r'\b\d+\b', string)[0])

for fld in folders:
    old_names = [ep for ep in os.listdir(main_dir+fld) if not ep.startswith(fld)]

    for old in old_names:
        new_name = main_dir+fld+"/"+fld+ " Episode " + str(num_from_str(old)) +" [Arabic] "+old[-4:]
        os.rename(main_dir+fld+"/"+old, new_name)
