# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770

from model.sorensen_dice import SorensenDiceCoefficient


class TestSDC:

    def test_1(self):
        assert SorensenDiceCoefficient.min_edit_dist("night", "nacht") == 0.25

    def test_2(self):
        assert SorensenDiceCoefficient.min_edit_dist("macht", "nacht") == 0.75

    def test_3(self):
        assert SorensenDiceCoefficient.min_edit_dist("night", "nacht") == 0.25