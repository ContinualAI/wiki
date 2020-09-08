# ContinualAI Wiki: a collaborative wiki on Continual/Lifelong Machine Learning
<div style="text-align:center">
	<img src="https://www.continualai.org/images/continualai_logo_name_black.png" width="160" height="100">
</div>

The aim of the project is to create an open-source, collaborative wiki to provide a starting point for researchers, developers and AI enthusiasts who share an interest in Continual Learning and are willing to learn more or contribute to this field.  
You can find info about CL workshops, media articles, companies using CL and much more.  

The wiki also provides a curated list of annotated papers in the [Research section](https://wiki.continualai.org/research.html). Be sure to check it out!

[Join our community](https://continualai.herokuapp.com/) on Slack to stay updated with the latest Continual Learning news.

Visit the wiki &rarr; http://wiki.continualai.org/

Below, you can find instructions on **how to contribute to the wiki**!

---------------------------------------------------

## Add a new paper to the Research section
ContinualAI wiki provides a [Research section](https://wiki.continualai.org/research.html) with a curated list of annotated papers. The list is maintained through a Mendeley group. You can join the group and help us keeping it updated (see next section).  

If you don't want to join the group, you can simply open a Github issue to suggest us a new paper (or even more than one). We will take care of adding it to the wiki as soon as possible. 

1. Open a new Github issue. You can use `new paper` or `new conference` tags to specify which kind of issue you are submitting.

2. Attach your bib file containing the paper you want to include in the wiki. If you don't have a bib file, just provide us with the link to the paper. The link should point to a location where paper metadata can be appropriately retrieved by common reference managers.


## Join the ContinualAI Mendeley group

You can give your contribution to the group by **adding new papers** or by helping **annotating the existing ones**.

1. Join our [Mendeley group](https://www.mendeley.com/community/continual-learning-papers/)

2. To **add a new paper**

	2.1. Add it to the group folder which best represents the paper contribution. Read some advices below if you are uncertain on this. You can add the paper from your library or directly from the paper webpage through the Mendeley plugin. 

	2.2 Through the Mendeley Desktop app, fill in the `Citation Key` field in the paper details. This must be in the form `[lastname][year][a]` (e.g. `smith2019a`) where `a` has to be replaced with the first available letter in order to make the citation unique. You can look for existing Citation Keys through the Mendeley search bar.
	*If you can't find the `Citation Key` field, enable it in `Tools -> Options -> Document Details` menu.*
    
    2.3 Make sure that at least `title`, `authors`, `year`, `publication type` and `venue` are specified.

3. To **annotate** an existing paper

	3.1. Check the list of existing tags in `tags.csv` file. If you want to add a new tag, please add it in there and submit a Pull Request (see `Contribute to the wiki` section).

	3.2. Add your tags in the `Tags` field of paper details. Please, remember to write the tag in square brackets e.g. `[mytag]`

	3.3. Add your notes in the `Notes` tab 

Wiki admins will periodically export the bibtex to keep the list updated. In case we forgot, join the [ContinualAI Slack](https://continualai.herokuapp.com/) and complain about our behavior in the `#wiki` channel.

#### Advices to add new papers in Mendeley

* Check if the paper already exist by using the `Citation Key` or the title in Mendeley search bar.

* Don't forget to add the publication venue (Journal, Proceedings...). Use `Journal = arXiv` if the paper is a preprint.

* CLAI Wiki uses a system based on categories. This can sometimes be limiting. In general, please consider to add the paper in the category which you consider the most relevant one. You can add the paper in at most **2** categories, if you believe that both are equally relevant.

* Please, do not add new tags if a similar category already exists.

----------------------------

## Contribute to the wiki
Adding new papers is not the only way for you to contribute. If you want to include your company in the wiki, add a CL workshop or other information you can submit Pull Requests!

1. [Fork the repo](https://help.github.com/articles/fork-a-repo/) and clone it locally.

2. Enter `wiki` folder

3. Install `sphinx`:  
`pip install sphinx`  
`pip install sphinx_rtd_theme`

4. Make your changes to the *.rst files

5. Build the html with the command:  
`make html`

6. open `_build/html/index.html` with your browser to check if everything is correct.

7. Make a Pull Request (with only the *.rst files), Travis CI will take care of the build!

## About ContinualAI

**[ContinualAI](https://continualai.org)** is an open research community on the topic of Continual Learning and AI!
We are a community of CL researchers and enthusiasts! Join us today **[on slack](https://continualai.herokuapp.com)**!
