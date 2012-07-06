import os,sys,string

try: 
    f = open("menuindex.txt").readlines()
except:
    print "Could not open menuindex.txt"
    f = []

os.system("mkdir cam")
o = open("cam/menuidx.dat", "w")
menu = open("../src/menuindexentries.h", "w")

print >> menu, """
// Auto-generated; do not edit this file.
// Edit doc/menuindex.py instead.
"""

print >> o, "001 About Magic Lantern"

sections = 0

#~ idx = {}
#~ idxp = {}
for l in f[1:]:
    l = l.strip("\n").split(" ")
    try: page, type, name = l[0], l[1], string.join(l[2:], " ")
    except:
        print l
    page = int(page)
    name = name.replace(r"$\leftrightarrow $", "<-->")
    name = name.replace(r"$\rightarrow $", "->")

    if type == "subsubsection": # each menu entry is a subsection
        item = name.split(":")[0]
        
        if " and " in item:
            and_terms = item.split(" and ")
            for t in and_terms:
                print >> o, "%03d %s" % (page, t.strip())
            continue
            
        item = item.split(" / ")[0]
        item = item.split(" (")[0]
        item = item.split(" X sec")[0]
        item = item.strip()
        #~ idx[item] = page
        #~ idxp[page] = item
        #print page, item
        print >> o, "%03d %s" % (page, item)

    if type == "section": # main sections in menu
        sections += 1
        item = name
        #print page, item
        print >> o, "%03d %s" % (page, item)
        print >> menu, """    {
        .name = "%s",
        .priv = "%s",
        .select = menu_help_go_to_label,
        .display = menu_print,
        //.essential = FOR_MOVIE | FOR_PHOTO,
    },""" % (item, item)

    if type == "end":
        lastpage = page - 1
        print >> o, "%03d end" % lastpage

#~ print idxp
o.close()
menu.close()
