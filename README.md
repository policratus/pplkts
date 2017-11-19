# 🐈👨👦👩👱👱 pplkts

Recognizes simple objects on images, like people and cats.

## 📷 Sample
![pplkts](https://github.com/policratus/pplkts/blob/master/sample/pplkts.jpg)

*Cat's Eye*, Dir. Lewis Teague. Perfs. Drew Barrymore, James Woods, Candy Clark. MGM/UA Entertainment Co., 1985

## 🛠 Installation
Assuming that you've a Unix like OS or emulation, [git](https://git-scm.com/), [Python](https://www.python.org/) 3 and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) installed, just issue:

```
mkvirtualenv pplkts
workon pplkts
git clone git@github.com:policratus/pplkts.git
cd pplkts
pip install -r requirements/requirements.txt
```

## ⚙ Usage
To open a picture and run the recognition, issue:

`./piplkts picture [/path/to/picture/file.ext]`

## ⛓ Dependencies
`Pplkts` uses heavily [OpenCV](http://opencv.org/) and was tested with OpenCV 3.3.0. Despite this dependency is added to `requirements.txt`, is **encouraged** to use a manually compiled version. This article from Manuel Ignacio López Quintero can help you: http://milq.github.io/install-opencv-ubuntu-debian/.

## 🔀 Forked from Piplcount
This project is a fork from my own project `Piplcount`, which recognizes frontal faces on webcam or video stream (e.g., from a file) and can be viewed at https://github.com/policratus/piplcount.
