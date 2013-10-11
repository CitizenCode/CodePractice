/* Simple implementation of a Linked List in C.
 * Note that this is not thread-safe.
 * Also note that it has only been tested on OS X 10.8.5 on AMD64.
 * And by that I mean completely untested so far.
 * Also it's only partially implemented.
 * Author:  Daniel Mannarino
 */

#include <stdio.h>
#include <stdlib.h>

struct Node {
    void * value;
    struct Node * next;
};

struct List {
    struct Node * head;
    struct Node * tail;
};

// Perfectly fine, but I think I prefer using get_empty_list, below
int init_List(struct List * list) {
    list->head = NULL;
    list->tail = NULL;
}

// Responsibly frees all nodes and values in a list
void destroy_list(struct List * list);

// Creates and returns a pointer to an empty list, or NULL pointer on failure
struct List * get_empty_list() {
    struct List * list = malloc(sizeof(struct List));
    if(list == NULL) {
        printf("WARNING:  Creation of empty List failed!!!\n");
    }
    else {
        list->head = NULL;
        list->tail = NULL;
    }
    return list;
}

// Add an element to the list.  Return a pointer to the list on success,
// NULL on failure
struct List * add_to_list(struct List * l, void * element);
//    //FIXME:  STUB
//}


// Run some tests to verify things work okay
int main(int argc, char * argv[]) {
    printf("Hello, list-lovers!\n");

    struct List * list;
    list = get_empty_list();
    if(list == NULL) {
        printf("WARNING:  Creation of initial List failed!!!\n");
        return(EXIT_FAILURE);
    }

    return(EXIT_SUCCESS);
}
