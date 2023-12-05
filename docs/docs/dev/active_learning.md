# Active Learning

Label Sleuth guides the users through the labeling process by suggesting a ranked list of elements that they should label next. This list is generated through the use of an active learning component. Label Sleuth automatically invokes the active learning component every time a new model is trained. The system employs a customizable and extensible architecture, which allows different active learning approaches to be used. 

## Active learning strategies

Label Sleuth currently supports the following active learning strategies:

::::{tab-set}
:::{tab-item} Binary mode

The employed active learning strategy can be configured by setting the value of the `binary_flow.active_learning_strategy` parameter in the system's [configuration file](configuration.md).

| Active learning strategy | Description |
|---|---|
| `RANDOM` | Randomly sample from unlabeled data (active learning baseline) |
| `HARD_MINING` <br /><defvalue>default</defvalue> | Uncertainty sampling/least confidence ([Lewis and Gale 1994](https://arxiv.org/abs/cmp-lg/9407020)) |
| `RETROSPECTIVE` | Select top scored instances by the model ([Ein-Dor et al. 2019](https://arxiv.org/abs/1911.10763)) |
| `COMBINED_RETROSPECTIVE_HM` | a combination between the previous two strategies |

:::
:::{tab-item} Multiclass mode

The employed active learning strategy can be configured by setting the value of the `multiclass_flow.active_learning_strategy` parameter in the system's [configuration file](configuration.md).

| Active learning strategy | Description |
|---|---|
| `MULTICLASS_ENTROPY` <br /><defvalue>default</defvalue>  | Uncertainty sampling/least confidence ([Lewis and Gale 1994](https://arxiv.org/abs/cmp-lg/9407020)) |

:::
::::

## Implement a new active learning strategy

In addition to the preloaded active learning strategies, Label Sleuth can be extended to support additional active learning techniques. To integrate a new active learning approach, follow the steps below: 

1. Implement a new `ActiveLearner`.
   
   Active learning modules inherit from the [ActiveLearner](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/active_learning/core/active_learning_api.py) API.
   The function to implement is:
   ```python
    def get_per_element_score(self, candidate_text_elements: Sequence[TextElement],
                              candidate_text_element_predictions: Sequence[Prediction], workspace_id: str,
                              dataset_name: str, category_name: str) -> Sequence[float]:    
   ```    
   Given sequences of text elements and the model predictions for these elements, this function returns an active learning score for each element.
   The elements with the highest scores will be recommended for the user to label next.

2. Add the newly implemented ActiveLearner to the `ActiveLearningCatalog`.
