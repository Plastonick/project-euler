struct HashableArray<T: Hashable>: Hashable {
	var array: [T]
	
	var hashValue: Int {
		var value = 0
		
		for member in array {
			value ^= member.hashValue
		}
		
		return value
	}
	
	init(_ array: [T]) {
		self.array = array
	}
	
	static func ==<T: Hashable>(lhs: HashableArray<T>, rhs: HashableArray<T>) -> Bool {
		return lhs.array == rhs.array
	}
}
