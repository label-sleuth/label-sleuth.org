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
If in the [configuration file](configuration.md) `login_required` is set to true, all requests should also pass an authorization header with the Bearer token returned by the  [login endpoint](#login).
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

The uploaded csv file must adhere to the following format: It should include a 'text' column, and may optionally include a 'document_id' column as well as metadata columns starting with the 'metadata_' prefix.

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

### Delete dataset

Delete dataset with specified name.

:::{warning}
This endpoint permanently deletes the given dataset. If the dataset is used by one or more workspaces, those will be deleted too, along with all the categories, user labels and models. The deletion _cannot_ be reversed.
:::

---

<span class="request_type">DELETE</span> ```/datasets/<dataset_name>```

---

**Example request:**

```
Empty
```

**Example response:**


```json
{
   "deleted_dataset": "my_dataset", 
   "deleted_workspace_ids": ["my_workspace1", "my_workspace2"]
}
```

### Get list of workspaces using dataset

Get IDs of all the workspaces that use the given dataset.

---

<span class="request_type">GET</span> ```/datasets/<dataset_name>/used_by```

---

**Example request:**

```
Empty
```

**Example response:**

```json
{
   "used_by": ["my_workspace1", "my_workspace2"]
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

Create new workspace. The request should include the name of the new workspace, the ID of the dataset that will be used to populate the workspace, and the mode of the workspace (`Binary` or `MultiClass`).

---

<span class="request_type">POST</span> ```/workspace```

---

**Example request:**

```json
{
   "workspace_id": "my_workspace",
   "dataset_id": "my_dataset",
   "workspace_type": "Binary"
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

```text
Empty
```

**Example response:**

```json
{   
   "workspaces": [
      {
            "id": "workspace1",
            "mode": "Binary"
      },
      {
         "id": "workspace2",
         "mode": "MultiClass"
      }
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

Endpoints related to categories. A category is defined in the context of a particular workspace.

### Create category

Create new category within a specified workspace. The request body should include the name, the description and the color (_only for multiclass workspaces_) of the new category. As part of the response, the backend will return the id of the created category.

_Note: the backend expects a color to be provided as a string. The available colors are managed by the frontend and can be found [here](https://github.com/label-sleuth/label-sleuth/blob/2bb13a44d025a9f2583003e3d9552faa6fce47f7/frontend/src/utils/utils.ts#L430)._

---

<span class="request_type">POST</span> ```/workspace/<workspace_id>/category```

---
::::{tab-set}
:::{tab-item} Binary mode
**Example request:**

```json
{
   "category_name": "my_category",
   "category_description": "my_description",
}
```

**Example response:**

```json
{
   "category_description": "my_description",
   "category_name": "my_category",
   "category_id": "0",
}
```

:::
:::{tab-item} Multiclass mode
**Example request:**

```json
{
   "category_name": "my_category",
   "category_description": "my_description",
   "category_color": "green"
}
```

**Example response:**

```json
{
   "category_description": "my_description",
   "category_name": "my_category",
   "category_id": "0",
   "category_color": "green"
}
```

:::
::::

### Delete category

Delete category with specified name.

:::{warning}
This endpoint permanently deletes the category along with all data associated with it, including user labels and models (_if it belongs to a binary workspace_). The deletion _cannot_ be reversed.
:::

If the category belongs to a multiclass workspace, until a new model is trained the model predictions for the deleted category will still be displayed with the string `(deleted)` appended to its name.

---

<span class="request_type">DELETE</span> ```/workspace/<workspace_id>/category/<category_id>```

---

**Example request:**

```text
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

Get all categories that exist in the selected workspace. In multiclass workspaces, the reponse list items have two additional attributes: `category_color` and `deleted`.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/categories```

---

::::{tab-set}
:::{tab-item} Binary mode

**Example request:**

```text
Empty
```

**Example response:**

```json
{
   "categories": [
      {
         "category_description": "",
         "category_name": "category1",
         "category_id": "0",
      },
      {
         "category_description": "",
         "category_name": "category2",
         "category_id": "1",
      }
   ]
}
```

:::

:::{tab-item} Multiclass mode

**Example request:**

```text
Empty
```

**Example response:**

```json
{
   "categories": [
      {
         "category_description": "",
         "category_name": "category1",
         "category_id": "0",
         "color": "amber",
         "deleted": true,
      },
      {
         "category_description": "",
         "category_name": "category2",
         "category_id": "1",
         "color": "amber",
         "deleted": false,
      }
   ]
}
```

:::
::::

## Label Management

Endpoints related to user-provided labels.

### Set element label

Update the label of a selected element. This endpoint either sets or removes the label for a given element.

- In binary workspaces, the `binary_label` is set to the `category_id`. If `binary_label == 'none'`, the element's label will be removed. Otherwise, the element will be assigned a boolean label depending on the string value ("true" -> True and "false" -> False).
- In multiclass workspaces, the category to label is the one specified in the `category_id` parameter. If `category_id == 'none'`, the element's label will be removed.

The `update_counter` determines whether the label changes will be reflected in the label change counters of the selected category (which may trigger the training of a new model). The parameter should be set to True, except for when labeling elements for evaluation. `iteration` refers to the model's version, while `source` is the panel where the element was labeled ([see available sources](https://github.com/label-sleuth/label-sleuth/blob/9561c9e7131da07c1978294a3633d42ac7eab473/frontend/src/const.ts#L115)).  

<span class="request_type">PUT</span> ```/workspace/<workspace_id>/element/<element_id>?category_id=<category_id>&mode=<mode>```

::::{tab-set}
:::{tab-item} Binary mode

**Example request:**

```json
{
   "category_id": "1",
   "binary_label": "true",
   "update_counter": true,
   "iteration": 0,
   "source": "label_next"
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

:::
:::{tab-item} Multiclass mode

**Example request:**

```json
{
   "category_id": "1",
   "update_counter": true,
   "iteration": 0,
   "source": "label_next"
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
      "model_predictions": 1,
      "text": "When I got home I found that the electrical supply had been disconnected despite my having paid ZESCO the full bill a few  days earlier.",
      "user_labels": 1
   },
   "workspace_id": "another_ws"
}
```

:::
::::

### Get labeled elements by value

Get user labeled elements. The `value` indicates the label type, which is `true` or `false` in binary workspaces and a category id in multiclass workspaces. `mode` can be either `Binary` or `MultiClass`. The following optional parameters may be provided as part of the request: The number `size` of elements to return and the index `start_idx` starting from which elements will be returned (used for pagination). If not provided, the following default values are used: `start_idx = 0` and `size = 100`. In binary workspaces, the `category_id` specifies the selected selected category.

---

::::{tab-set}
:::{tab-item} Binary mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/get_labeled_elements_by_value?category_id=<category_id>&value=<value>&start_index=<start_index>&size=<size>&mode=<mode>```

---

**Example request:**

```json
{
   "category_id": "1",
   "value": "true",
   "update_counter": true,
   "start_index": 0,
   "size": 100
}
```

**Example response:**

```json
{
   "elements": [
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
  ],
  "hit_count": 2
}
```

:::
:::{tab-item} Multiclass mode


<span class="request_type">GET</span> ```/workspace/<workspace_id>/get_labeled_elements_by_value?value=<value>&start_index=<start_index>&size=<size>&mode=<mode>```

---

**Example request:**

```json
{
   "value": 1,
   "update_counter": true,
   "start_index": 0,
   "size": 100
}
```

**Example response:**

```json
{
   "elements": [
      {
         "begin": 367,
         "docid": "isear_dev-0",
         "end": 473,
         "id": "isear_dev-0-3",
         "model_predictions": 1,
         "text": "When I realized that I had been wrong about a person close to me, because of pre-set ideas and prejudices.",
         "user_labels": 2
      },
      {
         "begin": 603,
         "docid": "isear_dev-0",
         "end": 803,
         "id": "isear_dev-0-5",
         "model_predictions": 1,
         "text": "I feared that I would not be able to hand in the book-report on time as I had started working very late.  The book was difficult to read and my teacher did not accept my work as it was handed in late.",
         "user_labels": 1
      }
  ],
  "hit_count": 2
}
```

:::
::::

### Import labels

Upload a csv file and add its contents as user labels in the selected workspace. The input file may contain labels for more than one category.

The uploaded csv file must adhere to the following format: It must include ‘text’, ‘category_name’ and ‘label’ columns, and may optionally include a `document_id` column. If document IDs are provided AND `app.config["CONFIGURATION"].apply_labels_to_duplicate_texts` is False, these labels will be assigned only to elements in the specified documents. Otherwise, labels are assigned to all elements matching the given texts.

---

<span class="request_type">POST</span> ```/workspace/<workspace_id>/import_labels```

---

**Example request:**

```text
Stream of a csv file
```

**Example response:**

```json
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

```text
Empty
```

**Example response:**

```text
Stream of a csv file
```

## Document \& Element Management

Endpoints related to documents and elements. These endpoints are called in the context of a particular workspace and optionally a category. Thus, they may return not just document and element information from the dataset, but also category labels, model predictions etc. that are associated with a particular document/element.

### Get document URIs

Get IDs of all documents in the dataset associated with the selected workspace.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/documents```

---

**Example request:**

```text
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

Get all elements in selected document. On binary workspaces, the `category_id` is optional. Providing it will make user labels and model predictions to be included. On multiclass workspaces, the `category_id` is not required.

::::{tab-set}
:::{tab-item} Binary mode

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/document/<document_id>?category_id=<category_id>```

---

**Example request:**

```text
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

:::
:::{tab-item} Multiclass mode

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/document/<document_id>```

---

**Example request:**

```text
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
         "model_predictions": 1,
         "text": "Startups worth more than 1b unicorn3 ",
         "user_labels": 1
      },
      {
         "begin": 38,
         "docid": "isear_dev-3 Unicorn",
         "end": 67,
         "id": "isear_dev-3 Unicorn-1",
         "model_predictions": 1,
         "text": "another sentence of unicorn3 ",
         "user_labels": 1
      }
   ]
}
```

:::
::::

### Get model predictions by value

Get elements in the selected workspace that received a `value` prediction from the relevant classification model (i.e., the latest trained model). The `value` indicates the prediction type, which is `true` or `false` in binary workspaces and a category id in multiclass workspaces. `mode` can be either `Binary` or `MultiClass`. The following optional parameters may be provided as part of the request: The number `size` of elements to return and the index `start_idx` starting from which elements will be returned (used for pagination). If not provided, the following default values are used: `start_idx = 0` and `size = 100`. In binary workspaces, the `category_id` specifies the selected category.

::::{tab-set}
:::{tab-item} Binary mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/elements_by_prediction?category_id=<category_id>&value=<value>&start_idx=<start_index>&size=<max_results>```

**Example request:**

```json
{
   "category_id": 1,
   "value": "true",
   "start_index": 0,
   "size": 100
}
```

**Example response:**

```json
{
   "elements": [
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
            "0": "true"
         },
         "text":"The 2011 Svalbard polar bear attack was an attack by a presumed starving polar bear on a group of university students and their guides.",
         "user_labels":{
            "0": "true"
         }
      }
   ],
   "hit_count":54405,
   "positive_fraction":0.16464211787776445
}
```

:::
:::{tab-item} Multiclass mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/elements_by_prediction?value=<value>&start_idx=<start_index>&size=<size>```

**Example request:**

```json
{   
   "value": 1,
   "start_index": 0,
   "size": 100
}
```

**Example response:**

```json
{
   "elements": [
      {
         "begin":0,
         "docid":"wiki_new-2011 Svalbard polar bear attack",
         "end":31,
         "id":"wiki_new-2011 Svalbard polar bear attack-0",
         "model_predictions": 0,
         "text":"2011 Svalbard polar bear attack",
         "user_labels": 1
      },
      {
         "begin":32,
         "docid":"wiki_new-2011 Svalbard polar bear attack",
         "end":167,
         "id":"wiki_new-2011 Svalbard polar bear attack-1",
         "model_predictions": 0,
         "text":"The 2011 Svalbard polar bear attack was an attack by a presumed starving polar bear on a group of university students and their guides.",
         "user_labels": 0
      }
   ],
   "hit_count": 54405,
   "positive_fraction": 0.16464211787776445
}
```

:::
::::

### Get prediction statistics

Get the label count for each label value.

::::{tab-set}

:::{tab-item} Binary mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/prediction_stats/category_id=<category_id>```

