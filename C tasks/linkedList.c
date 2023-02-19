
#include <stdio.h>
#include <stdlib.h>

/*
 * structures
 */

typedef struct nodeData {
  int intData;
  float floatData;
} Data;

typedef struct node {
  Data *data;
  struct node *next;
} Node;

/*
 * function headers
 */

Data *createData( int i, float f );
Node *createNode( Data *data );
void freeNode( Node *node );

Node *addNodeAtHead( Node *head, Node *new );
void insertNodeAfter( Node *location, Node *new );
Node *deleteNextNode( Node *location );

void printList( Node *head );
Node *freeList( Node *head );
Node *freeListR( Node *location );

/*
 * main
 */

int main( void ) {
  int i;
  Data *newData;
  Node *head, *newNode, *removed;

  // initialise an empty list
  head = NULL; 

  // create a linked list
  printf( "\nCreate a list of 5 items\n" );

  for( i=0; i<5; ++i ) {
    newData = createData( i, (float)i );
    newNode = createNode( newData ); 
    head = addNodeAtHead( head, newNode );
  }

  // traverse the list and print out the data
  printList( head );

  // insert a new node
  printf( "\nCreate a node and insert it\n" );

  newData = createData( -1, -2.0 );
  newNode = createNode( newData );
  insertNodeAfter( head->next, newNode );

  // traverse the list and print out the data
  printList( head );

  // delete a node following a given node
  printf( "\nDelete a node\n" );

  removed = deleteNextNode( head );
  freeNode( removed ); // deallocate the heap memory


  // traverse the list and print out the data
  printList( head );

  // insert a new node at the head
  printf( "\nCreate a node and insert it at the head\n" );

  newData = createData( -3, -8.0 );
  newNode = createNode( newData );

  head = addNodeAtHead( head, newNode );

  // traverse the list and print out the data
  printList( head );

  // free the list data structure
  printf( "\nDelete the entire list\n" );

  head = freeListR( head ); // recursive implementation

  // traverse the list and print out the data
  printList( head );

  return 0;
}

/*
 * delete a node from the list
 */

Node *deleteNextNode( Node *location ) {

  Node *toBeRemoved = location->next;
  location->next = toBeRemoved->next;  // unlink from the list

  return toBeRemoved;
}

/*
 * insert a node after a given location
 */

void insertNodeAfter( Node *location, Node *new ) {

  new->next = location->next;
  location->next = new;

  return;
}

/*
 * traverse the list and print out the data
 */

void printList( Node *head ) {

  Node *location = head;

  printf( "\n Current list\n" );
  while( location != NULL ) {
    printf(" %i %f \n", location->data->intData, location->data->floatData ); 
    location = location->next;
  }
  return;
}

/*
 * add a node to the list at the head
 */

Node *addNodeAtHead( Node *head, Node *newNode ) {

  newNode->next = head;

  return newNode;
}

/*
 * create node data
 */

Data *createData( int i, float f ) {

  Data *data = (Data *)malloc( sizeof(Data) );
  data->intData = i;
  data->floatData = f;

  return data;
}

/*
 * create a node
 */

Node *createNode( Data *data ) {

  Node *newNode = (Node *)malloc( sizeof(Node) );
  newNode->data = data;
  newNode->next = NULL;

  return newNode;
}

/*
 * free a node 
 */

void freeNode( Node *node ) {

  free( node->data );
  free( node );
  
  return;
}

/*
 * traverse the list and free all the memory
 */

Node *freeList( Node *head ) {

  Node *location = head;

  while( location != NULL ) {
    
    Node *next = location->next; // store the next location
    freeNode( location );  // free the current node
    location = next;       // next node
  }
  return NULL;
}

/*
 * traverse the list and free all the memory - recursive
 */

Node *freeListR( Node *location ) {

  if( location != NULL ) { // exit condition: next node == NULL

    Node *next = location->next; // store the next location
    freeNode( location );  // free the current node
    freeListR( next );     // recursive call
  }
  return NULL;
}

