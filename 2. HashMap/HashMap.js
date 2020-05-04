/**
 * Initialize your data structure here.
 */
var MyHashMap = function() {
    this.mapSize = 2000;
    this.map = new Array(this.mapSize).fill(0).map((el) => new LinkedList());
};

/**
 * value will always be non-negative.
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
MyHashMap.prototype.put = function(key, value) {
    this.map[hashFunction(key, this.mapSize)].update(key, value);
};

/**
 * Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
 * @param {number} key
 * @return {number}
 */
MyHashMap.prototype.get = function(key) {
    let prev = this.map[hashFunction(key, this.mapSize)].findPrev(key);
    if (prev.next) return prev.next.value;
    else return -1;
};

/**
 * Removes the mapping of the specified value key if this map contains a mapping for the key
 * @param {number} key
 * @return {void}
 */
MyHashMap.prototype.remove = function(key) {
    this.map[hashFunction(key, this.mapSize)].remove(key);
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */

function hashFunction(key, m) {
    return key % m;
}

class Node {
    constructor(key, value) {
        this.key = key;
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = new Node(null, null);
    }

    findPrev(key) {
        let p = this.head;
        while (p.next) {
            if (p.next.key === key) return p;
            p = p.next;
        }
        return p;
    }

    update(key, value) {
        let prev = this.findPrev(key);
        if (prev.next) prev.next.value = value;
        else prev.next = new Node(key, value);
    }

    remove(key) {
        let prev = this.findPrev(key);
        if (prev.next) prev.next = prev.next.next;
    }
}
