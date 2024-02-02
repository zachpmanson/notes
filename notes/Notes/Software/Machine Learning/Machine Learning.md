> We may have realized it's easier to build a brain than to understand one

-- [if you know who said this let me know please](https://news.ycombinator.com/item?id=34798846)

The process of making computers learn to solve problems themselves, based on examples of the problem.

>Suppose we arrange for some automatic means of testing the effectiveness of any current weight assignment in terms of actual performance and provide a mechanism for altering the weight assignment so as to maximize the performance. We need not go into the details of such a procedure to see that it could be made entirely automatic and to see that a machine so programmed would "learn" from its experience.

-- Arther Samuel, Artificial Intelligence: A Frontier of Automation

## Important concepts

- "weight assignment"
	- weights are variables, assignments are the values
	- weights are sometimes also referred to as parameters
- weight assignment has "actual performance"
	- the model's ability achieve its goal
	- this is distinct from the "results", meaning the output e.g. results are moves taken vs  actual performance is winning the game 
- "automatic means" of testing performance
- "mechanism" for improving performance by changing weight assignments
	- can compare two versions performance and move weights closer to the better performing model
- results != performances
	- results are the outputs
		- results are also called **predictions**
	- performance is the quality of outputs
		- measure of performance is called **loss**
- classification model is one that predicts a discrete category
- regression model is one that predicts >=1 numeric qualities
	- do not use *regression* to refer to linear regression models
- "overfitting" can occur when a model is trained for too long, and it starts to memorize the input data too precisely, rather than determining generalised rules
- validation set is the subset of all labelled data that is seperated from the training set, used for measuring the accuracy of the model
- model architecture is the functional form of a model
- metric is a function that measures the quality of a models predictions using the validation set
	- a simple example is the error rate of a classifier
- metric != loss
	- metric is designed for human consumption and review of a model
		- ideally this is as close to the end task as possible
	- loss is a measure that allows a training system to update its model weights automatically
	- they may be the same, they may not be
- "epochs", which are the number of times the training system runs on each label-value pair in the dataset
- transfer learning
	- when working with a pretrained model and using it for a different task to what it was originally trained for
- fine tuning is a transfer learning technique of additionally training a pretrained model with further data

Definitions from [[Practical Deep Learning]] Glossary, ch. 1:

Term | Meaning
---- | ------- 
Label | The data that we're trying to predict, such as "dog" or "cat"
Architecture | The _template_ of the model that we're trying to fit; the actual mathematical function that we're passing the input data and parameters to
Model | The combination of the architecture with a particular set of parameters
Parameters | The values in the model that change what task it can do, and are updated through model training
Fit | Update the parameters of the model such that the predictions of the model using the input data match the target labels
Train | A synonym for _fit_
Pretrained model | A model that has already been trained, generally using a large dataset, and will be fine-tuned
Fine-tune | Update a pretrained model for a different task
Epoch | One complete pass through the input data
Loss | A measure of how good the model is, chosen to drive training via SGD|Metric | A measurement of how good the model is, using the validation set, chosen for human consumption
Validation set | A set of data held out from training, used only for measuring how good the model is
Training set | The data used for fitting the model; does not include any data from the validation set|Overfitting | Training a model in such a way that it _remembers_ specific features of the input data, rather than generalizing well to data not seen during training
CNN | Convolutional neural network; a type of neural network that works particularly well for computer vision tasks

The training loop:

![[machine-learning.png]]

## Interesting Links

- [The Ghosts in the Data](https://vickiboykis.com/2021/03/26/the-ghosts-in-the-data/)