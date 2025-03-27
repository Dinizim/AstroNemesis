#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom.minidom import Entity


class Level:
    def __init__(self, window, name, menu_list):
        self.window = window
        self.name = name
        self.menu_list = menu_list
        self.entity_list: list[Entity] = []

    def run(self):
        pass
