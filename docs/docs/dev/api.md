---
layout: home
title: API 
---

<style>
.request_type {
   background-color: black;
   color: white;
   padding-left: 10px;
   padding-right: 10px;
   padding-top: 2px;
   padding-bottom: 2px;
   border-radius: 10px;
   margin-right: 12px;
}

span.pre {
   white-space: pre-wrap;
}
</style>

# REST API

This page describes the REST API that the system's frontend uses to communicate with the backend.

:::{note}
All requests should also pass an authorization header with the Bearer token returned by the  [login endpoint](#login).
:::

## User Management

Endpoints related to users.

### Login

Authenticate user into the system. The Bearer token returned from this call should be passed in the authorization header of all other endpoints. 

---

<span class="request_type">POST</span> ```/users/authenticate```

---

**Example request:**

```json
{
   "username": "admin",
   "password": "mypassword"
}
```

**Example response:**


```json
{
    "token": "AGEVuQJsVLCE7AsYBdQerDMopApb7iTZBLGELh6X9WAH23mvgXz",
    "username": "my_username"
}
```

## Dataset Management

Endpoints related to datasets. Note that datasets can be shared between workspaces. Therefore, the following endpoints are not in the context of a particular workspace.

### Add documents

Upload a csv file, and add its contents as a collection of documents in the dataset `dataset_name`.
If `dataset_name` does not already exist, it is created here. If it does exist, the process of adding documents also
includes updating labels and model predictions for all workspaces that use this dataset.

The uploaded csv file must adhere to the following format: It should include a 'text' column, and may optionally include a 'doc_id' column as well as metadata columns starting with the 'metadata_' prefix.

---

<span class="request_type">POST</span> ```/datasets/<dataset_name>/add_documents```

---

**Example request:**

```
Stream of a csv file
```

**Example response:**


```
{
    "dataset_name": "new_dataset_name",
    "num_docs": 2000,
    "num_sentences": 86944,
    "workspaces_to_update": []
}
```

### Get list of datasets

Get IDs of all existing datasets.

---

<span class="request_type">GET</span> ```/datasets```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "datasets": [
      {
         "dataset_id": "dataset1 "
      },
      {
         "dataset_id": "dataset2"
      }
   ]
}
```

## Workspace Management

Endpoints related to workspace. Note that each workspace is associated with a particular dataset at creation time.

### Create workspace

Create new workspace. The request should include the ID of the new workspace and the ID of the dataset that will be used to populate the workspace.

---

<span class="request_type">POST</span> ```/workspace```

---

**Example request:**

```json
{
   "workspace_id": "my_workspace",
   "dataset_id": "my_dataset"
}
```

**Example response:**


```json
{
   "workspace": {
      "dataset_name": "my_dataset",
      "first_document_id": "my_dataset-1",
      "workspace_id": "my_workspace"
   }
}
```

### Delete workspace

Delete workspace with specified ID.

:::{warning}
This endpoint permanently deletes the workspace along with all data associated with it, including categories, user labels, and models. The deletion _cannot_ be reversed.
:::

---

<span class="request_type">DELETE</span> ```/workspace/<workspace_id>```

---

**Example request:**

```
Empty
```

**Example response:**


```
{"workspace_id": "my_workspace"}
```


### Get list of workspaces

Get IDs of all existing workspaces.

---

<span class="request_type">GET</span> ```/workspaces```

---

**Example request:**

```
Empty
```

**Example response:**


```json
{   
   "workspaces": [
      "workspace1",
      "workspace2"
   ]
}
```


### Get workspace info

Get information for selected workspace.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "workspace": {
      "dataset_name": "my_dataset",
      "document_ids": [
         "my_dataset-0",
         "my_dataset-1"
      ],
      "first_document_id": "my_datset-0",
      "workspace_id": "my_workspace"
   }
}
```


## Category Management

Endpoints related to categories. A category is defined in the context of a particular workspace. As a user works on the system, all labels, classification models etc. are associated with a specific category.

