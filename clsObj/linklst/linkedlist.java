public class linkedlist {

    private class Node {
        int data = 0;
        Node next = null;

        Node (int data) {
            this.data = data;
        }
    }

    private Node head = null;    
    private Node tail = null;
    private int size = 10;

    public int getSize() {
        return size;
    }

    public boolean isSizeEmpty() {
        return size == 0;
    }

    public void firstNode (int data) {
        Node node = new Node(data);
        addFirstNode(node);
    }
    public void addFirstNode(Node node) {
        if (isSizeEmpty()) {
            this.head = this.tail = node;
        }
        else {
            node.next = this.head;
            this.head = node;
        }
        this.size++;
    }

     public void lastNode(int data) {
        Node node = new Node(data);
        addLastNode(node);
    }

    private void addLastNode(Node node) {
        if (this.size == 0) {
            this.head = this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
        this.size++;
    }

    public int removeFirst(int data) {
        if (this.size == 0) {
            return -1;
        }
        Node node = removeFirstNode();
        return node.data;
    }

    private Node removeFirstNode() {
        Node node = this.head;
        if (this.size == 1) {
            this.head = this.tail = null;
        } else {
            this.head = this.head.next;
            node.next = null;
        }
        this.size--;
        return node;
    }

     public int getFirst() {
        if (isSizeEmpty()) {
            return -1;
        }
        return getFirstNode().data;
    }

    private Node getFirstNode() {
        Node node = this.head;
        return node;
    }

    public int getLast() {
        if (this.size == 0) {
            return -1;
        }
        return getLastNode().data;
    }

    private Node getLastNode() {
        return this.tail;
    }

    public int getAt(int idx) {
        if (isSizeEmpty() || idx > this.size) {
            return -1;
        }
        Node node = getAtNode(idx);
        return node.data;
    }

    private Node getAtNode(int idx) {
        Node curr = this.head;
        while (idx-- > 0) {
            curr = curr.next;
        }
        return curr;
    }

        if (isEmpty()) {
            return -1;
        }

        Node node = removeLastNode();
        return node.data;
    }

    private Node removeLastNode() {
        Node node = this.tail;
        if (this.size == 1) {
            this.head = this.tail = null;
        } else {
            // for (int i = 0; i < size; i++) {
            // if (i == this.size-2) {
            // node.next = null;
            // this.tail = node;
            // } or
            // }
            Node secondLastNode = getAtNode(this.size - 2);
            secondLastNode.next = null;
            this.tail = secondLastNode;
        }
        this.size--;
        return node;
    }

}
