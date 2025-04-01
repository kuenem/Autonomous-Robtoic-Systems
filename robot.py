import pygame
import math
import numpy as np

from const import *

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points.
    Args:
        point1 (tuple): The first point (x, y).
        point2 (tuple): The second point (x, y).
    Returns:
        float: The Euclidean distance between the two points.
    """
    point1 = np.array(point1)
    point2 = np.array(point2)
    return np.linalg.norm(point1 - point2)

class Robot:
    def __init__(self, start_posistion, width, angle=0):
        """
        Initialize the Robot object.
        Args:
            start_posistion (tuple): The starting position of the robot (x, y).
            width (int): The width of the robot.
            angle (float): The angle of the robot in degrees.
        """
        self.meter_to_pixel = 100
        self.x = start_posistion[0]
        self.y = start_posistion[1]
        self.angle = angle
        self.width = width
        self.color = BLACK

        self.velocity_left = 0.01 * self.meter_to_pixel
        self.velocity_right = 0.01 * self.meter_to_pixel
        
        self.max_velocity = 0.02 * self.meter_to_pixel
        self.min_velocity = 0.0 * self.meter_to_pixel
        self.max_acceleration = 0.01 * self.meter_to_pixel

