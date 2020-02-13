# Dog Breeds detection

### Project Overview

Fun and enjoyable applications are great since they make our lives better and more pleasant. And since everyone loves dogs, I have decided to build an application to combine these two ideas: enjoyability and human best friend(dogs).
In this project, I have created a web application that is capable of determining the breed of a dog in a given image. The application uses a classifier(CNN) trained on the [dog dataset](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip).


## Required Packages

Please make sure to have the following packages installed on youre system:
[PyTorch](https://pytorch.org/) using ```bash pip install pytorch ```
[torchvision](https://pytorch.org/docs/stable/torchvision/index.html) using ```bash pip install torchvision ```
[Flask](https://www.palletsprojects.com/p/flask/) using ```bash pip install flask ```


## Techinques
I have used Convolutional Neural Network as my classifier which is the most powerful algorithm for most image processing tasks, including classification. It needs a huge amount of data compared to other machine learning approaches and techniques. 
And for human detection,  I have used [HaarCascades](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt.xml) (frontal) in order to detect human faces. This feature detection algorithm has been proving its great capability of detecting objects (faces in our case).
Our dataset is not considered to be huge since we only have about 63 images per class.
The algorithm (CNN) outputs an assigned probability/score for each class, so we can examine how much is our model confident with a particular decision it has made.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