### Create category

Create new category within a specified workspace. The request should include the name and the description of the new category.

---

<span class="request_type">POST</span> ```/workspace/<workspace_id>/category```

---

**Example request:**

```json
{
   "category_name": "my_category",
   "category_description": "my_description"
}
```

**Example response:**

```json
{
   "category_description": "my_description",
   "category_name": "my_category",
   "category_id": "0"
}
```

### Delete category

Delete category with specified name.

:::{warning}
This endpoint permanently deletes the category along with all data associated with it, including user labels and models. The deletion _cannot_ be reversed.
:::

---

<span class="request_type">DELETE</span> ```/workspace/<workspace_id>/category/<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "workspace_id": "my_workspace",
   "category_id": "0"
}
```

### Get list of categories

Get all categories that exist in the selected workspace.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/categories```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "categories": [
      {
         "category_description": "",
         "category_name": "category1",
         "category_id": "0"
      },
      {
         "category_description": "",
         "category_name": "category2",
         "category_id": "1"
      }
   ]
}
```

## Label Management

Endpoints related to user-provided labels.

### Set element label

Update the label of a selected element. This endpoint either sets or removes the label for a given element, depending on the `value` field. If `value == 'none'`, the element's label will be removed. Otherwise, the element will be assigned a bolean label depending on the string value ("true" -> True and "false" -> False. The `update_counter` determines whether the label changes will be reflected in the label change counters of the selected category (which may trigger the training of a new model). The parameter should be set to True, except for when labeling elements for precision evaluation.

---

<span class="request_type">PUT</span> ```/workspace/<workspace_id>/element/<element_id>?category_id=<category_id>```

---

**Example request:**

```json
{
   "category_id": "1",
   "value": "true",
   "update_counter": true
}
```

**Example response:**

```json
{
   "category_id": "1",
   "element": {
      "begin": 866,
      "docid": "isear_dev-0",
      "end": 1002,
      "id": "isear_dev-0-7",
      "model_predictions": {
         "1": "false"
      },
      "text": "When I got home I found that the electrical supply had been disconnected despite my having paid ZESCO the full bill a few  days earlier.",
      "user_labels": {
         "1": "true"
      }
   },
   "workspace_id": "another_ws"
}
```

### Get positive labeled elements

Get all elements for selected category that have been assigned a positive label by the user.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/positive_elements?category_id=<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "positive_elements": [
      {
         "begin": 367,
         "docid": "isear_dev-0",
         "end": 473,
         "id": "isear_dev-0-3",
         "model_predictions": {
            "1": "true"
         },
         "text": "When I realized that I had been wrong about a person close to me, because of pre-set ideas and prejudices.",
         "user_labels": {
            "1": "true",
            "2": "false"
         }
      },
      {
         "begin": 603,
         "docid": "isear_dev-0",
         "end": 803,
         "id": "isear_dev-0-5",
         "model_predictions": {
            "1": "true"
         },
         "text": "I feared that I would not be able to hand in the book-report on time as I had started working very late.  The book was difficult to read and my teacher did not accept my work as it was handed in late.",
         "user_labels": {
            "1": "true",
            "2": "true"
         }
      }
  ]
}
```

### Import labels

Upload a csv file and add its contents as user labels in the selected workspace. The input file may contain labels for more than one category.

The uploaded csv file must adhere to the following format: It must include 'text', 'category_name' and 'label' columns, and may optionally include a 'document_id' column.
If document IDs are provided AND `app.config["CONFIGURATION"].apply_labels_to_duplicate_texts` is False, these labels will be assigned only to elements in the specified documents. Otherwise, labels are assigned to all elements matching the given texts.

---

<span class="request_type">POST</span> ```/workspace/<workspace_id>/import_labels```

---

**Example request:**

```
Stream of a csv file
```

**Example response:**

```
{
    "categories": [
        {
            "category_id": "3",
            "counter": 30
        }
    ],
    "categoriesCreated": [],
    "linesSkipped": [],
    "total": 30
}
```

### Export labels

Download all user labels from the selected workspace as a csv file. Each row in the csv is a label for a specific element for a specific category.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/export_labels```

