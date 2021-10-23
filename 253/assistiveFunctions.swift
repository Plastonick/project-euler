//
//  File.swift
//  253-euler
//
//  Created by David Pugh on 22/01/2017.
//  Copyright © 2017 David Pugh. All rights reserved.
//

import Foundation
import Darwin

//determine number of disjoint sets
func numDisjoint(jigsaw: [Int]) -> Int {
	var currentElement = -1
	var numDisjointSets = 0
	
	for element in jigsaw {
		if element - currentElement > 1 {
			numDisjointSets += 1
		}
		
		currentElement = element
	}
	
	return numDisjointSets
}

//factorial function
func factorial(n: Int) -> Double {
	if n == 0 {
		return 1
	}
	
	var result: Double = 1
	
	for i in 1...n {
		result *= Double(i)
	}
	
	return result
}


//determines if there is a group of three consecutive numbers, assumes sorted (ascending) array
func existsGroupOfThree(jigsaw: [Int]) -> Bool {
	var count = 1
	var previousElement = -1
	
	for element in jigsaw {
		if (previousElement + 1) == element {
			count += 1
		} else {
			count = 1
		}
		
		if count == 3 {
			return true
		}
		
		previousElement = element
	}
	
	return false
}


// outputs list of length of all consecutive integer trains/segments in size order.
// e.g. [1, 2, 3, 6, 7, 9, 14, 15, 16] -> [3, 2, 1, 3] -[sorted]-> [1, 2, 3, 3]
func jigsawToDisjointSet(jigsaw: [Int]) -> [Int] {
	var disjointSet: [Int] = []
	var count = 1
	
	for i in 1..<jigsaw.count {
		if jigsaw[i] - jigsaw[i - 1] == 1 {
			count += 1
		} else {
			disjointSet.append(count)
			count = 1
		}
	}
	
	disjointSet.append(count)
	disjointSet.sort()
	
	return disjointSet
}


