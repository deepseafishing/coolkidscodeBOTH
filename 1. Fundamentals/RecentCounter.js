var RecentCounter = function() {
  this.times = [];
  this.minHeapIdx = 0;
};

/**
 * @param {number} t
 * @return {number}
 */
RecentCounter.prototype.ping = function(t) {
  this.times.push(t);
  for (let i = this.minHeapIdx; i < this.times.length; i++) {
    if (t - 3000 <= this.times[i]) {
      this.minHeapIdx = i;
      return this.times.length - i;
    }
  }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */
