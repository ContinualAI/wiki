# ContinualAI Wiki: a collaborative wiki on Continual/Lifelong Machine Learning
<div style="text-align:center">
	<img src="https://www.continualai.org/images/continualai_logo_name_black.png" width="160" height="100">
</div>

The aim of the project is to create an open-source, collaborative wiki to provide a starting point for researchers, developers and AI enthusiasts who share an interest in Continual Learning and are willing to learn more or contribute to this field. Join us now and help us improving it and keeping it up to date! :D

---------------------------------------------------

### How to contribute to the wiki

1. Star the project :-)

2. Join our community on Slack: https://continualai.herokuapp.com/

3. [Fork the repo on GitHub and clone it locally](https://help.github.com/articles/fork-a-repo/)

4. Enter the folder: 

	`cd wiki`

5. If you don't have sphinx installed run (make sure you're using Python 2.7):

	`pip install sphinx`\
	`pip install sphinx_rtd_theme`

6. Make your changes to the \*.rst files

7. Build the html with the command:

	`make html`

8. open you browser and check if everything is correct:

	`firefox _build/html/index.html`

9. Make a Pull Request (with only the \*.rst files), Travis CI will take care of the build! :D

#### How to contribute to the ContinualAI database of publications

ContinualAI maintain an updated [list of publications](https://wiki.continualai.org/research.html) on Continual Learning. 
You can give your contribution by **adding new papers** or by helping **annotating the existing ones**.

How? With few, simple steps!

1. Join our [Mendeley group](https://www.mendeley.com/community/continual-learning-papers/)

2. To **add a new paper**

	2.1. Add it to the group collection in the folder which best represents the paper contribution. You can add the paper from your library or directly from the paper webpage through the Mendeley plugin. 

	2.2 Through the Mendeley Desktop app, fill in the `Citation Key` field in the paper details. This must be in the form `[lastname][year][a]` (e.g. `smith2019a`) where `a` has to be replaced with the first available letter in order to make the citation unique. You can look for for existing Citation Keys through the Mendeley search bar.
	*If you can't find the `Citation Key` field, enable it in `Tools -> Options -> Document Details` menu.*

	2.3. Go to step 3.

3. To **annotate** an existing paper

	3.1. Check the list of existing tags in this [shared document](https://docs.google.com/spreadsheets/d/16jXX51HJ1dk0iTrKTPtZQND3jvQU0IjeVV6r2sQRul4/edit?usp=sharing). If you use a new tag, please add it in there.

	3.2. Add the appropriate tags in the `Tags` field of paper details.

	3.3. Add your notes in the `Notes` tab 

Wiki admins will periodically export the bibtex to keep the list updated. In case we forgot, join the [ContinualAI Slack](https://continualai.herokuapp.com/) and complain about our behavior in the `#wiki` channel :) 

----------------------------

### About ContinualAI

**[ContinualAI](https://continualai.org)** is an open research community on the topic of Continual Learning and AI! :-)
We are a community of CL researchers and enthusiasts! Join us today **[on slack](https://continualai.herokuapp.com)**! :D
