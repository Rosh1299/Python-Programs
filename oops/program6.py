# Implementation of Polymorphism
from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(control):
    control.draw()


ddl = DropDownList()
draw(ddl)
txt = TextBox()
draw(txt)

# Poly - Many
# Morph - Form
# Polymorphism - Many Forms

# Python supports duck typing.
