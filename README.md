# Frame-Selector
Frame-Selector is a video analysis tool written in 100% pure Python to choose the most distinct frames from a video.

This package has the following dependencies: **OpenCV 4.1.0**, **Numpy 1.16.2**, and **Matplotlib 2.2.2**.

## Tools 

Frame-Selector comes with three different methods for quantifying the degree of uniqueness between frames.

 - A **correlation** based approach. This measures the correlation between two frames, where a higher correlation is more similar, and a lower correlation is more distinct.
> This runs the fastest compared to the other two approaches, and is sensitive to larger changes in the image based on lighting and orientation, and the size of the object being displaced.
 - Two **feature** based approaches. These find ~500 keypoints in two frames using ORB (Oriented FAST and Rotated BRIEF).
	 - Calculate the **mean squared error** between their keypoints.
	 - Utilize **KNN (k-nearest-neighbors)** to match detected keypoints betweeen frames. The metric is the diplacement.
> These are more lighting and orientation agnostic, and are concerned more with the **context** of the video, i.e. what is moving, how much is it moving, etc. However, calculations for this style of approach can be computationally expensive.

## Feature Detection Demo:
(From left to right) Ground frame, more similar frame, less similar frame.
![Image](https://raw.githubusercontent.com/vitae-gravitas/Frame-Selector/master/README/features.png)
> This demo can be found in `experiments/match.py`.



