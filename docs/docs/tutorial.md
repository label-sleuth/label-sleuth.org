# Tutorial

New to Label Sleuth? We suggest following this quick tutorial to try it out. In this tutorial, you will use Label Sleuth to create a model that identifies sentences describing animal habitats in the sample dataset from Wikipedia.    

:::{note}
Before proceeding, make sure that you have already installed Label Sleuth, following our [installation instructions](installation.md).
:::

## Steps

### (1) Start Label Sleuth

If Label Sleuth is not already running (or you have not instructed it to load the sample dataset at startup), invoke it with the following command:

```
python -m label_sleuth.start_label_sleuth --load_sample_corpus wiki_animals_2000_pages
```

This starts the system and pre-loads a set of Wikipedia documents to use in the rest of the tutorial.

Once started, access Label Sleuth on your browser by navigating to the following page:

[http://localhost:8000/](http://localhost:8000/)


### (2) Create new workspace

::::{grid} 2
:padding: 4
:reverse:

:::{grid-item} 
:columns: 12 6 6 6
:margin: 0 4 0 0
```{image} ../_static/images/tutorial/create_workspace.png
   :alt: Create workspace screenshot
   :width: 250px
   :align: center
```
:::

:::{grid-item}
:columns: 12 6 6 6
Start by creating a new workspace. A workspace can be thought of as a project, which bundles different target categories for classification.

_**How:** To create a workspace, enter your preferred name and select the pre-loaded `wiki_animals_2000_pages` dataset._
:::

::::

### (3) Create new category

::::{grid} 2
:padding: 4
:reverse:

:::{grid-item} 
:columns: 12 6 6 6
:margin: 0 4 0 0
```{image} ../_static/images/tutorial/create_category.png
   :alt: Create category screenshot
   :width: 250px
   :align: center
```
:::

:::{grid-item}
:columns: 12 6 6 6
Within the new workspace, create a new category for classification. A category corresponds to the aspect that you want to identify in your dataset. For example, create a `Habitat` category to identify sentences describing the habitat of an animal.

_**How:** To create a category, click the `+` icon at the top of the screen. In the resulting dialog box enter the category name._
:::

::::

### (4) Start annotating

You are now ready to start annotating sentences as positive or negative w.r.t. the category you have created. For example, the following sentence is a positive example for the Habitat category:

```text
The Komodo dragon is endemic to the Indonesian islands of Komodo, Rinca, Flores, and Gili Motang
```

Focus more on annotating _positive_ examples (i.e., sentences that describe the habitat), as they are much more valuable for the AI model. There are initially two ways to identify elements to annotate:

#### a. Annotate by skimming documents

::::{grid} 2
:padding: 4
:reverse:

:::{grid-item} 
:columns: 12 6 6 6
:margin: 0 4 0 0
```{image} ../_static/images/tutorial/annotate_element.png
   :alt: Annotate element screenshot
   :width: 250px
   :align: center
```
:::

:::{grid-item}
:columns: 12 6 6 6

Skim the shown document in search of positive examples. If you find one, annotate it accordingly. If not, do not worry; we will next describe an easier way to discover positive examples.

_**How:** To annotate a sentence as positive, hover over it and click on the &#10003; icon. For negative examples, click on the ***x*** icon._
:::

::::

#### b. Search for positive examples

::::{grid} 2
:padding: 4
:reverse:

:::{grid-item} 
:columns: 12 6 6 6
:margin: 0 4 0 0
```{image} ../_static/images/tutorial/search_elements.png
   :alt: Search for positive elements screenshot
   :width: 250px
   :align: center
```
:::

:::{grid-item}
:columns: 12 6 6 6

A faster way to find positive examples is to search for terms that they contain. For example, for the Habitat category you can search for `lives in` or `is found in`. Look through the search results and annotate examples as positive or negative.

_**How:** If not already shown, bring up the search panel by clicking on the magnifying glass icon on the right. Enter search terms and annotate sentences in the search results as usual._
:::

::::

### (5) Continue annotating

::::{grid} 2
:padding: 4
:reverse:

:::{grid-item} 
:columns: 12 6 6 6
:margin: 0 4 0 0
```{image} ../_static/images/tutorial/progress_bar.png
   :alt: Annotation progress bar
   :width: 250px
   :align: center
```
:::

:::{grid-item}
:columns: 12 6 6 6

Initially, there is no AI model yet. Keep annotating until Label Sleuth prepares a first version of the model for you. The progress bar on the left shows how many annotations are missing until Label Sleuth starts training a model. A confetti animation will notify you when a first version of the model is ready.

_**How:** Keep annotating as usual. Check the progress bar on the left for annotation progress and wait for the confetti animation before proceeding._
:::

::::

### (6) Receive annotation guidance

::::{grid} 2
:padding: 4
:reverse:

:::{grid-item} 
:columns: 12 6 6 6
:margin: 0 4 0 0
```{image} ../_static/images/tutorial/label_next.png
   :alt: Label Next screenshot
   :width: 250px
   :align: center
```
:::

:::{grid-item}
:columns: 12 6 6 6

Once the first version of the AI model is ready, Label Sleuth will start guiding you by recommending which sentences to annotate next. Annotating the recommended sentences will improve the AI model the most.

_**How:** If not shown, bring up the recommendation panel by clicking on the `Label Next` button on the right. Annotate elements as usual._ 
:::

::::

### (7) Check the AI model's predictions

::::{grid} 2
:padding: 4
:reverse:

:::{grid-item} 
:columns: 12 6 6 6
:margin: 0 4 0 0
```{image} ../_static/images/tutorial/model_predictions.png
   :alt: Model predictions screenshot
   :width: 250px
   :align: center
```
:::

:::{grid-item}
:columns: 12 6 6 6

Sentences with a dotted blue outline are sentences that the AI model predicts to be positive. You can annotate some of them to provide the AI model with feedback on where it is correct and where it is wrong.

_**How:** If not shown, bring up the list of all positive predictions of the AI model by clicking on the `Positive predictions` button on the right. Alternatively, look for the blue outline in all other places where elements are shown (document, search, and label next panels)._ 
:::

::::

### (8) Keep going

Keep annotating. Occasionally, a new version of the AI model is created to provide better guidance of next elements to annotate and to better identify positive sentences.
Spend 30 mins with Label Sleuth. Does the AI model get better in finding positive sentences for your target category?


### (9) Great job!

You have mastered the basics of Label Sleuth! You are now ready to use it to create classification models for your own use cases.
