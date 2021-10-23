import Foundation
import Darwin

//caterpillar problem, project euler #253

//https://projecteuler.net/problem=253

//given a Jigsaw of 40 pieces, numbered and arranged in a line, if we pick up the unsorted pieces on the floor one by one and put them in their respective locations elsewhere, what is the average of the maximum number of disjoint "trains" (lists of consecutive integers) encountered whilst putting all 40 pieces in respective locations.

//naive solution is to attempt all 40! possiblities and record results

//attempting to itteratively remove peices from complete jigsaw (its the mathematical equivalent) and see max disjoint sets at each step. Record for all possible. e.g. if at some stage we have trains of length 2, 3, 7, and 9, we know how that behaves so can record how that behaves and reuse the answer for the next time our jigsaw has trains of length 2, 3, 7, and 9.

//size of jigsaw
let n = 40
let absMaxDis = Int(ceil(Double(n) / 2) + 1)
var maxCounts: [Double] = [Double](repeating: 0, count: absMaxDis)

//dictionary to contain counts per max segments of common disjointed sets.
//var countPerMaxSegments = Dictionary<HashableArray<Int>, [Double]>()
var countPerMaxSegments: [HashableArray<Int>: [Double]] = [:]

//function to calculate number of combinations for each possible max disjoint sets, computes itteratively using dictionaries.
//returns maxCount array, gives number of ways of getting 1 total disjoint sets, 2 total, 3, etc...

func calculateDisjointOutputs(curJigsaw: [Int], curMax: Int, maxCounts: [Double]) -> [Double] {
	var newMaxCounts = maxCounts
	
	//find number of disjoint sets, set newCurMax as max(curMax, newMax)
	var newCurMax = numDisjoint(jigsaw: curJigsaw)
	
	if newCurMax < curMax {
		newCurMax = curMax
	}

	//stop if no group of at least three consecutive integers, return newMaxCounts
	if !existsGroupOfThree(jigsaw: curJigsaw) {
		newMaxCounts[newCurMax] += factorial(n: curJigsaw.count)
		return newMaxCounts
	}
	
	//find all possible continuations of the jigsaw
	for i in 0..<curJigsaw.count {
		var newJigsaw = curJigsaw
		newJigsaw.remove(at: i)
		
		let setNotation = HashableArray(jigsawToDisjointSet(jigsaw: newJigsaw))
		
		if let knownMaxCounts = countPerMaxSegments[setNotation] {
			// merge knownMaxCounts and maxCounts
			
			for j in 0..<knownMaxCounts.count {
				if j > newCurMax {
					newMaxCounts[j] += knownMaxCounts[j]
				} else {
					newMaxCounts[newCurMax] += knownMaxCounts[j]
				}
			}
		
		} else {
			// determine maxCounts for unknown disjoint set type
			var unknownMaxCounts = calculateDisjointOutputs(curJigsaw: newJigsaw, curMax: 0, maxCounts: [Double](repeating: 0, count: absMaxDis))
			
			countPerMaxSegments[setNotation] = unknownMaxCounts
			
			// merge unKnownMaxCounts and maxCounts
			
			for j in 0..<unknownMaxCounts.count {
				if j > newCurMax {
					newMaxCounts[j] += unknownMaxCounts[j]
				} else {
					newMaxCounts[newCurMax] += unknownMaxCounts[j]
				}
			}
		}
	}
	
	return newMaxCounts
}


//to see how the problem behaves with different values, m MUST be less than n defined above.
for m in 40...40 {
	print("Size of Jigsaw is \(m)")
	let jigsaw = [Int](1...m)
	
	let finalMaxCounts = calculateDisjointOutputs(curJigsaw: jigsaw, curMax: 0, maxCounts: maxCounts)
	var sum: Double = 0
	
	for i in 0..<finalMaxCounts.count {
		sum += Double(i) * finalMaxCounts[i]
	}
	
	let average: Double = sum / factorial(n: m)
	
	print("The mean average maximum disjoint segments encountered was \(average).")
	print("There were \(countPerMaxSegments.count) dictionary entries. (Related to Partitions in Number Theory).")
	print()
}











