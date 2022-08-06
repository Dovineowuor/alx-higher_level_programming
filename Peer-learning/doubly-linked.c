#include <stdlib.h>
#include stdio.h>
struct node{
    struct node*prev;
    int data;
    struct node *next;
}
// Doubly linked lists's nodes
void push (Node ** head_ref, int new_data)
// Node creation and allocation allocation
Nude* new_node = new Node();
// Data insertion
new_node -> data = new_data;

// Node linkage

new_node -> next = (head_ref);

(*head_ref) = new_node

// Node insertion

void insertAfter(struct Node* prev_node, int new_data)

if (prev_node == NULL) {
    printf("Empty node please adjust the previous node as it can't be NULL ")

    return;
}

// Creating a new node
struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));

// Appending data 
new_node -> data = new_data;

// Linking a previous link of a node to the next node(creating a link to the next node)

new_node -> next = prev_node = next;

prev_node -> next = new_node

void append(struct Node** head_ref, int new_data)

// adding a node to the next link 

struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
struct Node *last = *head_ref

// Afdding data to the new node
new_node -> data = new_data;

//  Checking on the data alocated to the Doubly linked list

if (*head_ref == NULL){
    *head_ref = new_node;
     return;
    
}

while (last -> next != NULL)
last = last -<> next;

last -> new = New_node;
return;