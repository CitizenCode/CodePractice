/* A basic Linked List implementation in C */

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int value;
    struct Node * next;
};

int main(int argc, char * argv[]) {
    printf("Hello, world!\n");
    struct Node * head = (struct Node *) malloc(sizeof(struct Node));
    (*head).value = 19;
    (*head).next = NULL;

    struct Node * elem = head;

    int i;
    for(i = 0; i < 5; i++) {
        (*elem).value = i;
        (*elem).next = (struct Node *) malloc(sizeof(struct Node));
        // FIXME:  Make sure malloc succeeded!
        //(*((*elem).next)).next = NULL;
        elem->next->next = NULL;
        elem = (*elem).next;
    }

    // Traverse the list!
    elem = head;
    while(elem != NULL) {
        printf("This node's value is %i\n", (*elem).value);
        elem = (*elem).next;
    }

    free(head);
    return EXIT_SUCCESS;
}
