# Introduction to Continual Learning

Here, you will find an _informal_ introduction to Continual Learning. For a comprehensive overview of the field, have a look at our [research section](research.md), in which you can find in-depth surveys on the topic together with specific approaches and techniques to address the Continual Learning challenge.

## What is Continual / Lifelong Learning?

Continual Learning, also known as Lifelong learning, is built on the idea of learning continuously about the external world in order to enable the autonomous, incremental development of ever more complex skills and knowledge.

A Continual learning system can be defined as _an adaptive algorithm capable of learning from a continuous stream of information, with such information becoming progressively available over time and where the number of tasks to be learned \(e.g. membership classes in a classification task\) are not predefined. Critically, the accommodation of new information should occur without catastrophic forgetting or interference._  
Parisi et al. _Continual Lifelong Learning with Neural Networks: a review_, 2019.

Hence, in the Continual Learning scenario, a learning model is required to incrementally build and dynamically update internal representations as the distribution of tasks dynamically changes across its lifetime. Ideally, part of such internal representations will be general and invariant enough to be reusable across similar tasks, while another part should preserve and encode task-specific representations.

## The Deep Learning approach to Learning

Deep Learning is a subset of Machine Learning in which models - artificial neural networks, in most of the cases - learn to map input to output by building an adaptive, internal hierarchical representation. Artificial neural networks are made of units linked together by weighted connections. The learning process is defined by changing the value of the weights in order to minimize a cost function which measures how much the output produced by the model differs from the expected outcome.

Such learning process is adaptive, meaning that it only requires a \(possibly large\) set of data from which to learn and a suitable cost function to specify the type of task to be performed.

Decades of research showed that Deep Learning models are able to accomplish a range of different tasks, often surpassing human-level performance. They are widespread in several fields like language translation, self-driving cars, bio-medical applications, stock prediction in finance… just to name a few!

The astonishing accomplishments made by Deep Learning are confined to a specific task: without additional training, a Deep Learning neural network which is able to beat the \(human\) world champion at the game of Go will not be able to drive a car or to translate from English to French. However, nothing prevents us from continuing to train the network on new tasks.

What will be the behavior of the network at the end of the new learning phase? This question is at the heart of the Continual Learning field.

## The Catastrophic Forgetting phenomenon

When learning in a Continual Learning environment, the model is exposed to a streaming of inputs coming from different distributions, representing different tasks. At each learning step, the model will have to adapt in order to meet the expected behavior.

A well-known problem in learning multiple tasks sequentially is the _catastrophic forgetting_ phenomenon, which can be concisely summarized in one sentence: _the process of learning new knowledge quickly disrupts previously acquired information_. The catastrophic forgetting \(or simply forgetting\) is the main problem faced by Continual Learning algorithms.

Unfortunately, _all_ connectionist models are subjected to Catastrophic Forgetting. The consequence being that neural networks are not suitable to learn in Continual Learning environments, since their performance on previous tasks will degrade very quickly.

Catastrophic Forgetting can be characterized by looking at the _stability-plasticity_ dilemma: a learning model has to be plastic enough to learn new information, but it has also to be stable to preserve internal knowledge. This trade-off is never satisfied for traditional neural networks, where the plasticity easily overpowers the stability.

## Beyond forgetting

Even if Catastrophic Forgetting is the main focus of Continual Learning, there are other aspects that need to be considered when learning continuously.

Preserving old knowledge is important not only to perform well on previous tasks. It can also be used to perform better on incoming tasks. This feature, called _transfer learning_, enables Continual Learning algorithms to require only few examples of a new tasks to master it.

Another interesting opportunity when learning sequentially is the benefit that a previously learned task can receive new knowledge from subsequent learning. Such _backward transfer_ can positively affect the performance of a Continual Learning algorithm on previous tasks, without seeing any further examples from it. It is needless to say that, without a method that properly mitigate forgetting, no backward transfer is possible.

## Biological perspective

The main evolutionary advantage of learning is to rapidly change an organism’s behavior to succeed in a dynamic environment. These experience-driven alterations occur in much shorter time scales than genetic evolution can adapt to, allowing a single organism to persist in more situations than those whose behavior is fixed. Because of this, experience driven alterations are pervasive throughout the animal kingdom, from complex vertebrates to single celled organisms. The reason for this is simple: learned responses or acquired information from experiences help the chances of an organism’s success as opposed to a randomly selected behavior.

While some learning occurs only once, such as imprinting in ducklings, a majority occurs continuously throughout an organism’s lifespan. As the climate, ecological niche, food supply, or other factors alter, an organism may alter its response as well. Moreover, this may occur multiple times throughout an organism’s life. For example, a scavenging animal may learn the location of a food supply, returning multiple times to that location. When the source is exhausted, then the animal must learn to not only refrain from returning to the location, but also to learn to find a new source. This sequence may happen multiple times throughout an animal’s life, a reality of the scarcity of food.

### Simple Learning

Throughout the long studies of animal learning since the late 18th century, a large literature of general rules have been revealed. These universal laws include multiple scales and degrees of complexity, and may be pervasive throughout species of localized to only a few. For example, a quite common form of learning is sensitization and habituation, among the most basic forms. This results in the animal’s increased or reduced response to a given stimulus after repeated exposures. This occurs throughout the animal kingdom, from humans to single cells. For example, if you’re walking in a dark room and someone startles you, your reaction is likely to be more exaggerated than if you were startled in a well lit room. This is an example of sensitization, as the dark room exaggerates your response. The reciprocal of this can be observed in prairie dogs. Upon hearing the sound of approaching human footsteps, the animals retreat into their holes. As this occurs multiple times, the prairie dogs learn the footsteps are no longer a threat, thus no longer retreating once heard again. These phenomena can be observed at the single cell level as well. Differentiated PC12 cells secrete decreasing amounts of norepinephrine as they are repetitively stimulated by concentrations of a potassium ion. These simple learning rules persist throughout an organism’s lifespan, as it experiences different types and degrees of stimuli. Alone, these simple rules can produce an astounding degree of complex behavior, but they are even more impressive when coupled with other mechanisms.

### Associative Learning

Simple modulation of response alone may not be suitable for more complex organisms and environments. A finer degree of acuity may be demanded. Thus, evolution has produced other learning mechanisms designed to parse the causal structure of the environment, as well as to differentiate between individual features and stimuli. This type of learning is known as associative, as the animal links together structured information, and fits two main classes: classical and instrumental conditioning. Classical conditioning was made famous by Ivan Pavlov and his dogs, and includes an animal’s ability to link novel stimuli with responses, as such in the classical example of the ringing bell, a conditioned stimulus, resulting in the dog salivating. Other uses have been exhibited as well. Farmers were killing lions that were preying on their cattle. To deter the cats from the cattle, conservation specialists gave the lions cattle meat which would make them safely sick. This conditioned the lions away from the meat, and the number of cattle killed was drastically reduced. Conditioning of this sort could easily be noticed in the wild, and will continue throughout the organism’s lifetime, as more and more associations are built.

When classical conditioning is observed from the perspective of a longer term scale, complex interactions between the conditioning of the animal arise. While many of the rules governing these complex interactions are unknown, some have been uncovered. For example, some stimuli that are experienced but not linked to a response will show a slower learning curve when they are linked to a response, known as latent inhibition. Prior learning of a stimulus and response pair can also inhibit future stimuli from being learned, known as blocking. Organisms may also exhibit a response to novel stimuli as well, known as conditioning generalization.

Organisms may not have these events structured in such a way where the reward is immediately evident, but rather will have to use trial and error until a reward is found. For example, an octopus may try several different actions to open a jar with a crab trapped inside, eventually succeeding by twisting with its arms. When given a new jar, the octopus will open it in fewer attempts, hinting at learning mechanisms. This type of learning is known as instrumental conditioning. Organisms use this type of learning often in their environment, attempting to parse out hidden rewards that cannot be known. Many successes in machine learning have also leveraged it as well. The famous Q learning algorithm by Watkins was designed with this type of learning in mind, then paired with deep neural networks produced the general Atari playing algorithm.

Associative pairs require repeated reinforcement to persist. If an organism learns that an area may be unsafe, but repeatedly sees it as safe afterwards, then the prior pairing will fade. However, if the stimulus reappears, then the organism will learn much more quickly than the first pairing, hinting that pairings never fully fade.