---

**Example request:**

```
Empty
```

**Example response:**

```
Stream of a csv file
```


## Document \& Element Management

Endpoints related to documents and elements. These endpoints are called in the contect of a particular workspace and optionally a category. Thus, they may return not just document and element information from the dataset, but also category labels, model predictions etc. that are associated with a particular document/element.

### Get document URIs

Get IDs of all documents in the dataset associated with the selected workspace.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/documents```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "documents": [
      {
         "document_id": "wiki_animals_train-1 Unicorn"
      },
      {
         "document_id": "wiki_animals_train-2 Unicorn"
      }
  ]
}
```

### Get document elements

Get all elements in selected document. Note: The `category_id` is optional.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/document/<document_id>?category_id=<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "elements": [
      {
         "begin": 0,
         "docid": "isear_dev-3 Unicorn",
         "end": 37,
         "id": "isear_dev-3 Unicorn-0",
         "model_predictions": {
            "1": "true"
         },
         "text": "Startups worth more than 1b unicorn3 ",
         "user_labels": {
            "1": "true"
         }
      },
      {
         "begin": 38,
         "docid": "isear_dev-3 Unicorn",
         "end": 67,
         "id": "isear_dev-3 Unicorn-1",
         "model_predictions": {
            "1": "true"
         },
         "text": "another sentence of unicorn3 ",
         "user_labels": {
            "1": "true"
         }
      }
   ]
}
```

### Get document positive predictions

Get elements in the selected document that received a positive prediction from the relevant classification model (i.e., the latest trained model for the category specified in the request). The following optional parameters may be provided as part of the request: The index number `size` of elements to return and the index `start_idx` starting from which elements will be returned (used for pagination). If not provided, the following default values are used: `start_idx = 0` and `size = 100`.


---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/document/<document_id>/positive_predictions?category_id=<category_id>&start_idx=<start_index>&size=<max_results>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "elements": [
      {
         "begin": 0,
         "docid": "isear_dev-3 Unicorn",
         "end": 37,
         "id": "isear_dev-3 Unicorn-0",
         "model_predictions": {
                "1": "true"
         },
         "text": "Startups worth more than 1b unicorn3 ",
         "user_labels": {
            "1": "true"
         }
      },
      {
         "begin": 38,
         "docid": "isear_dev-3 Unicorn",
         "end": 67,
         "id": "isear_dev-3 Unicorn-1",
         "model_predictions": {
            "1": "true"
         },
         "text": "another sentence of unicorn3 ",
         "user_labels": {
            "1": "true"
         }
      }
   ]
}
```

### Get workspace positive predictions

Get elements in the selected workspace that received a positive prediction from the relevant classification model (i.e., the latest trained model for the category specified in the request). The following optional parameters may be provided as part of the request: The index number `size` of elements to return and the index `start_idx` starting from which elements will be returned (used for pagination). If not provided, the following default values are used: `start_idx = 0` and `size = 100`.
The response contains the total number of positive predictions in `hit_count` and the fraction of the positively predicted elements in the entire dataset in `positive_fraction`


