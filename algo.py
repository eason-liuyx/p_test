#!/usr/bin/env python

def quick_sort(arr, left, right):
	if left > right:
		return
	
	i = left
	j = right
	key = arr[left]
	while i < j:
		while i < j and key <= arr[j]:
			j -= 1

		arr[i] = arr[j]

		while i < j and key >= arr[i]:
			i += 1

		arr[j] = arr[i]

	arr[i] = key
	quick_sort(arr=arr, left=left, right=i - 1)
	quick_sort(arr=arr, left=i + 1, right=right)


def leastinterval(tasks, tasksize, n):
	a = [0] * 26
	for i in tasks:
		a[ord(i) - ord('A')] += 1

	print(a)

	quick_sort(arr=a, left=0, right=25)

	time = 0
	while a[25] > 0:
		i = 0
		while i <= n:
			if a[25] == 0: break
			if i < 25 and a[25 - i] > 0:
				a[25 - i] -= 1

			time += 1
			i += 1
		quick_sort(arr=a, left=0, right=25)

	return time


	
