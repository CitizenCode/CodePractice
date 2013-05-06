/* A basic binary (search) tree implementation in Java */

public class BinaryTree {

	  private static class Node {
		    int data;
		    Node left;
		    Node right;
		    
		    public Node (data, leftNode, rightNode) {
		      this.data = data;
		      this.left = leftNode;
		      this.right = rightNode;
		    }
		    
		    public Node (data) {
		      this.data = data;
		      this.left = null;
		      this.right = null;
		    }
		  }
		  
		  private Node rootNode = null;
		  
		  public BinaryTree(Node rootNode) {
			this.rootNode = rootNode;
		  }

		  public void insert( data ) {
			insert( this.rootNode, data );
		  }
		  
		  public void insert( Node node, int data ) {
			if (data <= node.data) {
			  if ( node.left != null )	
		        insert( node.left, data );
		      else
		        node.left = new Node( data );   	
			}
		    if (data > node.data)
		      if ( node.right != null )	
		        insert( node.right, data );
		      else
		        node.right = new Node( data );
		  }
		  
		  public void orderedPrint() {
			orderedPrint( this.rootNode );
		  }
		  
		  public void orderedPrint( Node node ) {
			if (node != null)
			  orderedPrint( node.left );
			  System.out.print(node.data);
			  orderedPrint( node.right );
		  }
		  
		  public static void main( String args[] ){
			  BinaryTree bt = new BinaryTree( new Node(5) );
		  } 
}
