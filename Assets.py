__author__ = 'Simon'
import pygame


class Assets(object):
    def __init__(self):
        self.landerLightGreen = pygame.image.load("assets/landing_light_green.png").convert()
        self.landerLightRed = pygame.image.load("assets/landing_light_red.png").convert()
        self.landerBody = pygame.image.load("assets/lander_body_prelim.png").convert()
        self.rotorA = pygame.image.load("assets/rotor_A.png").convert()
        self.rotorB = pygame.image.load("assets/rotor_B.png").convert()
        self.yellowBox = pygame.image.load("assets/yellow_box.png").convert()
        self.redBox = pygame.image.load("assets/red_box.png").convert()
        self.blueBox = pygame.image.load("assets/blue_box.png").convert()
        self.boxOverlay = pygame.image.load("assets/box_overlay.png").convert()
        self.background = pygame.image.load("assets/background.png").convert()
        self.upArrow = pygame.image.load("assets/upArrow.png").convert()
        self.leftArrow = pygame.image.load("assets/leftArrow.png").convert()
        self.rightArrow = pygame.image.load("assets/rightArrow.png").convert()
        self.space = pygame.image.load("assets/space.png").convert()
        self.ESC = pygame.image.load("assets/ESC.png").convert()
        self.mouse = pygame.image.load("assets/mouse.png").convert()