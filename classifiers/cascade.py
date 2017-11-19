"""
classifiers

Image classifiers for object recognition
"""
import os
import cv2

class Classifiers:
    """
    Methods for image classification
    """
    _path = os.path.dirname(
        os.path.realpath(
            __file__
        )
    )

    _faces_haar = _path + '/faces.xml'
    _eyes_haar = _path + '/eyes.xml'
    _cat_haar = _path + '/cat.xml'

    @classmethod
    def __init__(cls):
        cls._faces_haar_features = cv2.CascadeClassifier(cls._faces_haar)
        cls._eyes_haar_features = cv2.CascadeClassifier(cls._eyes_haar)
        cls._cat_haar_features = cv2.CascadeClassifier(cls._cat_haar)

    @classmethod
    def _detect_face(cls, image):
        """
        Detect faces on image using Haar cascades
        """
        faces = cls._faces_haar_features.detectMultiScale(
            image,
            scaleFactor=1.5,
            minNeighbors=5
        )

        return faces

    @classmethod
    def _detect_eyes(cls, image):
        """
        Detect eyes on image using Haar cascades
        """
        eyes = cls._eyes_haar_features.detectMultiScale(
            image,
            scaleFactor=2.5,
            minNeighbors=5
        )

        return eyes

    @classmethod
    def _detect_cat(cls, image):
        """
        Detect cats on image using Haar cascades
        """
        cat = cls._cat_haar_features.detectMultiScale(
            image,
            minSize=(80, 80)
        )

        return cat