**Example request:**

```text
Empty
```

**Example response:**

```json
{
    "false": {
        "count": 47586,
        "fraction": 0.7434034775273
    },
    "true": {
        "count": 16425,
        "fraction": 0.2565965224727
    }
}
```

:::

:::{tab-item} Multiclass mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/prediction_stats```

**Example request:**

```text
Empty
```

**Example response:**

```json
{
    "0": {
        "count": 1,
        "fraction": 1.5622314914624048e-05
    },
    "1": {
        "count": 1275,
        "fraction": 0.01991845151614566
    },
    "2": {
        "count": 5,
        "fraction": 7.811157457312024e-05
    },
    "3": {
        "count": 62728,
        "fraction": 0.9799565699645374
    },
    "4": {
        "count": 2,
        "fraction": 3.1244629829248096
    }
}
```

:::
::::

### Query elements

Get elements matching the query string `qry_string`. The following optional parameters may be provided as part of the request: the number `size` of elements to return and the index `start_idx` starting from which elements will be returned (used for pagination). In binary workspaces, the `category_id` specifies the selected category.

::::{tab-set}

:::{tab-item} Binary mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/query?qry_string=<qry_string>&category_id=<category_id>&start_idx=<start_idx>&size=<size>```

**Example request:**

```text
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

:::

:::{tab-item} Multiclass mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/query?qry_string=<qry_string>&start_idx=<start_idx>&size=<size>```

