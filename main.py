#!/usr/bin/env python

print("hello world")
import keyword
print(keyword.kwlist)

import algo

def test_quick_sort():
	tasks = ['A', 'A', 'A', 'B', 'B', 'B']
	tasksize = 6
	duration = algo.leastinterval(tasks, tasksize, n=2)
	print("duration is:", duration)

test_quick_sort()
