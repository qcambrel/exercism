def latest(scores):
	return scores[-1]


def personal_best(scores):
	return max(scores)


def personal_top_three(scores):
	scores_descending = sorted(scores, reverse=True)
	return scores_descending[:3]