/* A basic binary (search) tree implementation in Java */

public class BinaryTree {

    public static void main( String args[] ){
        Node n = new Node(5);
        BinaryTree bt = new BinaryTree( n );
        System.out.print("Hello: " + n.getData());
    } 

    private static class Node {
        private int data;
        private Node left;
        private Node right;

        public Node (int data, Node leftNode, Node rightNode) {
            this.data = data;
            this.left = leftNode;
            this.right = rightNode;
        }

        public Node (int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }

        public int getData() {
            return this.data;
        }
    }

    private Node rootNode = null;

    public BinaryTree(Node rootNode) {
        this.rootNode = rootNode;
    }

    public void insert( int data ) {
        insert( this.rootNode, data );
    }

    public void insert( Node node, int data ) {
        if (data <= node.data) {
            if ( node.left != null )  
                insert( node.left, data );
            else
                node.left = new Node( data );     
        }
        if (data > node.data) {
            if ( node.right != null )  
                insert( node.right, data );
            else
                node.right = new Node( data );
        }
    }

    public void orderedPrint() {
        orderedPrint( this.rootNode );
    }

    public void orderedPrint( Node node ) {
        if (node != null) {
            orderedPrint( node.left );
            System.out.print(node.data);
            orderedPrint( node.right );
        }
    }
}