**Example request:**

```text
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
         "model_predictions": null,
         "text": "The sadness came to me when I heard that my girlfriend whom I loved so much got married to another man before a rebuff from her.",
         "user_labels": 2
      },
      {
         "begin": 28094,
         "docid": "isear_dev-0",
         "end": 28158,
         "id": "isear_dev-0-235",
         "model_predictions": null,
         "text": "Sadness, no, I felt something much stronger when my father died.",
         "user_labels": null
      }
   ] 
}
```

:::
::::

## Models \& Active Learning

Endpoints related to models and active learning.

### Get labeling status

Get information about the labeling status. This endpoint returns the number of user labels per label type in the `labeling_counts` field, which are `true` and `false` in binary workspaces and the category ids in multiclass workspaces. A number between 0-100 that reflects when a new model will be trained is included in the response too. The `labeling_counts` may contain weak labels count too.

::::{tab-set}
:::{tab-item} Binary mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/status?category_id=<category_id>```

**Example request:**

```text
Empty
```

**Example response:**

```json
{
   "labeling_counts": {
      "false": 2,
      "true": 15
   },
   "progress": {
      "all": 60
   }
}
```

:::
:::{tab-item} Multiclass mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/status```

**Example request:**

```text
Empty
```

**Example response:**

```json
{
   "labeling_counts": {
      "0": 8,
      "1": 2,
      "2": 7
   },
   "progress": {
      "all": 60
   }
}

```

:::
::::

### Get all models for category

Get information about all the iteration flows. On binary workspaces model are specific to a category, hence the `category_id` query param must be provided.

::::{tab-set}
:::{tab-item} Binary mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/models?category_id=<category_id>```

**Example request:**

```
Empty
```

**Example response:**

```json
{
    "models": [
        {
            "iteration_status": "READY",
            "changed_fraction": 0.048352962826647035,
            "creation_epoch": 1659865447.163773,
            "estimated_precision": 0.6,
            "estimated_precision_num_elements": 5,
            "iteration": 0,
            "model_metadata": {
                "train_counts": {
                    "false": 53,
                    "true": 86,
                    "weak_false": 119
                }
            },
            "model_status": "READY",
            "model_type": "SVM_Ensemble",
            "positive_fraction": 0.15332857931542143
        },
        {
            "iteration_status": "READY",
            "changed_fraction": 0.038921604711078396,
            "creation_epoch": 1659866548.713974,
            "iteration": 1,
            "model_metadata": {
                "train_counts": {
                    "false": 59,
                    "true": 90,
                    "weak_false": 121
                }
            },
            "model_status": "READY",
            "model_type": "SVM_Ensemble",
            "positive_fraction": 0.1512582811924917
        }
    ]
}
```

:::
:::{tab-item} Multiclass mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/models```

**Example request:**

```
Empty
```

**Example response:**

```json
{
    "iterations": [
        {
            "creation_epoch": 1699454085.17256,
            "iteration": 0,
            "iteration_status": "READY",
            "model_metadata": {
                "train_counts": {
                    "0": 3,
                    "1": 2,
                    "2": 2
                }
            },
            "model_status": "READY",
            "model_type": "MulticlassSVM_Ensemble",
            "prediction_stats": {
                "0": {
                    "count": 18891,
                    "fraction": 0.2951211510521629
                },
                "1": {
                    "count": 35136,
                    "fraction": 0.5489056568402306
                },
                "2": {
                    "count": 9984,
                    "fraction": 0.15597319210760652
                }
            }
        },
        {
            "changed_fraction": 0.38518379653497054,
            "creation_epoch": 1699454119.195123,
            "iteration": 1,
            "iteration_status": "READY",
            "model_metadata": {
                "train_counts": {
                    "0": 6,
                    "1": 3,
                    "2": 4
                }
            },
            "model_status": "READY",
            "model_type": "MulticlassSVM_Ensemble",
            "prediction_stats": {
                "0": {
                    "count": 28443,
                    "fraction": 0.44434550311665183
                },
                "1": {
                    "count": 19096,
                    "fraction": 0.29832372560966086
                },
                "2": {
                    "count": 16472,
                    "fraction": 0.2573307712736873
                }
            }
        }
    ]
}
```

:::
::::

### Get elements to label

Get elements to label. If at least one iteration has completed, the endpoint returns a list of elements that the active learning module recommends that the user label next. The following optional parameters may be provided as part of the request: The number `size` of elements to return and the index `start_idx` starting from which elements will be returned (used for pagination). If not provided, the following default values are used: `start_idx = 0` and `size = 100`. In binary workspaces, the `category_id` specifies the selected category.

::::{tab-set}
:::{tab-item} Binary mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/active_learning?category_id=<category_id>&start_idx=<start_index>&size=<max_results>```

**Example request:**

```text
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

:::
:::{tab-item} Multiclass mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/active_learning?start_idx=<start_index>&size=<max_results>```

**Example request:**

```text
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
         "model_predictions": 0,
         "text": "When I heard that my step-mother had treated my mother in a wrong manner.",
         "user_labels": null
      },
      {
         "begin": 75744,
         "docid": "isear_dev-0",
         "end": 75761,
         "id": "isear_dev-0-668",
         "model_predictions": 0,
         "text": "During a meeting.",
         "user_labels": null
      }
   ]
}
```

:::
::::

### Force train for category

Manually trigger a new iteration flow.


::::{tab-set}
:::{tab-item} Binary mode

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/force_train?category_id=<category_id>```

---

**Example request:**

```text
Empty
```

**Example response:**

```json
{
    "labeling_counts": {
        "false": 1485,
        "true": 542
    }
}
```

:::
:::{tab-item} Multiclass mode

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/force_train```

---

**Example request:**

```text
Empty
```

**Example response:**

```json
{
   "labeling_counts": {
      "0": 8,
      "1": 2,
      "2": 7
   }
}
```

:::
::::

### Export predictions

Download the predictions of the model learned during iteration `iteration_index`, as a csv file. In binary workspaces, the `category_id` specifies the selected category. `mode` can be either `Binary` or `MultiClass`.

::::{tab-set}
:::{tab-item} Binary mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/export_predictions?category_id=<category_id>&iteration_index=<iteration_index>&mode=<mode>```

**Example request:**

```json
{
   "category_id": 0,
   "mode": "Binary"
}
```

**Example response:**

```json
Stream of a csv file
```

:::
:::{tab-item} Multiclass mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/export_predictions?iteration_index=<iteration_index>&mode=<mode>```

**Example request:**

```json
{
   "mode": "MultiClass"
}
```

**Example response:**

```json
Stream of a csv file
```

:::
::::

### Export model



Download the trained model files for the given iteration index. If the iteration is not provided, the model from the latest iteration is exported. In order for this to work, the ModelType curently in use must implement the `ModelAPI.export_model()` method. In binary workspaces, the `category_id` specifies the selected category.

::::{tab-set}
:::{tab-item} Binary mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/export_model?category_id=<category_id>&iteration_index=<iteration_number>```

**Example request:**

```text
Empty
```

**Example response:**

```text
Stream of ZIP file
```

:::
:::{tab-item} Multiclass mode

<span class="request_type">GET</span> ```/workspace/<workspace_id>/export_model?iteration_index=<iteration_number>```

**Example request:**

```text
Empty
```

**Example response:**

```text
Stream of ZIP file
```

:::
::::

## Model Evaluation

Endpoints related to evaluation of a model.

### Get elements for precision evaluation

Get a sample of elements that are predicted as positive for the category by the latest model. This sample can be used to evaluate the precision of the model predictions: the user should label this sample of elements. After they are labeled, an invocation of the ['Run precision evaluation'](#run-precision-evaluation) endpoint will compare the user-provided labels to the model predictions to estimate the precision of the latest model. This endpoint can be used only in binary workspaces.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/precision_evaluation_elements?category_id=<category_id>```

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

Run precision evaluation. This endpoint can be used only in binary workspaces.

---

<span class="request_type">POST</span> ```/workspace/<workspace_id>/precision_evaluation_elements?category_id=<category_id>```

---

**Example request:**

```json
{
  "ids": [
    "wiki_animals_2000_pages-Chestnut_headed bee_eater-15",
    "wiki_animals_2000_pages-Hairy_eared cerrado mouse-22",
    "wiki_animals_2000_pages-Spectacled bear-106",
    "wiki_animals_2000_pages-Scimitar oryx-152",
    "wiki_animals_2000_pages-Red_headed trogon-34"
  ],
  "iteration": 1,
  "changed_elements_count": 4
}
```

**Example response:**

```json
{
    "score": 0.98
}
```

### Cancel precision evaluation

Cancel precision evaluation. This endpoint can be used only in binary workspaces.

---

<span class="request_type">POST</span> ```/workspace/<workspace_id>/cancel_precision_evaluation?category_id=<category_id>```

---

**Example request:**

```json
{
    "changed_elements_count": 20
}
```

**Example response:**

```json
{
    "canceled": "OK"
}
```

### Get elements for accuracy evaluation

Get a sample of predicted elements. This sample can be
used to evaluate the accuracy of the model predictions: the user should label this sample of elements. After they are labeled, an invocation of the ['Run accuracy evaluation'](#run-accuracy-evaluation) endpoint will compare the user-provided labels to the model predictions to estimate the accuracy of the latest model. This endpoint can be used only in multiclass workspaces.

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/accuracy_evaluation_elements```

---

**Example request:**

```text
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
         "model_predictions": 1,
         "text": "Boyfriend \"chatting up\" another girl.",
         "user_labels": null
      },
      {
         "begin": 30939,
         "docid": "isear_dev-0",
         "end": 31101,
         "id": "isear_dev-0-260",
         "model_predictions": 1,
         "text": "My elder brother had been expelled from college and he was so frustated that he attempted suicide - he drank bottle fragments.  I was very sad when I learnt this.",
         "user_labels": null
      }
   ]
}
```

### Run accuracy evaluation

Run accuracy evaluation. This endpoint can be used only in multiclass workspaces.

---

<span class="request_type">POST</span> ```/workspace/<workspace_id>/accuracyn_evaluation_elements```

---

**Example request:**

```json
{
  "ids": [
    "wiki_animals_2000_pages-Chestnut_headed bee_eater-15",
    "wiki_animals_2000_pages-Hairy_eared cerrado mouse-22",
    "wiki_animals_2000_pages-Spectacled bear-106",
    "wiki_animals_2000_pages-Scimitar oryx-152",
    "wiki_animals_2000_pages-Red_headed trogon-34"
  ],
  "iteration": 1,
  "changed_elements_count": 4
}
```

**Example response:**

```json
{
    "score": 0.98
}
```

### Cancel accuracy evaluation

Cancel accuracy evaluation. This endpoint can be used only in multiclass workspaces.

---

<span class="request_type">POST</span> ```/workspace/<workspace_id>/cancel_accuracy_evaluation```

---

**Example request:**

```json
{
    "changed_elements_count": 20
}
```

**Example response:**

```json
{
    "canceled": "OK"
}
```

## Label Quality Reports

Endpoints related to label quality reports. These endpoints return labeled elements that may contain potential errors in their labels.

### Get label and model disagreements

Get all labeled elements where the predictions of the latest model for the category differ from the label provided by the user. 

_Note: At the moment, this endpoint is only available in binary workspaces._

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/disagree_elements?category_id=<category_id>```

---

**Example request:**

```text
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

_Note: At the moment, this endpoint is only available in binary workspaces._

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/suspicious_elements?category_id=<category_id>```

---

**Example request:**

```text
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

_Note: At the moment, this endpoint is only available in binary workspaces._

---

<span class="request_type">GET</span> ```/workspace/<workspace_id>/contradiction_elements?category_id=<category_id>```

---

**Example request:**

```text
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
