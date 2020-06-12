#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Copyright (c) 2020 ContinualAI                                               #
# Copyrights licensed under the MIT License.                                   #
# See the accompanying LICENSE file for terms.                                 #
#                                                                              #
# Date: 1-05-2020                                                              #
# Author(s): Vincenzo Lomonaco                                                 #
# E-mail: contact@continualai.org                                              #
# Website: www.continualai.org                                                 #
################################################################################

""" Simple script to generate the research.rst file loading references from
    a bibtex. """

# Python 2-3 compatible
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import bibtexparser
from bibtexparser.customization import convert_to_unicode
from bibtexparser.bparser import BibTexParser
import copy
import os

showbib_template = """
.. |[PAPERID][SECTION]| raw:: html

    <br>
    <button style="font-size:75%; line-height:15px" onclick="[PAPERID][SECTION]Function()" id="[PAPERID][SECTION]_btt">Bib</button>
    <button style="font-size:75%; line-height:15px" onclick="[PAPERID][SECTION]Function2()" id="[PAPERID][SECTION]_btt2">Abstract</button>
    <button style="font-size:75%; line-height:15px" onclick="[PAPERID][SECTION]Function3()" id="[PAPERID][SECTION]_btt3">Notes</button>
    
    <p style="background-color: #2980b929; font-size:75%; line-height:15px"><span id="[PAPERID][SECTION]_more" style="display: none">
        [BIBTEX]
    </span></p>
    <p style="background-color: #2980b929; font-size:75%; line-height:15px"><span id="[PAPERID][SECTION]_more2" style="display: none">
        [ABSTRACT]
    </span></p>
    <p style="background-color: #2980b929; font-size:75%; line-height:15px"><span id="[PAPERID][SECTION]_more3" style="display: none">
        [NOTE]
    </span></p>
    <script>
        function [PAPERID][SECTION]Function() {
          var moreText = document.getElementById("[PAPERID][SECTION]_more");
          var moreText2 = document.getElementById("[PAPERID][SECTION]_more2");
          var moreText3 = document.getElementById("[PAPERID][SECTION]_more3");
          var btnText = document.getElementById("[PAPERID][SECTION]_btt");

          if (moreText.style.display === "none") {
            btnText.innerHTML = "Bib";
            moreText.style.display = "inline";
          } else {
            btnText.innerHTML = "Bib";
            moreText.style.display = "none";
          }
          moreText2.style.display = "none";
          moreText3.style.display = "none";
        }
    </script>
    <script>
        function [PAPERID][SECTION]Function2() {
          var moreText = document.getElementById("[PAPERID][SECTION]_more2");
          var moreText1 = document.getElementById("[PAPERID][SECTION]_more");
          var moreText3 = document.getElementById("[PAPERID][SECTION]_more3");
          var btnText = document.getElementById("[PAPERID][SECTION]_btt2");

          if (moreText.style.display === "none") {
            btnText.innerHTML = "Abstract";
            moreText.style.display = "inline";
          } else {
            btnText.innerHTML = "Abstract";
            moreText.style.display = "none";
          }
          moreText1.style.display = "none";
          moreText3.style.display = "none";
        }
    </script>
    <script>
        function [PAPERID][SECTION]Function3() {
          var moreText = document.getElementById("[PAPERID][SECTION]_more3");
          var moreText1 = document.getElementById("[PAPERID][SECTION]_more");
          var moreText2 = document.getElementById("[PAPERID][SECTION]_more2");
          var btnText = document.getElementById("[PAPERID][SECTION]_btt3");

          if (moreText.style.display === "none") {
            btnText.innerHTML = "Notes";
            moreText.style.display = "inline";
          } else {
            btnText.innerHTML = "Notes";
            moreText.style.display = "none";
          }
          moreText1.style.display = "none";
          moreText2.style.display = "none";
        }
    </script>
    
"""

def remove_mendeley_notice_from_files(filename):
    with open(filename, 'r') as fin:
        data = fin.read().splitlines(True)

    if data[0].startswith("Automatically generated"):
        with open(filename, 'w') as fout:
            fout.writelines(data[5:])

def extract_bibtex(bib_database, id):

    # print("bib_database.entries: ", bib_database.entries)
    pos = None
    for i, entry in enumerate(bib_database.entries):
        if entry['ID'] == id:
            pos = i
            # print(entry['ID'])

    bib_db = copy.deepcopy(bib_database)
    # print(id)
    # print("pos:", pos)
    del bib_db.entries[pos+1:]
    del bib_db.entries[:pos]
    str = bibtexparser.dumps(bib_db)
    return str

