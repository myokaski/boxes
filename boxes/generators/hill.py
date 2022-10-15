#!/usr/bin/env python3
# Copyright (C) 2013-2018 Florian Festi
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from boxes import *


class Hill(Boxes):
    """Hill"""

    ui_group = "Misc"

    def __init__(self):
        Boxes.__init__(self)
        self.addSettingsArgs(edges.FingerJointSettings)
        #self.buildArgParser("outside", x=250, y=45, bottom_edge="h")
        self.buildArgParser(x=250, y=45, h=0, outside=False)
        self.argparser.add_argument(
            "--angle", action="store", type=float, default=10,
            help="angle of the hill")

    def render(self):

        x, y = self.x, self.y
        r = 3
        heights = [self.h, self.h + x * math.tan(math.radians(self.angle))]

        if self.outside:
            x = self.adjustSize(x, "e", "e")
            y = self.adjustSize(y, "f", "f")
            #for i in range(2):
            #    heights[i] = self.adjustSize(heights[i], "h", "e")
        else:
            for i in range(2):
                delta = heights[i] - self.adjustSize(heights[i], "h", "e")
                heights[i] = heights[i] + delta * math.cos(math.radians(self.angle))

        t = self.thickness
        h0, h1 = heights
        h2 = h1
        h3 = h0
        #b = self.bottom_edge
        diag = x / math.cos(math.radians(self.angle))

        #self.trapezoidWall(x, h0, h1, [b, "e", "e", "e"], move="right")
        #self.trapezoidWall(x, h2, h3, [b, "e", "e", "e"], move="right")
        self.rectangularWall(diag , y, "fefe", move="up")
        self.trapezoidWall(x, h0, h1, ["e", "e", "h", "e"], move="up")
        self.trapezoidWall(x, h2, h3, ["e", "e", "h", "e"], move="up")
