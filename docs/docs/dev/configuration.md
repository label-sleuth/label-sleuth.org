# System Configuration

Several aspects of Label Sleuth can be configured through the system's configuration file.

## Configuration file

The default configuration file is located at [label_sleuth/config.json](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/config.json).

A custom configuration file can be applied by passing the `--config_path` parameter to the "start_label_sleuth" command. In that case the following command can be used to invoke Label Sleuth:

```
 python -m label_sleuth.start_label_sleuth --config_path <path_to_my_configuration_json>
```

## Parameters

The following parameters can be set in the configuration file:

| Parameter | Description |
|-----------|-------------|
| `first_model_positive_threshold`  | Number of elements that must be assigned a positive label for the category in order to trigger the training of a classification model. <br /> <br /> _See also:_ The [training invocation](model_training.md#training-invocation) documentation. |
| `changed_element_threshold`       | Number of changes in user labels for the category -- relative to the last trained model -- that are required to trigger the training of a new model. A change can be a assigning a label (positive or negative) to an element, or changing an existing label. Note that `first_model_positive_threshold` must also be met for the training to be triggered. <br /> <br /> _See also:_ The [training invocation](model_training.md#training-invocation) documentation. |
| `training_set_selection_strategy` | Strategy to be used from [TrainingSetSelectionStrategy](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/training_set_selector/train_set_selector_api.py). A TrainingSetSelectionStrategy determines which examples will be sent to the classification models at training time - these will not necessarily be identical to the set of elements labeled by the user. For currently supported implementations see the [get_training_set_selector()](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/training_set_selector/training_set_selector_factory.py) function. <br /> <br /> _See also:_ The [training set selection](model_training.md#training-set-selection) documentation. |
| `model_policy`                    | Policy to be used from [ModelPolicies](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/models/core/model_policies.py). A [ModelPolicy](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/models/policy/model_policy.py) determines which type of classification model(s) will be used, and _when_ (e.g. always / only after a specific number of iterations / etc.). <br /> <br /> _See also:_ The [model selection](model_training.md#model-selection) documentation. |
| `active_learning_strategy`        | Strategy to be used from [ActiveLearningCatalog](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/active_learning/core/catalog.py). An [ActiveLearner](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/active_learning/core/active_learning_api.py) module implements the strategy for recommending the next elements to be labeled by the user, aiming to increase the efficiency of the annotation process. <br /> <br /> _See also:_ The [active learning](active_learning.md) documentation. |
| `precision_evaluation_size`       | Sample size to be used for estimating the precision of the current model when the precision evaluation function is invoked. <br /><br /> _Defaults to_ `20`. |
| `apply_labels_to_duplicate_texts` | Specifies how to treat elements with identical texts. If `true`, assigning a label to an element will also assign the same label to other elements which share the exact same text; if `false`, the label will only be assigned to the specific element labeled by the user. <br /><br /> _Defaults to_ `true`. |
| `language`                        | Specifies the chosen system-wide language. This determines some language-specific resources that will be used by models and helper functions (e.g., stop words). The list of supported languages can be found at the very end of [languages.py](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/models/core/languages.py). We welcome contributions of additional languages. <br /><br /> _Defaults to_ `ENGLISH`. |
| `login_required`                  | Specifies whether or not using the system will require user authentication. If `true`, the configuration file must also include a `users` parameter. <br /><br /> _Defaults to_ `false`. |
| `users`                           | Only relevant if `login_required` is `true`. Specifies the pre-defined login information in the following format: <pre>"users":[<br>&nbsp;{<br>&nbsp;&nbsp;&nbsp;"username": "<predefined_username1>",<br>&nbsp;&nbsp;&nbsp;"token":"<randomly_generated_token1>",<br>&nbsp;&nbsp;&nbsp;"password":"<predefined_user1_password>"<br>&nbsp;}<br>] </pre> * The list of usernames is static and currently all users have access to all the workspaces in the system. |
| `main_panel_elements_per_page` | Number of elements per page in the main panel, i.e., document view. <br /><br /> _Defaults to_ `500`. |  
| `sidebar_panel_elements_per_page` | Number of elements per page in the sidebar panels that use pagination. <br /><br /> _Defaults to_ `50`. |