def bibtex_string2html(str, remove_abstract=True):

    lines = str.split("\n")
    final_str = ""
    # print(lines)
    for i, line in enumerate(lines):

        if remove_abstract and line.strip().startswith("abstract"):
            continue

        if line == "":
            continue
        if i == 0:
            final_line = line + "<br>"
        else:
            final_line = line + "<br>"

        final_str += final_line

    # print(final_str)
    return final_str

def journal_or_booktitle(item):

    if "journal" in item.keys():
        return "*" + item["journal"] + "*"
    elif "booktitle" in item.keys():
        return "*" + item["booktitle"] + "*"
    elif item["ENTRYTYPE"] == "book":
        return "*" + item["publisher"] + "*"
    else:
        print("WARNING: venue missing!!!")
        return ""

def pages_or_void(item):

    if "pages" in item.keys():
        return ", " + item["pages"]
    else:
        return ""

def get_author(item):

    authors_list = item['author'].split(" and ")
    str = ""
    for i, aut in enumerate(authors_list):
        # print(aut)
        surname, name = aut.split(", ")
        authors_list[i] = name + " " + surname
        if i == len(authors_list) -1:
            str += " and " + name + " " + surname
        elif i == 0:
            str +=  name + " " + surname
        else:
            str +=  ', ' + name + " " + surname

    return str

def get_title(item):

    title = item['title'].replace("{", "").replace("}", "")

    if "url" in item.keys():
        return "`" + title + " <" + item["url"]+ ">`__"
    else:
        return title

# settings ---------------------------------------------------------------------
bibtex_path = "bibtex"
full_bib_db = "Continual Learning Papers.bib"
template_file_path = "research_template.rst"
tag2fill = "<TAG>"
output_filename = "research.rst"
# this respect also the order of the sections
bib_files = [
    "Continual Learning Papers-Classics.bib",
    "Continual Learning Papers-Review Papers and Books.bib",
    "Continual Learning Papers-Catastrophic Forgetting Studies.bib",
    "Continual Learning Papers-Benchmarks.bib",
    "Continual Learning Papers-Architectural Methods.bib",
    "Continual Learning Papers-Regularization Methods.bib",
    "Continual Learning Papers-Rehearsal Methods.bib",
    "Continual Learning Papers-Generative Replay Methods.bib",
    "Continual Learning Papers-Hybrid Methods.bib",
    "Continual Learning Papers-Metrics and Evaluations.bib",
    "Continual Learning Papers-Bioinspired Methods.bib",
    "Continual Learning Papers-Meta Continual Learning.bib",
    "Continual Learning Papers-Continual Meta Learning.bib",
    "Continual Learning Papers-Continual Reinforcement Learning.bib",
    "Continual Learning Papers-Continual Sequential Learning.bib",
    "Continual Learning Papers-Dissertation and Theses.bib",
    "Continual Learning Papers-Applications.bib",
    "Continual Learning Papers-Neuroscience.bib",
    "Continual Learning Papers-Robotics.bib",
    "Continual Learning Papers-Others.bib"
]
sec_descriptions = [
    "In this section you'll find pioneering and classic continual learning "
    "papers. We recommend to read all the papers in this section for a "
    "good background on current continual deep learning developments.",
    "In this section we collect all the main review papers and books on the "
    "subject. These may constitute a solid starting point for "
    "continual learning newcomers.",
    "In this section we list all the major contributions trying to understand "
    "catastrophic forgetting and its implication in machines that learn "
    "continually.",
    "In this section we list all the papers related to new benchmarks "
    "proposals for continual learning and related topics. ",
    "In this section we collect all the papers introducing a continual "
    "learning strategy employing some architectural methods.",
    "In this section we collect all the papers introducing a continual "
    "learning strategy employing some regularization methods.",
    "In this section we collect all the papers introducing a continual "
    "learning strategy employing some rehearsal methods.",
    "In this section we collect all the papers introducing a continual "
    "learning strategy employing some generative replay methods.",
    "In this section we collect all the papers introducing a continual "
    "learning strategy employing some hybrid methods.",
    "In this section we list all the papers related to the continual learning "
    "evalution protocols and metrics.",
    "In this section we list all the papers related to bio-inspired continual "
    "learning approaches.",
    "In this section we list all the papers related to the meta-continual "
    "learning.",
    "In this section we list all the papers related to the continual "
    "meta-learning.",
    "In this section we list all the papers related to the continual "
    "Reinforcement Learning.",
    "Here we maintain a list of all the papers related to the continual "
    "learning at the intersection with sequential learning.",
    "In this section we maintain a list of all the dissertation and thesis "
    "produced on continual learning and related topics.",
    "In this section we maintain a list of all applicative papers "
    "produced on continual learning and related topics.",
    "In this section we maintain a list of all Neuroscience papers "
    "that can be related (and useful) for continual machine learning.",
    "In this section we maintain a list of all Robotics papers "
    "that can be related to continual learning.",
    "In this section we list all the other papers not appearing in at least "
    "one of the above sections."
]

