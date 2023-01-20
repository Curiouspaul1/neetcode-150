class MinStack {
  private stack: Array<Array<number>>

  constructor() {
    this.stack = []
  }

  push(val: number): void {
    let temp = 0;
    if (this.stack.length > 0) {
      temp = this.stack[this.stack.length - 1][1]
    } else {
      temp = Infinity
    }
    let min = Math.min(temp, val);
    this.stack.push([val, min])
  }

  pop(): void {
    this.stack.pop();
  }

  top(): number {
    return this.stack[this.stack.length - 1][0]
  }

  getMin(): number {
    return this.stack[this.stack.length - 1][1]
  }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */