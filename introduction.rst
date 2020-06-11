Introduction
================================

In this page you’ll find a brief background on Continual/Lifelong Learning from both a Computer Science and Biological prospective.

What is Continual/Lifelong Learning?
---------------------------------------

Continual Learning (CL) is built on the idea of learning continuously and adaptively about the external world and enabling the autonomous incremental development of ever more complex skills and knowledge.

In the context of Machine Learning it means being able to smoothly update the prediction model to take into account different tasks and data distributions but still being able to re-use and retain useful knowledge and skills during time.

Hence, CL is the only paradigm which force us to deal with an higher and realistic time-scale where data (and tasks) becomes available only during time, we have no access to previous perception data and it’s imperative to build on top of previously learned knowledge.

Biological Prospective
---------------------------------------

The main evolutionary advantage of learning is to rapidly change an organism’s behavior to succeed in a dynamic environment. These experience driven alterations occur in much shorter timescales than genetic evolution can adapt to, allowing a single organism to percist in more situations than those whose behavior is fixed. Because of this, experience driven alterations are pervasive throughout the animal kingdom, from complex vertebrates to single celled organisms to a degree. The reason for this is simple, learned responses or acquired information from experiences helps the chances of an organism’s success as opposed to a randomly selected behavior.

While some learning occurs only once, such as imprinting in ducklings, a majority occurs continuously throughout an organism’s lifespan. As the climate, ecological niche, food supply, or other factors alter, an organism may alter its response as well. Moreover, this may occur multiple times throughout an organism’s life. For example, a scavenging animal may learn the location to a food supply, returning multiple times to that location. When the source is exhausted, then the animal must learn to not only to refrain from returning to the location, but also to learn a new source. This sequence may happen multiple times throughout an animals life, a reality of the scarcity of food.

Simple learning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Throughout the long studies of animal learning since the late 18th century, a large literature of general rules have been revealed. These universal laws include multiple scales and degrees of complexity, and may be pervasive throughout species of localized to only a few. For example, a quite common form of learning is sensitization and habituation, among the most basic forms. These result in the animals increased or reduced response to a given stimulus after repeated exposures. These occur throughout the animal kingdom, from humans to single cells. For example, if you’re walking in a dark room and someone startles you, your reaction is likely to be more exaggerated than if you were startled in a well lit room. This is an example of sensitization, as the dark room exaggerates your response. The reciprocal of this can be observed in Prairie dogs. Upon hearing the sound of approaching human footsteps, the animals retreat into their holes. As this occurs multiple times, the prairie dogs learn the footsteps are no longer a threat, thus no longer retreating once heard again. These phenomena can be observed at the single cell level as well. Differentiated PC12 cells secrete decreasing amounts of norepinephrine as they are repetitively stimulated by concentrations of a potassium ion. These simple learning rules persist throughout an organism’s lifespan, as it experiences different types and degrees of stimuli. Alone, these simple rules can produce an astounding degree of complex behavior, but they are even more impressive when coupled with other mechanisms.

Associative learning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Simple modulation of response alone may not be suitable for more complex organisms and environments. A finer degree of acuity may be demanded. Thus, evolution has produced other learning mechanisms designed to parse the causal structure of the environment, as well as to differentiate between individual features and stimuli. This type of learning is know as associative, as the animal links together structured information, and fits two main classes: classical and instrumental conditioning. Classical conditioning was made famous by Ivan Pavlov and his dogs, and includes an animal’s ability to link novel stimuli with responses, as such in the classical example of the ringing bell, a conditioned stimulus, resulting in the dog salivating. Other uses have been exhibited as well. Farmers were killing lions that were preying on their cattle. To deter the cats from the cattle, conservation specialists gave the lions cattle meat which would make them safely sick. This conditioned the lions away from the meat, and the number of cattle killed was drastically reduced. Conditioning of this sort could easily be noticed in the wild, and will continue throughout the organism’s lifetime, as more and more associations are built.

When classical conditioning is observed from the perspective of a longer term scale, complex interactions between the conditioning of the animal arise. While many of the rules governing these complex interactions are unknown, some have been uncovered. For example, some stimuli that are experienced but not linked to a response will show a slower learning curve when they are linked to a response, known as latent inhibition. Prior learning of a stimulus and response pair can also inhibit future stimuli from being learned, known as blocking. Organisms may also exhibit a response to novel stimuli as well, known as conditioning generalization.

Organisms may not have these events structured in such a way where the reward is immediately evident, but rather will have to use trial and error until a reward is found. For example, an octopus may try several different actions to open a jar with a crab trapped inside, eventually succeeding by twisting with its arms. When given a new jar, the octopus will open it with less attempts, hinting at learning mechanisms. This type of learning is known as instrumental conditioning. Organisms use this type of learning often in their environment, attempting to parse out hidden rewards that cannot be known. Many successes in machine learning have also leveraged it as well. The famous Q learning algorithm by Watkins was designed with this type of learning in mind, then paired with deep neural networks produced the general Atari playing algorithm.

Associative pairs require repeated reinforcement to persist. If an organism learns that an area may be unsafe, but repeatedly sees it as safe afterwards, then the prior pairing will fade. However, if the stimulus reappears, then the organism will learn much more quickly than the first pairing, hinting that pairings never fully fade.

.. 
    Neural Mechanisms
..
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..
    Stay tuned!