tags2color = {
    "framework": "Tomato",
    "som": "Cornsilk",
    "sparsity": "DarkSalmon",
    "dual": "green",
    "spiking": "yellow",
    "rnn": "AliceBlue",
    "nlp": "BlueViolet",
    "mnist": "MediumAquaMarine",
    "fashion": "LightGray",
    "cifar": "DarkCyan",
    "core50": "Chartreuse",
    "imagenet": "DeepPink",
    "vision": "#E5E4E2",
    "audio": "#50EBEC",
    "hebbian": "#99C68E",
    "omniglot": "#FDD017",
    "bayes": "Violet",
    "generative": "Maroon"
}
# ------------------------------------------------------------------------------

remove_mendeley_notice_from_files(os.path.join(bibtex_path, full_bib_db))

with open(os.path.join(bibtex_path, full_bib_db)) as bibtex_file:
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    full_bib_db = bibtexparser.load(bibtex_file, parser=parser)

str2injcet = ""
rst_end_str = ""
for i, bibfile in enumerate(bib_files):

    sec_title = bibfile.split("-")[1][:-4]
    with open(os.path.join(bibtex_path, bibfile)) as bibtex_file:
        parser = BibTexParser()
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    with open(template_file_path) as rf:
        template_str = rf.read()

    str2injcet += sec_title + \
                 "\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n" + \
                  sec_descriptions[i] + "\n\n"
    for item in sorted(
            bib_database.entries, key=lambda j: j['year'], reverse=True):
        # print(item)

        str2injcet_tags = ""
        if "mendeley-tags" in item.keys():
            # print(item["mendeley-tags"])
            str_tags = item["mendeley-tags"].replace(";", "").replace("[", "")
            str_tags = str_tags.replace(",", "")
            cur_tags = str_tags.replace(" ", "").split("]")
            del cur_tags[-1]
            # print(cur_tags)

            for tag in cur_tags:
                str2injcet_tags += ":raw:html:`<span " \
                                   "style='background-color:{}; padding: " \
                                   "2px; border-radius:4px; border: 1px " \
                                   "solid black;'>[{}]" \
                                   "</span>` ".format(tags2color[tag], tag)

        str2injcet += "- " + get_title(item) + \
                      " by " + get_author(item) + \
                      ". "+ journal_or_booktitle(item) + \
                      pages_or_void(item) + \
                      ", " + item['year'] + ". " + \
                      str2injcet_tags + \
                      " |" + item["ID"].replace("-","")\
                      + sec_title.replace(" ", "_") + "|" + "\n"

        # Add bib file button
        bib_str = showbib_template.replace(
            "[BIBTEX]", bibtex_string2html(
                extract_bibtex(full_bib_db, item["ID"])
            )
        )
        bib_str = bib_str.replace("[PAPERID]", item["ID"].replace("-",""))
        if "abstract" in item.keys():
            bib_str = bib_str.replace("[ABSTRACT]", item["abstract"])
        else:
            bib_str = bib_str.replace("[ABSTRACT]", "N.A.")
        if "annote" in item.keys():
            bib_str = bib_str.replace("[NOTE]", item["annote"].replace(
                "\n", "\n\t\t"))
            # pprint(item)
        else:
            bib_str = bib_str.replace("[NOTE]", "N.A.")
        bib_str = bib_str.replace("[SECTION]", sec_title.replace(" ", "_"))

        rst_end_str += bib_str

    if i != len(os.listdir(bibtex_path)) -1:
        str2injcet += "\n"
    else:
        str2injcet = str2injcet[:-1]

template_str = template_str.replace(tag2fill, str2injcet) + rst_end_str

with open(output_filename, "w") as wf:
    wf.write(template_str)