---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/positive_predictions?category_id=<category_id>&start_idx=<start_index>&size=<max_results>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "elements":[
      {
         "begin":0,
         "docid":"wiki_new-2011 Svalbard polar bear attack",
         "end":31,
         "id":"wiki_new-2011 Svalbard polar bear attack-0",
         "model_predictions":{
            "0":"true"
         },
         "text":"2011 Svalbard polar bear attack",
         "user_labels":{
            "0":"true"
         }
      },
      {
         "begin":32,
         "docid":"wiki_new-2011 Svalbard polar bear attack",
         "end":167,
         "id":"wiki_new-2011 Svalbard polar bear attack-1",
         "model_predictions":{
            "0":"true"
         },
         "text":"The 2011 Svalbard polar bear attack was an attack by a presumed starving polar bear on a group of university students and their guides.",
         "user_labels":{
            "0":"true"
         }
      }
   ],
   "hit_count":54405,
   "positive_fraction":0.16464211787776445
}
```

### Query elements

Get elements matching a regular expression. The following parameters must be provided as part of the request: The query string `qry_string` containing the regular expression to search for, the number `qry_size` of elements to return, and the index `sample_start_idx` starting from which elements will be returned (used for pagination).

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/query?qry_string=<my_query>&category_id=<category_id>&sample_start_idx=<sample_start_index>&qry_size=<query_size>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "hit_count": 4,
   "hit_count_unique": 4,
   "elements": [
      {
         "begin": 474,
         "docid": "isear_dev-0",
         "end": 602,
         "id": "isear_dev-0-4",
         "model_predictions": {},
         "text": "The sadness came to me when I heard that my girlfriend whom I loved so much got married to another man before a rebuff from her.",
         "user_labels": {
         "2": "true"
      }
      },
      {
         "begin": 28094,
         "docid": "isear_dev-0",
         "end": 28158,
         "id": "isear_dev-0-235",
         "model_predictions": {},
         "text": "Sadness, no, I felt something much stronger when my father died.",
         "user_labels": {}
      }
   ] 
}
```

## Models \& Active Learning

Endpoints related to models and active learning. 

### Get labeling status

Get information about the labeling status for the selected category. The endpoint returns the number of user labels for the category, as well as a number between 0-100 that reflects when a new model will be trained.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/status?category_id=<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "labeling_counts": {
      "false": 2,
      "true": 15
   },
   "notifications": [],
   "progress": {
      "all": 60
   }
}
```

### Get all models for category

Get information about all the iteration flows for the selected category and their current status.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/models?category_id=<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "models": [
      {
         "active_learning_status": "READY",
         "creation_epoch": 1643109517.890951,
         "iteration": 6,
         "model_id": "8ae60534-7dd0-11ec-a0a3-a648083b7a24,8ae6bfec-7dd0-11ec-a0a3-a648083b7a24",
         "model_metadata": {
            "category_id": "1",
            "changed_fraction": 0.0625,
            "positive_fraction": 0.22005208333333334,
            "train_counts": {
               "false": 4,
               "true": 95,
               "weak_false": 186
            }
         },
         "model_status": "READY",
         "model_type": "SVM_ENSEMBLE"
      },
      {
         "active_learning_status": "READY",
         "creation_epoch": 1643109617.141633,
         "iteration": 7,
         "model_id": "c60c997a-7dd0-11ec-a09b-a648083b7a24,c60f424c-7dd0-11ec-a09b-a648083b7a24",
         "model_metadata": {
            "category_id": "1",
            "changed_fraction": 0.036458333333333336,
            "positive_fraction": 0.21744791666666666,
            "train_counts": {
               "false": 4,
               "true": 112,
               "weak_false": 220
            }
         },
         "model_status": "READY",
         "model_type": " SVM_ENSEMBLE"
      }
   ]
}
```

### Get elements to label

Get elements to label. If at least one Iteration has completed for the selected category, the endpoint returns a list of elements that the active learning module recommends that the user labels next. The following optional parameters may be provided as part of the request: The index number `size` of elements to return and the index `start_idx` starting from which elements will be returned (used for pagination). If not provided, the following default values are used: `start_idx = 0` and `size = 100`.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/active_learning?category_id=<category_id>&start_idx=<start_index>&size=<max_results>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "elements": [
      {
         "begin": 44784,
         "docid": "isear_dev-0",
         "end": 44857,
         "id": "isear_dev-0-387",
         "model_predictions": {
            "0": "false"
         },
         "text": "When I heard that my step-mother had treated my mother in a wrong manner.",
         "user_labels": {}
      },
      {
         "begin": 75744,
         "docid": "isear_dev-0",
         "end": 75761,
         "id": "isear_dev-0-668",
         "model_predictions": {
            "0": "false"
         },
         "text": "During a meeting.",
         "user_labels": {}
      }
   ]
}
```

### Force train for category

Manually trigger a new iteration flow.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/force_train?category_id=<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```
{
    "labeling_counts": {
        "false": 1485,
        "true": 542
    },
    "model_id": "SVM_BOW_1c7ff1f6-fdf8-11ec-8a70-acde48001122,SVM_GloVe_1c8044da-fdf8-11ec-8a70-acde48001122"
}
```

### Export predictions

Download the predictions of the model learned during iteration `iteration_index` for category `category_id`, as a csv file.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/export_predictions?category_id=<category_id>&iteration_index=<iteration_index>```

