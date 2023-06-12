Neural networks are a kind of [[Machine Learning]] model based on the biological neuron.

## Origins 

The basis of neural networks originates from Warren McCulloch and Walter Pitts research into replicating the human neuron.  The first device that used the principles was created by Frank Rosenblatt in 1958, amazingly called the *Mark I Perceptron*. It was able to recognise simple shapes using custom built hardware based around an array of 400 photocells which were randomly connected to "neurons".  Weights were encoded in potentiometers and weight updates were executed using electric motors.

In 1986, the PDP Research Group released *Parallel Distributed Processing*, which defined parallel distributed processing as the following:

>1.  A set of _processing units_
>2.  A _state of activation_
>3. An _output function_ for each unit
>4. A _pattern of connectivity_ among units
>5. A _propagation rule_ for propagating patterns of activities through the network of connectivities
>6. An _activation rule_ for combining the inputs impinging on a unit with the current state of that unit to produce an output for the unit
>7. A _learning rule_ whereby patterns of connectivity are modified by experience
>8. An _environment_ within which the system must operate

Modern neural networks handle all of these requirements.

## In Machine Learning

Neural networks are an extremely flexible model that can be tailored to suit many different kinds of problems (the *universal approximation theorem* proves that it can solve any problem to any level of accuracy), it is a matter of finding good weight assignments.  A general method for iteratively improving the weights of a neural network is **stochastic gradient descent**.