"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
	rule_sheet = {
		'YACHT': score_yacht,
		'ONES': score_ones,
		'TWOS': score_twos,
		'THREES': score_threes,
		'FOURS': score_fours,
		'FIVES': score_fives,
		'SIXES': score_sixes,
		'FULL_HOUSE': score_full_house,
		'FOUR_OF_A_KIND': score_four_of_a_kind,
		'LITTLE_STRAIGHT': score_little_straight,
		'BIG_STRAIGHT':score_big_straight,
		'CHOICE': score_choice
	}
	return rule_sheet[category](dice)


def score_yacht(dice):
	return 50 if len(set(dice)) == 1 else 0


def score_choice(dice):
	return sum(dice)


def score_ones(dice):
	return 1 * dice.count(1)


def score_twos(dice):
	return 2 * dice.count(2)


def score_threes(dice):
	return 3 * dice.count(3)


def score_fours(dice):
	return 4 * dice.count(4)


def score_fives(dice):
	return 5 * dice.count(5)


def score_sixes(dice):
	return 6 * dice.count(6)


def score_full_house(dice):
	solver = [len(set(dice)) == 2, dice.count(max(dice)) > 1, dice.count(min(dice)) > 1]
	return sum(dice) if sum(solver) == 3 else 0


def score_four_of_a_kind(dice):
	solver = {
		dice.count(max(dice)) >= 4: sum([die for die in dice if die == max(dice)][:4]),
		dice.count(min(dice)) >= 4: sum([die for die in dice if die == min(dice)][:4])
	}
	return solver[True] if True in solver else 0


def score_little_straight(dice):
	return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0


def score_big_straight(dice):
	return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0