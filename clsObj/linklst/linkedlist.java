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

}
