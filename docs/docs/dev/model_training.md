# Model Training

While the user is providing labels for a category, Label Sleuth iteratively trains a machine learning model for the selected category in the background. Model training consists of three main steps explained in detail below:

1. [Training invocation](#training-invocation): Decide when to invoke model training
2. [Training set selection](#training-set-selection): Create training set to be used for training
3. [Model selection](#model-selection): Decide which model to use for training and invoke the training procedure

## Training invocation

In order to cater to domain experts, model training does not have to be explicitly invoked by the user. Instead Label Sleuth automatically invokes model training in the background when certain conditions are met. To ensure that the user can see the the most up to date model predictions and received appropriate active learning guidance, model training is repeated with Label Sleuth training new models (which can be thought of as new versions of the classifier) as the user continues labeling.

### Training invocation criteria

Label Sleuth starts a new model training iteration whenever the following two conditions are both met:

|   Condition&nbsp;on | Description | Default |
|---|---|---|
| **Number of positive labels** | The user has to provide a minimum number of positive labels. The threshold of required positive labels can be configured by setting the value of the `first_model_positive_threshold` parameter in the system's [configuration file](configuration.md). | 20 |
| **Number of label changes** | The user has to change a minimum number of labels since the last model training iteration (unless it is the first iteration). A change can be assigning a label (positive or negative) to an element, or changing an existing label. The threshold of required label changes can be configured by setting the value of the `changed_element_threshold` parameter in the system's [configuration file](configuration.md). | 20 |

## Training set selection

When the training invocation criteria are satisfied, Label Sleuth selects the examples that will be sent to the model for training (i.e., the training set). These are not necessarily identical to the set of elements labeled by the user, as the system may remove elements or add more weakly labeled elements to create a more balanced dataset. The method used to generate the training set is described by the chosen _training set selection strategy_.

### Training set selection strategies

Label Sleuth currently supports the following training set selection strategies:

| Training set selection strategy | Description |
|---|---|
| `ALL_LABELED` | Use examples labeled by the user (without any modification). |
| `ALL_LABELED_PLUS_UNLABELED_AS_NEGATIVE_EQUAL_RATIO` | Ensure a ratio of _1 negative example for every positive example_. See below for details of how this ratio is ensured. |
| `ALL_LABELED_PLUS_UNLABELED_AS_NEGATIVE_X2_RATIO` <br /><defvalue>default</defvalue> | Ensure a ratio of _2 negative example for every positive example_. See below for details of how this ratio is ensured.   |
| `ALL_LABELED_PLUS_UNLABELED_AS_NEGATIVE_X10_RATIO` | Ensure a ratio of _10 negative example for every positive example_. See below for details of how this ratio is ensured.  |

If one of the training set selections strategies specifying a ratio of negative to positive examples is chosen, Label Sleuth ensures the respective ratio as follows: If the user has labeled fewer negative examples than the ratio, some _unlabeled_ examples are automatically added to the training set as negative examples. On the other hand, if the number of negative examples labeled by the user exceeds the ratio, only a sample of the user-labeled negative examples are included in the training set.

The employed training set selection strategy can be configured by setting the value of the `training_set_selection_strategy` parameter in the system's [configuration file](configuration.md). Note that in each case, Label Sleuth removes duplicates so that only unique elements are included in the training set. 

## Model selection

Once the training set is selected, the system uses the selected training set to train a machine learning model. Label Sleuth employs a customizable and extensible architecture, which allows different machine learning models to be trained. 

### Models

Label Sleuth currently includes implementations of the following machine learning models:

| Model name | Description | Implementation details | Hardware requirements
|---|---|---|---|
| `NB_OVER_BOW` | Naive Bayes over Bag-of-words | [scikit-learn](https://scikit-learn.org) implementation | - |
| `NB_OVER_GLOVE` | Naive Bayes over GloVe | - | - |
| `SVM_OVER_BOW` | Support Vector Machine over Bag-of-words | [scikit-learn](https://scikit-learn.org) implementation  | - |
| `SVM_OVER_GLOVE` | Support Vector Machine over GloVe | - | - |
| `SVM_ENSEMBLE` | Ensemble of `SVM_OVER_BOW` and `SVM_OVER_GLOVE` | - | - |
| `HF_BERT` | BERT ([Devlin et al. 2018](https://arxiv.org/abs/1810.04805)) | Pytorch implementation using the [Hugging Face Transformers](https://github.com/huggingface/transformers) library | GPU _(recommended)_ |

 Within the codebase, the list of supported models can be found in Label Sleuth's [model catalog](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/models/core/catalog.py). Note that some model may have special hardware requirements to perform as expected (e.g., they require the presence of a GPU).

### Model policies

The model architecture that is trained in each iteration is prescribed by the employed _model policy_. In its most basic form, a model policy is _static_, resulting in the system always using the same model for every iteration. However, model policies can also be _dynamic_, allowing the system to switch between different types of models depending on the iteration. For instance, one can create a model policy instructing Label Sleuth to use a light and fast to train model (such as SVM) for the first few iterations and then switch to more complex and slower to train model (such as BERT) for later iterations. Label Sleuth currently supports the following model policies: 

| Model policy | Model type | Description |
|---|---|---|
| `STATIC_SVM_BOW` | Static | Use the `SVM_OVER_BOW` model in every iteration |
| `STATIC_SVM_GLOVE` | Static | Use the `SVM_OVER_GLOVE` model in every iteration |
| `STATIC_SVM_ENSEMBLE`  <br /><defvalue>default</defvalue> | Static | Use the `SVM_ENSEMBLE` model in every iteration |
| `STATIC_HF_BERT` | Static | Use the `HF_BERT` in every iteration |

Within the codebase, the list of available model policies can be found [here](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/models/core/model_policies.py). The model policy can be configured by setting the `model_policy` parameter in the system's [configuration file](configuration.md).

### Implement a new model

In addition to the preloaded models, Label Sleuth can be extended to support additional machine learning models. To integrate a new classification model, follow the steps below:    

1. Implement a new `ModelAPI`.

    Machine learning models are integrated by adding a new implementation of the ModelAPI.
    The main functions are *_train()*, *load_model()* and *infer()*:

    
    **Train** a new model.

    ```python    
    def _train(self, model_id: str, train_data: Sequence[Mapping], train_params: dict):
   ```
    - model_id: a unique identifier for the model
    - train_data: a list of dictionaries with at least the "text" and "label" fields. Additional fields can be passed e.g.
    *[{'text': 'text1', 'label': 1, 'additional_field': 'value1'}, {'text': 'text2', 'label': 0, 'additional_field': 'value2'}]*
    - train_params - dictionary for additional train parameters (can be None)

    <br />

    **Load** a trained model.
    ```python   
    def load_model(self, model_path: str):
    ```
    - model_path: path to a directory containing all model components
   
    Returns an object that contains all the components that are necessary to perform inference (e.g., the trained model itself, the language recognized by the model, a trained vectorizer/tokenizer etc.).

    **Infer** a given sequence of elements and return the results.

    ```python
    def infer(self, model_components, items_to_infer) -> Sequence[Prediction]:
    ```
    - model_components: the return value of `load_model()`, i.e., an object containing all the components that are necessary to perform inference
    - items_to_infer: a list of dictionaries with at least the "text" field. Additional fields can be passed,
    e.g. *[{'text': 'text1', 'additional_field': 'value1'}, {'text': 'text2', 'additional_field': 'value2'}]*
    
    Returns a list of [Prediction](https://github.com/label-sleuth/label-sleuth/blob/1424a9ab01697e12396bc33fd608158d61d55e24/label_sleuth/models/core/prediction.py#L20) objects - one for each item in *items_to_infer* - where 
    Prediction.label is a boolean and Prediction.score is a float in the range [0-1].
    Additional outputs can be passed by inheriting from the base Prediction class and overriding the get_predictions_class() method.

2. Add the newly implemented ModelAPI to `ModelsCatalog`
3. Add one or more policies that use the new model to `ModelPolicies`
