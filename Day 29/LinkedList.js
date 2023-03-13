
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        return this;
    }

    add(data) {
        const node = new Node(data);
        if (!this.head) {
            this.head = node;
            this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
        return this;
    }

    remove() {
        if (!this.head) return null;
        const node = this.head;
        this.head = this.head.next;
        return node.data;
    }

    print() {
        let node = this.head;
        while (node) {
            console.log(node.data);
            node = node.next;
        }
    }

    removeEveryNthNode(n) {
        let node = this.head;
        let count = 1;
        while (node) {
            if (count % n === 0) {
                node.data = node.next.data;
                node.next = node.next.next;
            }
            count++;
            node = node.next;
        }
        return this;
    }
}

const list = new LinkedList().add(1).add(2).add(3).add(4).add(5).add(6).add(7).add(8).add(9).add(10)
.add(11).add(12).add(13).add(14).add(15).removeEveryNthNode(3);

list.print();