---

**Example request:**

```
Empty
```

**Example response:**

```
{
    "labeling_counts": {
        "false": 1485,
        "true": 542
    },
    "model_id": "SVM_BOW_1c7ff1f6-fdf8-11ec-8a70-acde48001122,SVM_GloVe_1c8044da-fdf8-11ec-8a70-acde48001122"
}
```


### Export model

Download the trained model files for the given category and iteration index. If the iteration is not provided, the model from the latest iteration is exported. In order for this to work, the ModelType curently in use must implement the ModelAPI.export_model() method.  

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/export_model?category_id=<category_id>&iteration_index=<iteration_number>```

---

**Example request:**

```
Empty
```

**Example response:**

```
Stream of ZIP file
```

## Model Evaluation

Endpoints related to evaluation of a model.

### Get elements for precision evaluation

Get a sample of elements that are predicted as positive for the category by the latest model. This sample can be
used to evaluate the precision of the model predictions: the user should label this sample of elements. After they are labeled, an invocation of the run precision evaluation endpoint will compare the user-provided labels to the model predictions to estimate the precision of the latest model.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/evaluation_elements?category_id=<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "elements": [
      {
         "begin": 53760,
         "docid": "isear_dev-0",
         "end": 53797,
         "id": "isear_dev-0-471",
         "model_predictions": {
            "1": "true"
         },
         "text": "Boyfriend \"chatting up\" another girl.",
         "user_labels": {}
      },
      {
         "begin": 30939,
         "docid": "isear_dev-0",
         "end": 31101,
         "id": "isear_dev-0-260",
         "model_predictions": {
            "1": "true"
         },
         "text": "My elder brother had been expelled from college and he was so frustated that he attempted suicide - he drank bottle fragments.  I was very sad when I learnt this.",
         "user_labels": {}
      }
   ]
}
```

### Run precision evaluation

Run precision evaluation.

---

<span class="request_type">POST</span> ```/workspace/<workspace_id>/estimate_precision?category_id=<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```
{
    "score": 0.98
}
```

## Label Quality Reports

Endpoints related to label quality reports. These endpoints return labeled elements that may contain potential errors in their labels.

### Get label and model disagreements

Get all labeled elements where the predictions of the latest model for the category differ from the label provided by the user.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/disagree_elements?category_id=<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "disagree_elements": [
      {
         "begin": 36842,
         "docid": "isear_dev-0",
         "end": 37012,
         "id": "isear_dev-0-309",
         "model_predictions": {
            "2": "false"
         },
         "text": "I had wasted some time instead of doing something I needed to do to give to a friend. (Also in the time I wasted I had done some things I did not consider morally right).",
         "user_labels": {
            "2": "true"
         }
      },
      {
         "begin": 37013,
         "docid": "isear_dev-0",
         "end": 37338,
         "id": "isear_dev-0-310",
         "model_predictions": {
            "2": "false"
         },
         "text": "A friend of mine had said something about not liking to come to my place just before coming to my place.   In the meanwhile I got to learn about this from another friend of mine and when she arrived at my place I really treated her badly.  I was later ashamed of the way I had treated someone when the person was at my place.",
         "user_labels": {
            "2": "true"
         }
      }
   ]
}
```

### Get suspicious elements

Get elements where the user label might be incorrect, based on an analysis of all elements labeled so far. Elements are ordered from most to least "suspicious" according to the analysis.

The current implementation relies on cross validation: Several models are trained on different parts of the labeled data; labels are suspected as incorrect if a model's prediction on a left-out element disagrees with the user label for that element.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/suspicious_elements?category_id=<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "elements": [
      {
         "begin": 603,
         "docid": "isear_dev-0",
         "end": 803,
         "id": "isear_dev-0-5",
         "model_predictions": {
            "123": "true"
         },
         "text": "I feared that I would not be able to hand in the book-report on time as I had started working very late.  The book was difficult to read and my teacher did not accept my work as it was handed in late.",
         "user_labels": {
            "1": "true",
            "123": "true"
         }
      },
      {
         "begin": 0,
         "docid": "isear_dev-0",
         "end": 150,
         "id": "isear_dev-0-0",
         "model_predictions": {
            "123": "true"
         },
         "text": "I was angry when my friends said that I should not receive Nursing Science books because there was a rumour that I was intending to leave the college.",
         "user_labels": {
            "123": "true"
         }
      }
   ]
}
```


### Get contradicting elements

Get pairs of labeled elements that may be inconsistent with each other. Each pair consists of an
element given a positive label and an element given a negative label by the user; since the two elements are similar to each other, there is a possibility that one of the labels is incorrect. Pairs are sorted from most to least similar to each other.

The current implementation relies on distances between text embeddings to identify the opposite-label elements that are similar to each other. In addition, for each pair the endpoint returns a list of unique tokens for each element, i.e. tokens that do not appear in the other element in the pair. This can be used to visualize the similarities/differences between the two texts.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/contradiction_elements?category_id=<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "pairs": [
      [
         {
            "begin": 71054,
            "docid": "isear_dev-0",
            "end": 71071,
            "id": "isear_dev-0-625",
            "model_predictions": {
               "1": "true"
            },
            "text": "When I fell down.",
            "user_labels": {
               "1": "true"
            }
         },
         {
            "begin": 45472,
            "docid": "isear_dev-0",
            "end": 45580,
            "id": "isear_dev-0-395",
            "model_predictions": {
               "1": "false"
            },
            "text": "I was looking after my cousin's little daughter; she fell down, was slightly injured and cried vociferously.",
            "user_labels": {
               "1": "false"
            }
         }
      ]
    ]
}
```

## Additional Analyses

### Get labeled elements enriched tokens

Get tokens and bigrams that are characteristic of positively labeled elements versus negatively labeled
elements for the selected category, along with weights indicating the relative significance of each token/bigram. These can be used to visualize the characteristic vocabulary of the category, e.g. using a word cloud. The current implementation relies on calculating the Mutual Information between the ngrams and the user labels.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/labeled_info_gain?category_id=<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "info_gain": [
      {
         "text": "done",
         "weight": 15.161635078058437
      },
      {
         "text": "well",
         "weight": 15.161635078058437
      },
      {
         "text": "angry",
         "weight": 6.497295321059118
      },
      {
         "text": "person",
         "weight": 6.497295321059118
      }
   ]
}
```

### Get predictions enriched tokens

Get tokens and bigrams that are characteristic of positively predicted elements versus negatively predicted
elements by the latest model for the selected category, along with weights indicating the relative significance of each token/bigram. These can be used to visualize the characteristic vocabulary of the model predictions, e.g. using a word cloud. The current implementation relies on calculating the Mutual Information between the ngrams and the model predictions.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/predictions_info_gain?category_id=<category_id>```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "info_gain": [
      {
         "text": "done",
         "weight": 15.161635078058437
      },
      {
         "text": "well",
         "weight": 15.161635078058437
      },
      {
         "text": "angry",
         "weight": 6.497295321059118
      },
      {
         "text": "person",
         "weight": 6.497295321059118
      }
   ]
}
```
