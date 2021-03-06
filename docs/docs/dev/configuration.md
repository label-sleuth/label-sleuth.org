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
|----|-----|
`first_model_positive_threshold` | Number of elements that must be assigned a positive label for the category in order to trigger the training of a classification model. <br /> <br /> _See also:_ The [training invocation](model_training.md#training-invocation) documentation.|
`changed_element_threshold` | Number of changes in user labels for the category -- relative to the last trained model -- that are required to trigger the training of a new model. A change can be a assigning a label (positive or negative) to an element, or changing an existing label. Note that `first_model_positive_threshold` must also be met for the training to be triggered. <br /> <br /> _See also:_ The [training invocation](model_training.md#training-invocation) documentation. |
`training_set_selection_strategy` | Strategy to be used from [TrainingSetSelectionStrategy](https://github.com/label-sleuth/label-sleuth/blob/316bacb7cca7d7b78a11b96d397aac9bfd7e33bf/label_sleuth/training_set_selector/train_set_selector_api.py#L9). A TrainingSetSelectionStrategy determines which examples will be sent in practice to the classification models at training time - these will not necessarily be identical to the set of elements labeled by the user. For currently supported implementations see [get_training_set_selector()](https://github.com/label-sleuth/label-sleuth/blob/316bacb7cca7d7b78a11b96d397aac9bfd7e33bf/label_sleuth/training_set_selector/training_set_selector_factory.py#L7). <br /> <br /> _See also:_ The [training set selection](model_training.md#training-set-selection) documentation.|
`model_policy` | Policy to be used from [ModelPolicies](https://github.com/label-sleuth/label-sleuth/blob/316bacb7cca7d7b78a11b96d397aac9bfd7e33bf/label_sleuth/models/core/model_policies.py#L5). A [ModelPolicy](https://github.com/label-sleuth/label-sleuth/blob/316bacb7cca7d7b78a11b96d397aac9bfd7e33bf/label_sleuth/models/policy/model_policy.py#L6) determines which type of classification model(s) will be used, and _when_ (e.g. always / only after a specific number of iterations / etc.). <br /> <br /> _See also:_ The [model selection](model_training.md#model-selection) documentation.|
`active_learning_strategy` | Strategy to be used from [ActiveLearningStrategies](https://github.com/label-sleuth/label-sleuth/blob/316bacb7cca7d7b78a11b96d397aac9bfd7e33bf/label_sleuth/active_learning/core/active_learning_strategies.py#L4). An [ActiveLearner](https://github.com/label-sleuth/label-sleuth/blob/316bacb7cca7d7b78a11b96d397aac9bfd7e33bf/label_sleuth/active_learning/core/active_learning_api.py#L11) module implements the strategy for recommending the next elements to be labeled by the user, aiming to increase the efficiency of the annotation process. For currently supported implementations see [get_active_learner()](https://github.com/label-sleuth/label-sleuth/blob/316bacb7cca7d7b78a11b96d397aac9bfd7e33bf/label_sleuth/active_learning/core/active_learning_factory.py#L8). <br /> <br /> _See also:_ The [active learning](active_learning.md) documentation. |
`precision_evaluation_size` | Sample size to be used for estimating the precision of the current model. To be used in future versions of the system, which will provide built-in evaluation capabilities.
`apply_labels_to_duplicate_texts` | Specifies how to treat elements with identical texts. If `true`, assigning a label to an element will also assign the same label to other elements which share the exact same text; if `false`, the label will only be assigned to the specific element labeled by the user. |
`language` | Specifies the chosen system-wide language. This determines some language-specific resources that will be used by models and helper functions (e.g., stop words). The list of supported languages can be found in [Languages](https://github.com/label-sleuth/label-sleuth/blob/b7d60ac5e62448514d10f9de093c5c987bca2e96/label_sleuth/models/core/languages.py#L58). We welcome contributions of additional languages.
`login_required` | Specifies whether or not using the system will require user authentication. If `true`, the configuration file must also include a `users` parameter, mapping the keys and values of the [User](https://github.com/label-sleuth/label-sleuth/blob/316bacb7cca7d7b78a11b96d397aac9bfd7e33bf/label_sleuth/configurations/users.py#L5) dataclass for each user. |
